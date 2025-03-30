![](_page_0_Picture_0.jpeg)

BSI Technical Guideline TR-03121-3

# Biometrics for Public Sector Applications

Part 3: Application Profiles, Function Modules and Processes

Volume 6: Immigration Authorities (IMA)

Version 5.3

Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn E-Mail: TRBiometrics@bsi.bund.de Internet: https://bsi.bund.de © Federal Office for Information Security 2022

## **Table of Contents**

| 1.    | Volume Immigration Authorities<br>                                               | 1  |
|-------|----------------------------------------------------------------------------------|----|
| 2.    | Application Profiles<br>                                                         | 2  |
| 2.1.  | Application Profile Multimodal Processing in Immigration Authorities for EES<br> | 2  |
| 2.2.  | Application Profile Multimodal Processing in Immigration Authorities for SIS<br> | 3  |
| 3.    | Partial Application Processes<br>                                                | 6  |
| 3.1.  | PAP ACQ-FI-SV-4: Supervised Facial Image Acquisition without CIR Lookup<br>      | 6  |
| 3.2.  | PAP ACQ-FP442-SV-1: Supervised Acquisition 4-4-2 for Enrolment<br>               | 7  |
| 3.3.  | PAP ACQ-FP4141-SV-1: Supervised Acquisition 4-1-4-1 for Enrolment<br>            | 11 |
| 3.4.  | PAP ACQ-FPS-SV-1: Supervised Acquisition Single Slap<br>                         | 15 |
| 4.    | Function Modules<br>                                                             | 19 |
| 4.1.  | FM Category Acquisition Hardware<br>                                             | 19 |
| 4.2.  | FM Category Acquisition Software<br>                                             | 22 |
| 4.3.  | FM Category Biometric Image Processing<br>                                       | 23 |
| 4.4.  | FM Category Quality Assessment<br>                                               | 24 |
| 4.5.  | FM Category Presentation Attack Detection<br>                                    | 30 |
| 4.6.  | FM Category Compression<br>                                                      | 31 |
| 4.7.  | FM Category Operation<br>                                                        | 33 |
| 4.8.  | FM Category User Interface<br>                                                   | 34 |
| 4.9.  | FM Category Logging<br>                                                          | 36 |
| 4.10. | FM Category Coding<br>                                                           | 41 |
|       | List of Abbreviations<br>                                                        | 48 |
|       | Bibliography<br>                                                                 | 49 |

## **List of Figures**

| 2.1.  | Data Acquisition and Processing at an Immigration Authority<br>                          | 2  |
|-------|------------------------------------------------------------------------------------------|----|
| 2.2.  | Data Acquisition and Processing at an Immigration Authority<br>                          | 4  |
| 3.1.  | Partial Application Process "Supervised Facial Image Acquisition without CIR Lookup"<br> | 7  |
| 3.2.  | Partial Application Process Task "Capture Live Facial Image"<br>                         | 7  |
| 3.3.  | Partial Application Process "Supervised Acquisition 4-4-2 for Enrolment"<br>             | 8  |
| 3.4.  | Partial Application Process Task "Capture Slap Supervised"<br>                           | 10 |
| 3.5.  | Partial Application Process Task "Capture Plain Fingerprint Supervised"<br>              | 11 |
| 3.6.  | Partial Application Process "Supervised Acquisition 4-1-4-1 for Enrolment"<br>           | 12 |
| 3.7.  | Partial Application Process Task "Capture Slap Supervised"<br>                           | 14 |
| 3.8.  | Partial Application Process Task "Capture Plain Fingerprint Supervised"<br>              | 15 |
| 3.9.  | Partial Application Process "Supervised Acquisition Slap"<br>                            | 15 |
| 3.10. | Partial Application Process Task "Capture Slap Supervised"<br>                           | 17 |
| 3.11. | Partial Application Process Task "Capture Plain Fingerprint Supervised"<br>              | 18 |

## <span id="page-4-0"></span>**1. Volume Immigration Authorities**

German [Immigration Authorities \(IMA\)](#page-51-1) are assigned various tasks, which, among others, include the issuance of resident permits, the renewal of resident permits, or the handling of illegal staying [Third-Country Natio](#page-51-2) [nals \(TCNs\).](#page-51-2) Using biometrics in these tasks enhances the quality of these tasks and is therefore usually not only legally allowed but even more compulsory. The biometric modalities, which are generally in use, fin gerprints (flat) and the facial image. Which biometrics are needed in a given use-case heavily depends on the specific use-case and the corresponding legislation. This also applies to usage of the biometrics once they are acquired, which might be an enrolment in identity registers, a 1:1-verification against biometric data in an identity register or in an electronic document, or a 1:n identification in identity registers.

To achieve a uniform level of quality and security across Germany whenever biometric data is used, stan dardized approach is needed when it comes to the acquisition of biometric for further usage. On the one hand, varying quality in the acquisition of biometrics would inevitably also result subse quent processes, which should be avoided. On the other hand, a standardized acquisition (quality, data format, etc.) also facilitates standardization of all subsequent steps in public sector applications.

This [Technical Guideline \(TR\)](#page-51-3) therefore defines standards for the acquisition of biometric data to be used in applications of the German immigration authorities. Different processes are modelled with the goal, that for each relevant use-cases, a process can be found herein, which meets the specific technical and legal demands. Nevertheless, the decision, which process is to be called in which use-case at which time, is not in the scope of this document.

This volume consists out of two [Application Profiles \(APs\),](#page-51-4) nameley [Section 2.1](#page-5-3) and [Section 2.2](#page-6-0)

## <span id="page-5-0"></span>**2. Application Profiles**

## <span id="page-5-3"></span><span id="page-5-1"></span>**2.1. Application Profile Multimodal Processing in Immigration Authorities for EES**

## **2.1.1. Mandatory Process**

[Figure 2.1](#page-5-2) depicts the acquisition process at an Immigration Authority. In general, the biometric data of the applicant SHALL be captured sequentially. Depending on the use-case it is required to acquire fingerprints and / or a facial image of the biometric subject. For all acquisitions enrolment quality SHALL be used in order to simplify the over all processes (e.g. a facial image that has been used for a verification is not needed to be recaptured for an enrolment).

In the case of fingerprint acquisition for a verification within [Entry-Exit System \(EES\)](#page-51-5) as [Central Identity Re](#page-51-6) [gister \(CIR\)](#page-51-6) it would be sufficient to acquire the four flat fingerprints of the slap which is stored within the [EES](#page-51-5).

In the case of facial image acquisition a digital camera SHALL be used.

In the end the acquired biometrics are used for enrolment, verifications and / or identifications within one or multiple [CIRs.](#page-51-6) Within this application profile this is mainly [EES](#page-51-5).

<span id="page-5-2"></span>![](_page_5_Figure_8.jpeg)

**Figure 2.1.** Data Acquisition and Processing at an Immigration Authority

## **2.1.2. Relevant Standards and Conditions**

In addition to the legal requirements, further basic directives and standards are applicable:

- **•** [\[BIB\\_ISO\\_FINGER\]](#page-52-1)
- **•** [\[BIB\\_ISO\\_FACE\]](#page-52-2)

## **2.1.3. Mandatory Function Modules**

All Function Modules which SHALL be applied for the Application Profile are presented in [Table 2.1 where](#page-6-1) by slash-separated entries denote alternative Function Modules and comma-separated requi rements for all specified Function Modules.

<span id="page-6-1"></span>

| Module Category               | Required Function Modules                                                                      |
|-------------------------------|------------------------------------------------------------------------------------------------|
| Acquisition Hardware          | FM AH-FI-DC,<br>FM AH-FP-OPT                                                                   |
| Acquisition Software          | FM AS-FI-DC,<br>FM AS-FP-MF,<br>FM AS-FP-SLP                                                   |
| Biometric Image Processing    | FM BIP-FI-APP,<br>FM BIP-FP-APP                                                                |
| Quality Assessment            | FM QA-FI-GENERIC,<br>FM QA-FI-IMA,<br>FM QA-FP-APP                                             |
| Presentation Attack Detection | FM PAD-FP-APP                                                                                  |
| Coding                        | FM COD-ALL-IMA,<br>FM COD-ALL-EES,<br>FM COD-FI-GENERIC,<br>FM<br>COD-FI-EES,<br>FM COD-FP-EES |
| Compression                   | FM COM-FI-GENERIC,<br>FM COM-FI-IMA,<br>FM COM-FP-IMA,<br>FM<br>COM-FP-WSQE                    |
| Operation                     | FM O-FI-ALL,<br>FM O-FI-DC,<br>FM O-FP-ALL                                                     |
| User Interface                | FM UI-FI-OP,<br>FM UI-FI-BSJ,<br>FM UI-FP-OP,<br>FM UI-FP-BSJ                                  |
| Reference Storage             | -                                                                                              |
| Biometric Comparison          | -                                                                                              |
| Logging                       | FM LOG-ALL-GENERIC,<br>FM LOG-ALL-IMA,<br>FM LOG-FI-GENERIC,<br>FM LOG-FP-GENERIC              |
| Evaluation                    | Will be amended in a future version of this TR.                                                |

**Table 2.1** Required Function Modules Application Profile Multimodal Processing in Immigration Authorities for EES

## **2.1.4. Mandatory Partial Application Processes**

All Partial Application Processes which SHALL be applied for the Application Profile are presented in [Ta](#page-6-2) [ble 2.2](#page-6-2) whereby slash-separated entries denote alternative Partial Application Processes and comma-separa ted entries denote requirements for all specified Partial Application Processes.

<span id="page-6-2"></span>

| No. | Required Partial Application Process                                    |
|-----|-------------------------------------------------------------------------|
| 1   | PAP ACQ-FI-SV-4: Supervised Facial Image Acquisition without CIR Lookup |
| 2   | PAP ACQ-FPS-SV-1: Supervised Acquisition Single Slap                    |

**Table 2.2** Required Partial Application Processes Application Profile Multimodal Processing in Immigration Authorities for EES

## <span id="page-6-0"></span>**2.2. Application Profile Multimodal Processing in Immigration Authorities for SIS**

## **2.2.1. Mandatory Process**

[Figure 2.2](#page-7-0) depicts the acquisition process at an Immigration Authority. The of ten flat finger prints of the biometric subject SHALL be conducted. For all acquisitions enrolment quality SHALL be used in order to simplify the over all processes (e.g. a set of fingerprints that has been used for a verification within [Schengen Information System \(SIS\)](#page-51-7) is not needed to be recaptured for an enrolment later).

<span id="page-7-0"></span>In the end the acquired biometrics are used for enrolment, verifications and / or identifications within one or multiple [CIRs.](#page-51-6) Within this application profile this is mainly [SIS](#page-51-7).

![](_page_7_Figure_2.jpeg)

**Figure 2.2.** Data Acquisition and Processing at an Immigration Authority

## **2.2.2. Relevant Standards and Conditions**

In addition to the legal requirements, further basic directives and standards are applicable: [\[BIB\\_ISO\\_FINGER\]](#page-52-1)

## **2.2.3. Mandatory Function Modules**

All Function Modules which SHALL be applied for the Application Profile are presented in [Table 2.3 where](#page-7-1) by slash-separated entries denote alternative Function Modules and comma-separated requi rements for all specified Function Modules.

<span id="page-7-1"></span>

| Module Category               | Required Function Modules                                   |
|-------------------------------|-------------------------------------------------------------|
| Acquisition Hardware          | FM AH-FP-OPT                                                |
| Acquisition Software          | FM AS-FP-MF,<br>FM AS-FP-SLP                                |
| Biometric Image Processing    | FM BIP-FP-APP                                               |
| Quality Assessment            | FM QA-FP-APP                                                |
| Presentation Attack Detection | FM PAD-FP-APP                                               |
| Coding                        | FM COD-ALL-IMA,<br>FM COD-ALL-GSAT3,<br>FM COD-FP-GSAT3     |
| Compression                   | FM COM-FP-IMA,<br>FM COM-FP-WSQE                            |
| Operation                     | FM O-FP-ALL                                                 |
| User Interface                | FM UI-FP-OP,<br>FM UI-FP-BSJ                                |
| Reference Storage             | -                                                           |
| Biometric Comparison          | -                                                           |
| Logging                       | FM LOG-ALL-GENERIC,<br>FM LOG-ALL-IMA,<br>FM LOG-FP-GENERIC |
| Evaluation                    | Will be amended in a future version of this TR.             |

**Table 2.3** Required Function Modules Application Profile Multimodal Processing in Immigration Authorities for SIS

## **2.2.4. Mandatory Partial Application Processes**

All Partial Application Processes which SHALL be applied for the Application Profile are presented in [Ta](#page-8-0) [ble 2.4](#page-8-0) whereby slash-separated entries denote alternative Partial Application Processes and comma-separa ted entries denote requirements for all specified Partial Application Processes.

<span id="page-8-0"></span>

| No. | Required Partial Application Process                                                                        |
|-----|-------------------------------------------------------------------------------------------------------------|
| 1   | PAP ACQ-FP442-SV-1: Supervised Acquisition 4-4-2 for Enrolment /<br>PAP ACQ-FP4141-SV-1: Supervised Acquisi |
|     | tion 4-1-4-1 for Enrolment                                                                                  |

**Table 2.4** Required Partial Application Profile Multimodal Processing in Immigration Authorities for SIS

## <span id="page-9-0"></span>**3. Partial Application Processes**

The [Partial Application Processes \(PAPs\)](#page-51-8) specified by the following sections provide process specifications of basic biometric processes, e.g. the acquisition, identification or verification of biometrics or the evaluation processes for verification and identification. The [PAPs](#page-51-8) are referenced by the relevant Application Profiles and are part of the overall processes specified therein.

A [PAP](#page-51-8) MAY also be a task. A task is a process which functions as a generic reusable building block which is used by another [PAP](#page-51-8) and is not referenced by an Application Profile directly.

The specific Function Modules that SHALL be implemented in the processes of this chapter are specified by the relevant Application Profiles.

## <span id="page-9-2"></span><span id="page-9-1"></span>**3.1. PAP ACQ-FI-SV-4: Supervised Facial Image Acquisition without CIR Lookup**

## **3.1.1. Process**

The facial image acquisition process, refer to [Figure 3.1](#page-10-1), described by this section requires a supervised si tuation. Note, that the [PAP Task ACQ-FI-1: Capture Live Facial Image](#page-10-3) is used here. The biometric subject's facial image is captured using live enrolment equipment (including a digital camera within a photo studio setup) operated by an operator[1](#page-9-3) .

In case the system detects a face, the facial image capture SHALL be performed automatically. However, the operator SHALL also have the option to perform the capture manually. An immediately performed cropping and de-rotation to the face and software quality assessment for the captured facial image ensures its biometric usability. If the quality assessment succeeds positively, image SHALL be shown to operator. qua lity is assessed as insufficient and the timeout has not exceeded yet, system SHALL recapture. If ope rator has captured manually, the image SHALL be shown to the operator in any case. In case the timeout has exceeded, the system SHALL identify the best captured facial image and show this image to the operator. The operator has the option to correct the cropping and de-rotation on the shown image manually. The operator has the option to accept the captured facial image. The image is then release to the calling application. This is also the case, if the quality has been assessed as insufficient by the system. In the negative case, the facial image SHALL be discarded, the timeout is reset and a recapture is performed.

If the timeout exceeds and no facial image has been captured (neither with sufficient nor with insufficient quality), the process terminates without releasing an image. It is operator's decision to restart acquisi tion process or to perform other actions.

The process SHALL be supervised by an operator.

<span id="page-9-3"></span><sup>1</sup> See ISO/IEC 19794-5, Annex B for "Best practices for Face Images"

<span id="page-10-1"></span>![](_page_10_Figure_1.jpeg)

**Figure 3.1.** Partial Application Process "Supervised Facial Image Acquisition without CIR Lookup"

#### **3.1.1.1. Interface Requirements**

If [High Level Biometric Services \(HLBS\)](#page-51-9) is used by the system, "Service Definition Basic Facial Image Ac quisition System" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented.

## <span id="page-10-3"></span>**3.1.2. PAP Task ACQ-FI-1: Capture Live Facial Image**

<span id="page-10-2"></span>[Figure 3.2](#page-10-2) depicts the basic process of a live facial image capture. If the image acquisition is not supervised [Presentation Attack Detection \(PAD\)](#page-51-10) SHALL be performed. In case of supervised image acquisition [PAD](#page-51-10) is OPTIONAL.

![](_page_10_Figure_7.jpeg)

**Figure 3.2.** Partial Application Process Task "Capture Live Facial Image"

## <span id="page-10-0"></span>**3.2. PAP ACQ-FP442-SV-1: Supervised Acquisition 4-4-2 for Enrolment**

#### **3.2.1. Process**

[Figure 3.3](#page-11-0) depicts the capture process for the 4-4-2 enrolment scenario. Note, that the [PAP Task ACQ-FPS-](#page-11-1)[SV-1: Capture Slap Supervised](#page-11-1) is used here. The 4-4-2 sequences are described in detail subsequently:

- 1. acquire right hand: index finger, middle finger, ring finger, little finger
- 2. acquire left hand: index finger, middle finger, ring finger, little finger
- 3. thumbs of both hands (simultaneously)

Additional single finger captures are possible for each slap capture. This variant is only RECOMMENDED to be provided by the workflow if a slap capture does not yield to sufficient quality.

The process SHALL be supervised by an operator.

<span id="page-11-0"></span>![](_page_11_Figure_3.jpeg)

**Figure 3.3.** Partial Application Process "Supervised Acquisition 4-4-2 for Enrolment"

## **3.2.1.1. Interface Requirements**

If [HLBS](#page-51-9) is used by the system, the "Service Definition Fingerprint Acquisition" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented.

## <span id="page-11-1"></span>**3.2.2. PAP Task ACQ-FPS-SV-1: Capture Slap Supervised**

[Figure 3.4](#page-13-0) depicts the basic process for a plain supervised slap capture. A plain slap capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain slap capture is subsequently described in detail. The quality assessment conducted according to the requi rements of the applicable [FM Category Quality Assessment](#page-27-0). Note, that the [PAP Task ACQ-FPP-SV-2: Cap](#page-13-1) [ture Plain Fingerprint Supervised](#page-13-1) is used here.

If the biometric subject is physically not capable to place all fingers of the slap on the capture hardware at the same time to achieve a slap image of good quality, the operator can decide to capture each finger of the slap in single finger capture mode. This SHALL be possible during the entire process. Hereby, single finger capture mode refers to the [PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised](#page-13-1) as described below.

- 1. The counter variable for the number of attempts for capturing the current slap SHALL be initialized as *i* = 1.
- 2. The slap image SHALL be retrieved from hardware. While the image is retrieved from hardware, [PAD](#page-51-10) SHALL be performed. Note: The operator have the option to manually conduct capture of sla p(s).
- 3. The fingerprints SHALL be segmented and each SHALL be quality assessed.
	- a. In case the quality of the fingerprints meets the quality requirements defined in the corresponding [Quality Assessment \(QA\)](#page-51-11) Function Module, the captured slap and the set of segmented fingerprints and parameter data (e.g. quality values) SHALL be temporarily stored.
	- b. In case the quality requirements for one or more fingerprints of the slap are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a single slap consists of a maximum of three capture attempts). The counter SHALL be set to *i* = *i* + 1.
- 4. A uniqueness check SHALL be conducted for the captured slap image to detect capture of wrong fin gers, e.g. due to interchanged hands or multiple acquisition of the same hand finger. Note, that it is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available.
	- a. In case
		- **•** the comparison of any fingerprint of the current slap with any previously accepted fingerprint of a previous slap or
		- **•** the comparison of any fingerprint of the current slap with another fingerprint of the current slap

is successful, the uniqueness check SHALL raise an alert.

- b. In case the comparisons of all fingerprints of the current slap with all fingerprints of previous slaps are not successful, the uniqueness check SHALL NOT show a warning.
- 5. Generally, a slap classifier SHALL be used for the captured slap image to detect the capture of the wrong slap. It SHALL be configurable to switch the classifier off or in evaluation mode (logging of result wi thout showing the result/error to the operator). Note, that the slap classifier is only required for 4 finger slaps. Other acquisitions currently do not require the corresponding FM.
	- a. If the result of the classification concludes that the acquired slap mismatches the expected slap, an error SHALL be reported.
	- b. If the result of the classification concludes that the acquired slap matches the expected slap, no error SHALL be reported.

If the quality check of the third capture attempt fails (counter *i* is set to 3), the best of the captured slaps SHALL be identified according to the corresponding [QA](#page-51-11) Function Module and temporarily stored along with the corresponding information.

The process SHALL be supervised by an operator.

At the end of the process the operator decides on one of the three options:

- 1. Use the acquired slap.
- 2. Recapture the current slap. The counter SHALL be reset to *i* = 1.
- 3. Restart the total slap acquisition workflow.

The operator SHALL have the following veto options:

- **•** Select none of the captured slaps despite sufficient quality.
- **•** Select a slap of insufficient quality from the acquisition process.

At any point of the process the operator MAY decide to acquire any finger of the slap individually.

<span id="page-13-0"></span>![](_page_13_Figure_1.jpeg)

**Figure 3.4.** Partial Application Process Task "Capture Slap Supervised"

## <span id="page-13-1"></span>**3.2.2.1. PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised**

[Figure 3.5](#page-14-1) depicts the basic supervised capture process for a plain fingerprint capture. A plain fingerprint capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture process. The plain fingerprint capture is described in detail subsequently. The quality assessment is conducted according to the requirements of the applicable [FM Category Quality Assessment.](#page-27-0)

- 1. The counter variable for the number of attempts capturing current fingerprints SHALL be initia lized as *i* = 1.
- 2. The fingerprint image SHALL be retrieved from hardware. While the image is retrieved from hardware, [PAD](#page-51-10) SHALL be performed. Note: The operator SHALL have the option to manually conduct the capture of fingerprint(s).
- 3. The fingerprint SHALL be quality assessed and the captured fingerprint and parameter data (e.g. quality values) SHALL be temporarily stored.
- 4. In case the quality requirements for the fingerprint are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a finger consists of a maximum of three capture attempts). The counter SHALL be set to *i* = *i* + 1.
- 5. A uniqueness check SHALL be conducted for the captured fingerprint image to detect the capture of wrong fingers, e.g. due to interchanged hands or multiple acquisition of the same hand finger. Note: It is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available.
	- a. In case the comparison of current fingerprint with any previously captured is success ful, the uniqueness check SHALL report an alert.
	- b. In case the comparison of current fingerprint with any previously captured is not suc cessful, the uniqueness check SHALL NOT report an alert.
- 6. The acquired finger prints and the results of [PAD,](#page-51-10) [QA](#page-51-11) and uniqueness check SHALL be displayed to the operator.

If the quality check of the third capture attempt fails (counter *i* is set to 3), the best of the captured fingerprint images SHALL be identified according to the corresponding [QA](#page-51-11) Function Module and temporarily stored along with the corresponding information.

The process SHALL be supervised by an operator.

At the end of the process the operator decides on one of the three options:

- 1. Use the acquired fingerprint.
- 2. Recapture the current fingerprint. The counter SHALL be reset to *i* = 1.
- 3. Restart the [Figure 3.5](#page-14-1) acquisition workflow.

The operator SHALL have the following veto options:

- **•** Select none of the captured fingerprints despite sufficient quality.
- **•** Select a fingerprint of insufficient quality from the acquisition process.

<span id="page-14-1"></span>![](_page_14_Figure_4.jpeg)

**Figure 3.5.** Partial Application Process Task "Capture Plain Fingerprint Supervised"

## <span id="page-14-0"></span>**3.3. PAP ACQ-FP4141-SV-1: Supervised Acquisition 4-1-4-1 for Enrolment**

## **3.3.1. Process**

[Figure 3.6](#page-15-0) depicts the acquisition process for 4-1-4-1 the enrolment scenarios. Note, that the [PAP Task](#page-11-1) [ACQ-FPS-SV-1: Capture Slap Supervised is used here. The 4-1-4-1 sequence described in detail subsequent](#page-11-1) ly:

- 1. capture right hand: index finger, middle finger, ring finger, little finger
- 2. capture right hand: thumb
- 3. capture left hand: index finger, middle finger, ring finger, little finger
- 4. capture left hand: thumb

Additional single finger captures are possible for the slaps. This variant is only RECOMMENDED, IF a slap capture does not yield to sufficient quality.

The process SHALL be supervised by an operator.

<span id="page-15-0"></span>![](_page_15_Figure_1.jpeg)

**Figure 3.6.** Partial Application Process "Supervised Acquisition 4-1-4-1 for Enrolment"

## **3.3.1.1. Interface Requirements**

If [HLBS](#page-51-9) is used by the system, the "Service Definition Fingerprint Acquisition" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented.

## **3.3.2. PAP Task ACQ-FPS-SV-1: Capture Slap Supervised**

[Figure 3.4](#page-13-0) depicts the basic process for a plain supervised slap capture. A plain slap capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain slap capture is subsequently described in detail. The quality assessment conducted according to the requi rements of the applicable [FM Category Quality Assessment](#page-27-0). Note, that the [PAP Task ACQ-FPP-SV-2: Cap](#page-13-1) [ture Plain Fingerprint Supervised](#page-13-1) is used here.

If the biometric subject is physically not capable to place all fingers of the slap on the capture hardware at the same time to achieve a slap image of good quality, the operator can decide to capture each finger of the slap in single finger capture mode. This SHALL be possible during the entire process. Hereby, single finger capture mode refers to the [PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised](#page-13-1) as described below.

- 1. The counter variable for the number of attempts for capturing the current slap SHALL be initialized as *i* = 1.
- 2. The slap image SHALL be retrieved from hardware. While the image is retrieved from hardware, [PAD](#page-51-10) SHALL be performed. Note: The operator have the option to manually conduct capture of sla p(s).
- 3. The fingerprints SHALL be segmented and each SHALL be quality assessed.
	- a. In case the quality of the fingerprints meets the quality requirements defined in the corresponding [QA](#page-51-11) Function Module, the captured slap and the set of segmented fingerprints and parameter data (e.g. quality values) SHALL be temporarily stored.
	- b. In case the quality requirements for one or more fingerprints of the slap are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a single slap consists of a maximum of three capture attempts). The counter SHALL be set to *i* = *i* + 1.
- 4. A uniqueness check SHALL be conducted for the captured slap image to detect capture of wrong fin gers, e.g. due to interchanged hands or multiple acquisition of the same hand finger. Note, that it is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available.
	- a. In case
		- **•** the comparison of any fingerprint of the current slap with any previously accepted fingerprint of a previous slap or
		- **•** the comparison of any fingerprint of the current slap with another fingerprint of the current slap

is successful, the uniqueness check SHALL raise an alert.

- b. In case the comparisons of all fingerprints of the current slap with all fingerprints of previous slaps are not successful, the uniqueness check SHALL NOT show a warning.
- 5. Generally, a slap classifier SHALL be used for the captured slap image to detect the capture of the wrong slap. It SHALL be configurable to switch the classifier off or in evaluation mode (logging of result wi thout showing the result/error to the operator). Note, that the slap classifier is only required for 4 finger slaps. Other acquisitions currently do not require the corresponding FM.
	- a. If the result of the classification concludes that the acquired slap mismatches the expected slap, an error SHALL be reported.
	- b. If the result of the classification concludes that the acquired slap matches the expected slap, no error SHALL be reported.

If the quality check of the third capture attempt fails (counter *i* is set to 3), the best of the captured slaps SHALL be identified according to the corresponding [QA](#page-51-11) Function Module and temporarily stored along with the corresponding information.

The process SHALL be supervised by an operator.

At the end of the process the operator decides on one of the three options:

- 1. Use the acquired slap.
- 2. Recapture the current slap. The counter SHALL be reset to *i* = 1.
- 3. Restart the total slap acquisition workflow.

The operator SHALL have the following veto options:

- **•** Select none of the captured slaps despite sufficient quality.
- **•** Select a slap of insufficient quality from the acquisition process.

At any point of the process the operator MAY decide to acquire any finger of the slap individually.

<span id="page-17-0"></span>![](_page_17_Figure_1.jpeg)

**Figure 3.7.** Partial Application Process Task "Capture Slap Supervised"

## **3.3.2.1. PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised**

[Figure 3.5](#page-14-1) depicts the basic supervised capture process for a plain fingerprint capture. A plain fingerprint capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture process. The plain fingerprint capture is described in detail subsequently. The quality assessment is conducted according to the requirements of the applicable [FM Category Quality Assessment.](#page-27-0)

- 1. The counter variable for the number of attempts capturing current fingerprints SHALL be initia lized as *i* = 1.
- 2. The fingerprint image SHALL be retrieved from hardware. While the image is retrieved from hardware, [PAD](#page-51-10) SHALL be performed. Note: The operator SHALL have the option to manually conduct the capture of fingerprint(s).
- 3. The fingerprint SHALL be quality assessed and the captured fingerprint and parameter data (e.g. quality values) SHALL be temporarily stored.
- 4. In case the quality requirements for the fingerprint are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a finger consists of a maximum of three capture attempts). The counter SHALL be set to *i* = *i* + 1.
- 5. A uniqueness check SHALL be conducted for the captured fingerprint image to detect the capture of wrong fingers, e.g. due to interchanged hands or multiple acquisition of the same hand finger. Note: It is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available.
	- a. In case the comparison of current fingerprint with any previously captured is success ful, the uniqueness check SHALL report an alert.
	- b. In case the comparison of current fingerprint with any previously captured is not suc cessful, the uniqueness check SHALL NOT report an alert.
- 6. The acquired finger prints and the results of [PAD,](#page-51-10) [QA](#page-51-11) and uniqueness check SHALL be displayed to the operator.

If the quality check of the third capture attempt fails (counter *i* is set to 3), the best of the captured fingerprint images SHALL be identified according to the corresponding [QA](#page-51-11) Function Module and temporarily stored along with the corresponding information.

The process SHALL be supervised by an operator.

At the end of the process the operator decides on one of the three options:

- 1. Use the acquired fingerprint.
- 2. Recapture the current fingerprint. The counter SHALL be reset to *i* = 1.
- 3. Restart the [Figure 3.5](#page-14-1) acquisition workflow.

The operator SHALL have the following veto options:

- **•** Select none of the captured fingerprints despite sufficient quality.
- **•** Select a fingerprint of insufficient quality from the acquisition process.

<span id="page-18-1"></span>![](_page_18_Figure_4.jpeg)

**Figure 3.8.** Partial Application Process Task "Capture Plain Fingerprint Supervised"

## <span id="page-18-0"></span>**3.4. PAP ACQ-FPS-SV-1: Supervised Acquisition Single Slap**

## **3.4.1. Process**

[Figure 3.9](#page-18-2) depicts the supervised acquisition process of a slap.

At first the operator flags the missing fingers of the hand of the biometric subject. (Alternative: The operator flags the missing fingers of both hands of the biometric subject.)

The biometric subject SHALL be guided to place the hand correctly on the scanner and the slap SHALL be captured. Note, that the [Section 3.2.2](#page-11-1) is used here.

If already slaps of both hands were acquired, the process SHALL end here. Otherwise the operator SHALL decide if he likes to capture the slap of the other hand, too.

The process SHALL be supervised by an operator.

<span id="page-18-2"></span>![](_page_18_Figure_13.jpeg)

**Figure 3.9.** Partial Application Process "Supervised Acquisition Slap"

#### **3.4.1.1. Interface Requirements**

If [HLBS](#page-51-9) is used by the system, the "Service Definition Fingerprint Acquisition" of Part 2, Volume 2 of this Technical Guideline SHALL be implemented.

## **3.4.2. PAP Task ACQ-FPS-SV-1: Capture Slap Supervised**

[Figure 3.4](#page-13-0) depicts the basic process for a plain supervised slap capture. A plain slap capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture sequence. The plain slap capture is subsequently described in detail. The quality assessment conducted according to the requi rements of the applicable [FM Category Quality Assessment](#page-27-0). Note, that the [PAP Task ACQ-FPP-SV-2: Cap](#page-13-1) [ture Plain Fingerprint Supervised](#page-13-1) is used here.

If the biometric subject is physically not capable to place all fingers of the slap on the capture hardware at the same time to achieve a slap image of good quality, the operator can decide to capture each finger of the slap in single finger capture mode. This SHALL be possible during the entire process. Hereby, single finger capture mode refers to the [PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised](#page-13-1) as described below.

- 1. The counter variable for the number of attempts for capturing the current slap SHALL be initialized as *i* = 1.
- 2. The slap image SHALL be retrieved from hardware. While the image is retrieved from hardware, [PAD](#page-51-10) SHALL be performed. Note: The operator have the option to manually conduct capture of sla p(s).
- 3. The fingerprints SHALL be segmented and each SHALL be quality assessed.
	- a. In case the quality of the fingerprints meets the quality requirements defined in the corresponding [QA](#page-51-11) Function Module, the captured slap and the set of segmented fingerprints and parameter data (e.g. quality values) SHALL be temporarily stored.
	- b. In case the quality requirements for one or more fingerprints of the slap are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a single slap consists of a maximum of three capture attempts). The counter SHALL be set to *i* = *i* + 1.
- 4. A uniqueness check SHALL be conducted for the captured slap image to detect capture of wrong fin gers, e.g. due to interchanged hands or multiple acquisition of the same hand finger. Note, that it is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available.
	- a. In case
		- **•** the comparison of any fingerprint of the current slap with any previously accepted fingerprint of a previous slap or
		- **•** the comparison of any fingerprint of the current slap with another fingerprint of the current slap

is successful, the uniqueness check SHALL raise an alert.

- b. In case the comparisons of all fingerprints of the current slap with all fingerprints of previous slaps are not successful, the uniqueness check SHALL NOT show a warning.
- 5. Generally, a slap classifier SHALL be used for the captured slap image to detect the capture of the wrong slap. It SHALL be configurable to switch the classifier off or in evaluation mode (logging of result wi thout showing the result/error to the operator). Note, that the slap classifier is only required for 4 finger slaps. Other acquisitions currently do not require the corresponding FM.
	- a. If the result of the classification concludes that the acquired slap mismatches the expected slap, an error SHALL be reported.
	- b. If the result of the classification concludes that the acquired slap matches the expected slap, no error SHALL be reported.

If the quality check of the third capture attempt fails (counter *i* is set to 3), the best of the captured slaps SHALL be identified according to the corresponding [QA](#page-51-11) Function Module and temporarily stored along with the corresponding information.

The process SHALL be supervised by an operator.

At the end of the process the operator decides on one of the three options:

- 1. Use the acquired slap.
- 2. Recapture the current slap. The counter SHALL be reset to *i* = 1.

3. Restart the total slap acquisition workflow.

The operator SHALL have the following veto options:

- **•** Select none of the captured slaps despite sufficient quality.
- **•** Select a slap of insufficient quality from the acquisition process.

At any point of the process the operator MAY decide to acquire any finger of the slap individually.

<span id="page-20-0"></span>![](_page_20_Figure_6.jpeg)

**Figure 3.10.** Partial Application Process Task "Capture Slap Supervised"

#### **3.4.2.1. PAP Task ACQ-FPP-SV-2: Capture Plain Fingerprint Supervised**

[Figure 3.5](#page-14-1) depicts the basic supervised capture process for a plain fingerprint capture. A plain fingerprint capture can be part of more complex acquisition processes, e.g. a ten finger acquisition by the 4-1-4-1 capture process. The plain fingerprint capture is described in detail subsequently. The quality assessment is conducted according to the requirements of the applicable [FM Category Quality Assessment.](#page-27-0)

- 1. The counter variable for the number of attempts capturing current fingerprints SHALL be initia lized as *i* = 1.
- 2. The fingerprint image SHALL be retrieved from hardware. While the image is retrieved from hardware, [PAD](#page-51-10) SHALL be performed. Note: The operator SHALL have the option to manually conduct the capture of fingerprint(s).
- 3. The fingerprint SHALL be quality assessed and the captured fingerprint and parameter data (e.g. quality values) SHALL be temporarily stored.
- 4. In case the quality requirements for the fingerprint are not met, the capture SHALL be repeated up to two times (i.e. the acquisition of a finger consists of a maximum of three capture attempts). The counter SHALL be set to *i* = *i* + 1.
- 5. A uniqueness check SHALL be conducted for the captured fingerprint image to detect the capture of wrong fingers, e.g. due to interchanged hands or multiple acquisition of the same hand finger. Note: It is RE COMMENDED to conduct the uniqueness check as early as possible after a fingerprint image is available.
	- a. In case the comparison of current fingerprint with any previously captured is success ful, the uniqueness check SHALL report an alert.
	- b. In case the comparison of current fingerprint with any previously captured is not suc cessful, the uniqueness check SHALL NOT report an alert.
- 6. The acquired finger prints and the results of [PAD,](#page-51-10) [QA](#page-51-11) and uniqueness check SHALL be displayed to the operator.

If the quality check of the third capture attempt fails (counter *i* is set to 3), the best of the captured fingerprint images SHALL be identified according to the corresponding [QA](#page-51-11) Function Module and temporarily stored along with the corresponding information.

The process SHALL be supervised by an operator.

At the end of the process the operator decides on one of the three options:

- 1. Use the acquired fingerprint.
- 2. Recapture the current fingerprint. The counter SHALL be reset to *i* = 1.
- 3. Restart the [Figure 3.5](#page-14-1) acquisition workflow.

The operator SHALL have the following veto options:

- **•** Select none of the captured fingerprints despite sufficient quality.
- **•** Select a fingerprint of insufficient quality from the acquisition process.

<span id="page-21-0"></span>![](_page_21_Figure_9.jpeg)

**Figure 3.11.** Partial Application Process Task "Capture Plain Fingerprint Supervised"

## <span id="page-22-0"></span>**4. Function Modules**

This chapter lists all Function Modules for the defined Application Profiles.

## <span id="page-22-1"></span>**4.1. FM Category Acquisition Hardware**

Devices that are used for digitising physical, representable biometric characteristics are called [Acquisition](#page-51-12) [Hardware \(AH\).](#page-51-12) Digital cameras to capture images of the face, fingerprint sensors, or signature tablets can be named as examples.

## <span id="page-22-2"></span>**4.1.1. FM AH-FI-DC**

This Function Module describes the requirements for facial image cameras and physical setups that are used to obtain facial images.

#### **4.1.1.1. Requirements**

- **•** The minimum physical resolution of the camera SHALL allow a cropping of an image to 1200 x 1600 pixels without any upscaling. Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed.
- **•** Adequate image quality to meet the requirements of [\[BIB\\_ISO\\_FACE\]](#page-52-2) SHALL be provided.
- **•** The physical and environmental conditions for capturing facial images, such as the positioning of ca mera, proper lighting of the face and a uniform background as described in [\[BIB\\_ISO\\_FACE\]](#page-52-2) SHALL be complied with.
- **•** The camera system SHALL be able to capture images in colour (24 bit RGB). Note, this requirement is OP TIONAL for scenarios where only a facial verification is performed.

## <span id="page-22-3"></span>**4.1.2. FM AH-FP-OPT**

This Function Module describes the requirements for optical high quality fingerprint scanners (single finger and multi finger).

#### **4.1.2.1. Requirements**

- **•** For the acquisition of the fingerprints, optical sensors using the principal of frustrated total reflection or direct contact (the imaging system is the sensor surface, typically separated by a transparent protection layer) according to the certification requirements of [\[BIB\\_ISO\\_FINGER\]](#page-52-1) (especially this means a resolution of 500 ppi or 1000 ppi) SHALL be used exclusively.
- **•** For the acquisition of the fingerprints, only devices are permitted which meet the following requirements (in analogy to [\[BIB\\_EBTS/F\]](#page-52-3)). Notwithstanding, a capturing area of at minimum 16 mm width and 20 mm height is REQUIRED (deviating from table F 1 in [\[BIB\\_EBTS/F\]\)](#page-52-3) for single finger scanners.

#### **4.1.2.1.1. Grey Scale Linearity**

When measuring a stepped series of uniform target reflectance patches ("step tablet") that substantially covers the scanner's grey range, the average value of each patch SHALL be within 7.65 grey levels of a linear, least squares regression line fitted between target reflectance patch values (independent variable) and scanner out put grey levels of 8 bit resolution (dependent variable).

#### **4.1.2.1.2. Resolution and Geometrical Accuracy**

Resolution: The scanner's final output fingerprint image SHALL have a resolution, in both sensor detector row and column directions, in the range: (*R ¡* 0*:*01*R*) to (*R* + 0*:*01*R*). The magnitude of *R* is either 500 ppi or 1000 ppi; a scanner MAY be certified at either one or both of these resolution levels. The scanner's true optical resolution SHALL be greater than or equal to *R*.

Across-Bar geometric accuracy: When scanning a 1.0 cy/mm, multiple parallel bar target, in both vertical bar and horizontal bar orientations, the absolute value of the difference (*D*) between the actual distance across parallel target bars (*X*), and the corresponding distance measured in the image (*Y*) SHALL NOT exceed the following values for at least 99 % of the tested cases in each print block measurement area and in each of the two directions:

**•** for 500 ppi scanners:

*D ·* 0*:*0007, for 0*:*00 *< X ·* 0*:*07 and

- *D ·* 0*:*01*X*, for 0*:*07 *· X ·* 1*:*50
- **•** for 1000 ppi scanners:

*D ·* 0*:*0005, for 0*:*00 *< X ·* 0*:*07 and

*D ·* 0*:*0071*X*, for 0*:*07 *· X ·* 1*:*50

where *D* = *jY ¡ Xj*, *X* = actual target distance, *Y* = measured image distance (*D; X; Y* are in inches).

Along-Bar geometric accuracy: When scanning a 1.0 cy/mm, multiple parallel bar target, in both vertical bar and horizontal bar orientations, the maximum difference in the horizontal or vertical direction, respectively, between the locations of any two points within a 1.5 inch segment of a given bar image, SHALL be less than 0.016 inches for at least 99 % of the tested cases in each print block measurement area and in each of the two orthogonal directions.

#### **4.1.2.1.3. Contrast Transfer Function**

The spatial frequency response SHALL be measured using a binary grid target (Ronchi-Grating), denoted as [contrast transfer function \(CTF\)](#page-51-13) measurement. When measuring the bar [CTF,](#page-51-13) it SHALL meet or exceed the minimum modulation values defined by equation [Equation 4.1](#page-23-0) or equation [Equation 4.2, in both the de](#page-23-1) tector's row and detector's column directions, and over any region of the scanner's field of view. [CTF](#page-51-13) values computed from equations [Equation 4.1](#page-23-0) and [Equation 4.2 for nominal test frequencies are given in the fol](#page-23-1) lowing table. None of the [CTF](#page-51-13) modulation values measured at specification spatial frequencies SHALL exceed 1.05. The output bar target image SHALL NOT exhibit any significant amount of aliasing. It is NOT REQUIRED that the bar target contains the exact frequencies listed in [Table 4.1,](#page-23-2) however, the target does need to cover the listed frequency range and contain bar patterns close to each of the listed frequencies.

The following equations are used to obtain the minimum acceptable [CTF](#page-51-13) modulation values when using bar targets that contain frequencies not listed in [Table 4.1](#page-23-2):

<span id="page-23-0"></span>**•** 500 ppi scanner, for f = 1.0 to 10.0 cy/mm:

$$CTF = 3.04105 \cdot 10^{-4} \cdot f^2 - 7.99095 \cdot 10^{-2} \cdot f + 1.02774 \tag{4.1}$$

<span id="page-23-1"></span>**•** 1000 ppi scanner, for f = 1.0 to 20.0 cy/mm:

$$CTF = -1.85487 \cdot 10^{-5} \cdot f^3 + 1.41666 \cdot 10^{-3} \cdot f^2 - 5.73701 \cdot 10^{-2} \cdot f + 1.01341 \tag{4.2}$$

For a given bar target, the specification frequencies include all of the bar frequencies which that target has in the range 1 to 10 cy/mm (500 ppi scanner) or 1 to 20 cy/mm (1000 ppi scanner).

<span id="page-23-2"></span>

| Frequency [cy/mm] | Minimum Modulation for 500 ppi<br>scanners | Minimum Modulation for<br>1000 ppi scanners | Maximum Modulation |
|-------------------|--------------------------------------------|---------------------------------------------|--------------------|
| 1.0               | 0.948                                      | 0.957                                       | 1.05               |

| Frequency [cy/mm] | Minimum Modulation for 500 ppi<br>scanners | Minimum Modulation for<br>1000 ppi scanners | Maximum Modulation |
|-------------------|--------------------------------------------|---------------------------------------------|--------------------|
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

#### **4.1.2.1.4. Signal-to-Noise Ratio and the Grey–Level Uniformity**

The white [signal-to-noise ratio \(SNR\)](#page-51-14) and black [SNR](#page-51-14) SHALL each be greater than or equal to 125.0, in at least 97 % of respective cases, within each measurement area.

The grey level uniformity is defined for the three following cases:

- **•** Adjacent row, column uniformity: At least 99 % of the average grey levels between every two adjacent quar ter-inch long rows and 99 % between every two adjacent quarter-inch long columns, within each imaged area, SHALL NOT differ by more than 1.0 grey levels when scanning a uniform low reflectance target, and SHALL NOT differ by more than 2.0 grey levels when scanning a uniform high reflectance target.
- **•** Pixel to pixel uniformity: For at least 99.9 % of all pixels within every independent 0.25 inch by 0.25 inch area located within each imaged area, individual pixel's grey level SHALL NOT vary from the average by more than 22.0 grey levels, when scanning a uniform high reflectance target, and SHALL NOT vary from the average by more than 8.0 grey levels, when scanning a uniform low reflectance target.
- **•** Small area uniformity: For every two independent 0.25 inch by 0.25 inch areas located within each imaged area, the average grey levels of the two areas SHALL NOT differ by more than 12.0 grey levels when scanning a uniform high reflectance target, and SHALL NOT differ by more than 3.0 grey levels when scanning a uniform low reflectance target.

#### **4.1.2.1.5. Grey Scale Range of Fingerprint Images**

A fingerprint scanner operating at 500 ppi or 1000 ppi, SHALL perform the following sets of live scans:

- **•** For a standard roll and plain finger live scanner: capture complete set of fingerprints from each 10 sub jects; i.e. 10 rolls (all 5 fingers from each hand), 2 plain thumb impressions, and 2 plain 4-finger impressions.
- **•** For a palm scanner component of a live scan system: capture left and right palms from each of 10 subjects.
- **•** For an identification flat live scanner: capture left and right 4-finger plain impressions and dual thumb plain impressions from each of 10 subjects.

Within the histogram of each image all grey values with at least 5 Pixels in this are counted. The histo gram SHALL show no break and no other artefact. At least 80 % of the captured individual fingerprint images SHALL have a grey scale dynamic range of at least 200 grey levels, and at least 99% SHALL have a dynamic range of at least 128 grey levels.

## <span id="page-25-0"></span>**4.2. FM Category Acquisition Software**

The Function Module category [Acquisition Software \(AS\) contains all functionality regarding image proces](#page-51-15) sing for biometric purposes. Therefore, these Function Modules usually contains device driver software for the acquisition hardware or, in general, software that is very close to the physical hardware such as firmware. Furthermore, colour management and image enhancement mechanisms are part of this software layer.

## <span id="page-25-1"></span>**4.2.1. FM AS-FI-DC**

This Function Module describes the requirements and interfaces for acquisition software used for facial image cameras in order to obtain digitised images.

#### **4.2.1.1. Requirements**

- **•** In regard to the application scenario an adequate resolution of the camera SHALL be chosen to acquire a facial image of at least 1200 x 1600 pixels with an inter eye distance of at least 120 pixels.
- **•** The images SHALL be captured and stored in colour (24 bit RGB). Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed.
- **•** In normal mode of operation, no compression artefacts SHALL be detectable in the image.

#### **4.2.1.2. Recommendations**

- **•** The image data SHOULD be provided without any compression or with lossless compression. If the acqui sition device does not support a lossless mode, the image MAY alternatively be provided with the minimal level of compression possible.
- **•** Acquisition software that supports calibration procedures for the respective digital camera SHOULD be used (in particular colour management).

## <span id="page-25-2"></span>**4.2.2. FM AS-FP-MF**

This Function Module describes the requirements and interfaces for acquisition software for multi finger scanners.

#### **4.2.2.1. Requirements**

- **•** The image provided by acquisition software SHALL meet the criteria of fingerprints as described in [\[BIB\\_ISO\\_FINGER\]](#page-52-1). The requirements according to the certification requirements of [\[BIB\\_ISO\\_FINGER\]](#page-52-1) SHALL be met.
- **•** For the acquisition process, a pre-qualification of the fingerprints to prefer high quality SHALL be used. The activation of the acquisition SHALL occur automatically. The capture SHOULD prefer the highest quality image of a sequence.
- **•** This functionality MAY be part of the hardware firmware and MAY NOT be available as separate software component.
- **•** The thresholds of the pre-qualification for performing a capture SHALL be documented by the vendor.
- **•** If the acquisition software allows multiple thresholds for pre-qualification, it SHALL be configurable by the system administrator.
- **•** In case further requirements demand for an export of the uncompressed fingerprint image data BMP SHALL be used as image format.

#### **4.2.2.2. Recommendations**

In order to prevent unwanted duplicate acquisitions of the same fingers or slaps, the software SHOULD start the acquisition process not before the fingers from a previous acquisition have been removed from the sensor surface.

## <span id="page-26-1"></span>**4.2.3. FM AS-FP-SLP**

This Function Module describes the requirements and interfaces for acquisition software for four finger slap scanners running in slap acquisition mode.

#### **4.2.3.1. Requirements**

- **•** It SHALL be classified by software whether the left or right hand slap has been acquired. Thumb clas sification is NOT REQUIRED. This MAY be achieved by using the acquired fingerprint images or with the help of further sensors or images (e.g. surveillance) if available.
- **•** The classification SHALL have a performance of at least 99% i.e. 99% of all left hand slaps SHALL be correctly classified as left hand slaps and 99% of all right hand slaps SHALL be correctly classified as right hand slaps.
- **•** In case the classification can return more than two possible results, e.g. "left", "right", or "unknown", a clas sification threshold SHALL be configurable.
- **•** It SHALL be configurable to switch the classification off or to only use the classification result information for evaluation purposes.

## <span id="page-26-0"></span>**4.3. FM Category Biometric Image Processing**

The Function Module [Biometric Image Processing \(BIP\) provides the extraction of all relevant biometric in](#page-51-16) formation from the data which is provided by the acquisition hardware or the acquisition software layer. Thus, a proprietary data block is transformed to a digital image of a biometric characteristic. In general, specific image processing for biometric characteristics is addressed here.

## <span id="page-26-2"></span>**4.3.1. FM BIP-FI-APP**

This Function Module describes requirements and interfaces for biometric image processing with respect to the output of (integrated) camera systems to obtain a facial image that fulfils the requirements.

#### **4.3.1.1. Requirements**

- **•** The colour depth SHALL be 24 bit RGB. Note, this requirement is OPTIONAL for scenarios where only a facial verification is performed.
- **•** The face SHALL be fully visible in the foreground of the provided image.
- **•** The minimum distance between both eyes for capture positions of the biometric subject in the preferred area of the camera range SHALL be 120 pixels.
- **•** The face SHALL be cropped and de-rotated from the overall scene in the captured image. Post processing of the image orientation in regard to pitch and jaw (see [\[BIB\\_ISO\\_FACE\]](#page-52-2)) SHALL NOT be done.
- **•** The size of the face within the image SHALL be according to the geometric requirements of [\[BIB\\_ISO\\_FACE\]](#page-52-2) and [QA](#page-51-11) category of this [TR.](#page-51-3)

## <span id="page-26-3"></span>**4.3.2. FM BIP-FP-APP**

This Function Module describes requirements and interfaces for the biometric image processing to provide up to four single finger images for the subsequent reference storage or biometric comparison.

#### **4.3.2.1. Requirements**

- **•** The resolution of the fingerprint image has to be 500 ppi corresponding to the certification requirements of [\[BIB\\_ISO\\_FINGER\]](#page-52-1) and, therefore, MAY differ from the scan resolution.
- **•** Depending on the call, as many individual fingerprints as requested SHALL be extracted from the input image and provided as single fingerprints.

Note: Segmentation for single finger scanners is OPTIONAL.

For this segmentation process, the following requirements SHALL be fulfilled:

- **•** ability to accept fingerprints which are rotated in the same direction up to 45 degrees
- **•** in the same direction rotated fingerprints have to be corrected to be vertical
- **•** segment the first part over the finger (fingertip)
- **•** segmentation has to occur on uncompressed data
- **•** Fingerprint images SHALL NOT be upscaled. If the targeted system or database requires fingerprint images of higher size than captured the fingerprint image SHALL be evenly surrounded with white pixels to reach the desired size.

## <span id="page-27-0"></span>**4.4. FM Category Quality Assessment**

The Function Module [Quality Assessment contains all kinds of mechanisms and procedures to check the qua](#page-51-11) lity of the biometric data or to select the best quality data out of multiple instances.

## <span id="page-27-1"></span>**4.4.1. FM QA-FI-GENERIC**

This Function Module describes requirements and interfaces for software that is used for quality assessment of digital images to ensure compliance with [\[BIB\\_ISO\\_FACE\].](#page-52-2)

#### **4.4.1.1. Requirements**

#### **4.4.1.1.1. General Requirements**

The [QA](#page-51-11) module is used for the software-based automatic check of the conformance of the picture to [\[BIB\\_ISO\\_FACE\]](#page-52-2) after the digitisation. Thereby, the geometric properties of the picture as well as the digital parameters of the image are analysed and rated.

The standard which is relevant for the quality of facial images [\[BIB\\_ISO\\_FACE\] hierarchically describes requi](#page-52-2) rements for the facial images. In the following, full frontal images are expected.

The [QA](#page-51-11) module SHALL analyse and evaluate all of the quality criteria listed in [Table 4.2](#page-28-0). For the criteria marked with "M", the quality values SHALL be provided while quality values for the criteria marked with "O" MAY be provided in the defined format according to the respective criteria.

A criterion is fulfilled if its calculated value is in the given threshold boundaries.

Based on the results of all provided quality criteria the [QA](#page-51-11) module SHALL reject or approve the picture. The total result is true if every single quality criteria is fulfilled.

The [QA](#page-51-11) module SHALL provide an interface for conformance testing where a single image (JPEG or JPEG2000 encoded) can be processed and the calculated values and configuration data are returned. The image type to process depends on the image type requirements of the application profile to implement.

The [QA](#page-51-11) module SHOULD operate on cropped images retrieved from the image processing according to [FM](#page-26-0) [Category Biometric Image Processing.](#page-26-0)

<span id="page-28-0"></span>

| ID                        | Criterion                                              | ISO-Ref., compare<br>[BIB_ISO_FACE] | Mandatory / Optional | Unit/Range               |
|---------------------------|--------------------------------------------------------|-------------------------------------|----------------------|--------------------------|
|                           | Pose of the head                                       |                                     |                      |                          |
| 1.1                       | Yaw, neck axis                                         | 7.2.2                               | O                    | Degrees                  |
| 1.2                       | Pitch, ear axis                                        | 7.2.2                               | O                    | Degrees                  |
| 1.3                       | Roll, nose axis                                        | 7.2.2                               | M                    | Degrees                  |
|                           | Facial expression                                      |                                     |                      |                          |
| 2.1                       | Neutral expression                                     | 7.2.3                               | O                    | Arbitrary units          |
| 2.2                       | Mouth closed                                           | 7.2.3                               | M                    | Arbitrary units          |
| 2.3                       | No raised eyebrows                                     | 7.2.3                               | O                    | Arbitrary units          |
| Eyes                      |                                                        |                                     |                      |                          |
| 3.1                       | Eyes open                                              | 7.2.3                               | O                    | Arbitrary units          |
| 3.2                       | No occlusion (glasses,<br>hair, eye patch)             | 7.2.11 7.2.12                       | O                    | Arbitrary units          |
| 3.3                       | Eyes looking to the ca<br>mera                         | 7.2.3                               | O                    | Arbitrary units          |
| Background                |                                                        |                                     |                      |                          |
| 4.1                       | Uniformity (plainness,<br>no textures, colour)         | 7.2.6 A.2.4.3                       | O                    | Arbitrary units          |
| 4.2                       | No shadows                                             | 7.2.6 A.2.4.2                       | O                    | Arbitrary units          |
| 4.3                       | No further people / ob<br>jects                        | 7.2.4 A2.3                          | O                    | Arbitrary units          |
| Geometry                  |                                                        |                                     |                      |                          |
| 5.1                       | Image height                                           | 8.3.5 A.3.1.1 A.3.2.1               | M                    | In pixel                 |
| 5.2                       | Image width                                            | 8.3.4 A.3.1.1 A.3.2.1               | M                    | In pixel                 |
| 5.3                       | Ratio: Head width /<br>image width                     | 8.3.4                               | M                    | As ratio between 0 and 1 |
| 5.4                       | Ratio: Head height /<br>image height                   | 8.3.5                               | M                    | As ratio between 0 and 1 |
| 5.5                       | Vertical position of the<br>face                       | 8.3.3                               | M                    | As ratio between 0 and 1 |
| 5.6                       | Horizontally centred<br>face                           | 8.3.2                               | M                    | As ratio between 0 and 1 |
| 5.7                       | Eye distance                                           | 8.4.1 A3.1.1                        | M                    | In pixel                 |
| Subject lighting          |                                                        |                                     |                      |                          |
| 6.1                       | Equally distributed<br>lighting                        | 7.2.7                               | O                    | Arbitrary units          |
| 6.2                       | No shadows over the<br>face nor in the eye-so<br>ckets | 7.2.8 7.2.9                         | O                    | Arbitrary units          |
| 6.3                       | No hot spots on skin                                   | 7.2.10                              | O                    | Arbitrary units          |
| 6.4                       | No effects on glasses                                  | 7.2.11                              | O                    | Arbitrary units          |
| Photographic requirements |                                                        |                                     |                      |                          |
| 7.1                       | Proper exposure                                        | 7.3.2                               | M                    | Arbitrary units          |

| ID  | Criterion                                   | ISO-Ref., compare<br>[BIB_ISO_FACE] | Mandatory / Optional | Unit/Range                                                                                                                                                          |
|-----|---------------------------------------------|-------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 7.2 | Focus and depth of field                    | 7.3.3                               | M                    | Arbitrary units                                                                                                                                                     |
| 7.3 | No unnatural colours                        | 7.3.4                               | O                    | Arbitrary units                                                                                                                                                     |
| 7.4 | No red eyes                                 | 7.3.4                               | O                    | Arbitrary units                                                                                                                                                     |
| 7.5 | Colour space                                | 7.4.2.3                             | M                    | According to [BIB_ISO_FACE]<br>using Decimal notation (e.g.<br>"1" for RGB-24bit, "2" for<br>YUV422 or "3" for 8bit-grey<br>scale and "0" for unknown or<br>errors) |
| 7.6 | Grey scale density and<br>colour saturation | 7.4.2.1 7.4.2.2                     | M                    | Counted numbers of intensi<br>ty values existing within the<br>image                                                                                                |

**Table 4.2** Mapping of Relevant Quality Criteria

#### **4.4.1.1.2. Requirements Identification of the Best Capture**

When multiple captures of facial images and their corresponding set of quality metrics are passed, the best capture of the captures SHALL be identified as described in the following:

- 1. If exactly one facial image conforms to more mandatory criteria than all other images, this image is chosen.
- 2. If more than one image is conform to most mandatory criteria than all other images, the most recent image among the facial images fulfilling the most criteria SHALL be choosen. If no timestamp is available, a random selection SHALL be applied among the facial images fulfilling the most criteria.

## <span id="page-29-0"></span>**4.4.2. FM QA-FI-IMA**

This Function Module describes requirements and interfaces for software that is used for quality assessment of digital images within the context of immigration authorities to ensure compliance with [\[BIB\\_ISO\\_FACE\].](#page-52-2)

#### **4.4.2.1. Requirements**

The threshold requirements of [Table 4.3](#page-29-1) SHALL be in place within the context of immigration authorities. These thresholds relate to the generic quality criteria of [FM QA-FI-GENERIC.](#page-27-1)

<span id="page-29-1"></span>

| ID  | Criterion                                    | Minimum | Maximum | Unit/Range               |  |
|-----|----------------------------------------------|---------|---------|--------------------------|--|
|     | Image ratio 4:3 (Image height / image width) |         |         |                          |  |
| 1.1 | Yaw, neck axis                               | -5      | 5       | Degrees                  |  |
| 1.2 | Pitch, ear axis                              | -5      | 5       | Degrees                  |  |
| 1.3 | Roll, nose axis                              | -8      | 8       | Degrees                  |  |
| 5.1 | Image height                                 | 800     | 1600    | In pixel                 |  |
| 5.2 | Image width                                  | 600     | 1200    | In pixel                 |  |
| 5.3 | Ratio: Head width / image width              | 0,5     | 0,75    | As ratio between 0 and 1 |  |
| 5.4 | Ratio: Head height / image height            | 0,6     | 0,9     | As ratio between 0 and 1 |  |
| 5.5 | Vertical position of the face                | 0,3     | 0,5     | As ratio between 0 and 1 |  |
| 5.6 | Horizontally centred face                    | 0,45    | 0,55    | As ratio between 0 and 1 |  |
| 5.7 | Eye distance                                 | 120     | -       | In pixel                 |  |

**Table 4.3** Quality Threshold Requirements for Facial Images for Immigration Authorities

## <span id="page-30-0"></span>**4.4.3. FM QA-FP-APP**

This Function Module describes requirements for the quality assessment of plain or rolled fingerprints inclu ding quality assessment of single fingerprint, respectively slap and selection of the best quality image out of multiple instances.

#### **4.4.3.1. Requirements**

#### **4.4.3.1.1. Quality Algorithm**

As quality algorithm, the latest version of [NIST Fingerprint Image Quality 2 \(NFIQ2\)](#page-51-17) [\[BIB\\_NFIQ2\]](#page-52-4) SHALL be used, and therefore, images with 1000 ppi SHALL be resampled to 500 ppi before application of [NFIQ2](#page-51-17). Note, that the resampled image SHALL be used for [NFIQ2](#page-51-17) only. As resulting quality value, the output value of [NFIQ2](#page-51-17) in the integer range of [0,100] SHALL be used. In the case of failure, the returned error code 255 indicates that a computation was not successful and the resulting quality value SHALL be returned as the result, as described in [Section 4.9.1.](#page-39-2)

#### **4.4.3.1.2. Quality Evaluation Process for a Slap or Single Fingerprint**

In case a single captured fingerprint, respectively slap is passed, the [QA](#page-51-11) SHALL be performed as described in the following. Beforehand, the fingerprints of the passed capture SHALL be segmented (considering missing fingers). Note, that in verification applications, a [QA](#page-51-11) is not conducted. Thus, every slap capture is considered sufficient and no thresholds are specified here. Skipping the [QA](#page-51-11) is expected to accelerate the overall process. OPTIONALLY, a [QA](#page-51-11) can be performed.

- 1. For each segmented fingerprint *FA;j* of a passed capture *A*, a quality value *QA;j* is calculated with *j 2* 1*; :::;* 10 (up to 4 fingers in one slap) representing the specific finger code according to [\[BIB\\_ISO\\_FIN](#page-52-1) [GER\].](#page-52-1)
- 2. The resulting quality value is compared with the defined threshold *T Hj* for this finger. The application specific thresholds as defined in the following section apply.
- 3. In case all of the fingerprint qualities reach the specified threshold (i.e. *8j; QA;j ¸ T Hj* ), the boolean infor mation *b* = 1 indicates a successful capture.
- 4. In case one or more fingerprints do not reach the threshold (i.e. *9j; QA;j < T Hj* ), the boolean information *b* = 0 indicates insufficient quality of the capture.
- 5. For the segmented fingerprint *FA;j* the corresponding parameter set *PA;j* is compiled and returned.
- 6. As a result of the [QA](#page-51-11) process, the following values are returned to the calling process:
	- a. the boolean information *b*
	- b. the parameter set *PA* = *QA;j ; :::; QA;l* with *j; l 2* 1*; :::;* 10 representing the specific finger code

#### **4.4.3.1.3. Identification of the Best Capture out of Multiple Captures**

When multiple captures *Ai ;i 2* 1*; :::; n* and their corresponding set of segmented fingerprints *FAi ;j* with *j 2* 1*; :::;* 10 representing the specific finger code according to [\[BIB\\_ISO\\_FINGER\]](#page-52-1) are passed, the best of the captures SHALL be identified as described in the following section:

- 1. For each segmented fingerprint *FAi ;j* of a passed capture *Ai* , the quality value *QAi ;j* is calculated with re presenting the specific finger code according to [\[BIB\\_ISO\\_FINGER\]](#page-52-1).
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
- 3. As a result of the [QA](#page-51-11) process, the following values are returned:
	- a. the identifier *i* representing the capture yielding the best quality
	- b. the parameter set *PA* = *QAi;j ; QAi;l* with *j; l 2* 1*; :::*10.

#### **4.4.3.1.4. Thresholds for Plain Fingerprints for Enrolment Purposes**

The following thresholds as indicated in [Table 4.4](#page-32-0) apply when fingerprints are captured plain for enrolment purposes. Note, the thresholds in [Table 4.4](#page-32-0) do not apply to plain captured fingerprint in enrolment scenarios where the plain fingerprints are captured for control purpose of rolled fingerprints. In that case, thresholds as indicated in [Table 4.5](#page-32-1) apply for the plain fingerprints.

<span id="page-32-0"></span>

| Finger Position     | Finger Code | NFIQ2 Threshold |
|---------------------|-------------|-----------------|
| Right thumb         | 1           | 30              |
| Right index finger  | 2           | 30              |
| Right middle finger | 3           | 20              |
| Right ring finger   | 4           | 10              |
| Right little finger | 5           | 10              |
| Left thumb          | 6           | 30              |
| Left index finger   | 7           | 30              |
| Left middle finger  | 8           | 20              |
| Left ring finger    | 9           | 10              |
| Left little finger  | 10          | 10              |

**Table 4.4** Thresholds for Plain Fingerprints for Enrolment Purposes

#### **4.4.3.1.5. Thresholds for Plain Control Fingerprints and Fingerprints used for Identification Searches**

The following thresholds as indicated in [Table 4.5](#page-32-1) apply when fingerprints are captured plain for the purpose of control slaps (used for comparison with rolled prints) or use in identification searches. Note, the thres holds in [Table 4.5](#page-32-1) do apply to plain captured fingerprint in enrolment scenarios where the plain fingerprints are captured for control purpose of rolled fingerprints.

<span id="page-32-1"></span>

| Finger Position     | Finger Code | NFIQ2 Threshold |
|---------------------|-------------|-----------------|
| Right thumb         | 1           | 20              |
| Right index finger  | 2           | 20              |
| Right middle finger | 3           | 20              |
| Right ring finger   | 4           | 10              |
| Right little finger | 5           | 10              |
| Left thumb          | 6           | 20              |
| Left index finger   | 7           | 20              |
| Left middle finger  | 8           | 20              |
| Left ring finger    | 9           | 10              |
| Left little finger  | 10          | 10              |

**Table 4.5** Thresholds for Plain Control /Identification Fingerprints

#### **4.4.3.1.6. Thresholds for Rolled Fingerprints**

The following thresholds as indicated in [Table 4.6](#page-32-2) apply when fingerprints are captured rolled for enrolment purposes.

<span id="page-32-2"></span>

| Finger Position     | Finger Code | NFIQ2 Threshold |
|---------------------|-------------|-----------------|
| Right thumb         | 1           | 20              |
| Right index finger  | 2           | 15              |
| Right middle finger | 3           | 15              |
| Right ring finger   | 4           | 10              |

| Finger Position     | Finger Code | NFIQ2 Threshold |
|---------------------|-------------|-----------------|
| Right little finger | 5           | 5               |
| Left thumb          | 6           | 20              |
| Left index finger   | 7           | 15              |
| Left middle finger  | 8           | 15              |
| Left ring finger    | 9           | 10              |
| Left little finger  | 10          | 5               |

**Table 4.6** Thresholds for Rolled Fingerprints

## <span id="page-33-0"></span>**4.5. FM Category Presentation Attack Detection**

The objective of the Function Module [Presentation Attack Detection](#page-51-10) is to avoid presentations with the goal to subvert an enrolment, verification of identification process.

## <span id="page-33-1"></span>**4.5.1. FM PAD-FP-APP**

This Function Module describes requirements for [PAD](#page-51-10) in the context of acquisition biometric charac teristics of fingerprints.

## **4.5.1.1. Requirements**

#### **4.5.1.1.1. General Requirements**

The capture system SHALL contain a [PAD](#page-51-10) subsystem according to [\[BIB\\_ISO\\_PAD\\_1\] detecting spoofing at](#page-52-5) tempts using artefacts by which an attacker is trying to establish a different biometric characteristic as probe in the verification or identification process.

The [PAD](#page-51-10) subsystem MAY consist of hardware and software (e.g. the used fingerprint scanner have addi tional sensors designed for this purpose).

According to the used fingerprint scanner, [PAD](#page-51-10) subsystem SHALL be able to detect artefact classes listed in the following:

- **•** Fingertips, created in different thicknesses
- **•** Single fingers (massive)

The [PAD](#page-51-10) subsystem SHALL be able to detect all typical artefact material types listed in the following:

- **•** Artefacts created from different kinds of silicon
- **•** Artefacts created from different kinds of latex
- **•** Artefacts created from different kinds of gelatine
- **•** Artefacts created from different kinds of wood glue
- **•** Artefacts created from different kinds of window painting
- **•** Artefacts created from different kinds of paper

each in different colourings.

Also, the detection subsystem SHALL be adequate to the usage setting in correspondence with the security requirements in question. The performance MAY be described by a risk analysis for every considered attack type. The current version of [\[BIB\\_ISO\\_PAD\\_3\]](#page-52-6) SHALL be taken into account.

The [PAD SHALL be conducted both in supervised acquisition scenarios, e.g. a counter scenario, and un](#page-51-10) supervised acquisition scenarios, e.g. in [self-service system \(SSS\)](#page-51-18) scenarios. Thereby, the [PAD SHALL be con](#page-51-10) ducted for all acquisition purposes, e.g. enrolment, identification and verification.

#### **4.5.1.1.2. Integration Requirements**

The [PAD](#page-51-10) subsystem SHALL be independent of the regular capture subsystem.

It SHALL signal its detection results in the form of a [PAD](#page-51-10) score for each finger individually. Additionally, an overall result SHALL be returned to the calling application.

The score for each finger SHALL be a normalized as double in the range [0,1] using at least ten uniformly distributed interim values, where 1 indicates bona fide and 0 presentation attack. A binary score SHALL NOT be used (e.g. True or False, 1 or 0). The [PAD](#page-51-10) subsystem SHALL additionally provide detailed information about the scores of the [PAD.](#page-51-10)

The overall result SHALL be a boolean value (e.g. True or False). The value SHALL be true, if any of the fingers individual result triggers a [PAD](#page-51-10) alarm.

Even if the Function Module is used within a comparison scenario, the detection result SHALL be signaled in any case, independent from any biometric matching score. Also, the omission of the detection result SHALL be signalled in any case.

The [PAD](#page-51-10) result SHALL correspond to the respective finger capture attempt.

Note, that an image of the fingerprint or slap in question SHALL be acquired independently of a possible PAD alarm.

#### **4.5.1.1.3. Maintenance Requirements**

As new technologies and new attack mechanisms are developed over time, the [PAD](#page-51-10) subsystem SHALL be updated and checked whenever necessary, so it stays capable against old and new attacks and attack types.

#### **4.5.1.1.4. Certification Requirements**

To ensure comparable performance of presentation attack detection subsystems, the system SHALL be certi fied either under the Common Criteria Agreement according to one of following Protection Profiles:

- **•** BSI-CC-PP-0063-2010: Fingerprint Spoof Detection Protection Profile (FSDPP)
- **•** BSI-CC-PP-0062-2010: Fingerprint Spoof Detection Protection Profile based on Organisational Security Policies (FSDPP\_OSP)
- **•** BSI-CC-PP-0118-2022: Common Criteria Protection Profile Biometric Mechanisms Protection Profile (BMPP), Version 2.0, base PP and at least the functional package PAD

or according to BSI TR-03122: Conformance Test Specification for Technical Guideline TR-03121 - Biometrics for Public Sector Applications, respectively this technical guideline.

## <span id="page-34-0"></span>**4.6. FM Category Compression**

The objective of the Function Module [Compression \(COM\)](#page-51-19) is to keep the biometric data within a feasible size without losing too much quality for a biometric verification or identification.

## <span id="page-34-1"></span>**4.6.1. FM COM-FI-GENERIC**

The following requirements are generic and apply to all [Function Modules \(FMs\)](#page-51-20) regarding compression of facial images.

#### **4.6.1.1. Requirements**

Multiple lossy compressions of the facial image data SHALL NOT take place with the exception of the initial capture by a digital camera whenever that camera does not support uncompressed image capture.

## <span id="page-35-0"></span>**4.6.2. FM COM-FI-IMA**

This Function Module describes requirements and interfaces for the compression of live images used within the context of immigration authorities.

#### **4.6.2.1. Requirements**

#### **4.6.2.1.1. General Requirements**

For conformance testing the software component encapsulating the compression SHALL provide an interface that accepts predefined test data instead of performing the regular process.

#### **4.6.2.1.2. Compression Requirements**

The following compression requirements as indicated in [Table 4.7](#page-35-3) apply for facial images for immigration authorities.

<span id="page-35-3"></span>

| Property                          | Value                                                                      |
|-----------------------------------|----------------------------------------------------------------------------|
| Compression method (Image format) | JPEG 2000 (compare [BIB_ISO_15444]) or JPEG (compare<br>[BIB_ISO_10918-1]) |
| Multiple lossy compressions       | not allowed                                                                |
| Maximum compression ratio         | 1:20                                                                       |
| Minimum file size                 | -                                                                          |
| Maximum file size                 | 375 kB                                                                     |

**Table 4.7** Compression Requirements for Facial Images for Immigration Authorities

## <span id="page-35-1"></span>**4.6.3. FM COM-FP-IMA**

This Function Module describes requirements and interfaces for the compression of fingerprint images con tained in [\[BIB\\_ANSI\\_NIST\\_2011:2015\]](#page-52-9) files within the context of immigration authorities.

#### **4.6.3.1. Requirements**

The NIST file size after compression SHALL have a maximum file size of 5332 kB for [EES](#page-51-5) purposes.

The NIST file size after compression SHALL have a maximum file size of 3000 kB for [SIS](#page-51-7) purposes.

## <span id="page-35-2"></span>**4.6.4. FM COM-FP-WSQE**

This Function Module describes requirements and interfaces for the compression of fingerprint images by [Wavelet Scalar Quantisation \(WSQ\)](#page-51-21) method.

#### **4.6.4.1. Requirements**

[WSQ](#page-51-21) SHALL be used as compression method for fingerprint images. A bit rate of 0.75 SHALL be used as compression parameter. This is equivalent to a compression factor of approximately 1:15[1](#page-35-4) (according to [\[BIB\\_ISO\\_FINGER\]\)](#page-52-1). The implementation of the used [WSQ](#page-51-21) algorithm SHALL be certified by the FBI and SHALL be referenced by the respective certificate number (coded in the [WSQ](#page-51-21) header). The certified [WSQ](#page-51-21) im plementation SHALL be version 3.1 and SHALL base on NBIS Version 5.0. Multiple lossy compressions SHALL NOT take place.

<span id="page-35-5"></span>If the resulting effective compression rate *C* does not fulfil the requirement of [Equation 4.3](#page-35-5) for this particular case only a stronger or weaker compression *C* SHALL be used.

$$1 : 20 \le = C \le = 1 : 10 \tag{4.3}$$

<span id="page-35-4"></span><sup>1</sup> For estimation of compression factor it is allowed to crop to the minimum size containing the fingerprint defined if a sensor is used with a larger capturing area than this minimum.

Therefore, an iterative process SHALL be applied, which results in an image file with an effective compression rate within the defined range, refer to [Equation 4.3](#page-35-5).

<span id="page-36-4"></span>The effective compression rate SHALL be calculated by [Equation 4.4](#page-36-4) where *Swsq* is the size in bytes of the resulting [WSQ](#page-51-21) file and *Sraw* is the size in bytes of the raw fingerprint image.

$$C = \frac{S\_{wsq}}{S\_{raw}}\tag{4.4}$$

## <span id="page-36-0"></span>**4.7. FM Category Operation**

Within the Function Module [Operation \(O\),](#page-51-22) the working process is specified for the respective operator. All steps that have to be executed are described sequentially and in more detail. This also includes descriptions of how to proceed in error cases.

## <span id="page-36-1"></span>**4.7.1. FM O-FI-ALL**

This Function Module describes requirements to be observed by the operator who handles the facial image acquisition process. This includes the full working process.

#### **4.7.1.1. Requirements**

- **•** If the software based [QA](#page-51-11) rejects the image, the operator SHALL have the option to give a veto in order to release the image despite a negative software decision and vice versa.
- **•** The operator SHALL be responsible for an adequate cleanliness of all capture hardware components.

#### **4.7.1.2. Recommendations**

OPTIONALLY, the operator can use the photo guideline.

## <span id="page-36-2"></span>**4.7.2. FM O-FI-DC**

This Function Module describes requirements to be observed by the operator who handles the facial image acquisition process with a digital camera.

#### **4.7.2.1. Requirements**

- **•** The operator SHALL ensure that different environmental lighting conditions caused by direct or indirect sunlight and different seasons of the year SHALL NOT influence the proper and uniform lighting of the captured facial image.
- **•** Direct and cross irradiation of lighting SHALL be avoided by the operator.

## <span id="page-36-3"></span>**4.7.3. FM O-FP-ALL**

This Function Module describes requirements to be observed by the operator who handles the acquisition process of fingerprint images.

#### **4.7.3.1. Requirements**

#### **4.7.3.1.1. Operation of Devices**

- **•** The operator SHALL be responsible for an adequate cleanliness of all capture hardware components. Fin gerprint scanners SHALL be cleaned regularly to provide good probe images.
- **•** The fingerprint scanner SHALL be regularly calibrated (e.g. once a day), if the used tech nology requires such a calibration. The operator SHALL ensure that the sensor platen is clean before cali bration to reduce the risk of ghost images.

#### **4.7.3.1.2. Environmental Requirements**

- **•** The operator SHALL ensure that different environmental lighting conditions caused by direct or indirect sunlight and different seasons of the year SHALL NOT influence the scanner capture process.
- **•** Direct and cross irradiation of lighting on the sensor platen SHALL be avoided completely.

## <span id="page-37-0"></span>**4.8. FM Category User Interface**

It is the task of the [User Interface \(UI\)](#page-51-23) to display and visualise the respective information that is obtained from the underlying Function Modules.

## <span id="page-37-1"></span>**4.8.1. FM UI-FI-OP**

This Function Module describes requirements for the user interface of the software displaying the result of the quality assessment and verification (if performed) of facial images to the operator.

#### **4.8.1.1. Requirements**

The following SHALL be shown to the operator for the enrolment:

- **•** displaying of the current evaluated picture
- **•** displaying of all criteria evaluated with the current value and threshold as well as their relation: OK/NOK for every criterion
- **•** displaying of the summarised result OK/NOK for the current picture
- **•** provision of the veto power for the operator
	- **•** enforcement of OK for obvious reasons (e.g. disability)
	- **•** enforcement of OK without obvious reasons
	- **•** enforcement of NOK to overrule software based quality assessment

If verifications are performed[2](#page-37-3) the following SHALL be shown to operator:

- **•** Visual feedback of the verification process SHALL be provided for the operator. At least both images (live and reference) and the (boolean) result of the verification SHALL be displayed to the operator.
- **•** If the verification fails, then the operator SHALL get access to at least one complete and coherent set of biometric samples and verification results corresponding to a single verification attempt. For instance, in case of verification of a live-captured facial image against a facial image from chip (Data Group 2) and [CIR](#page-51-6), such a complete set would consist of the live-captured facial image, the facial image extracted from chip, the facial image stored in the [CIR](#page-51-6), and both corresponding verification results of the live-captured facial image against the facial image from chip and the [CIR](#page-51-6) image.

## <span id="page-37-2"></span>**4.8.2. FM UI-FI-BSJ**

This Function Module describes requirements for the user interface of facial image acquisition shown to the biometric subject.

#### **4.8.2.1. Requirements**

In case the acquisition system is required by another[3](#page-37-4) Function Module to have a feedback screen for the facial acquisition, the following requirements SHALL be fulfilled:

**•** The acquisition system SHALL show a digital or physical mirror image to the biometric subject to guide it for the correct positioning in front of the camera.

<span id="page-37-3"></span><sup>2</sup> This is only the case if the application profile defines verification processes explicitly.

<span id="page-37-4"></span><sup>3</sup> If no Function Module of the Application Profile to implement requires a feedback screen, there is no need to implement the requirements within this section.

- **•** The acquisition system SHALL show user guidance information to help the biometric subject with cor rect positioning in front of the camera when one of the following conditions is met:
	- **•** The biometric subject is too close to or too far away from the camera.
	- **•** The biometric subject is too far left or right to the camera.
	- **•** The biometric subject is too high or low and the camera is not able to compensate this with a vertical adjustment.
	- **•** The biometric subject is in too much movement.
	- **•** The biometric subject is not facing frontally to the camera.
	- **•** The eyes of the biometric subject are closed.
	- **•** The mouth of the biometric subject is opened.
	- **•** Multiple faces were detected in front of the camera.

If [PAD](#page-51-10) was conducted: Neither the [PAD](#page-51-10) result nor [PAD](#page-51-10) score SHALL be displayed to the person whose facial image is acquired. In a supervised acquisition scenario the process operator MAY be responsible for screen po sitioning, so that the [PAD](#page-51-10) result or the [PAD](#page-51-10) score is not displayed to the person whose facial image is acquired.

#### **4.8.2.2. Recommendations**

- **•** An indicator showing the capture status SHOULD be displayed to the biometric subject.
- **•** Graphics (e.g. buttons or pictograms) SHOULD use a uniform colour palette without utilizing clashing co lours.

## <span id="page-38-0"></span>**4.8.3. FM UI-FP-OP**

This Function Module describes requirements for the user interface of software displaying live feed back and results of the fingerprint acquisition, [QA and control verification of fingerprint images to the ope](#page-51-11) rator.

#### **4.8.3.1. Requirements**

- **•** The user interface SHALL signal which fingerprints are expected for the current slap or fingerprint acqui sition such that the operator can guide the biometric subject to place the correct fingers on the fingerprint scanner.
- **•** Visual feedback of the fingerprint acquisition at least displaying of the final images SHALL be provided to the operator.
- **•** If a uniqueness check error occurs, the fingers involved in the unexpected successful comparisons SHALL be pictorially displayed to the operator and in case of a slap image only the affected finger(s) SHALL be marked in the displayed image. In case a control verification was attempted and no successful comparison occurred during the control verification, a warning SHALL be displayed to the operator that the control verification was not successful.
- **•** The segmented single fingerprints SHALL be visualised to the operator identify potential failures in seg mentation. This can be realised by displaying the result containing up to ten segmented single fingerprints. In case the amount of captured fingerprints mismatches with the amount of expected fingers a warning SHALL be displayed to the operator.
- **•** If a slap acquisition is in place and a slap classifier is in use (and activated not only for evaluation purpose), a warning SHALL be displayed to the operator when the classification result mismatches with the expected slap of the current acquisition.
- **•** If [PAD](#page-51-10) was performed and a presentation attack was detected, a warning SHALL be displayed to the operator and displayed for each finger individually. An overall result SHALL also be displayed additionally.
- **•** The indication of the quality level SHALL be displayed to the operator.
- **•** The provision of the veto power for the operator SHALL be shown to the operator for the enrolment:
	- **•** enforcement of OK for obvious reasons (e.g. disability)
	- **•** enforcement of OK without obvious reasons
	- **•** enforcement of NOK to overrule software based quality assessment

#### **4.8.3.2. Recommendations**

A live view from the fingerprint scanner SHOULD be displayed to operator during acquisi tion. This also includes live information, e.g. about the correct positioning of fingers on fingerprint scan ner or about the current quality level, that supports the operator guiding the biometric subject.

The user interface SHOULD show a graphical representation of the fingerprints that are expected for cur rent slap or fingerprint acquisition.

## <span id="page-39-1"></span>**4.8.4. FM UI-FP-BSJ**

This Function Module describes requirements for the user interface of the biometric subject for fingerprint acquisitions. The user interface MAY be e.g. monitors, buttons, pictograms or status lights.

#### **4.8.4.1. Requirements**

The following requirements SHALL be met for the user interface:

- **•** An indicator showing the capture status and an indication when the capture process has finished SHALL be displayed to the biometric subject. The capture status SHALL include: Where to place the fingers, an indication of the scanning process and the feedback in case of mispositioning of fingers.
- **•** In an unsupervised scenario a visualisation which fingerprint or hand to place on the sensor SHALL be given, whereby in the case of a supervised scenario the visualisation MAY be given.

If [PAD](#page-51-10) was conducted: Neither the [PAD](#page-51-10) result nor [PAD](#page-51-10) score SHALL be displayed to the person whose finger prints are acquired. In a supervised acquisition scenario the process operator MAY be responsible for screen positioning, so that the [PAD](#page-51-10) result or the [PAD](#page-51-10) score is not displayed to the person whose fingerprints are acquired.

#### **4.8.4.2. Recommendations**

The following recommendations SHOULD be met for the user interface:

- **•** Graphics (e.g. buttons or pictograms) SHOULD use a uniform colour palette without utilizing clashing co lours.
- **•** The acquisition process SHOULD be displayed as real time feedback to the biometric subject (e.g. with the help of a feedback monitor).

## <span id="page-39-0"></span>**4.9. FM Category Logging**

The Function Module [Logging \(LOG\)](#page-51-24) contains logging requirements. The requirements of this chapter and the requirements of the schema of information to log apply both.

## <span id="page-39-2"></span>**4.9.1. FM LOG-ALL-GENERIC**

The Function Module Logging contains requirements as to which data has be logged for a specific appli cation.

#### **4.9.1.1. Requirements**

- **•** A transaction SHALL cover all information concerning one single biometric subject. Created IDs (except the transaction UUID) only need to be unique locally within one transaction, as usually only one transaction is stored per XML-file. However, for scenarios where multiple transactions are collected within one XMLfile, the created IDs SHALL be unique globally.
- **•** During the biometric process all available data SHALL be gathered / created by the application.
- <span id="page-40-1"></span>**•** generic process information:
	- **•** name of the implemented application profile (e.g. BCL\_ManualBorderControl) if suitable (only applicable for scheme version 4v7 and higher)
	- **•** a globally unique Transaction ID conforming to [\[BIB\\_RFC4122\]](#page-52-10) Version 1 UUID specification
	- **•** global start time of the transaction (timestamp of the beginning of the biometric process as defined by the application profile[4](#page-40-0) )
	- **•** global end time of the transaction (timestamp biometric process as defined by ap plication profile)
	- **•** fully qualified host name (or if not available any other locally unique identifier serving as host name) of the station
	- **•** type of station (e.g. stationary/mobile)
	- **•** location of station (The exact semantic of this value is profile-dependent. See the specific profile for a refined definition.)
	- **•** the software used in this transaction (biometric component), at least with the following identifiers
		- **•** vendor name
		- **•** software name
		- **•** version number (Using a version numbering scheme which allows for proper lexicographic ordering is highly recommended)
		- **•** optional configuration information
	- **•** error code (optional) detailing any abnormal termination of the process
	- **•** a transaction reference if this transaction is dependent or derived from another transaction (reference to [Transaction ID\)](#page-40-1)
- **•** information about any identification processes performed during this transaction:

<span id="page-40-0"></span><sup>4</sup> For example this may be the moment in time when the operator has started the process by clicking on "start acquisition".

- **•** a globally unique ID conforming to [\[BIB\\_RFC4122\]](#page-52-10) Version 1 UUID specification for the identification (only applicable for scheme version 4v7 and higher)
- **•** start time of the identification process (i.e. beginning of capturing biometric data)
- **•** submit time of the identification process (i.e. when the captured data is submitted to the backend system for identification)
- **•** end time of the identification process (i.e. when the results from the backend system are available or the process terminated with a timeout)
- **•** a list of modalities used for identification
- **•** the result of the identification
- **•** the count of candidates available
- **•** for each candidate:
	- **•** the rank of the candidate
	- **•** score and threshold information
- **•** an error code in case of abnormal termination of the identification process
- **•** information about any enrolment processes performed during this transaction:
	- **•** a globally unique ID conforming to [\[BIB\\_RFC4122\]](#page-52-10) Version 1 UUID specification for the enrolment (only applicable for scheme version 4v7 and higher)
	- **•** start time of the enrolment process (i.e. beginning of capturing biometric data)
	- **•** optional submit time of the enrolment process (i.e. when the captured data is submitted to the backend for identification). This element SHALL be present in cases where the central system replies directly with enrolment status information.
	- **•** end time of the enrolment process (e.g. when the process terminated with a timeout)
	- **•** a list of modalities used for enrolment
	- **•** the enrolment status (i.e. whether the subject was enrolled successfully)
	- **•** an error code in case of abnormal termination of the enrolment process
	- **•** information about any control verifications performed during enrolment
- **•** information about any verification processes performed during this transaction
	- **•** a globally unique ID conforming to [\[BIB\\_RFC4122\]](#page-52-10) Version 1 UUID specification for the verificationcr (only applicable for scheme version 4v7 and higher)
	- **•** start time of the verification process (i.e. beginning of capturing biometric data)
	- **•** end time of the verification process
	- **•** information about the references used for this verification processes (image type, position codes)
	- **•** the verification result
	- **•** for each verification:
		- **•** the verification result
		- **•** for each comparison: the result of the comparison, the duration of the comparison process, detailed scoring and threshold information an error code in case of abnormal termination the compa rison process
		- **•** an error code in case of abnormal termination of the verification process
- **•** information about the records collected in this transaction:
	- **•** unique ID of record
	- **•** size of record
	- **•** type of record (encoding format)
	- **•** purpose of the record (enrolment, identification, verification)

The vendor SHALL provide a detailed list of error codes used with complete semantic descriptions.

## <span id="page-42-0"></span>**4.9.2. FM LOG-ALL-IMA**

The Function Module Logging contains requirements as to which data has to be logged for the application of immigration authorities.

#### **4.9.2.1. Requirements**

In order to allocate logs of immigration authorities to their respective application profile the element Appli cationProfile SHALL be filled as described in [Table 4.8](#page-42-2).

<span id="page-42-2"></span>

| Application Profile within TR                            | ApplicationProfile-Element                    |
|----------------------------------------------------------|-----------------------------------------------|
| Application Profile Multimodal Processing in Immigration | IMA_MultiModalProcessingImmigrationAuthoritie |
| Authorities for EES                                      | sEES                                          |
| Application Profile Multimodal Processing in Immigration | IMA_MultiModalProcessingImmigrationAuthori    |
| Authorities for SIS                                      | tiesSIS                                       |

**Table 4.8** Mapping Logs to Application Profiles

#### **4.9.2.2. Recommendations**

It is RECOMMENDED to store the images of the fingerprints and the facial image not only in the application specific container (e.g. GSAT-XML or EES-ANSI-NIST) record within the log, but also as separated records (e.g. in JPEG, BMP, WSQ). In this case, exactly the same image is to be used. Thereby, the log-reading applications are able to parse the images easier, as they only need knowledge about the syntax of the TR-03121 log schema.

## <span id="page-42-1"></span>**4.9.3. FM LOG-FI-GENERIC**

This Function Module describes requirements and interfaces for the logging of information regarding facial images for all profiles.

#### **4.9.3.1. Requirements**

Within a transaction for each facial image used for enrolment / verification / identification, all available data items SHALL be collected

- **•** a globally unique ID conforming to [\[BIB\\_RFC4122\]](#page-52-10) Version 1 UUID specification for the acquisition (only applicable for scheme version 4v7 and higher)
- **•** name of the implemented application profile (e.g. BCL\_ManualBorderControl) if suitable (only applicable for scheme version 4v7 and higher)
- **•** the overall result for the acquisition process (only applicable for scheme version 4v7 and higher)
- **•** the purpose of the acquisition (enrolment, identification, verification)
- **•** start time of the facial acquisition process
- **•** end time of the facial acquisition process
- **•** the time out if configured (only applicable for scheme version 4v7 and higher)
- **•** software used in this facial acquisition process
- **•** hardware used in this facial acquisition process
- **•** the source of the facial image under consideration
- **•** the count of face captures performed
- **•** for each face capture:
	- **•** if a veto was put by the operator: the type of veto (OK/NOK)
	- **•** the operation mode (if information is available)
	- **•** the vertical position of the camera (if information is available, only applicable for scheme version 4v7 and higher)
	- **•** the illumination level (if information is available, only applicable for scheme version 4v7 and higher)
	- **•** the focus distance (if information is available, only applicable for scheme version 4v7 and higher)
- **•** for the selected capture, detailed quality information about the result, detailing:
	- **•** information about the quality assessment software
	- **•** duration of quality assessment
	- **•** detailed quality values accompanied by:
		- **•** identifiers
		- **•** upper and lower value bounds, if available
		- **•** upper and lower threshold bounds, if available
	- **•** any error code in case of abnormal termination of the quality assessment
- **•** information about [PAD](#page-51-10) data during the capture:
	- **•** information about the [PAD](#page-51-10) subsystem
	- **•** the overall [PAD](#page-51-10) assessment result
	- **•** for each probe:
		- **•** the [PAD](#page-51-10) result
		- **•** detailed [PAD](#page-51-10) quality values accompanied by identifiers, upper and lower value bounds and upper and lower threshold bounds
- **•** information about the user interface:
	- **•** an indication of a displayed [PAD](#page-51-10) alert if [PAD](#page-51-10) was performed during the acquisition process, the [PAD](#page-51-10) result was at least once detected and displayed to the operator during the acquisition process
	- **•** an indication that a live feedback screen was available to the biometric subject if a live feedback screen was available to the biometric subject
- **•** an error code in case of abnormal termination of the facial acquisition process

The vendor SHALL provide a detailed list of error codes used with complete semantic descriptions

## <span id="page-43-0"></span>**4.9.4. FM LOG-FP-GENERIC**

This Function Module describes requirements and interfaces for the logging of information regarding finger print images for all profiles.

#### **4.9.4.1. Requirements**

- **•** Within a transaction for each fingerprint acquisition performed enrolment, verification, control veri fication or identification, all data defined in FingerAcquisition SHALL be collected, if available. If a finger print could not be acquired, the reason for each missing finger SHALL be logged.
- **•** For each capture process of a dedicated fingerprint or slap, all available information SHALL be logged. In case of multiple captures for a finger or slap the number of the capture details for which slap was selected as the best capture SHALL be specified. Within the finger capture the reference to the corresponding record of the probe SHALL be set. Further details of each during capture performed attempt pro vided, including the reference to the corresponding record if available. In case of an unacceptable capture attempt the reason for rejection of this capture attempt SHALL be selected. If the rejection reason is other an error code detailing the reason of rejection SHALL be set.
- **•** For the best capture attempt, detailed quality information about the result SHALL be logged. For all other capture attempts quality information, if calculated during the process, SHOULD be logged. For each finger or slap within a capture the quality result value and the threshold SHALL be presented within a range from 0 to 100 when available. If an overall quality value can be estimated by the quality assessment algorithm it SHALL be specified.
- **•** If a slap classification is performed during the acquisition process, the details SHALL be logged as Finger ClassifierInformation. This includes the classification results, information about the configured threshold of the algorithm and whether the classifier has been used in evaluation mode.
- **•** When a uniqueness check is performed, the results SHALL be collected. If the FMR is known, the security level for the uniqueness check SHALL be contained. The log SHALL specify all detected duplicate fingers.
- **•** For each performed [PAD](#page-51-10) the detailed [PAD quality values accompanied by identifiers, upper and lower va](#page-51-10) lue bounds and upper and lower threshold bounds SHALL be collected. In case the probe is a slap and a [PAD](#page-51-10) result is expected for each individual finger of the slap, the finger code SHALL be defined and [PAD](#page-51-10) information SHALL be present for each finger.
- **•** If a user interface is available during the acquisition process, the displayed information, e.g. an indication of a [PAD](#page-51-10) alert or live feedback screen SHALL be logged.
- **•** In unsupervised acquisition scenarios all available surveillance information SHALL be stored for each cor responding capture attempt. The surveillance image contained within a record SHALL be linked to the fin gerprint capture attempt.

If multiple persons have been present during the fingerprint acquisition process or single capture attempts, the detection of multiple persons SHALL be logged.

- **•** When the acquisition process is performed with the presence of a configured timeout the corresponding value SHALL be specified in milliseconds. The logging of the configured value SHALL be independent from the occurrence of a timeout.
- **•** If a control verification is performed (e.g. for rolled vs flat fingerprints or for fingerprints acquired at a [SSS](#page-51-18) vs fingerprints acquired at the counter) all available information SHALL be logged within a Verification element.
- **•** In case of abnormal termination of the fingerprint acquisition process or any of its sub-processes, the error code SHALL be logged. Errors during the fingerprint segmentation or uniqueness check SHALL be specified additionally by their corresponding error element. The vendor SHALL provide a detailed list of all error codes used with complete semantic descriptions.

## <span id="page-44-0"></span>**4.10. FM Category Coding**

This Function Module [Coding \(COD\)](#page-51-25) contains the procedures to encode quality data as well as biometric data in defined formats. Interoperability is provided by means of standard compliant coding.

## <span id="page-45-0"></span>**4.10.1. FM COD-ALL-IMA**

This Function Module describes requirements and interfaces for the overall coding of biometric biogra phic data used within the context of immigration authorities.

#### **4.10.1.1. Requirements**

- **•** The logging data as defined by the FM of the [FM Category Logging](#page-39-0) SHALL be encoded as XML according to the schema definition as ima-log element. The XML encoding is defined by the XML schema definition in the file "ima4v7.xsd" and referenced schema files.
- **•** Optional attributes and elements of the schema SHALL be considered as far as possible (e.g. error codes only need to be logged, in case an error occurred; an acquisition element is only required, in case an acquisition process has at least been started).
- **•** All log data SHALL be encoded as far as it is available throughout the acquisition process (e.g. fingerprint quality data is encoded if and only if fingerprint capture was performed).

## <span id="page-45-1"></span>**4.10.2. FM COD-ALL-EES**

This Function Module describes requirements and interfaces for the coding of general information according to EES-ANSI-NIST transactions.

#### **4.10.2.1. Requirements**

The general coding SHALL be conformant to the current version of the [\[BIB\\_EES\\_ICD\]](#page-52-11) in the binary format. Some required EES-ANSI-NIST data fields (e.g. biographic information) may not be available for the acquisi tion system (see [Table 4.9](#page-45-3)) . In order to keep the schema conformance during the entire process, these fields SHALL be filled with conformant placeholders. These placeholders SHALL be replaced as soon as possible with the actual values by the calling application.

<span id="page-45-3"></span>

| Record Type | Mnemonic | Field Name                    |
|-------------|----------|-------------------------------|
| 1           | PRY      | Priority                      |
| 1           | ORI      | Originating Agency Identifier |
| 10          | SRC      | Source Agency                 |
| 14          | SRC      | Source Agency                 |

**Table 4.9** Potential EES-ANSI-NIST Fields for Placeholders

## <span id="page-45-2"></span>**4.10.3. FM COD-ALL-GSAT3**

This Function Module describes requirements and interfaces for the coding of general information according to the German Standard for [Automated Fingerprint Identification System \(AFIS\)](#page-51-26) transactions in XML format.

#### **4.10.3.1. Requirements**

For data format and encoding, the XML-based standard [\[BIB\\_GSAT3\]](#page-52-12) SHALL apply. The current version of the [German Standard for AFIS Transactions Version 3 \(GSAT3\)](#page-51-27) SHALL be used. Some required [GSAT3](#page-51-27) data fields (e.g. biographic information) may not be available for the acquisition system. In order to keep the schema conformance during the entire process, these fields SHALL be filled with placeholders. These placeholders SHALL be replaced as soon as possible with the actual values by the calling application.

#### **4.10.3.2. Recommendations**

The example-placeholders listed in the [Table 4.10](#page-46-0) MAY be used.

<span id="page-46-0"></span>

| Mnemonic | Remarks                                         | Position in document                                                                                                                                                                                                                                                                 |
|----------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DAT      | Section: 8.13.<br>Example: 1555-05-05           | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageInformationRecord/<br>int-i:Transaction/<br>ansi-nist:TransactionDate/<br>nc:Date/                                                                                                                                    |
| DAI      | Section: 8.16.<br>Example: ABC                  | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageInformationRecord/<br>int-i:Transaction/<br>ansi-nist:TransactionDestinatio<br>nOrganization/<br>nc:OrganizationIdentification/<br>nc:IdentificationID/                                                               |
| DAI      | Section: 8.18.<br>Example: DEU                  | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageInformationRecord/<br>int-i:Transaction/<br>ansi-nist:TransactionDestinatio<br>nOrganization/<br>nc:OrganizationLocation/<br>nc:LocationAddress/<br>nc:StructuredAddress/<br>nc:LocationCountryISO3166Al<br>pha3Code/ |
| ORI      | Section: 8.20.<br>Example: org_abc              | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageInformationRecord/<br>int-i:Transaction/<br>ansi-nist:TransactionOrigina<br>tingOrganization/<br>nc:OrganizationIdentification/<br>nc:IdentificationID/                                                               |
| ???      | Section: 8.19.<br>Example: DEU                  | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageInformationRecord/<br>int-i:Transaction/<br>ansi-nist:TransactionOrigina<br>tingOrganization/<br>nc:OrganizationLocation/<br>nc:LocationAddress/<br>nc:StructuredAddress/<br>nc:LocationCountryISO3166Al<br>pha3Code/ |
| GMT      | Section: 8.30.<br>Example: 1555-05-25T11:17:33Z | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageInformationRecord/<br>int-i:Transaction/<br>ansi-nist:TransactionUTCDate/<br>nc:DateTime/                                                                                                                             |
| TCN      | Section: 8.23.<br>Example: 2100000005A          | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageInformationRecord/<br>int-i:Transaction/<br>ansi-nist:TransactionControlI<br>dentification/<br>nc:IdentificationID/                                                                                                   |

| Mnemonic | Remarks                                                                                                                                | Position in document                                                                                                                                                                                                                                                                                                                                        |
|----------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRY      | Section: 8.14.<br>Example: 2                                                                                                           | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageInformationRecord/<br>int-i:Transaction/<br>ansi-nist:TransactionPriorityVa<br>lue/                                                                                                                                                                                                          |
| TOT      | Section: 8.12.<br>Example: CPS                                                                                                         | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageInformationRecord/<br>int-i:Transaction/<br>int-i:TransactionAugmentation/<br>int-i:TransactionCategoryCode/                                                                                                                                                                                 |
| OB6      | Section: 9.33.<br>Example: DEU<br>According to GSAT3 this can also con<br>tain a complete address instead of only<br>the country code. | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>int-i:RecordActivity/<br>ansi-nist:CaptureOrganization/<br>nc:OrganizationLocation/<br>nc:LocationAddress/<br>nc:StructuredAddress/<br>nc:LocationCountryISO3166Al<br>pha3Code/ |
| OB1      | Section: 9.28.<br>Example: UTO                                                                                                         | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>int-i:RecordActivity/<br>ansi-nist:CaptureOrganization/<br>nc:OrganizationName/                                                                                                 |
| SEX      | Section: 9.51.<br>Example: F                                                                                                           | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>gsat:RecordSubject/<br>int-i:PersonSexCode/                                                                                                                                     |
| PCN      | Section: 9.68.<br>Example: 111111111V001                                                                                               | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>gsat:TransactionMetadata/<br>gsat:PersonalControlNumber/<br>nc:IdentificationID/                                                                                                |

| Mnemonic | Remarks                                  | Position in document                                                                                                                                                                                                                                                                                                 |
|----------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OIC1     | Section: 9.66.<br>Example: Erika         | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>gsat:TransactionMetadata/<br>gsat:OfficerInCharge/<br>nc:PersonGivenName/                                                                |
| OIC2     | Section: 9.67.<br>Example: Mustermann    | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>gsat:TransactionMetadata/<br>gsat:OfficerInCharge/<br>nc:PersonSurName/                                                                  |
| OIC      | Section: 9.65.<br>Example: 069 12345-678 | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>gsat:TransactionMetadata/<br>gsat:OfficerInCharge/<br>nc:ContactTelephoneNumber/<br>nc:FullTelephoneNumber/<br>nc:TelephoneNumberFullID/ |
| SEN      | Section: 9.71.<br>Example: ABC           | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>gsat:TransactionMetadata/<br>gsat:Workflow/<br>gsat:Sender/                                                                              |
| REG      | Section: 9.72.<br>Example: AS            | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>gsat:TransactionMetadata/<br>gsat:Workflow/<br>gsat:Laenderkennung/                                                                      |

| Mnemonic | Remarks                                                                                              | Position in document                                                                                                                                                                                                                                                                                           |
|----------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SNA      | Section: 9.74.<br>Example: NATIONAL                                                                  | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>gsat:TransactionMetadata/<br>gsat:Workflow/<br>gsat:System/<br>gsat:Name/                                                          |
| SPC      | Section: 9.75.<br>Example: FASTID                                                                    | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageDescriptiveTextRe<br>cord/<br>itl:UserDefinedDescriptiveText/<br>gsat:DomainDefinedDescriptive<br>Fields/<br>gsat:TransactionMetadata/<br>gsat:Workflow/<br>gsat:System/<br>gsat:Process/                                                       |
| ???      | Section: 13.6.<br>Example: DEU<br>Appears for every captured fingerprint.                            | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageFingerprintImageRe<br>cord/<br>itl:FingerprintImage/<br>ansi-nist:ImageCaptureDetail/<br>ansi-nist:CaptureOrganization/<br>nc:OrganizationLocation/<br>nc:LocationAddress/<br>nc:StructuredAddress/<br>nc:LocationCountryISO3166Al<br>pha3Code/ |
| ???      | Section: None<br>Example: org_abc<br>Appears for every captured fingerprint.<br>Not defined in GSAT3 | itl:NISTBiometricInformationEx<br>changePackage/<br>itl:PackageFingerprintImageRe<br>cord/<br>itl:FingerprintImage/<br>ansi-nist:ImageCaptureDetail/<br>ansi-nist:CaptureOrganization/<br>nc:OrganizationName/                                                                                                 |

**Table 4.10** GSAT3 Placeholders

## <span id="page-49-0"></span>**4.10.4. FM COD-FI-GENERIC**

This Function Module describes requirements for the coding used during the acquisition process of facial images.

#### **4.10.4.1. Requirements**

All results of the acquisition process SHALL be encoded in XML as FaceAcquisition.

The XML encoding is defined by the XML schema definition in:

- **•** biotypes4v6.xsd for volume ARE
- **•** biotypes4v7.xsd for volumes BCL and IMA

**•** biotypes5v1.xsd for volume GID

## <span id="page-50-0"></span>**4.10.5. FM COD-FI-EES**

This Function Module describes requirements for the coding used within the context of border control.

#### **4.10.5.1. Requirements**

- **•** The coding for facial images SHALL be conformant to the current version of the [\[BIB\\_EES\\_ICD\]](#page-52-11) in the binary format.
- **•** The minimum image resolution SHALL be 600 x 800 pixels.
- **•** The maximum image resolution SHALL be 1200 x 1600 pixels.

## **4.10.6. FM COD-FI-GSAT3**

This Function Module describes requirements and interfaces for the coding of facial images according to the German Standard for [AFIS](#page-51-26) transactions in XML format.

#### **4.10.6.1. Requirements on Encoding**

For data format and encoding, the XML-based standard [\[BIB\\_GSAT3\]](#page-52-12) SHALL apply. The current version of [GSAT3](#page-51-27) SHALL be used.

#### <span id="page-50-1"></span>**4.10.7. FM COD-FP-EES**

This Function Module describes requirements for the coding used to send fingerprint images to the [Central](#page-51-28) [System EES \(CS EES\).](#page-51-28)

#### **4.10.7.1. Requirements**

The coding for fingerprint images SHALL be conformant to the current version of the [\[BIB\\_EES\\_ICD\]](#page-52-11) in the binary format.

#### <span id="page-50-2"></span>**4.10.8. FM COD-FP-GSAT3**

This Function Module describes requirements and interfaces for the coding of fingerprint images according to the German Standard for [AFIS](#page-51-26) transactions in XML format.

#### **4.10.8.1. Requirements on Encoding**

For data format and encoding, the XML-based standard [\[BIB\\_GSAT3\]](#page-52-12) SHALL apply. The current version of the [GSAT3](#page-51-27) SHALL be used.

Note, if all fingers are available, a total number of 14 fingerprint records (itl:PackageFingerprintImageRecord) is to be transferred (10 fingerprints plus 4 slap images of right hand, left hand, right thumb and left thumb), regardless of the setting in use (4-1-4-1 or 4-4-2).

## <span id="page-51-0"></span>**List of Abbreviations**

<span id="page-51-28"></span><span id="page-51-27"></span><span id="page-51-26"></span><span id="page-51-25"></span><span id="page-51-24"></span><span id="page-51-23"></span><span id="page-51-22"></span><span id="page-51-21"></span><span id="page-51-20"></span><span id="page-51-19"></span><span id="page-51-18"></span><span id="page-51-17"></span><span id="page-51-16"></span><span id="page-51-15"></span><span id="page-51-14"></span><span id="page-51-13"></span><span id="page-51-12"></span><span id="page-51-11"></span><span id="page-51-10"></span><span id="page-51-9"></span><span id="page-51-8"></span><span id="page-51-7"></span><span id="page-51-6"></span><span id="page-51-5"></span><span id="page-51-4"></span><span id="page-51-3"></span><span id="page-51-2"></span><span id="page-51-1"></span>

| Abbreviation | Description                                     |
|--------------|-------------------------------------------------|
| AFIS         | Automated Fingerprint Identification System     |
| AH           | Acquisition Hardware                            |
| AP           | Application Profile                             |
| AS           | Acquisition Software                            |
| BIP          | Biometric Image Processing                      |
| CIR          | Central Identity Register                       |
| COD          | Coding                                          |
| COM          | Compression                                     |
| CS EES       | Central System EES                              |
| CTF          | contrast transfer function                      |
| EES          | Entry-Exit System                               |
| FM           | Function Module                                 |
| GSAT3        | German Standard for AFIS Transactions Version 3 |
| HLBS         | High Level Biometric Services                   |
| IMA          | Immigration Authorities                         |
| LOG          | Logging                                         |
| NFIQ2        | NIST Fingerprint Image Quality 2                |
| O            | Operation                                       |
| PAD          | Presentation Attack Detection                   |
| PAP          | Partial Application Process                     |
| QA           | Quality Assessment                              |
| SIS          | Schengen Information System                     |
| SNR          | signal-to-noise ratio                           |
| SSS          | self-service system                             |
| TCN          | Third-Country National                          |
| TR           | Technical Guideline                             |
| UI           | User Interface                                  |
| WSQ          | Wavelet Scalar Quantisation                     |

## <span id="page-52-0"></span> **Bibliography**

- <span id="page-52-9"></span>[BIB\_ANSI\_NIST\_2011:2015] *ANSI/NIST-ITL 1-2011: Update 2015, American National Standard for Infor mation Systems – Data Format for the Interchange of Fingerprint, Facial & Other Biometric Informa tion ANSI/NIST-ITL 1-2011 NIST Special Publication 500-290 Edition 3, available at: http://dx.doi.or g/10.6028/NIST.SP.500-290e3.*
- <span id="page-52-3"></span>[BIB\_EBTS/F] *FBI Electronic Biometric Transmission Specification Version 11, Appendix F, April 2021.*
- <span id="page-52-11"></span>[BIB\_EES\_ICD] *euLISA EES Interface Control Document, Annex 5 - NIST Fields, Version 06\_05, 2022, 14.02.2022.*
- <span id="page-52-12"></span>[BIB\_GSAT3] *German Standard for AFIS transactions. XML schema files current version..*
- <span id="page-52-8"></span>[BIB\_ISO\_10918-1] *ISO/IEC 10918-1:1994 "Information technology – Digital compression and coding of conti nuous-tone still images: Requirements and guidelines".*
- <span id="page-52-7"></span>[BIB\_ISO\_15444] *ISO/IEC 15444-1:2004 "Information technology – JPEG 2000 image coding system: Core coding system".*
- <span id="page-52-2"></span>[BIB\_ISO\_FACE] *ISO/IEC 19794-5:2005 "Information technology - Biometric data interchange formats – Part 5: Face image data".*
- <span id="page-52-1"></span>[BIB\_ISO\_FINGER] *ISO/IEC 19794-4:2005 "Information technology - Biometric data interchange formats – Part 4: Finger image data".*
- <span id="page-52-5"></span>[BIB\_ISO\_PAD\_1] *ISO/IEC 30107-1:2016 "Information technology – Biometric presentation attack detection – Part 1: Framework".*
- <span id="page-52-6"></span>[BIB\_ISO\_PAD\_3] *ISO/IEC 30107-3:2017 "Information technology – Biometric presentation attack detection – Part 3: Testing and reporting".*
- <span id="page-52-4"></span>[BIB\_NFIQ2] *NIST Fingerprint Image Quality 2.*
- <span id="page-52-10"></span>[BIB\_RFC4122] *RFC 4122: A Universally Unique IDentifier (UUID) URN Namespace.*
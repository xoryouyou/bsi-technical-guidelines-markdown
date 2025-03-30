![](_page_0_Picture_0.jpeg)

BSI Technical Guideline TR-03121-1

# Biometrics for Public Sector Applications

Part 1: Framework

Version 5.3

Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn E-Mail: TRBiometrics@bsi.bund.de Internet: https://www.bsi.bund.de © Federal Office for Information Security 2022

| 1.   | Changelog<br><br>1                                                    |
|------|-----------------------------------------------------------------------|
| 1.1. | Changelog Version 5.3-draft1<br><br>1                                 |
| 1.2. | Changelog Version 5.3-draft2<br><br>6                                 |
| 1.3. | Changelog Version 5.3<br><br>12                                       |
| 2.   | Introduction<br><br>18                                                |
| 2.1. | Motivation and Objectives of Technical Guideline Biometrics<br><br>18 |
| 2.2. | Target Audience and User<br><br>18                                    |
| 2.3. | Terminology<br><br>19                                                 |
| 2.4. | Business Process Modelling Notation (BPMN)<br><br>19                  |
| 3.   | Structure of Technical Guideline Biometrics<br><br>20                 |
| 4.   | How to use this Technical Guideline<br><br>22                         |
| 5.   | Logging scheme<br><br>23                                              |
| 5.1. | Use cases<br><br>23                                                   |
| 5.2. | XML schemas<br><br>23                                                 |
| 6.   | Application Profiles<br><br>24                                        |
| 7.   | Organisation of the Function Modules<br><br>25                        |
| 8.   | Organisation of the Partial Application Processes<br><br>28           |
|      | List of Abbreviations<br><br>29                                       |
|      | Bibliography<br><br>30                                                |

### **List of Figures**

| 2.1. | BPMN Symbols used for the Process Modelling<br> | 19 |
|------|-------------------------------------------------|----|
| 3.1. | Class Diagram of the Technical Guidelines<br>   | 21 |

### <span id="page-4-0"></span>**1. Changelog**

The following tables present the changes introduced to this Technical Guideline since version 5.2. chan gelog lists the changes grouped per part of this Technical Guideline, and per building block [\(Application Pro](#page-32-1) [file \(AP\),](#page-32-1) [Partial Application Process \(PAP\)](#page-32-2), Task, [Function Module \(FM\)](#page-32-3)) or element (section, table, figure):

- **•** *Added* for new features
- **•** *Changed* for changes in existing functionality
- **•** *Deprecated* for soon-to-be removed features
- **•** *Removed* for now removed features
- **•** *Fixed* for any bug fixes
- **•** *Security* in case of vulnerabilities

#### <span id="page-4-1"></span>**1.1. Changelog Version 5.3-draft1**

This chapter includes all changes between Version 5.2 and Version 5.3-draft1.

#### **1.1.1. Changelog BSI TR-03121, General**

| Element Name | Type of<br>Change | Change Description                                      |
|--------------|-------------------|---------------------------------------------------------|
| Bibliography | Changed           | Changed EES ICD Version to 00_07_00, 14th February 2022 |

**Table 1.1** Changelog BSI TR-03121, General

#### **1.1.2. Changelog BSI TR-03121, Part 1**

| Element Name                                                 | Type of<br>Change | Change Description                                                                                                                                                                                                     |  |  |
|--------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| LNK, REQ                                                     | Removed           | Removed LNK (Linking) and REQ (Request) in Overview PAP ID Primary Information<br>Items due to lack of existence.                                                                                                      |  |  |
| CL, FP1P, FPP,<br>FPR, TF, FP                                | Removed           | Removed CL (Candidate List), FP1P (1 Plain Fingerprint), FPP (Plain FPR (Rol<br>led Fingerprint), TF (Traveller File) and FP (Fingerprint) in Overview PAP ID Optional In<br>formation Items due to lack of reference. |  |  |
| FP10R, ALL, AU<br>TO, EES                                    | Added             | Added FP10R (Fingerprint 10 Finger Rolled), ALL (Overall), AUTO (Automated) and EES<br>(Entry-Exit-System) in Overview PAP ID Optional Information Items due to existing refe<br>rence.                                |  |  |
| Overview FM<br>Categories Op<br>tional Informati<br>on Items | Added             | Added a new table.                                                                                                                                                                                                     |  |  |

**Table 1.2** Changelog BSI TR-03121, Part 1

#### **1.1.3. Changelog BSI TR-03121, Part 2, Volume HLBS**

| Element Name                                     | Type of<br>Change | Change Description                                                                                                                                                     |
|--------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Service Definition "Fin<br>gerprint Acquisition" | Changed           | Changed type of Feedback-parameter "ExpectedFingers" from Iso19794FingerCode<br>to BiometricCodeList.                                                                  |
| Service Definition "Fin<br>gerprint Acquisition" | Changed           | Marked Configuration-parameter "MissingFingers" as deprecated.                                                                                                         |
| Service Definition "Fin<br>gerprint Acquisition" | Changed           | Added new User Command "SelectMissingFingers" to enable more dynamic selec<br>tion of missing fingers instead of static configuration.                                 |
| Service Definition "Fin<br>gerprint Acquisition" | Changed           | Added new value "SelectMissingFingers" to LiveStatus Feedback.                                                                                                         |
| Service Definition "Fin<br>gerprint Acquisition" | Changed           | Added new User Command "Capture" (e.g. in case fingerprint acquisition system<br>does not trigger automatically due to insufficient quality during pre-qualification). |

**Table 1.3** Changelog BSI TR-03121, Part 2

#### **1.1.4. Changelog BSI TR-03121, Part 3**

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                        | Type of<br>Change | Change Description                                                                                                                             |
|-----------------------|------------------------------|-----------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| GID                   | AP                           | Facial<br>Images<br>Cloud                                                   | Changed           | Replaced word "photographer" by "service provider".                                                                                            |
| BCL, GID,<br>ARE, IMA | FM                           | AS-FI-DC                                                                    | Changed           | Moved already existing recommendations regarding image formats<br>to designated subsection. Deleted the list of uncompressed image<br>formats. |
| GID                   | Basics                       | Basics for<br>German<br>Identi<br>ty Docu<br>ments                          | Added             | Rearrangement of the first three APs from former version.                                                                                      |
| GID                   | AP                           | Scan-of<br>Photo<br>graph                                                   | Added             | Rearrangement of the first three APs from former version.                                                                                      |
| GID                   | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Faci<br>al Image<br>Live En<br>rolment | Added             | Rearrangement of the first three APs from former version.                                                                                      |
| GID                   | AP                           | Supervi<br>sed Faci<br>al Image<br>Live En<br>rolment                       | Added             | Rearrangement of the first three APs from former version.                                                                                      |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                                | Type of<br>Change | Change Description                                        |
|-----------------------|------------------------------|-------------------------------------------------------------------------------------|-------------------|-----------------------------------------------------------|
| GID                   | AP                           | Facial<br>Image<br>Digi<br>tal-Trans<br>mission<br>via De<br>Mail (BSI<br>TR-03136) | Added             | Rearrangement of the first three APs from former version. |
| GID                   | AP                           | Facial<br>Image<br>Digi<br>tal-Trans<br>missi<br>on via<br>Cloud (BSI<br>TR-03170)  | Changed           | Title changed.                                            |
| GID                   | AP                           | Supervi<br>sed Fin<br>gerprint<br>Live En<br>rolment<br>Process                     | Added             | Rearrangement of the first three APs from former version. |
| GID                   | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Fin<br>gerprint<br>Live En<br>rolment          | Added             | Rearrangement of the first three APs from former version. |
| GID                   | AP                           | German<br>Identity<br>Card                                                          | Removed           | Rearrangement of the first three APs from former version. |
| GID                   | AP                           | German<br>Electronic<br>Passport                                                    | Removed           | Rearrangement of the first three APs from former version. |
| GID                   | AP                           | German<br>Residence<br>Permit                                                       | Removed           | Rearrangement of the first three APs from former version. |
| GID                   | AP                           | Scan-of<br>Photo<br>graph                                                           | Changed           | Added Deadline                                            |
| GID                   | PAP                          | ACQ-FI<br>SV-1                                                                      | Changed           | Added Deadline                                            |
| BCL, IMA              | FM                           | COD-FI<br>EES                                                                       | Changed           | Max. and min. image resolution added.                     |
| BCL, GID,<br>ARE, IMA | FM                           | AH-FI-DC                                                                            | Changed           | Colour image requirement added.                           |
| BCL, GID              | FM                           | AS-FP-SF                                                                            | Changed           | Added documentation of pre-qualification threshold.       |
| GID                   | FM                           | EVA-ALL<br>GID                                                                      | Changed           | Added annual report time period definition                |

| TR Volume             | Block /<br>Section /<br>Type | Name                           | Type of<br>Change | Change Description                                                                                                                                                           |
|-----------------------|------------------------------|--------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ARE                   | PAP                          | ACQ-FI<br>SV-2                 | Changed           | Added identification and pre-selection of best image and updated<br>display settings for the operator.                                                                       |
| BCL                   | FM                           | AH-FI<br>BCL                   | Changed           | New definition for distance between camera system and biometric<br>subject.                                                                                                  |
| GID                   | FM                           | AH-FI<br>SSS2                  | Changed           | New definition for distance between camera system and biometric<br>subject.                                                                                                  |
| BCL, GID              | FM                           | AS-FP-SF                       | Changed           | Timeout moved to PAP                                                                                                                                                         |
| BCL, GID,<br>IMA, ARE | FM                           | AS-FP-MF                       | Changed           | Timeout moved to PAP                                                                                                                                                         |
| GID                   | FM                           | COD-FI<br>GID2                 | Changed           | Removed one requirement.                                                                                                                                                     |
| GID                   | FM                           | BIP-FI<br>GID                  | Changed           | Modified one requirement.                                                                                                                                                    |
| BCL                   | FM                           | CMP-FI<br>VER                  | Changed           | Modified one Requirement on the Algorithm Performance.                                                                                                                       |
| BCL, GID              | FM                           | CMP-FP<br>VER                  | Changed           | Modified one Requirement on the Algorithm Performance.                                                                                                                       |
| GID                   |                              |                                | Changed           | Volume title changed from Enrolment Scenarios for Identity Docu<br>ments to German Identity Documents                                                                        |
| GID                   | PAP Task                     | ACQ-FPP<br>USV-1               | Changed           | Removed one bullet point                                                                                                                                                     |
| GID                   | AP                           | Biometric<br>Data<br>Selection | Changed           | Modified text (third and fifth bullet point) figure regarding Faci<br>al Image Selection Procedure to better map the process                                                 |
| BCL, GID,<br>IMA      | FM                           | COD-FI<br>GENERIC              | Changed           | Modified Requirements                                                                                                                                                        |
| BCL, GID,<br>ARE, IMA | FM                           | LOG-ALL<br>GENERIC             | Changed           | UUIDs SHALL be logged for enrolments, verifications and identifica<br>tions (only scheme version 4v7)                                                                        |
| BCL, GID,<br>ARE, IMA | FM                           | LOG-FI<br>GENERIC              | Changed           | UUID SHALL be logged for the acquisition (only scheme version 4v7)                                                                                                           |
| BCL, GID,<br>ARE, IMA | FM                           | LOG-FP<br>GENERIC              | Changed           | UUID SHALL be logged for the acquisition (only scheme version 4v7)                                                                                                           |
| GID                   | PAP                          | ACQ<br>FP2P<br>USV-1           | Changed           | Only index fingers with sufficient quality are recorded unsupervised.                                                                                                        |
| GID                   | PAP                          | ACQ<br>FP2P<br>USV-2           | Changed           | Only index fingers with sufficient quality are recorded unsupervised.                                                                                                        |
| GID                   | PAP                          | ACQ<br>FP2P<br>USV-2           | removed           | Brackets reffering to self service systems removed. The whole chap<br>ter is written in context of self service systems.                                                     |
| GID                   | FM                           | AH-FI<br>SSS2                  | Changed           | Modified Requirements                                                                                                                                                        |
| GID                   | -                            | -                              | Added             | Added overview process section to chapter "Basics for German Iden<br>tity Documents" which briefly explains the relation between ap<br>plication profiles of the GID volume. |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                               | Type of<br>Change | Change Description                                                                                                                                                                                                             |
|-----------------------|------------------------------|------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID                   | FM                           | AH-FI-DC                                                                           | Removed           |                                                                                                                                                                                                                                |
| GID                   | FM                           | AH-FI<br>DC2                                                                       | Added             |                                                                                                                                                                                                                                |
| GID                   | FM                           | AH-FI-ICS                                                                          | Removed           |                                                                                                                                                                                                                                |
| GID                   | FM                           | AH-FI<br>ICS2                                                                      | Added             |                                                                                                                                                                                                                                |
| GID                   | FM                           | AS-FI-DC                                                                           | Removed           |                                                                                                                                                                                                                                |
| GID                   | FM                           | AS-FI<br>DC2                                                                       | Added             |                                                                                                                                                                                                                                |
| BCL, GID,<br>ARE, IMA | FM                           | UI-FP-OP                                                                           | Changed           | Clarified: Fingers involved in the unexpected successful comparisons<br>SHALL be pictorially displayed.                                                                                                                        |
| GID                   | FM                           | BIP-FI<br>GID                                                                      | Changed           | Updated image size and added inter eye distance.                                                                                                                                                                               |
| GID                   | AP                           | Facial<br>Image<br>Digi<br>tal-Trans<br>missi<br>on via<br>Cloud (BSI<br>TR-03170) | Changed           | QA and further processing of the facial image(s) within the facial<br>images cloud is now optional. However, in the end the facial image(s)<br>for transmission to the counter at the agency have to comply to<br>COD-FI-GID2. |
| GID                   | FM                           | QA-FI<br>GID                                                                       | Changed           | Updated image size and inter eye distance.                                                                                                                                                                                     |
| BCL, GID,<br>ARE, GIS | FM                           | QA-FP<br>APP                                                                       | Modified          | The error code and result value are now specified in a more under<br>standable fashion.                                                                                                                                        |
| GID                   | FM                           | COM-FI<br>JPG                                                                      | Changed           | Updated image size.                                                                                                                                                                                                            |
| GID                   | FM                           | COD-FI<br>GID2                                                                     | Changed           | Updated image size.                                                                                                                                                                                                            |
| GID                   | FM                           | COD-ALL<br>GID                                                                     | Changed           | Increased Schema-Version to 5v0, changed root element to gid-log.                                                                                                                                                              |
| GID                   | FM                           | LOG-ALL<br>GENERIC                                                                 | Changed           | Adapted logging to new Schema-Version 5v0.                                                                                                                                                                                     |
| GID                   | FM                           | LOG-FI<br>GENERIC                                                                  | Changed           | Adapted logging to new Schema-Version 5v0.                                                                                                                                                                                     |
| GID                   | FM                           | LOG-FP<br>GENERIC                                                                  | Changed           | Adapted logging to new Schema-Version 5v0.                                                                                                                                                                                     |
| GID                   | FM                           | LOG-FI<br>GID                                                                      | Changed           | Adapted logging to new Schema-Version 5v0.                                                                                                                                                                                     |
| GID                   | FM                           | LOG-FP<br>GID                                                                      | Changed           | Adapted logging to new Schema-Version 5v0.                                                                                                                                                                                     |
| GID                   | FM                           | LOG-ALL<br>GID                                                                     | Changed           | Adapted logging to new Schema-Version 5v0.                                                                                                                                                                                     |
| GID                   | FM                           | COD-FI<br>EXIF                                                                     | Removed           | Will be covered implicit within this TR within the AP of biometric<br>data Selection at the counter                                                                                                                            |

| TR Volume             | Block /<br>Section /<br>Type | Name                                          | Type of<br>Change | Change Description                                                                                                                                                                                                           |
|-----------------------|------------------------------|-----------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID                   | AP                           | Processing<br>for Docu<br>ment Pro<br>duction | Added             |                                                                                                                                                                                                                              |
| BCL, GID              | FM                           | AS-FP-SF                                      | Changed           | Modified requirements regarding timeout                                                                                                                                                                                      |
| BCL, GID,<br>ARE, IMA | FM                           | AS-FP-MF                                      | Changed           | Modified requirements regarding timeout                                                                                                                                                                                      |
| BCL, GID,<br>ARE, IMA | FM                           | COD-FI<br>GENERIC                             | Changed           | Adapted logging to new Schema-Version 5v0 for GID.                                                                                                                                                                           |
| GID                   | AP                           | Biometric<br>Data<br>Selection                | Changed           | Precised process and added annotations at the process.                                                                                                                                                                       |
| GID                   | FM                           | REF-FI<br>GID                                 | Changed           | FM COM-FI-JPG removed to be applied on the facial image for refe<br>rence storage. In case image originates from facial images cloud ad<br>ditional information from the log-file has to be extracted refe<br>rence storage. |
| GID                   | FM                           | COD-FI<br>GID                                 | Changed           | Removed section about reference storage, removed information<br>about TR-03121 logging nodes (definitions are placed in the LOG<br>FMs).                                                                                     |
| GID                   | FM                           | COD-FI<br>GID                                 | Changed           | Removed information about TR-03121 logging nodes (definitions<br>are placed in the LOG FMs).                                                                                                                                 |
| GID                   | FM                           | LOG-FI<br>GID2                                | Added             | Added information on how to log facial images and further informa<br>tion relating to the facial images for GID.                                                                                                             |
| GID                   | FM                           | LOG-FP<br>GID2                                | Added             | Added information on how to log fingerprint images for GID.                                                                                                                                                                  |
| BCL,GID               | PAP Task                     | ACQ-FPS<br>USV-1                              | Modified          | Distinguished between two different timeouts and therefore chan<br>ged BPMN model as well as describing text.                                                                                                                |
| GID                   | PAP Task                     | ACQ-FPP<br>USV-1                              | Modified          | Distinguished between two different timeouts and therefore chan<br>ged BPMN model as well as describing text.                                                                                                                |
| BCL, GID,<br>ARE, IMA | FM                           | UI-FI-BSJ                                     | Modified          | Added information about Presentation Attack Detection (PAD).                                                                                                                                                                 |
|                       | FM                           | PAD-FP/<br>FI-APP/<br>APP1                    | Changed           | Show Presentation Attack Detection result in any case.                                                                                                                                                                       |

**Table 1.4** Changelog BSI TR-03121, Part 3

#### <span id="page-9-0"></span>**1.2. Changelog Version 5.3-draft2**

This chapter includes all changes between Version 5.3-draft1 and Version 5.3-draft2.

#### **1.2.1. Changelog BSI TR-03121, General**

| Element Name | Type of<br>Change | Change Description                                       |
|--------------|-------------------|----------------------------------------------------------|
| Bibliography | Changed           | Updated [BIB_ISO_19795-1:2006] to [BIB_ISO_19795-1:2021] |

**Table 1.5** Changelog BSI TR-03121, General

#### **1.2.2. Changelog BSI TR-03121, Part 1**

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | -                  |

**Table 1.6** Changelog BSI TR-03121, Part 1

#### **1.2.3. Changelog BSI TR-03121, Part 2, Volume HLBS**

| Element Name                       | Type of<br>Change | Change Description                |
|------------------------------------|-------------------|-----------------------------------|
| Data Type "Application<br>Profile" | Changed           | Updated GID Application Profiles. |
| ServiceInformation                 | Changed           | Added Parameter Version.          |

**Table 1.7** Changelog BSI TR-03121, Part 2

#### **1.2.4. Changelog BSI TR-03121, Part 3**

| TR Volume        | Block /<br>Section /<br>Type | Name                                                                        | Type of<br>Change | Change Description                                                                                                                              |
|------------------|------------------------------|-----------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| GID              | PAP                          | ACQ<br>FP2P-SV-1                                                            | Changed           | New Layout                                                                                                                                      |
| GID              | PAP                          | ACQ<br>FP2P-SV-2                                                            | Changed           | New Layout                                                                                                                                      |
| BCL, GID,<br>IMA | PAP Task                     | ACQ-FPS<br>SV-1                                                             | Changed           | Added option for the operator regarding manual conduct of capture                                                                               |
| BCL, GID,<br>IMA | PAP Task                     | ACQ-FPS<br>SV-1                                                             | Changed           | Added case in which a comparison of each finger print of the current<br>slap with any other finger print of the current is being conduc<br>ted. |
| BCL, GID,<br>IMA | PAP Task                     | ACQ-FPS<br>SV-1                                                             | Changed           | Added 'Perform PAD' to the description. Figure and description now<br>match.                                                                    |
| BCL, GID,<br>IMA | PAP Task                     | ACQ-FPS<br>SV-1                                                             | Changed           | Added step 6 to the description. Information displayed at the end of<br>the process now explicitly include PAD and QA information.              |
| ARE              | PAP Task                     | ACQ-FPS<br>SV-2                                                             | Changed           | Added option for the operator regarding manual conduct of capture                                                                               |
| BCL, GID,<br>IMA | PAP Task                     | ACQ-FPP<br>SV-2                                                             | Changed           | Added option for the operator regarding manual conduct of capture                                                                               |
| BCL, GID,<br>IMA | PAP Task                     | ACQ-FPS<br>SV-2                                                             | Added             | Added step 6 to the description. Information displayed at the end of<br>the process now explicitly include PAD and QA information.              |
| BCL, GID,<br>IMA | PAP Task                     | ACQ-FPS<br>SV-2                                                             | Changed           | Changed step 4 (sequence check) such that a PAD warning also oc<br>curs if fingers are matching within the currently acquired slap.             |
| BCL, GID         | PAP Task                     | ACQ-FI-1                                                                    | Changed           | Changed BPMN. Description of FM for PAD is now generic.                                                                                         |
| GID              | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Faci<br>al Image<br>Live En<br>rolment | Changed           | Added mandatory PAP ACQ-FI-AUTO-1.                                                                                                              |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                        | Type of<br>Change | Change Description                                                                                                       |
|-----------------------|------------------------------|-----------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| GID                   | AP                           | Biometric<br>Data<br>Selection                                              | Changed           | Merged three sub-chapters with mostly the same text into one                                                             |
| GID                   | AP                           | Processing<br>for Docu<br>ment Pro<br>duction                               | Added             | Quality assessements added to mandatory FM's                                                                             |
| BCL, GID,<br>ARE, IMA | FM                           | COM-FI<br>GENERIC                                                           | Added             | Added new chapter and assigned a generic COM requirement to it.                                                          |
| GID                   | FM                           | LOG-ALL<br>GID                                                              | Changed           | Added ApplicationProfile-Element table                                                                                   |
| GID                   | PAP Task                     | ACQ-FPS<br>USV-1                                                            | Changed           | Discard all captured images after first sequence error.                                                                  |
| GID                   | PAP Task                     | ACQ-FPP<br>USV-1                                                            | Changed           | Discard all captured images after first sequence error.                                                                  |
| GID                   | AP                           | Applicati<br>on Profile<br>Processing<br>for Docu<br>ment Pro<br>duction    | Removed           | Removed requirement regarding holograms in pass production.                                                              |
| GID, BCL,<br>ARE, IMA | FM                           | QA-FP<br>APP                                                                | Changed           | Images of 500 ppi shall be used for NFIQ 2.0.                                                                            |
| GID, BCL              | FM                           | PAD-FI<br>APP                                                               | Changed           | Further specification of PAD results included via reference. Techni<br>cal information shall now be stored if available. |
| GID                   | AP                           | Processing<br>for Docu<br>ment Pro<br>duction                               | Changed           | Changed Melderegister to Pass- und Ausweisregister in all BPMNs<br>and texts.                                            |
| GID                   | FM                           | AS-FI<br>ICS2                                                               | Created           | New FM                                                                                                                   |
| GID                   | FM                           | AH-FI<br>ICS2                                                               | Changed           | Added requirement regarding background for capturing facial<br>images                                                    |
| GID                   | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Faci<br>al Image<br>Live En<br>rolment | Changed           | In Mandatory Function Modules: Replaced FM AS-FI-DC2 with FM<br>AS-FI-ICS2                                               |
| GID                   | AP                           | Processing<br>for Docu<br>ment Pro<br>duction                               | Changed           | Removed process for Register of Residents and removed FM COM<br>FI-JPG and FM REF-FI-GID and FM COD-FI-GID2              |
| GID                   | AP                           | Biometric<br>Data<br>Selection                                              | Changed           | Added process for Register of Residents and added FM COM-FI-JPG<br>and FM REF-FI-GID                                     |
| GID                   | FM                           | LOG-FP<br>GID2                                                              | Changed           | Introduced Finger Element.                                                                                               |

| TR Volume             | Block /<br>Section /<br>Type | Name                                          | Type of<br>Change | Change Description                                                                   |
|-----------------------|------------------------------|-----------------------------------------------|-------------------|--------------------------------------------------------------------------------------|
| GID                   | AP                           | Biometric<br>Data<br>Selection                | Changed           | Added Evaluation of PAD Alarm                                                        |
| GID                   | FM                           | AH-FI<br>SSS2                                 | Changed           | Minimum distance fixed to 70 cm                                                      |
| GID                   | FM                           | COD-FI<br>PRD                                 | Created           | Coding requirements for document production                                          |
| GID                   | AP                           | Processing<br>for Docu<br>ment Pro<br>duction | Changed           | Added FM COD-FI-PRD                                                                  |
| GID                   | FM                           | COD-FI<br>ROR                                 | Added             | Coding requirements for Register of Residence                                        |
| GID                   | AP                           | Biometric<br>Data<br>Selection                | Changed           | Added FM COD-FI-ROR                                                                  |
| GID, ARE              | FM                           | O-ALL                                         | Added             | Added further requirements to the organisational requirements.                       |
| GID, ARE              | FM                           | COM-FI<br>JPG                                 | Added             | Added and Updated requirements regarding compression rates of<br>images.             |
| GID                   | FM                           | LOG-FP<br>GID2                                | Changed           | Added instructions for FingerprintCaptureAllowed                                     |
| BCL                   | FM                           | COD-FI<br>VER                                 | Changed           | Changed the references from outdated ones to bcl-log.                                |
| BCL, GID,<br>ARE, IMA | FM                           | QA-FI<br>GENERIC                              | Changed           | Added '0' as error code for criteria 7.5                                             |
| GID, BCL              | FM                           | PAD-FI<br>APP                                 | Removed           | Removed a case, where the omission of the PAD alarm is allowed.                      |
| GID, BCL              | FM                           | PAD-FI<br>APP1                                | Removed           | Removed a case, where the omission of the PAD alarm is allowed.                      |
| GID, BCL              | FM                           | PAD-FI<br>APP_5_0                             | Removed           | Removed a case, where the omission of the PAD alarm is allowed.                      |
| GID, BCL              | FM                           | PAD-FI<br>APP1                                | Changed           | Transition rules now specify a new date. The FM has to be applied<br>until May 2025. |
| GID                   | FM                           | COM-FI<br>JP2                                 | Changed           | Changed the constant file size from 15kB to 18kB.                                    |
| GID, BCL              | FM                           | PAD-FP<br>APP                                 | Changed           | Removed the requirement to test complete hands as massive arti<br>facts              |
| GID, BCL              | FM                           | PAD-FP<br>APP1                                | Changed           | Removed the requirement to test complete hands as massive arti<br>facts              |
| GID, BCL              | FM                           | AS-FP-SF                                      | Changed           | Thresholds for pre-qualification configurable, image data format                     |
| BCL, GID,<br>ARE, IMA | FM                           | LOG-FP<br>GENERIC                             | Changed           | Added logging instructions for control verifications.                                |
| BCL, GID,<br>ARE, IMA | FM                           | COM-FI<br>JPG                                 | Changed           | Added medium image size                                                              |
| GID                   | FM                           | LOG-FP<br>GID2                                | Changed           | Introduced tradd:BinaryData                                                          |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                 | Type of<br>Change | Change Description                                                                                                                                                |
|-----------------------|------------------------------|----------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID                   | FM                           | AS-FI<br>DC2                                                         | Changed           | Info added: If necessary, downscaling of the facial image MAY be do<br>ne before cropping.                                                                        |
| GID, BCL              | FM                           | PAD-FP<br>APP                                                        | Changed           | Provided additional information over how the overall PAD result<br>differs from the result of inidividual fingers.                                                |
| BCL                   | FM                           | LOG-FP<br>BCL                                                        | Removed           | Removed the FM.                                                                                                                                                   |
| ARE, BCL,<br>GID, IMA | FM                           | LOG-FP<br>GENERIC                                                    | Added             | Added the requirements prior included in LOG-FP-BCL.                                                                                                              |
| GID                   | FM                           | COM-FI<br>JPG                                                        | Removed           | Removed from GID.                                                                                                                                                 |
| BCL                   | FM                           | LOG-FP<br>BCL                                                        | Removed           | Removed FM from BCL.                                                                                                                                              |
| GID, ARE              | FM                           | LOG-FP<br>GENERIC                                                    | Added             | Added LOG-FP-BCL requirements.                                                                                                                                    |
| ARE                   | FM                           | AH-FP<br>ALL                                                         | Added             | Added an alternative set of requirements for certification processes.<br>This includes the requirements for certification of capacitive fin<br>gerprint scanners. |
| GID                   | AP                           | Supervi<br>sed Facial<br>Image Ac<br>quisition<br>System             | Added             | Added application profile for supervised facial image acquisition<br>with an integrated camera system.                                                            |
| GID                   | FM                           | AH-FI<br>ICS2                                                        | Changed           | Added requirement for body height range.                                                                                                                          |
| GID                   | FM                           | REF-FI<br>GID                                                        | Changed           | XML for AdditionalInformation is placed within Value-element.                                                                                                     |
| GID                   | FM                           | LOG-FI<br>GID2                                                       | Changed           | XML for AdditionalInformation is placed within Value-element.                                                                                                     |
| GID                   | AP                           | Supervi<br>sed Facial<br>Image Ac<br>quisition<br>Live En<br>rolment | Changed           | Added PAP ACQ-FI-SV-4.                                                                                                                                            |
| GID                   | AP                           | Biometric<br>Data<br>Selection                                       | Changed           | Added description for fingerprint selection procedure.                                                                                                            |
| GID                   | AP                           | Biometric<br>Data<br>Selection                                       | Changed           | Added post-processing step for operator                                                                                                                           |
| GID                   | AP                           | Facial<br>Image<br>Digi<br>tal-Trans<br>mission<br>via Cloud         | Changed           | Added FM LOG-FI-GID2                                                                                                                                              |

| TR Volume | Block /<br>Section /<br>Type | Name                                                                               | Type of<br>Change | Change Description                                                                                                                                   |
|-----------|------------------------------|------------------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID       | AP                           | Facial<br>Image<br>Digi<br>tal-Trans<br>mission<br>via De<br>Mail                  | Changed           | Added FM LOG-FI-GID2                                                                                                                                 |
| GID       | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Faci<br>al Image<br>Live En<br>rolment        | Changed           | Removed FM UI-FI-OP                                                                                                                                  |
| GID       | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Fin<br>gerprint<br>Live En<br>rolment         | Changed           | Removed FM REF-FP-CHIP                                                                                                                               |
| GID       | AP                           | Supervi<br>sed Fin<br>gerprint<br>Live En<br>rolment                               | Changed           | Removed FM REF-FP-CHIP                                                                                                                               |
| GID       | AP                           | Biometric<br>Data<br>Selection                                                     | Changed           | Updated selection process concerning quality and veto decisions                                                                                      |
| GID       | PAP                          | Capture<br>Slap Un<br>supervised                                                   | Changed           | Rearranged and changed the workflow for capture of unsupervi<br>sed slaps                                                                            |
| GID       | Basics                       | Basics for<br>German<br>Identi<br>ty Docu<br>ments                                 | Changed           | Mentions now biometric data selection and quality assessment at the<br>counter. The AP Facial image acquisition at the counter is now man<br>datory. |
| GID       | AP                           | Facial<br>Image<br>Digital<br>Trans<br>mission<br>via De<br>Mail (BSI<br>TR-03136) | Changed           | Renamed AP to Facial Image Digital Transmission via De-Mail (BSI<br>TR-03136)                                                                        |
| GID       | AP                           | Facial<br>Image<br>Digital<br>Transmis<br>sion via<br>Cloud (BSI<br>TR-03170)      | Changed           | Renamed AP to Facial Image Digital Transmission via Cloud (BSI<br>TR-03170)                                                                          |

| TR Volume | Block /<br>Section /<br>Type | Name                                                                               | Type of<br>Change | Change Description                                                                                              |
|-----------|------------------------------|------------------------------------------------------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------|
| GID       | PAP                          | ACQ-FI<br>AUTO                                                                     | Changed           | Renamed hardware with capture system and counter with calling<br>application for clarification.                 |
| GID       | PAP                          | ACQ-FPP<br>SV                                                                      | Changed           | Alerts replaced errors in this PAP.                                                                             |
| GID       | FM                           | AS-FI<br>ICS2                                                                      | Changed           | Requirement removed: The integrated camera system SHALL have<br>the diffuse lighting activated within software. |
| GID       | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Faci<br>al Image<br>Live En<br>rolment        | Changed           | Renamed to Unsupervised Self-Service Facial Image Acquisition Sys<br>tem                                        |
| GID       | AP                           | Supervi<br>sed Faci<br>al Image<br>Live En<br>rolment                              | Changed           | Renamed to Supervised Facial Image Acquisition with Digitial Ca<br>mera                                         |
| GID       | AP                           | Facial<br>Image<br>Digital<br>Trans<br>mission<br>via De<br>Mail (BSI<br>TR-03146) | Changed           | Renamed to Facial Image Digital Delivery via De-Mail (BSI<br>TR-03146)                                          |
| GID       | AP                           | Facial<br>Image<br>Digital<br>Transmis<br>sion via<br>Cloud (BSI<br>TR-03170)      | Changed           | Renamed to Facial Image Digital Delivery via Cloud (BSI TR-03170)                                               |
| GID       | AP                           | Supervi<br>sed Fin<br>gerprint<br>Live En<br>rolment                               | Changed           | Renamed to Supervised Fingerprint Acquisition                                                                   |
| GID       | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Fin<br>gerprint<br>Live En<br>rolment         | Changed           | Renamed to Unsupervised Self-Service Fingerprint Acquisition Sys<br>tem                                         |
| GID       | FM                           | AH-FI<br>DC2                                                                       | Changed           | Moved no (minimal) compression recommendations to require<br>ments.                                             |

**Table 1.8** Changelog BSI TR-03121, Part 3

#### <span id="page-15-0"></span>**1.3. Changelog Version 5.3**

This chapter includes all changes between Version 5.3-draft2 and Version 5.3.

#### **1.3.1. Changelog BSI TR-03121, General**

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | -                  |

**Table 1.9** Changelog BSI TR-03121, General

#### **1.3.2. Changelog BSI TR-03121, Part 1**

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | -                  |

**Table 1.10** Changelog BSI TR-03121, Part 1

#### **1.3.3. Changelog BSI TR-03121, Part 2, Volume HLBS**

| Element Name                                                                                                                                               | Type of<br>Change | Change Description                                                                                                                                                                                                                                                                                      |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| SlapClassifier                                                                                                                                             | Changed           | Chapter "Service Definition for Self-Service System", sub-chapter "Automated Ac<br>quisition of Slap Fingerprints", sub-sub-chapter "Configuration", table "Automated<br>Acquisition of Slap Fingerprints Configuration": Changed Parameter ID "SlapClassi<br>fier" from Mandatory (M) to Optional (O). |  |
| Service Definition Faci<br>al Image Acquisition Sys<br>tem, User Command "Ro<br>tate Manually"                                                             | Changed           | Added information about rotation value.                                                                                                                                                                                                                                                                 |  |
| Service Definition Basic<br>Facial Image Acquisition<br>System, User Command<br>"Rotate Manually"                                                          | Changed           | Added information about rotation value.                                                                                                                                                                                                                                                                 |  |
| Service Definition Fa<br>cial Image Acquisition<br>System, User Command<br>"SetManualFocusPoint"                                                           | Changed           | Added (parameter) name "Focus"                                                                                                                                                                                                                                                                          |  |
| Service Definition Fa<br>cial Image Acquisition<br>System, User Command<br>"SetVerticalPosition"                                                           | Changed           | Added (parameter) name "Position"                                                                                                                                                                                                                                                                       |  |
| Service Definition Faci<br>Changed<br>Added (parameter) name "Step"<br>al Image Acquisition Sys<br>tem, User Command "In<br>crementVerticalPosition"       |                   |                                                                                                                                                                                                                                                                                                         |  |
| Service Definition Faci<br>Changed<br>Added (parameter) name "Step"<br>al Image Acquisition Sys<br>tem, User Command "De<br>crementVerticalPosition"       |                   |                                                                                                                                                                                                                                                                                                         |  |
| Service Definition Fa<br>Changed<br>Added (parameter) name "Level"<br>cial Image Acquisition<br>System, User Command<br>"SetAbsoluteIlluminati<br>onLevel" |                   |                                                                                                                                                                                                                                                                                                         |  |

| Element Name                                                                                                                                 | Type of<br>Change                         | Change Description              |  |
|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|---------------------------------|--|
| Service Definition Faci<br>al Image Acquisition Sys<br>tem, User Command "In<br>crementIlluminationLe<br>vel"                                | Changed                                   | Added (parameter) name "Step"   |  |
| Service Definition Faci<br>al Image Acquisition Sys<br>tem, User Command "De<br>crementIlluminationLe<br>vel"                                | Changed                                   | Added (parameter) name "Step"   |  |
| Service Definition Fa<br>cial Image Acquisition<br>System, User Command<br>"CropManually"                                                    | Changed                                   | Added (parameter) name "Region" |  |
| Service Definition Faci<br>al Image Acquisition Sys<br>tem, User Command "Ro<br>tateManually"                                                | Changed                                   | Added (parameter) name "Angle"  |  |
| Service Definition Basic<br>Changed<br>Added (parameter) name "Region"<br>Facial Image Acquisition<br>System, User Command<br>"CropManually" |                                           |                                 |  |
| Service Definition Basic<br>Facial Image Acquisition<br>System, User Command<br>"RotateManually"                                             | Changed<br>Added (parameter) name "Angle" |                                 |  |
| Service Definition Rolled<br>Added<br>Added new service definition.<br>Fingerprint Acquisition                                               |                                           |                                 |  |

**Table 1.11** Changelog BSI TR-03121, Part 2

#### **1.3.4. Changelog BSI TR-03121, Part 3**

| TR Volume | Block /<br>Section /<br>Type | Name                                | Type of<br>Change | Change Description                                                                                                                                                                                                                                                                  |
|-----------|------------------------------|-------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID       | FM                           | COM-FI<br>JP2                       | Changed           | Changed filesize from 18kb (+/-5%) to 17kB (+0/-5%).                                                                                                                                                                                                                                |
| ARE       | AP                           | Arrival At<br>testation<br>Document | Removed           | Prior to removing all Function Modules regarding Evaluation from<br>ARE-Volume, in Table "Required Function Modules Application Pro<br>file Arrival Attestation Document" for "Evaluation" removed all 3 re<br>ferences: FM EVA-ALL-ARE, FM EVA-FI-ARE as well as FM-EVA-FP<br>ARE. |
| ARE       | FM                           | EVA-ALL<br>ARE                      | Removed           | Removed FM from ARE-Volume                                                                                                                                                                                                                                                          |
| ARE       | FM                           | EVA-ALL<br>GENERIC                  | Removed           | Removed FM from ARE-Volume                                                                                                                                                                                                                                                          |
| ARE       | FM                           | EVA-ALL<br>PROCESS                  | Removed           | Removed FM from ARE-Volume                                                                                                                                                                                                                                                          |
| ARE       | FM                           | EVA-FI<br>ARE                       | Removed           | Removed FM from ARE-Volume                                                                                                                                                                                                                                                          |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                      | Type of<br>Change | Change Description                                                                                                                                                            |
|-----------------------|------------------------------|---------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ARE                   | FM                           | EVA-FI<br>CENTRAL                                                         | Removed           | Removed FM from ARE-Volume                                                                                                                                                    |
| ARE                   | FM                           | EVA-FI<br>GENERIC                                                         | Removed           | Removed FM from ARE-Volume                                                                                                                                                    |
| ARE                   | FM                           | EVA-FP<br>ARE                                                             | Removed           | Removed FM from ARE-Volume                                                                                                                                                    |
| ARE                   | FM                           | EVA-FP<br>CENTRAL                                                         | Removed           | Removed FM from ARE-Volume                                                                                                                                                    |
| ARE                   | FM                           | EVA-FP<br>GENERIC                                                         | Removed           | Removed FM from ARE-Volume                                                                                                                                                    |
| ARE                   | FM                           | EVA-FP<br>PAD                                                             | Removed           | Removed FM from ARE-Volume                                                                                                                                                    |
| ARE                   | FM                           | QA-FI<br>ARE                                                              | Changed           | Added criterion "Colour space" (ID 7.5) to table in FM QA-FI-ARE in<br>cluding further information about the possible existence of greyscale<br>images.                       |
| IMA                   | FM                           | LOG-ALL<br>IMA                                                            | Changed           | Modified recommendations on FM LOG-ALL-IMA in order to speci<br>fy the case of separated records.                                                                             |
| ARE                   | PAP Task                     | ACQ<br>FPR-1                                                              | Changed           | Added comment for successful comparison.                                                                                                                                      |
| ARE                   | FM                           | LOG-ALL<br>ARE                                                            | Changed           | Added more precise information regarding "Issuance status of Arri<br>val Attestation Document"                                                                                |
| GID, ARE,<br>IMA, BCL | FM                           | QA-FI<br>GENERIC                                                          | Changed           | Changed the description of the process when more than one image<br>fullfills the most mandatory criteria.                                                                     |
| ARE, BCL              | PAP                          | ACQ<br>FPR-1                                                              | Added             | Added the Uniqueness Check to the Capture Rolled Finger process<br>and the respective process overview.                                                                       |
| GID                   | FM                           | LOG-ALL<br>GID                                                            | Changed           | Changed AP names in ApplicationProfile-Element table                                                                                                                          |
| ARE                   | FM                           | COD-ALL<br>ARE                                                            | Changed           | Biometric information embedded in the XML log can now either be<br>saved as an XML or a base64 encoded XML.                                                                   |
| ARE                   | AP                           | Arrival At<br>testation<br>Document<br>in Special<br>Situations           | Added             | Added Application Profile for the Arrival Attestation Document in<br>Special Situations which differs from the standard Application Profi<br>le Arrival Attestation Document. |
| ARE                   | FM                           | CMP-FP<br>CV                                                              | Changed           | Changed all occurences of cross-comparison to control-verification<br>including the titel (now ends with CV, was CC)                                                          |
| BCL                   | FM                           | COM-FP<br>BCL                                                             | Changed           | File size                                                                                                                                                                     |
| IMA                   | FM                           | COM-FP<br>IMA                                                             | Changed           | File size                                                                                                                                                                     |
| GID                   | AP                           | Supervi<br>sed Facial<br>Image Ac<br>quisition<br>with Digi<br>tal Camera | Changed           | Added FM UI-FI-OP as a Mandatory Function Module                                                                                                                              |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                           | Type of<br>Change | Change Description                                                                                                                                                                                      |
|-----------------------|------------------------------|--------------------------------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID                   | AP                           | Biometric<br>Data<br>Selection                                                 | Changed           | Added AP Supervised Facial Image Acquisition System to possible<br>sources in Facial Image Selection Procedure within AP Biometric<br>Data Selection.                                                   |
| GID                   | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Facial<br>Image Ac<br>quisition<br>System | Changed           | Added FM COM-FI-GENERIC as a Mandatory Function Module.                                                                                                                                                 |
| GID                   | AP                           | Supervi<br>sed Facial<br>Image Ac<br>quisition<br>with Digi<br>tial Came<br>ra | Changed           | Added FM COM-FI-GENERIC as a Mandatory Function Module.                                                                                                                                                 |
| BCL                   | FM                           | AS-FI-BCL                                                                      | Changed           | Renamed FM AS-FI-BCL to FM AS-FI-ICS3                                                                                                                                                                   |
| GID                   | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Facial<br>Image Ac<br>quisition<br>System | Changed           | Added FM AS-FI-ICS3 as a Mandatory Function Module                                                                                                                                                      |
| GID                   | AP                           | Supervi<br>sed Facial<br>Image Ac<br>quisition<br>System                       | Changed           | Added FM AS-FI-ICS3 as a Mandatory Function Module                                                                                                                                                      |
| GID                   | AP                           | Biometric<br>Data<br>Selection                                                 | Changed           | Added footnote regarding redundant operations in an application                                                                                                                                         |
| GID, ARE,<br>BCL      | Basics                       | GSAT3                                                                          | Changed           | Changed all references to state conformance the current/ most re<br>cent version of GSAT3 to ensure compatibility despite the different<br>production cycles for this guideline and the GSAT3 standard. |
| ARE                   | AP                           | Arrival At<br>testation<br>Document                                            | Changed           | Changed FM AS-FP-SLP from requirement to recommendation.                                                                                                                                                |
| BCL, GID,<br>ARE, IMA | PAP Task                     | ACQ-FPS<br>SV-2                                                                | Changed           | Added footnote that slap classification is only a recommendation for<br>volume ARE.                                                                                                                     |
| ARE                   | FM                           | BIP-FI<br>DC-HQ                                                                | Changed           | Added information that the resolution requirement og GSAT over<br>write the mentioned one in the TR                                                                                                     |
| BCL, GID              | FM                           | Presenta<br>tion At<br>tack De<br>tection<br>for facial<br>images              | Changed           | Added certification according to technical guideline as alternative to<br>certification under Common Criteria.                                                                                          |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                                   | Type of<br>Change | Change Description                                                                                                                                                                                                                                                                                                 |
|-----------------------|------------------------------|----------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BCL, GID              | FM                           | Presenta<br>tion At<br>tack De<br>tection<br>for facial<br>images                      | Changed           | Added new Protection Profile "Biometric Mechanisms" as possible<br>Common Criteria certification.                                                                                                                                                                                                                  |
| BCL, GID,<br>ARE, IMA | FM                           | Presenta<br>tion At<br>tack De<br>tection<br>for finger<br>prints                      | Changed           | Added certification according to technical guideline as alternative to<br>certification under Common Criteria.                                                                                                                                                                                                     |
| BCL, GID,<br>ARE, IMA | FM                           | Presenta<br>tion At<br>tack De<br>tection<br>for finger<br>prints                      | Changed           | Added new Protection Profile "Biometric Mechanisms" as possible<br>Common Criteria certification.                                                                                                                                                                                                                  |
| ARE                   | FM                           | Hardware<br>certifi<br>cation of<br>additio<br>nal fin<br>gerprint<br>scanner<br>types | Added             | Alternatively to the certification of optical fingerprint scanners ac<br>cording to AH-FP-OPT, the new Function Module AH-FP-ALL al<br>lows for the usage of FBI-certifications instead. Via AH-FP-ALL, ad<br>ditional fingerprint scanner types such as capacitive scanners may be<br>used in the context of ARE. |
| BCL, GID,<br>ARE, IMA | FM                           | QA-FP<br>APP                                                                           | Changed           | The quality requirements for fingerprints allow for NFIQ2 in general<br>instead of NFIQ 2.0 only.                                                                                                                                                                                                                  |

**Table 1.12** Changelog BSI TR-03121, Part 3

## <span id="page-21-0"></span>**2. Introduction**

#### <span id="page-21-1"></span>**2.1. Motivation and Objectives of Technical Guideline Biometrics**

Biometric methods are used in many different areas of applications. The solutions and systems available on the market are able to serve a broad range regarding performance, security, usability and standard confor mance. For public sector applications, it is necessary to define precise requirements and general conditions. Furthermore, the systems have to be defined in a way which allows for extension in future developments.

The objective of this Technical Guideline (TR Biometrics) is to offer a basis for a consistent and comparable quality of public sector applications and for building a common architecture.

This guideline has the following objectives:

- **•** *Modularity:* The complete guideline is built from several single guideline modules. For a single application area only the respective modules have to be taken into account. This is done in order to avoid side effects between different kinds of applications which would occur due to changes of special functions.
- **•** *Clarity:* The concept of this guideline follows a well structured framework. With this framework it is easily understandable which kind of guideline modules are valid for the respective application scenario.
- **•** *Expandability:* Modularity is the key component of expandability in the scope of this guideline. This is valid regarding new applications as well as new functional units.
- **•** *Standard conformance:* The Technical Guideline takes national and international standards and guidelines into account and deploys them for governmental applications.
- **•** *Conformance and certification:* The guideline modules are designed in such a way that requirements and conditions for single functional units are clearly separated from each other. Products for single functional units are clearly defined regarding the interfaces and the range of their functionality so that they can be tested for conformance with this guideline and certified.
- **•** *Ability to reference:* The use of functional units allows to specify precise requirements for products that are used in according application scenarios. Therefore, this guideline can be used as a reference e.g. for tenders.
- **•** *Market orientation:* The definition of functional units is related to the products that can be found on the market. Requirements of the guideline can be unambiguously assigned to respective systems and com ponents.

It should be noted that the content of this guideline is limited to aspects biometric characteristics. In terfaces to further technologies (e.g. connection of optical or electronic document readers) are out of scope of this document.

#### <span id="page-21-2"></span>**2.2. Target Audience and User**

Audience for this guideline are institutions that are dealing with projects using biometric characteristics in public sector applications. These include:

- **•** Agencies that are issuing identity documents or visas, e.g. passport agencies of the local authorities mis sions abroad of the Federal Foreign Office.
- **•** Public Authorities using biometric applications for identity verification of people, e.g. the German Federal Police (Polizeien des Bundes) or the Police of the Federal States (Polizeien der Länder), the German Customs Administration (Bundeszollverwaltung) or the Federal Administrative Office (Bundesverwaltungsamt).

Beside these users, this guideline also addresses vendors of biometric systems as well integrators and app lication developers.

#### <span id="page-22-0"></span>**2.3. Terminology**

The key words "MUST", MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this Technical Guideline are to be interpreted as described in [\[BIB\\_RFC2119\]](#page-33-1).

#### <span id="page-22-1"></span>**2.4. Business Process Modelling Notation (BPMN)**

<span id="page-22-2"></span>The processes in this Technical Guideline are modelled using the Business Process Modelling Notation (BPMN). [Figure 2.1](#page-22-2) gives an overview over the relevant icons herein.

![](_page_22_Figure_6.jpeg)

![](_page_22_Figure_7.jpeg)

### <span id="page-23-0"></span>**3. Structure of Technical Guideline Biometrics**

This Technical Guideline consists of the following parts:

**•** Part 1: Framework (TR-03121-1)

TR-03121-1 is the framework document of the guideline. It explains the concept and the relation between the different parts.

**•** Part 2: Software Architecture (TR-03121-2)

The [High Level Biometric Services \(HLBS\)](#page-32-5) as well as Service Definitions for specific use cases are specified here.

- **•** Part 3: Application Profiles, Function Modules and Processes (TR-03121-3)
	- **•** In the third part, the different Application Profiles with corresponding Partial Application Processes and Function Modules are defined. These contain the detailed technical requirements for each of com ponents.
		- **•** Application Profiles may reference Function Modules, Partial Processes and Service De finitions (refer to Part 2).
		- **•** Partial Application Processes may refer to Function Module Categories and may be comprised of *Tasks*. Tasks are processes which are part of more than one Partial Application Process.
	- **•** For practical purposes, this part is split up in different volumes to serve different user groups.
		- **•** [Border Control \(BCL\)](#page-32-6)
		- **•** [German Identity Documents \(GID\)](#page-32-7)
		- **•** [Alien Register Enrolment \(ARE\)](#page-32-8)
		- **•** [Immigration Authorities \(IMA\)](#page-32-9)

Please refer to [Figure 3.1](#page-24-0) for a class diagram of the structure described above.

<span id="page-24-0"></span>![](_page_24_Figure_1.jpeg)

**Figure 3.1.** Class Diagram of the Technical Guidelines

Additionally, the Technical Guideline BSI-TR 03122 "Conformance Test Specification for Technical Guideline TR-03121 Biometrics for Public Sector Applications" describes the requirements that are essential to declare conformance or to declare the absence of conformance. It consists of the following parts:

- **•** Part 1: Framework (TR-03122-1)
- **•** Part 3: Test Cases for Function Modules and Processes (TR-03122-3)

### <span id="page-25-0"></span>**4. How to use this Technical Guideline**

This chapter gives a short overview how to read and apply this guideline step by step.

- 1. The user chooses the desired Application Profile. With the help of the Application Profile the user can get a deeper insight into the application, the required software architecture components and the described functionality. TR-03121-2 offers further information about the software architecture component model.
- 2. Based on the Application Profile, the mandatory Partial Application Processes and Function Modules are identified. One profile can link to several Partial Application Processes and Function Modules due dif ferent kinds of underlying biometric characteristics or the fact that different technologies (e.g. scanners or digital cameras for the digitisation of a photo) are used.

Function Modules are referenced by an explicit identifier, e.g. AH-FP-GID. The first part identifies the requirement type (e.g. Hardware), the second part represents the biometric characteristic (e.g. fingerprint), and the last part denotes a further descriptor, typically the scope (e.g. German Identity Document).

Function Modules for different biometric characteristics are divided by a comma while a choice between different technologies is denoted by a slash (e.g. AH-FP-FTR, AH-PH-FBS/AH-PH-DC).

If a Function Module is denoted with a placeholder between a less-than and greater-than sign (< >) the actual referenced Function Module is dependant on the context in which the Function Module has been mentioned. For example the Function Module AH-FI-<VL> has been mentioned within a Partial Applica tion Process used in the [BCL volume, then the actual referenced Function Module is AH-FI-BCL. The sa](#page-32-6) me procedure holds for Application Profiles denoted as <AP> analogously. If no specific Function Module applies, then there are no further requirements defined for this context.

Partial Application Processes are referenced by an explicit identifier, refer to Partial Application Profile section.

3. On the basis of identifier according Function Module and Partial Application Processes can be ex amined. Every Function Module and Partial Application Process provides detailed technical requirements and recommendations. Note, each reference to a Function Module or Partial Application Processes is a link within the document.

### <span id="page-26-0"></span>**5. Logging scheme**

#### <span id="page-26-1"></span>**5.1. Use cases**

This chapter specifies a logging scheme, which allows to document all technical activities performed. The schema files contain additional and mandatory information on technical requirements. Such a logging sche me SHALL be used to measure the quality of the biometric processes across different systems, regardless of the used hard- or software. This enables the possibility of an operational monitoring for technical as well as functional processes and evaluations.

#### <span id="page-26-2"></span>**5.2. XML schemas**

The logging scheme is based on a transactional logging format which collects performance and evaluation results from the different application domains. The schema file trbio4v7.xsd imports all other schema files and as such the main file used for validation.

A separate XML schema definition exists for each volume of TR-03121-3, which SHALL be used within the respective application area. [Table 5.1](#page-26-3) gives an overview of the different XML schema files.

<span id="page-26-3"></span>

| Application domain             | Schemafile      | Namespace                         |
|--------------------------------|-----------------|-----------------------------------|
| Alien register enrolment       | aad4v6.xsd      | http://trbio.bsi.bund.de/aad/4    |
| Border control log             | bcl4v7.xsd      | http://trbio.bsi.bund.de/bcl/4    |
| Type definitions               | biotypes4v7.xsd | http://trbio.bsi.bund.de/base/4   |
| German identity documents      | gid4v6.xsd      | http://trbio.bsi.bund.de/gid/4    |
| High level biometric services  | hlbs4v7.xsd     | http://trbio.bsi.bund.de/hlbs/4   |
| Immigration authorities        | ima4v7.xsd      | http://trbio.bsi.bund.de/ima/4    |
| Conformance test specification | biocts4v7.xsd   | http://trbio.bsi.bund.de/biocts/4 |

**Table 5.1** Overview XML schema files

### <span id="page-27-0"></span>**6. Application Profiles**

Different areas in which this guideline can be used are defined in separate Application Profiles. Application Profiles can have mandatory status, e.g. through published regulations and laws or by requirements given in tenders. Besides, such Application Profiles can also be considered as Best Practices. Thus, the certification process SHALL use one or more seperate Application Profiles.

An Application Profile is described with the following items:

- **•** Introduction (legal requirements)
- **•** Process overview
	- **•** Target audience
	- **•** Users
- **•** Relevant standards and conditions
- **•** List of
	- **•** mandatory Function Modules
	- **•** mandatory Partial Application Processes

### <span id="page-28-0"></span>**7. Organisation of the Function Modules**

Specific technical requirements are structured in Function Modules. They contain detailed require ments for the respective component. Function Modules are aligned to the products on the market and to the targets of evaluation. Every Function Module is built of one or more subclauses which are assigned to unique identifiers. Within the subclauses requirements and recommendations are specified in detail.

Function Modules are referenced by their ID, which can contain up to three information items pointing to its contents. The basic structure of an ID is: "FM AAA-BBB-CCC".

Here, *AAA* is the primary information item, pointing to the main contents. *BBB* and *CCC* are optional infor mation items, which can further specify the Function Module. These information items may be two to seven alphanumeric digits. [Table 7.1](#page-28-1) gives an overview of the different primary information items used for Func tion Module categories. [Table 7.2](#page-29-0) gives an overview of the different optional information items *BBB* used for Function Module categories.

<span id="page-28-1"></span>

| Primary Information Item | Function Module Category   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AH                       | Acquisition Hardware       | Devices that are used for digitising phy<br>sical representable biometric characte<br>ristics are called Acquisition Hardware.<br>Scanners for capturing photographs, di<br>gital cameras to capture facial images,<br>fingerprint sensors, or signature tablets<br>can be named as examples.                                                                                                                                                                                                            |
| AS                       | Acquisition Software       | Acquisition Software encapsulates all<br>functionality regarding image proces<br>sing except for biometric purposes. The<br>refore, this module usually contains de<br>vice driver software for the Acquisiti<br>on Hardware or in general software that<br>is very close to the physical hardware.<br>Furthermore, colour management and<br>image enhancement mechanisms are<br>often part of this software layer.                                                                                      |
| BIP                      | Biometric Image Processing | The module Biometric Image Proces<br>sing provides the extraction of all rele<br>vant biometric information from the<br>data, which is provided by the Acquisi<br>tion Hardware or the Acquisition Soft<br>ware layer. Thus, a proprietary data<br>block is transformed to a digital image<br>of a biometric characteristic. In gene<br>ral, specific image processing for bio<br>metric characteristics is addressed he<br>re e.g. provision of full frontal images or<br>segmentation of fingerprints. |

| Primary Information Item | Function Module Category      | Description                                                                                                                                                                                                                                                                                                              |
|--------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMP                      | Biometric Comparison          | The module Biometric Comparison en<br>closes the mechanisms and algorithms<br>to verify or identify an identity based on<br>a one-to-one or one-to-many biometric<br>comparison between reference data and<br>a current biometric sample (usually a<br>live presented image) no matter where<br>the reference is stored. |
| COD                      | Coding                        | This module contains the procedures to<br>code logging data as well as biometric<br>data in defined formats. Interoperability<br>is provided by means of standard comp<br>liant coding.                                                                                                                                  |
| COM                      | Compression                   | The objective of the module Compres<br>sion is to keep the biometric data be<br>low a feasible size without losing too<br>much quality for biometric verification<br>or identification.                                                                                                                                  |
| EVA                      | Evaluation                    | Methods and interfaces which are used<br>in the scope of evaluation are con<br>tent of this module.                                                                                                                                                                                                                      |
| LOG                      | Logging                       | The module Logging contains require<br>ments how and in which modality data<br>has to be logged.                                                                                                                                                                                                                         |
| O                        | Operation                     | Within the module Operation, the<br>working process is specified for the re<br>spective operator.                                                                                                                                                                                                                        |
| PAD                      | Presentation Attack Detection | The Presentation Attack Detection mo<br>dules give requirements on fake detec<br>tion. This encloses, among other things,<br>functionality and certification require<br>ments.                                                                                                                                           |
| QA                       | Quality Assessment            | This module contains all kinds of me<br>chanisms and procedures to check the<br>quality of the biometric data or to select<br>the best quality data out of multiple in<br>stances. Quality Assessment is typical<br>ly used in evaluation of an application's<br>performance over time.                                  |
| REF                      | Reference Storage             | The objective of this module is to store<br>biometric data in a way that it can be<br>used for reference purposes later on.                                                                                                                                                                                              |
| UI                       | User Interface                | The User Interface modules give requi<br>rements on visualization and user in<br>teraction. This encloses, among other<br>things, functionality, quality assurance<br>information, and veto messages.                                                                                                                    |

**Table 7.1** Overview FM Categories Primary Information Items

<span id="page-29-0"></span>

| Optional Information Item | Function Module Category                        |
|---------------------------|-------------------------------------------------|
| ALL                       | Overall                                         |
| CCTV                      | Closed Circuit Television (Surveillance Camera) |

| Optional Information Item | Function Module Category |
|---------------------------|--------------------------|
| FI                        | Facial Image             |
| FP                        | Fingerprint              |

**Table 7.2** Overview FM Categories Optional Information Items

### <span id="page-31-0"></span>**8. Organisation of the Partial Application Processes**

Partial Application Processes are referenced by their ID, which can contain up to three information items pointing to its contents. The basic structure of an ID is: "PAP (Task) AAA-BBB-CCC-#".

Here, "Task" is optional and is only used if the *PAP* is a task. *AAA* is the primary information item, pointing to the main contents. *BBB* and *CCC* are optional information items, which can further specify the [PAP](#page-32-2). These information items may be one to six alphanumeric digits. The abbreviations used for the [PAP](#page-32-2) IDs are listed in [Table 8.1](#page-31-1) and [Table 8.2](#page-31-2). All [PAP](#page-32-2) IDs end with a number *#*. This number is usually 1, unless multiple IDs with similar preceding information items exist. In this case, they are enumerated increasingly.

<span id="page-31-1"></span>

| Primary Information Item | Description    |
|--------------------------|----------------|
| ACQ                      | Acquisition    |
| ASS                      | Assessment     |
| EVA                      | Evaluation     |
| ID                       | Identification |
| UPD                      | Update         |
| VER                      | Verification   |

**Table 8.1** Overview PAP ID Primary Information Items

<span id="page-31-2"></span>

| Optional Information Item | Description                                 |
|---------------------------|---------------------------------------------|
| ALL                       | Overall                                     |
| AUTO                      | Automated                                   |
| B                         | Biometrics (fingerprints and facial images) |
| EES                       | Entry-Exit-System                           |
| FI                        | Facial Image                                |
| FP10R                     | Fingerprint 10 Finger Rolled                |
| FP2P                      | 2 Plain Fingerprints                        |
| FP4141                    | Fingerprint 4-1-4-1                         |
| FP442                     | Fingerprint 4-4-2                           |
| FPS                       | Single Slap Fingerprint Image               |
| ID                        | Identification                              |
| nCIR                      | no Connected Identity Register              |
| SV                        | Supervised                                  |
| USV                       | Unsupervised                                |
| VER                       | Verification                                |
| wCIR                      | with Connected Identity Register            |

**Table 8.2** Overview PAP ID Optional Information Items

### <span id="page-32-0"></span>**List of Abbreviations**

<span id="page-32-9"></span><span id="page-32-8"></span><span id="page-32-7"></span><span id="page-32-6"></span><span id="page-32-5"></span><span id="page-32-4"></span><span id="page-32-3"></span><span id="page-32-2"></span><span id="page-32-1"></span>

| Abbreviation | Description                   |
|--------------|-------------------------------|
| AP           | Application Profile           |
| ARE          | Alien Register Enrolment      |
| BCL          | Border Control                |
| FM           | Function Module               |
| GID          | German Identity Documents     |
| HLBS         | High Level Biometric Services |
| IMA          | Immigration Authorities       |
| PAD          | Presentation Attack Detection |
| PAP          | Partial Application Process   |

## <span id="page-33-0"></span> **Bibliography**

<span id="page-33-1"></span>[BIB\_RFC2119] *RFC 2119: Key words for use in RFCs to Indicate Requirement Levels.*
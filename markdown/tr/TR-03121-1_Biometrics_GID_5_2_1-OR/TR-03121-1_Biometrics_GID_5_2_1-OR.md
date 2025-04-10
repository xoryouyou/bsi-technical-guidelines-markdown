![](_page_0_Picture_0.jpeg)

#### BSI Technical Guideline TR-03121-1

# Biometrics for Public Sector Applications

Part 1: Framework

Version 5.2.1

Federal Office for Information Security PO Box 20 03 63 53133 Bonn E-Mail: [TRBiometrics@bsi.bund.de](mailto:TRBiometrics@bsi.bund.de) Internet:<https://www.bsi.bund.de> © Federal Office for Information Security 2021

| 1   | Changelog<br><br>1                                                    |
|-----|-----------------------------------------------------------------------|
| 1.1 | Changelog Version 5.2-draft1<br><br>1                                 |
| 1.2 | Changelog Version 5.2-draft2<br><br>1                                 |
| 1.3 | Changelog Version 5.2-draft3<br><br>4                                 |
| 1.4 | Changelog Version 5.2<br><br>7                                        |
| 1.5 | Changelog Version 5.2.1<br><br>8                                      |
| 2   | Introduction<br><br>10                                                |
| 2.1 | Motivation and Objectives of Technical Guideline Biometrics<br><br>10 |
| 2.2 | Target Audience and User<br><br>10                                    |
| 2.3 | Terminology<br><br>10                                                 |
| 2.4 | Business Process Modelling Notation (BPMN)<br><br>11                  |
| 3   | Structure of Technical Guideline Biometrics<br><br>12                 |
| 4   | How to use this Technical Guideline<br><br>14                         |
| 5   | Logging scheme<br><br>15                                              |
| 5.1 | Use cases<br><br>15                                                   |
| 5.2 | XML schemas<br><br>15                                                 |
| 6   | Application Profiles<br><br>16                                        |
| 7   | Function Modules<br><br>17                                            |
| 7.1 | Organisation of the Function Modules<br><br>17                        |
| 7.2 | Function Module Classes<br><br>17                                     |
| 8   | Partial Application Processes<br><br>19                               |
| 8.1 | Organisation of the Partial Application Processes<br><br>19           |
|     | List of Abbreviations<br><br>20                                       |
|     | Bibliography<br><br>21                                                |

### List of figures

| 2.1. | BPMN Symbols used for the Process Modelling<br> | 11 |
|------|-------------------------------------------------|----|
| 3.1. | Class Diagram of the Technical Guidelines<br>   | 13 |

## <span id="page-6-0"></span>1 Changelog

The following tables present the changes introduced to this Technical Guideline since version 5.1. chan gelog lists the changes grouped per part of this Technical Guideline, per building block [\(Application Profile](#page-25-1) [\(AP\)](#page-25-1), [Partial Application Process \(PAP\),](#page-25-2) Task, [Function Module \(FM\)\)](#page-25-3) or element (section, table, figure).

#### <span id="page-6-1"></span>1.1 Changelog Version 5.2-draft1

This chapter includes all changes between Version 5.1 and Version 5.2-draft1.

#### 1.1.1 Changelog BSI TR-03121, Part 3

| TR Volume | Block /<br>Section /<br>Type | Name | Type of<br>Change | Change Description                                                   |
|-----------|------------------------------|------|-------------------|----------------------------------------------------------------------|
| IMA       | -                            | -    | Added             | Initial release of volume BSI TR-03121-3.6 (Immigration Authorities) |
|           |                              |      |                   |                                                                      |

**Table 1.1** Changelog BSI TR-03121, Part 3

#### <span id="page-6-2"></span>1.2 Changelog Version 5.2-draft2

This chapter includes all changes between Version 5.2-draft1 and Version 5.2-draft2.

#### 1.2.1 Changelog BSI TR-03121, Part 1

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | No Changes         |

**Table 1.2** Changelog BSI TR-03121, Part 1

#### 1.2.2 Changelog BSI TR-03121, Part 2, Volume HLBS

| Element Name                                                                                                                       | Type of<br>Change | Change Description                                                                                                                                                                                                                 |  |
|------------------------------------------------------------------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Service Definition "Faci<br>al Image Acquisition Sys<br>tem"                                                                       | Changed           | Added User Command "RotateManually" and feedback "QACroppedFacialImageRo<br>tation". Added information for feedback "QAEntireFacialImage" that the ImageRe<br>gion SHALL be used for marking the area of the cropped facial image. |  |
| Service Definition "Basic<br>Facial Image Acquisition<br>System"                                                                   | Added             | Service Definition Basic Facial Image Acquisition System added.                                                                                                                                                                    |  |
| Service Definition "Faci<br>al Image Acquisition Sys<br>tem"                                                                       | Changed           | Changed possbile value annotation for feedback images from "Image in a common<br>data format (jpeg, bmp or png) expected" to "Image in a common data format (e.g.<br>jpeg or bmp) expected".                                       |  |
| Service Definition "Fin<br>gerprint Acquisition"                                                                                   | Changed           | Changed possbile value annotation for feedback images from "Image in a common<br>data format (jpeg, bmp or png) expected" to "Image in a common data format (e.g.<br>jpeg or bmp) expected".                                       |  |
| Service Definition for<br>Changed<br>"Self Service System"                                                                         |                   | Changed possbile value annotation for feedback images from "Image in a common<br>data format (jpeg, bmp or png) expected" to "Image in a common data format (e.g.<br>jpeg or bmp) expected".                                       |  |
| Data Types "Application<br>Profile"                                                                                                | Added             | Format Restriction added: "IMA_MultiModalProcessingImmigrationAuthori<br>tiesEES "                                                                                                                                                 |  |
| Data Types "Application<br>Added<br>Format Restriction added: "IMA_MultiModalProcessingImmigrationAuthori<br>Profile"<br>tiesSIS " |                   |                                                                                                                                                                                                                                    |  |

**Table 1.3** Changelog BSI TR-03121, Part 2

#### 1.2.3 Changelog BSI TR-03121, Part 3

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                | Type of<br>Change   | Change Description                                                                                                                    |
|-----------------------|------------------------------|---------------------------------------------------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| BCL                   | FM                           | UI-FI-BSJ                                                           | Fixed               | Requirements for the UI of the feedback screen take only effect, if<br>another FM requires the system to have such a feedback screen. |
| BCL, GID,<br>ARE, IMA | FM                           | QA-FI-SB                                                            | Changed,<br>Renamed | Removed volume specific information (threshold requirements) and<br>renamed FM to QA-FI-GENERIC.                                      |
| BCL                   | FM                           | QA-FI-BCL                                                           | Added               | Volume specific threshold requirements added to this FM.                                                                              |
| GID                   | FM                           | QA-FI-GID                                                           | Added               | Volume specific threshold requirements added to this FM.                                                                              |
| ARE                   | FM                           | QA-FI-ARE                                                           | Added               | Volume specific threshold requirements added to this FM.                                                                              |
| IMA                   | FM                           | QA-FI<br>IMA                                                        | Added               | Volume specific threshold requirements added to this FM.                                                                              |
| BCL, IMA              | FM                           | COM-FI<br>EES                                                       | Removed             | Removed FM from volumes BCL and IMA.                                                                                                  |
| BCL                   | FM                           | COM-FI<br>BCL                                                       | Added               | Added compression requirements for entire volume.                                                                                     |
| IMA                   | FM                           | COM-FI<br>IMA                                                       | Added               | Added compression requirements for entire volume.                                                                                     |
| BCL, IMA              | FM                           | COM-FP<br>EES                                                       | Removed             | Removed FM from volumes BCL and IMA.                                                                                                  |
| BCL                   | FM                           | COM-FP<br>BCL                                                       | Added               | Added compression requirements for entire volume.                                                                                     |
| IMA                   | FM                           | COM-FP<br>IMA                                                       | Added               | Added compression requirements for entire volume.                                                                                     |
| IMA                   | FM                           | REF-FI<br>AAD                                                       | Removed             | Removed FM from volume IMA.                                                                                                           |
| IMA                   | FM                           | REF-FP<br>AAD                                                       | Removed             | Removed FM from volume IMA.                                                                                                           |
| IMA                   | FM                           | O-ALL<br>USV                                                        | Removed             | Removed FM from volume IMA.                                                                                                           |
| IMA                   | FM                           | COM-FP<br>WSQ                                                       | Removed             | Removed FM from volume IMA.                                                                                                           |
| IMA                   | AP                           | Multi<br>modal Pro<br>cessing in<br>Immigrati<br>on Autho<br>rities | Changed             | "elongation of resident permits" changed to "renewal per<br>mits".                                                                    |
| IMA                   | PAP                          | ACQ-FI<br>SV-4                                                      | Changed             | Reference in Fig. fixed.                                                                                                              |
| IMA                   | PAP Task                     | ACQ-FPS<br>SV-1                                                     | Changed             | "Increment i" added in Fig.                                                                                                           |
| GID                   | FM                           | EVA-FI<br>GENERIC                                                   | Changed             | Detailed description in Tab.                                                                                                          |
| GID                   | FM                           | EVA-FP<br>GENERIC                                                   | Changed             | Detailed description in Tab.                                                                                                          |
| BCL                   | FM                           | AS-FP-MF                                                            | Removed             | PNG as return format.                                                                                                                 |
| BCL                   | FM                           | AS-FI-ICS                                                           | Removed             | PNG as return format.                                                                                                                 |
| BCL                   | FM                           | AS-FP-SLP                                                           | Changed             | Classification threshold only for more than two classes.                                                                              |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                                            | Type of<br>Change | Change Description                                                                                                                                                                           |
|-----------------------|------------------------------|-------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BCL, GID,<br>ARE, IMA | FM                           | LOG-ALL<br>GENERIC                                                                              | Changed           | Added Application Profile element.                                                                                                                                                           |
| BCL, GID,<br>ARE, IMA | FM                           | LOG-FI<br>GENERIC                                                                               | Changed           | Added Application Profile and time out, element. For each capture<br>added the operation mode, vertical position, illumination level and<br>focus distance attribute.                        |
| BCL, GID,<br>ARE, IMA | FM                           | LOG-FP<br>GENERIC                                                                               | Changed           | Added Application Profile and time out element.                                                                                                                                              |
| IMA                   | PAP                          | ACQ-FI<br>SV-4                                                                                  | Changed           | Adapted Capture Process to new HLBS Service Definition Basic Faci<br>al Image Acquisition System                                                                                             |
| BCL, IMA              | PAP Task                     | ACQ-FI-1                                                                                        | Changed           | Removed annotation with used FMs on "Retrieve image from hard<br>ware", due to ambiguous mapping of FMs in Volumes where FM is<br>not used.                                                  |
| BCL, GID,<br>ARE, IMA | PAP                          | Introduc<br>tion                                                                                | Changed           | Removed example FM categories that may apply for Application<br>Profiles, as not all of them are existing in each Volume.                                                                    |
| IMA                   | FM                           | COD-ALL<br>IMA                                                                                  | Added             | Added new log schema for immigration authorities.                                                                                                                                            |
| IMA                   | AP                           | Multi<br>modal Pro<br>cessing in<br>Immigrati<br>on Autho<br>rities                             | Changed           | Removed rolled finger acquisition and facial image acquisition from<br>overall process.                                                                                                      |
| IMA                   | FM                           | AH-FI-ICS                                                                                       | Removed           | Not relevant for IMA Volume.                                                                                                                                                                 |
| IMA                   | FM                           | AS-FI-ICS                                                                                       | Removed           | Not relevant for IMA Volume.                                                                                                                                                                 |
| IMA                   | FM                           | AS-FP<br>ROLL                                                                                   | Removed           | Not relevant for IMA Volume.                                                                                                                                                                 |
| IMA                   | PAP                          | ACQ-FI<br>M-1                                                                                   | Removed           | Not relevant for IMA Volume.                                                                                                                                                                 |
| IMA                   | PAP                          | ACQ<br>FP10R<br>SV-1                                                                            | Removed           | Not relevant for IMA Volume.                                                                                                                                                                 |
| IMA                   | PAP                          | ACQ<br>FP4141-<br>SV-1                                                                          | Changed           | HLBS Service Definition to implement referenced.                                                                                                                                             |
| IMA                   | PAP                          | ACQ<br>FP442-<br>SV-1                                                                           | Changed           | HLBS Service Definition to implement referenced.                                                                                                                                             |
| IMA                   | AP                           | Applicati<br>on Profi<br>le Multi<br>modal Pro<br>cessing in<br>Immigrati<br>on Autho<br>rities | Changed           | Split into two APs: "Application Profile Multimodal Processing in<br>Immigration Authorities for EES" and "Application Profile Multi<br>modal Processing in Immigration Authorities for SIS" |
| IMA                   | Introduc<br>tion             | Introduc<br>tion                                                                                | Changed           | Introduction taken from "Application Profile Multimodal Processing<br>in Immigration Authorities"                                                                                            |
| BCL, IMA              | FM                           | BIP-FI<br>BCL                                                                                   | Renamed           | Renamed FM BIP-FI-BCL to BIP-FI-APP.                                                                                                                                                         |
| BCL, IMA              | FM                           | BIP-FI<br>APP                                                                                   | Changed           | Generalised wording (e.g. passenger to biometric subject) to better<br>suit for more volumes.                                                                                                |

| TR Volume                     | Block /<br>Section /<br>Type | Name                                                                                                       | Type of<br>Change | Change Description                                                                                      |
|-------------------------------|------------------------------|------------------------------------------------------------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------|
| BCL                           | FM                           | LOG-ALL<br>BCL                                                                                             | Changed           | Added recommendation to log record image also separately.                                               |
| IMA                           | FM                           | LOG-ALL<br>IMA                                                                                             | Added             | Added new FM to IMA Volume.                                                                             |
| BCL, IMA                      | FM                           | COD-ALL<br>EES                                                                                             | Added             | Added new FM to BCL and IMA Volume.                                                                     |
| IMA                           | FM                           | COD-ALL<br>GSAT3                                                                                           | Added             | Added new FM to IMA Volume.                                                                             |
| BCL, IMA                      | PAP                          | ACQ-FPS<br>SV-1                                                                                            | Changed           | Shortened to technical aspects and renamed "Supervised Acquisi<br>tion Single Slap".                    |
| BCL, IMA                      | PAP                          | ACQ-FPS<br>SV-1                                                                                            | Changed           | HLBS Service Definition to implement referenced.                                                        |
| -                             | Bibliogra<br>phy             | EES_ICD_FP Removed                                                                                         |                   | -                                                                                                       |
| -                             | Bibliogra<br>phy             | EES_ICD_FI Removed                                                                                         |                   | -                                                                                                       |
| -                             | Bibliogra<br>phy             | EES_ICD                                                                                                    | Added             | Version 06_00_00, 2021                                                                                  |
| BCL, GID,<br>VIS, GIS,<br>IMA | FM                           | AS-FP-SLP                                                                                                  | Changed           | This FM only applies, when the scanner runs in slap acquisition mo<br>de.                               |
| IMA                           | AP                           | Applicati<br>on Profi<br>le Multi<br>modal Pro<br>cessing in<br>Immigra<br>tion Aut<br>horities for<br>SIS | Changed           | FI acquisition removed.                                                                                 |
| BCL, IMA                      | PAP Task                     | ACQ-FPP<br>SV-2                                                                                            | Changed           | Added the operator decision to accept or recapture a fingerprint of<br>the process diagram in the text. |

**Table 1.4** Changelog BSI TR-03121, Part 3

#### <span id="page-9-0"></span>1.3 Changelog Version 5.2-draft3

This chapter includes all changes between Version 5.2-draft2 and Version 5.2-draft3.

#### 1.3.1 Changelog BSI TR-03121, General

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | No Changes         |

**Table 1.5** Changelog BSI TR-03121, Part 1

#### 1.3.2 Changelog BSI TR-03121, Part 1

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | No Changes         |

**Table 1.6** Changelog BSI TR-03121, Part 1

#### 1.3.3 Changelog BSI TR-03121, Part 2, Volume HLBS

| Element Name                              | Type of<br>Change | Change Description                                                                                                      |
|-------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------|
| Service Definition Self<br>Service System | Changed           | Removed ReferenceImage configuration parameter for SSS Service Definition (Au<br>tomated Acquisition of Facial Images). |
| Client-Server Connection<br>Scenarios     | Added             | Figure for logical HLBS Architecture.                                                                                   |

**Table 1.7** Changelog BSI TR-03121, Part 2

#### 1.3.4 Changelog BSI TR-03121, Part 3

| TR Volume                          | Block /<br>Section /<br>Type | Name                                                                                          | Type of<br>Change | Change Description                                                                                                                                                      |
|------------------------------------|------------------------------|-----------------------------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BCL                                | FM                           | AH-ALL<br>SSS                                                                                 | Changed           | Clarified that the identification of multiple persons is required du<br>ring the capture of fingerprints.                                                               |
| BCL, IMA                           | PAP Task                     | ACQ-FPS<br>SV-1                                                                               | Fixed             | Uniformed information of text and process diagram (added more in<br>formation about counter handling in the text).                                                      |
| ARE                                | PAP Task                     | ACQ-FPS<br>SV-2                                                                               | Fixed             | Uniformed information of text and process diagram (added more in<br>formation about counter handling in the text).                                                      |
| BCL, GID                           | PAP Task                     | ACQ-FPP<br>SV-2                                                                               | Fixed             | Uniformed information of text and process diagram (added more in<br>formation about counter handling in the text).                                                      |
| ARE                                | PAP Task                     | ACQ-FPS<br>SV-2                                                                               | Changed           | Slap classifier added.                                                                                                                                                  |
| ARE                                | AP                           | Applicati<br>on Profile<br>Arrival At<br>testation<br>Document                                | Changed           | FM AS-FP-SLP added to List of Mandatory Function Modules.                                                                                                               |
| BCL                                | AP                           | Applicati<br>on Profile<br>Automa<br>ted Border<br>Control<br>(Face-Ve<br>rification<br>Only) | Changed           | FM COD-FI-GENERIC added to List of Mandatory Function Modu<br>les.                                                                                                      |
| BCL, VIS,<br>IMA                   | FM                           | COD-ALL<br>GENERIC                                                                            | Removed           |                                                                                                                                                                         |
| BCL                                | FM                           | AH-FI<br>BCL                                                                                  | Changed           | Background blurring removed.                                                                                                                                            |
| BCL, GID,<br>VIS, ARE,<br>GIS, IMA | FM                           | QA-FI-SB                                                                                      | Removed           | All references to FM QA-FI-SB changed to FM QA-FI-GENERIC and<br>FM QA-FI-<VL>                                                                                          |
| BCL                                | PAP                          | ACQ-FI<br>M-1                                                                                 | Renamed           | The process was renamed from PAP ACQ-FI-M-1 "Manual Facial<br>Image Acquisition System" to PAP ACQ-FI-SV-5 "Supervised Facial<br>Image Acquisition System".             |
| BCL                                | PAP                          | ACQ-FI<br>SV-5                                                                                | Changed           | Specified process to perform cropping and de-rotation face auto<br>matically with the option for the operator to optimise the cropping<br>and the de-rotation manually. |
| BCL                                | PAP                          | ACQ-FI<br>AUTO-1                                                                              | Changed           | Specified process to perform cropping and de-rotation face auto<br>matically.                                                                                           |
| BCL                                | PAP                          | ACQ-FI<br>USV-1                                                                               | Changed           | Specified process to perform cropping and de-rotation face auto<br>matically.                                                                                           |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                         | Type of<br>Change | Change Description                                                                                                                                  |
|-----------------------|------------------------------|------------------------------------------------------------------------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| BCL                   | PAP Task                     | Slap Ac<br>quisition<br>Request<br>EES                                       | Removed           |                                                                                                                                                     |
| BCL                   | PAP                          | ACQ-FPS<br>USV-1                                                             | Changed           | Process simplified. Title changed to: "Unsupervised Acquisition Slap"<br>and process description added.                                             |
| ARE                   | FM                           | COD-ALL<br>AAD                                                               | Renamed           | Renamed FM COD-ALL-AAD to FM COD-ALL-ARE.                                                                                                           |
| ARE                   | FM                           | COD-ALL<br>ARE                                                               | Changed           | The name of corresponding schema file for logging changed from<br>aadXvX.xsd to areXvX.xsd and the root element changed from<br>aad-app to are-log. |
| ARE                   | FM                           | EVA-ALL<br>AAD                                                               | Renamed           | Renamed FM EVA-ALL-AAD to FM EVA-ALL-ARE.                                                                                                           |
| ARE                   | FM                           | EVA-FI<br>AAD                                                                | Renamed           | Renamed FM EVA-FI-AAD to FM EVA-FI-ARE.                                                                                                             |
| ARE                   | FM                           | EVA-FP<br>AAD                                                                | Renamed           | Renamed FM EVA-FP-AAD to FM EVA-FP-ARE.                                                                                                             |
| ARE                   | FM                           | LOG-ALL<br>AAD                                                               | Renamed           | Renamed FM LOG-ALL-AAD to FM LOG-ALL-ARE.                                                                                                           |
| ARE                   | FM                           | REF-FI<br>AAD                                                                | Renamed           | Renamed FM REF-FI-AAD to FM REF-FI-ARE.                                                                                                             |
| ARE                   | FM                           | REF-FP<br>AAD                                                                | Renamed           | Renamed FM REF-FP-AAD to FM REF-FP-ARE.                                                                                                             |
| GID, ARE,<br>GIS, IMA | FM                           | AS-FI-DC                                                                     | Changed           | Camera resolution SHALL be chosen to acquire a facial image of at<br>least 1200 x 1600 pixels with an inter eye distance of at 120 pi<br>xels.      |
| GID, VIS              | PAP Task                     | ACQ-FPP<br>USV-1                                                             | Added             | Display warning message to user, if sequence check fails.                                                                                           |
| BCL                   | FM                           | AS-FI-ICS                                                                    | Removed           | Export requirements for uncompressed images removed.                                                                                                |
| GID                   | FM                           | COD-FI<br>GID2                                                               | Added             |                                                                                                                                                     |
| GID                   | AP                           | Facial<br>Images<br>Cloud                                                    | Added             | Initial Release.                                                                                                                                    |
| GID                   | AP                           | Biometric<br>Data<br>Selection<br>Procedure                                  | Added             | Initial Release.                                                                                                                                    |
| GID                   | FM                           | PAD-FI<br>APP1                                                               | Added             |                                                                                                                                                     |
| BCL                   | AP                           | Applicati<br>on Profile<br>Semi-Mo<br>bile Ma<br>nual Bor<br>der Con<br>trol | Added             | Initial Release.                                                                                                                                    |
| BCL                   | AP                           | Applicati<br>on Profi<br>le Update<br>Process                                | Removed           | Removed empty application profile.                                                                                                                  |

| TR Volume        | Block /<br>Section /<br>Type | Name                                                                                                         | Type of<br>Change | Change Description                                                                                     |
|------------------|------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------|
| BCL              | AP                           | Applicati<br>on Profile<br>Second Li<br>ne                                                                   | Removed           | Removed unused application profile. See application profile MBC or<br>Semi-Mobile MBC as replacements. |
| IMA              | AP                           | Applica<br>tion Pro<br>file Mul<br>timodal<br>Processing<br>in Immi<br>gration<br>Autho<br>rities for<br>EES | Changed           | FM QA-FI-PG is no requirement anymore within this application<br>profile.                              |
| BCL, GID,<br>ARE | PAP                          | General<br>Process<br>Require<br>ments                                                                       | Removed           |                                                                                                        |
| BCL, GID,<br>ARE | FM                           | Category<br>Biometric<br>Compari<br>son                                                                      | Changed           | FM is now recommended.                                                                                 |
| BCL              | PAP                          | VER-FP-1                                                                                                     | Removed           |                                                                                                        |

**Table 1.8** Changelog BSI TR-03121, Part 3

#### <span id="page-12-0"></span>1.4 Changelog Version 5.2

This chapter includes all changes between Version 5.2-draft3 and Version 5.2.

#### 1.4.1 Changelog BSI TR-03121, General

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | No Changes         |

**Table 1.9** Changelog BSI TR-03121, Part 1

#### 1.4.2 Changelog BSI TR-03121, Part 1

| Element Name                | Type of<br>Change | Change Description                       |
|-----------------------------|-------------------|------------------------------------------|
| Function Modu<br>le Classes | Add               | Primary Information Item added to table. |

**Table 1.10** Changelog BSI TR-03121, Part 1

#### 1.4.3 Changelog BSI TR-03121, Part 2, Volume HLBS

| Element Name                          | Type of<br>Change | Change Description                                                                                                                                                         |
|---------------------------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| API DataType "Applicati<br>onProfile" | Changed           | Added elements "BCL_SemiMobileManualBorderControl" and "BCL_SelfService<br>System". Removed "VIS_ManualCounter" and "GIS_MultimodalIndenticiationWi<br>thWatchlistChecks". |

**Table 1.11** Changelog BSI TR-03121, Part 2

#### 1.4.4 Changelog BSI TR-03121, Part 3

| TR Volume             | Block /<br>Section /<br>Type | Name              | Type of<br>Change | Change Description                                                                                                                                                                                         |
|-----------------------|------------------------------|-------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID                   | FM                           | QA-FI-PT          | Clarified         | The way template gets on the image is variable (e.g. manually done<br>by supervisor or automatically done by software) and the medium of<br>the template is not fixed (it can be physically or digitally). |
| GID                   | FM                           | COD-ALL<br>GID    | Changed           | Relevant schema version is 4v6 for this release.                                                                                                                                                           |
| ARE                   | FM                           | COD-ALL<br>ARE    | Changed           | Relevant schema version is 4v6 for this release.                                                                                                                                                           |
| BCL, GID,<br>ARE, IMA | FM                           | COD-FI<br>GENERIC | Changed           | Relevant schema version for volumes BCL and IMA is 4v7. Relevant<br>schema version for volumes GID and ARE is 4v6.                                                                                         |
| BCL                   | FM                           | LOG-ALL<br>BCL    | Changed           | Added mapping of BCL Application Profiles to ApplicationProfi<br>le-element for logging.                                                                                                                   |
| IMA                   | FM                           | LOG-ALL<br>IMA    | Changed           | Added mapping of IMA Application Profiles to ApplicationProfi<br>le-element for logging. Removed requriement to not log purpose in<br>case purpose is ambiguous (purpose "other" may be used now).         |
| BCL, GID,<br>ARE, IMA | FM                           | QA-FI<br>GENERIC  | Changed           | Clarified that the image type to process depends on require<br>ments of the application profile to implement.                                                                                              |
| BCL, GID,<br>ARE, IMA | FM                           | LOG               | Changed           | Clarified that the logging modules and schema-requirements apply<br>both.                                                                                                                                  |
| BCL, GID,<br>ARE, IMA | FM                           | LOG-FP<br>GENERIC | Changed           | Reference to probe SHALL be logged.                                                                                                                                                                        |
| BCL                   | FM                           | COD-ALL<br>BCL    | Changed           | Optional schema elements/attributes SHALL be considered as far as<br>possible.                                                                                                                             |
| GID                   | FM                           | COD-ALL<br>GID    | Changed           | Optional schema elements/attributes SHALL be considered as far as<br>possible.                                                                                                                             |
| ARE                   | FM                           | COD-ALL<br>ARE    | Changed           | Optional schema elements/attributes SHALL be considered as far as<br>possible.                                                                                                                             |
| IMA                   | FM                           | COD-ALL<br>IMA    | Changed           | Optional schema elements/attributes SHALL be considered as far as<br>possible.                                                                                                                             |
| BCL, GID              | PAP Task                     | ACQ-FPS<br>USV-1  | Changed           | Harmonized BPMN-process with process description (sequence<br>check only required for acquisitions of multiple slaps).                                                                                     |

**Table 1.12** Changelog BSI TR-03121, Part 3

#### <span id="page-13-0"></span>1.5 Changelog Version 5.2.1

This chapter includes all changes between Version 5.2 and Version 5.2.1.

#### 1.5.1 Changelog BSI TR-03121, General

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | No Changes         |

**Table 1.13** Changelog BSI TR-03121, Part 1

#### 1.5.2 Changelog BSI TR-03121, Part 1

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | No Changes         |

**Table 1.14** Changelog BSI TR-03121, Part 1

#### 1.5.3 Changelog BSI TR-03121, Part 2, Volume HLBS

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
| -            | -                 | No Changes         |

**Table 1.15** Changelog BSI TR-03121, Part 2

#### 1.5.4 Changelog BSI TR-03121, Part 3

| TR Volume | Block /<br>Section /<br>Type | Name                                        | Type of<br>Change | Change Description                                               |
|-----------|------------------------------|---------------------------------------------|-------------------|------------------------------------------------------------------|
| GID       | AP                           | Facial<br>Images<br>Cloud                   | Removed           | AP only required for Live Enrolment May 2025.                    |
| GID       | AP                           | Biometric<br>Data<br>Selection<br>Procedure | Removed           | AP only required for Live Enrolment May 2025.                    |
| GID       | FM                           | COD-FI<br>GID2                              | Removed           | Part of AP Facial Images Cloud and therefore not needed anymore. |
| GID       | FM                           | COD-FI<br>EXIF                              | Removed           | Part of AP Facial Images Cloud and therefore not needed anymore. |

**Table 1.16** Changelog BSI TR-03121, Part 3

### <span id="page-15-0"></span>2 Introduction

### <span id="page-15-1"></span>2.1 Motivation and Objectives of Technical Guideline Biometrics

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

#### <span id="page-15-2"></span>2.2 Target Audience and User

Audience for this guideline are institutions that are dealing with projects using biometric characteristics in public sector applications. These include:

- **•** Agencies that are issuing identity documents or visas, e.g. passport agencies of the local authorities mis sions abroad of the Federal Foreign Office.
- **•** Public Authorities using biometric applications for identity verification of people, e.g. the German Federal Police (Polizeien des Bundes) or the Police of the Federal States (Polizeien der Länder), the German Customs Administration (Bundeszollverwaltung) or the Federal Administrative Office (Bundesverwaltungsamt).

Beside these users, this guideline also addresses vendors of biometric systems as well integrators and app lication developers.

#### <span id="page-15-3"></span>2.3 Terminology

The key words "MUST", MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this Technical Guideline are to be interpreted as described in [\[BIB\\_RFC2119\]](#page-26-1).

#### <span id="page-16-0"></span>2.4 Business Process Modelling Notation (BPMN)

<span id="page-16-1"></span>The processes in this Technical Guideline are modelled using the Business Process Modelling Notation (BPMN). [Figure 2.1](#page-16-1) gives an overview over the relevant icons herein.

![](_page_16_Figure_3.jpeg)

**Figure 2.1.** BPMN Symbols used for the Process Modelling

### <span id="page-17-0"></span>3 Structure of Technical Guideline Biometrics

This Technical Guideline consists of the following parts:

**•** Part 1: Framework (TR-03121-1)

TR-03121-1 is the framework document of the guideline. It explains the concept and the relation between the different parts.

**•** Part 2: Software Architecture (TR-03121-2)

The [High Level Biometric Services \(HLBS\)](#page-25-4) as well as Service Definitions for specific use cases are specified here.

- **•** Part 3: Application Profiles, Function Modules and Processes (TR-03121-3)
	- **•** In the third part, the different Application Profiles with corresponding Partial Application Processes and Function Modules are defined. These contain the detailed technical requirements for each of com ponents.
		- **•** Application Profiles may reference Function Modules, Partial Processes and Service De finitions (refer to Part 2).
		- **•** Partial Application Processes may refer to Function Module Categories and may be comprised of *Tasks*. Tasks are processes which are part of more than one Partial Application Process.
	- **•** For practical purposes, this part is split up in different volumes to serve different user groups.

Please refer to [Figure 3.1](#page-18-0) for a class diagram of the structure described above.

<span id="page-18-0"></span>![](_page_18_Figure_1.jpeg)

**Figure 3.1.** Class Diagram of the Technical Guidelines

Additionally, the Technical Guideline BSI-TR 03122 "Conformance Test Specification for Technical Guideline TR-03121 Biometrics for Public Sector Applications" describes the requirements that are essential to declare conformance or to declare the absence of conformance. It consists of the following parts:

- **•** Part 1: Framework (TR-03122-1)
- **•** Part 3: Test Cases for Function Modules and Processes (TR-03122-3)
- **•** Part 4: Additional Test Cases (TR-03122-4)

### <span id="page-19-0"></span>4 How to use this Technical Guideline

This chapter gives a short overview how to read and apply this guideline step by step.

- 1. The user chooses the desired Application Profile. With the help of the Application Profile the user can get a deeper insight into the application, the required software architecture components and the described functionality. TR-03121-2 offers further information about the software architecture component model.
- 2. Based on the Application Profile, the mandatory Partial Application Processes and Function Modules are identified. One profile can link to several Partial Application Processes and Function Modules due dif ferent kinds of underlying biometric characteristics or the fact that different technologies (e.g. scanners or digital cameras for the digitisation of a photo) are used.

Function Modules are referenced by an explicit identifier, e.g. AH-FP-GID. The first part identifies the requirement type (e.g. Hardware), the second part represents the biometric characteristic (e.g. fingerprint), and the last part denotes a further descriptor, typically the scope (e.g. German Identity Document).

Function Modules for different biometric characteristics are divided by a comma while a choice between different technologies is denoted by a slash (e.g. AH-FP-FTR, AH-PH-FBS/AH-PH-DC).

If a Function Module is denoted with a placeholder between a less-than and greater-than sign (< >) the actual referenced Function Module is dependant on the context in which the Function Module has been mentioned. For example the Function Module AH-FI-<VL> has been mentioned within a Partial Applica tion Process used in the Border Control (BCL) volume, then the actual referenced Function Module is AH-FI-BCL. The same procedure holds for Application Profiles denoted as <AP> analogously. If no specific Function Module applies, then there are no further requirements defined for this context.

Partial Application Processes are referenced by an explicit identifier, refer to Partial Application Profile section.

3. On the basis of identifier according Function Module and Partial Application Processes can be ex amined. Every Function Module and Partial Application Process provides detailed technical requirements and recommendations. Note, each reference to an Function Module or Partial Application Processes is a link within the document.

### <span id="page-20-0"></span>5 Logging scheme

#### <span id="page-20-1"></span>5.1 Use cases

This chapter specifies a logging scheme, which allows to document all technical activities performed. The schema files contain additional and mandatory information on technical requirements.

#### <span id="page-20-2"></span>5.2 XML schemas

The schema file trbio4v7.xsd imports all other schema files and as such the main file used for validation.

[Table 5.1](#page-20-3) gives an overview of the different XML schema files.

<span id="page-20-3"></span>

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

### <span id="page-21-0"></span>6 Application Profiles

Different areas in which this guideline can be used are defined in separate Application Profiles. Application Profiles can have mandatory status, e.g. through published regulations and laws or by requirements given in tenders. Besides, such Application Profiles can also be considered as Best Practices.

An Application Profile is described with the following items:

- **•** Introduction (legal requirements)
- **•** Process overview
	- **•** Target audience
	- **•** Users
- **•** Relevant standards and conditions
- **•** List of
	- **•** mandatory Function Modules
	- **•** mandatory Partial Application Processes

### <span id="page-22-0"></span>7 Function Modules

#### <span id="page-22-1"></span>7.1 Organisation of the Function Modules

Specific technical requirements are structured in Function Modules. They contain detailed require ments for the respective component.

Function Modules are aligned to the products on the market and to the targets of evaluation.

Every Function Module is built of one or more sub-clauses which are assigned to unique identifiers. Within the sub-clauses requirements and recommendations are specified in detail.

Partial Application Processes are referenced by their ID, which can contain up to three information items pointing to its contents.

The basic structure of an ID is: "FM AAA-BBB-CCC", where "AAA" is the so-called primary information item (see: [Table 7.1\)](#page-22-3).

#### <span id="page-22-2"></span>7.2 Function Module Classes

[Table 7.1](#page-22-3) gives an overview of the different Function Module categories.

<span id="page-22-3"></span>

| Function Module Category   | Primary Information Item | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Acquisition Hardware       | AH                       | Devices that are used for digitising phy<br>sical representable biometric characte<br>ristics are called Acquisition Hardware.<br>Scanners for capturing photographs, di<br>gital cameras to capture facial images,<br>fingerprint sensors, or signature tablets<br>can be named as examples.                                                                                                                                                                                                            |
| Acquisition Software       | AS                       | Acquisition Software encapsulates all<br>functionality regarding image proces<br>sing except for biometric purposes. The<br>refore, this module usually contains de<br>vice driver software for the Acquisiti<br>on Hardware or in general software that<br>is very close to the physical hardware.<br>Furthermore, colour management and<br>image enhancement mechanisms are<br>often part of this software layer.                                                                                      |
| Biometric Image Processing | BIP                      | The module Biometric Image Proces<br>sing provides the extraction of all rele<br>vant biometric information from the<br>data, which is provided by the Acquisi<br>tion Hardware or the Acquisition Soft<br>ware layer. Thus, a proprietary data<br>block is transformed to a digital image<br>of a biometric characteristic. In gene<br>ral, specific image processing for bio<br>metric characteristics is addressed he<br>re e.g. provision of full frontal images or<br>segmentation of fingerprints. |
| Biometric Comparison       | CMP                      | The module Biometric Comparison en<br>closes the mechanisms and algorithms<br>to verify or identify an identity based on<br>a one-to-one or one-to-many biometric<br>comparison between reference data and<br>a current biometric sample (usually a<br>live presented image) no matter where<br>the reference is stored.                                                                                                                                                                                 |

| Function Module Category      | Primary Information Item | Description                                                                                                                                                                                                                                                                             |
|-------------------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Coding                        | COD                      | This module contains the procedures to<br>code logging data as well as biometric<br>data in defined formats. Interoperability<br>is provided by means of standard comp<br>liant coding.                                                                                                 |
| Compression                   | COM                      | The objective of the module Compres<br>sion is to keep the biometric data be<br>low a feasible size without losing too<br>much quality for biometric verification<br>or identification.                                                                                                 |
| Evaluation                    | EVA                      | Methods and interfaces which are used<br>in the scope of evaluation are con<br>tent of this module.                                                                                                                                                                                     |
| Logging                       | LOG                      | The module Logging contains require<br>ments how and in which modality data<br>has to be logged.                                                                                                                                                                                        |
| Operation                     | O                        | Within the module Operation, the<br>working process is specified for the re<br>spective operator.                                                                                                                                                                                       |
| Presentation Attack Detection | PAD                      | The Presentation Attack Detection mo<br>dules give requirements on fake detec<br>tion. This encloses, among other things,<br>functionality and certification require<br>ments.                                                                                                          |
| Quality Assessment            | QA                       | This module contains all kinds of me<br>chanisms and procedures to check the<br>quality of the biometric data or to select<br>the best quality data out of multiple in<br>stances. Quality Assessment is typical<br>ly used in evaluation of an application's<br>performance over time. |
| Reference Storage             | REF                      | The objective of this module is to store<br>biometric data in a way that it can be<br>used for reference purposes later on.                                                                                                                                                             |
| User Interface                | UI                       | The User Interface modules give requi<br>rements on visualization and user in<br>teraction. This encloses, among other<br>things, functionality, quality assurance<br>information, and veto messages.                                                                                   |

**Table 7.1** Overview Function Module Categories

### <span id="page-24-0"></span>8 Partial Application Processes

#### <span id="page-24-1"></span>8.1 Organisation of the Partial Application Processes

Partial Application Processes are referenced by their ID, which can contain up to three information items pointing to its contents.

The basic structure of an ID is: "PAP (Task) AAA-BBB-CCC-#".

Here, "Task" is optional and is only used if the PAP is a task. *AAA* is the primary information item, pointing to the main contents. *BBB* and *CCC* are optional information items, which can further specify the [PAP](#page-25-2). These information items may be 1-6 alphanumeric digits. The abbreviations used for the [PAP](#page-25-2) ID are listed in [Ta](#page-24-2) [ble 8.1](#page-24-2) and [Table 8.2.](#page-24-3) All [PAP](#page-25-2) IDs end with a number *#*. This number is usually 1, unless multiple IDs with similar preceding information items exist. In this case, they are enumerated increasingly.

<span id="page-24-2"></span>

| Primary Information Item | Description    |
|--------------------------|----------------|
| ACQ                      | Acquisition    |
| ASS                      | Assessment     |
| EVA                      | Evaluation     |
| ID                       | Identification |
| LNK                      | Linking        |
| REQ                      | Request        |
| UPD                      | Update         |
| VER                      | Verification   |

**Table 8.1** Overview PAP ID Primary Information Items

<span id="page-24-3"></span>

| Optional Information Item | Description                                 |
|---------------------------|---------------------------------------------|
| B                         | Biometrics (fingerprints and facial images) |
| CL                        | Candidate List                              |
| FI                        | Facial Image                                |
| FP                        | Fingerprint                                 |
| FP1P                      | 1 Plain Fingerprint                         |
| FP2P                      | 2 Plain Fingerprints                        |
| FP4141                    | Fingerprint 4-1-4-1                         |
| FP442                     | Fingerprint 4-4-2                           |
| FPP                       | Plain Fingerprint                           |
| FPR                       | Rolled Fingerprint                          |
| FPS                       | Single Slap Fingerprint Image               |
| ID                        | Identification                              |
| nCIR                      | no Connected Identity Register              |
| SV                        | Supervised                                  |
| TF                        | Traveller File                              |
| USV                       | Unsupervised                                |
| VER                       | Verification                                |
| wCIR                      | with Connected Identity Register            |

**Table 8.2** Overview PAP ID Optional Information Items

### <span id="page-25-0"></span>List of Abbreviations

<span id="page-25-4"></span><span id="page-25-3"></span><span id="page-25-2"></span><span id="page-25-1"></span>

| Abbreviation | Description                   |
|--------------|-------------------------------|
| AP           | Application Profile           |
| FM           | Function Module               |
| HLBS         | High Level Biometric Services |
| PAP          | Partial Application Process   |

### <span id="page-26-0"></span>Bibliography

<span id="page-26-1"></span>[BIB\_RFC2119] *RFC 2119: Key words for use in RFCs to Indicate Requirement Levels.*
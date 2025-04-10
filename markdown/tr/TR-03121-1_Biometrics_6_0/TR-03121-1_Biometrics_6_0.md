![](_page_0_Picture_0.jpeg)

BSI Technical Guideline TR-03121-1

# Biometrics for Public Sector Applications

Part 1: Framework

Version 6.0

![](_page_0_Picture_5.jpeg)

Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn E-Mail: trbiometrics@bsi.bund.de Internet: https://www.bsi.bund.de © Federal Office for Information Security 2023

| 1.   | Changelog<br>                                                   | 1  |
|------|-----------------------------------------------------------------|----|
| 1.1. | Changelog Version 5.4-draft1<br>                                | 1  |
| 1.2. | Changelog Version 5.4-draft2<br>                                | 4  |
| 1.3. | Changelog Version 6.0<br>                                       | 8  |
| 2.   | Introduction<br>                                                | 12 |
| 2.1. | Motivation and Objectives of Technical Guideline Biometrics<br> | 12 |
| 2.2. | Target Audience and User<br>                                    | 12 |
| 2.3. | Terminology<br>                                                 | 13 |
| 2.4. | Business Process Modelling Notation (BPMN)<br>                  | 13 |
| 3.   | Structure of Technical Guideline Biometrics<br>                 | 14 |
| 4.   | How to use this Technical Guideline<br>                         | 16 |
| 5.   | Logging scheme<br>                                              | 17 |
| 5.1. | Use cases<br>                                                   | 17 |
| 5.2. | XML schemas<br>                                                 | 17 |
| 6.   | Application Profiles<br>                                        | 18 |
| 7.   | Organisation of the Function Modules<br>                        | 19 |
| 8.   | Organisation of the Partial Application Processes<br>           | 22 |
|      | List of Abbreviations<br>                                       | 23 |
|      | Bibliography<br>                                                | 24 |

### **List of Figures**

| 2.1. | BPMN Symbols used for the Process Modelling<br> | 13 |
|------|-------------------------------------------------|----|
| 3.1. | Class Diagram of the Technical Guidelines<br>   | 15 |

### <span id="page-4-0"></span>**1. Changelog**

The following tables present the changes introduced to this Technical Guideline since version 5.2. chan gelog lists the changes grouped per part of this Technical Guideline, and per building block [\(Application Pro](#page-26-1) [file \(AP\),](#page-26-1) [Partial Application Process \(PAP\)](#page-26-2), Task, [Function Module \(FM\)](#page-26-3)) or element (section, table, figure):

- **•** *Added* for new features
- **•** *Changed* for changes in existing functionality
- **•** *Deprecated* for soon-to-be removed features
- **•** *Removed* for now removed features
- **•** *Fixed* for any bug fixes
- **•** *Security* in case of vulnerabilities

#### <span id="page-4-1"></span>**1.1. Changelog Version 5.4-draft1**

This chapter includes all changes between Version 5.3 and Version 5.4-draft1.

#### **1.1.1. Changelog BSI TR-03121, General**

| Element Name | Type of<br>Change | Change Description                             |
|--------------|-------------------|------------------------------------------------|
| Schema       | Changed           | Changed schema version to 5v1 for all volumes. |

**Table 1.1** Changelog BSI TR-03121, General

#### **1.1.2. Changelog BSI TR-03121, Part 1**

| Element Name   | Type of<br>Change | Change Description                                    |
|----------------|-------------------|-------------------------------------------------------|
| Logging scheme | Changed           | Updated chapter according to new usage of schema 5v1. |

**Table 1.2** Changelog BSI TR-03121, Part 1

#### **1.1.3. Changelog BSI TR-03121, Part 2, Volume HLBS**

| Element Name                                                   | Type of<br>Change | Change Description                   |
|----------------------------------------------------------------|-------------------|--------------------------------------|
| Service Definition Faci<br>al Image Acquisition Sys<br>tem     | Changed           | Usage of schema 5v1 for all volumes. |
| Service Definition Basic<br>Facial Image Acquisition<br>System | Changed           | Usage of schema 5v1 for all volumes. |
| Service Definition Finger<br>print Acquisition                 | Changed           | Usage of schema 5v1 for all volumes. |
| Service Definition Rolled<br>Fingerprint Acquisition           | Changed           | Usage of schema 5v1 for all volumes. |

| Element Name                              | Type of<br>Change | Change Description                   |
|-------------------------------------------|-------------------|--------------------------------------|
| Service Definition Self<br>Service System | Changed           | Usage of schema 5v1 for all volumes. |

**Table 1.3** Changelog BSI TR-03121, Part 2

#### **1.1.4. Changelog BSI TR-03121, Part 3**

| TR Volume             | Block /<br>Section /<br>Type | Name                            | Type of<br>Change | Change Description                                                                    |
|-----------------------|------------------------------|---------------------------------|-------------------|---------------------------------------------------------------------------------------|
| ARE, BCL,<br>GID, IMA | FM                           | LOG-ALL<br>GENERIC              | Changed           | Changed requirements for IDs.                                                         |
| ARE, BCL,<br>GID, IMA | FM                           | LOG-FI<br>GENERIC               | Changed           | Introduced Delivery Element and tradd:BinaryData.                                     |
| GID                   | FM                           | LOG-FP<br>GENERIC               | Changed           | Introduced Delivery Element and tradd:BinaryData.                                     |
| GID                   | FM                           | LOG-FI<br>GID2                  | Changed           | Introduced Delivery Element and tradd:BinaryData.                                     |
| GID                   | FM                           | LOG-FP<br>GID2                  | Changed           | Introduced tradd:BinaryData Element.                                                  |
| GID                   | FM                           | COD-FI<br>GENERIC               | Changed           | Introduced Delivery Element.                                                          |
| GID                   | Basics                       | Legal Re<br>quire<br>ments      | Changed           | Added bibliography reference to EU regulation 1157/2019.                              |
| BCL, IMA              | FM                           | COM<br>FI-BCL,<br>COM-FI<br>IMA | Changed           | Changing description of compression ratio                                             |
| ARE, IMA              | FM                           | COM-FP<br>WSQE                  | Changed           | Changing description of compression ratio                                             |
| GID                   | FM                           | BIP-FI<br>GID                   | Changed           | Updated requirements                                                                  |
| ARE                   | PAP Task                     | ACQ<br>FPR-1                    | Changed           | Logging of each quality value of a capture attempt                                    |
| IMA                   | FM                           | COM-FP<br>IMA                   | Changed           | GSAT3 format for SIS instead of NIST file                                             |
| ARE                   | FM                           | COD-ALL<br>ARE                  | Changed           | Changed root element to are-log for new schema version 5v1.                           |
| BCL                   | FM                           | COD-ALL<br>BCL                  | Changed           | Changed schema version to 5v1.                                                        |
| GID                   | FM                           | COD-ALL<br>GID                  | Changed           | Changed root element to gid-log for new schema version 5v1.                           |
| IMA                   | FM                           | COD-ALL<br>IMA                  | Changed           | Changed schema version to 5v1.                                                        |
| ARE, BCL,<br>GID, IMA | FM                           | COD-FI<br>GENERIC               | Changed           | Changed schema version 5v1 for all volumes.                                           |
| BCL                   | FM                           | COD-FI<br>VER                   | Changed           | Fixed element to log for verifications bcl-log and example refe<br>rence accordingly. |

| TR Volume             | Block /<br>Section /<br>Type | Name                         | Type of<br>Change     | Change Description                                                                                                                                                                                                                                                                                                                                            |
|-----------------------|------------------------------|------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BCL                   | FM                           | COD-FP<br>VER                | Changed               | Fixed element to log for verifications bcl-log and example refe<br>rence accordingly.                                                                                                                                                                                                                                                                         |
| ARE                   | FM                           | LOG-ALL<br>ARE               | Changed               | Reduced information in LOG FM and moved to schema documenta<br>tion.                                                                                                                                                                                                                                                                                          |
| ARE, BCL,<br>GID, IMA | FM                           | LOG-ALL<br>GENERIC           | Changed               | Reduced information in LOG FM and moved to schema documenta<br>tion.                                                                                                                                                                                                                                                                                          |
| GID                   | FM                           | LOG-ALL<br>GID               | Changed               | Added application profile log information.                                                                                                                                                                                                                                                                                                                    |
| ARE, BCL,<br>GID, IMA | FM                           | LOG-FI<br>GENERIC            | Changed               | Added FaceDelivery. Removed information from FM, as they are al<br>ready defined in the schema. Restructured left information.                                                                                                                                                                                                                                |
| ARE, BCL,<br>GID, IMA | FM                           | LOG-FP<br>GENERIC            | Changed               | Added FaceDelivery. Removed information from FM, as they are al<br>ready defined in the schema. Restructured left information.                                                                                                                                                                                                                                |
| GID                   | FM                           | LOG-FP<br>GID                | Changed               | Restructured FM.                                                                                                                                                                                                                                                                                                                                              |
| GID                   | FM                           | LOG-FI<br>GID                | Changed               | Resturctured FM.                                                                                                                                                                                                                                                                                                                                              |
| ARE                   | FM                           | LOG-ALL<br>ARE               | Changed               | Added ApplicationProfile information.                                                                                                                                                                                                                                                                                                                         |
| GID                   | AP                           | AP Scan<br>of Photo<br>graph | Ad<br>ded/Chan<br>ged | Application Profile "Scan of Photograph" was added again to Volume<br>GID since there will be a few special cases, in which scanning of pho<br>tographs is still permitted after 1st of May 2025. The scan shall result<br>in a facial image of 622x800 pixels (meaning scan with 600 dpi) to be<br>compliant with the future passport production procedures. |
| GID                   | FM                           | COD-FI<br>PRD                | Changed               | All facial images which are delivered to the German passport pro<br>duction shall have a size of 622x800 pixels, no matter the source of<br>the image (live enrolled, delivered, scanned).                                                                                                                                                                    |
| GID                   | FM                           | COD-FI<br>ROR                | Changed               | Images captured live or delivered to the authority are stored in the<br>Register of Residents with a resolution of at least 1244x1600 pixels.<br>Scanned images are stored with a resolution of at least 622x800 pi<br>xels.                                                                                                                                  |
| GID                   | FM                           | COD-FI<br>GID/GID2           | Renamed               | COD-FI-GID was renamed to COD-FI-CHIP. COD-FI-GID2 re<br>named to COD-FI-GID.                                                                                                                                                                                                                                                                                 |
| GID                   | FM                           | QA-FI<br>GID                 | Changed               | Quality assessment was adapted to the new scanning scenario: The<br>quality assessment is to be conducted on the original image. For<br>live captured and delivered images, the original image has a size of<br>1244x1600 pixels (with an IED of at least 300 pixels), for scanned<br>images, the size is 622x800 pixels (with an IED of at least 90 pixels). |
| GID                   | FM                           | LOG-FI<br>GID2               | Changed               | Facial images are stored as JPEG in the future. File type "icao-cbeff<br>bit-bdb-19794-5" was therefore replaced with "JPEG".                                                                                                                                                                                                                                 |
| ARE, BCL,<br>GID, IMA | FM                           | Different<br>FMs             | Changed               | For facial images in colour, the colour space "sRGB" with a colour<br>depth of 24 bit is now mandatory in all Volumes. For grey scale<br>images 8 bit sRGB is used.                                                                                                                                                                                           |
| ARE, BCL,<br>GID, IMA | FM                           | UI-FI-BSJ                    | Partly Remo<br>ved    | UI-FI-BSJ ist only required in scenarios with automated facial image<br>acquisition. FM was consequently removed from all scenarios in<br>which a digital camera is used.                                                                                                                                                                                     |
| BCL, GID              | FM                           | AH-FI<br>ICS/ICS2            | Changed               | Mandatory Digital Mirror: The feedback screen (digital mirror) is<br>now mandatory in all scenarios where facial images are captured au<br>tomatically (i.e. SSS, FIAS and ABC in Volumes BCL and GID).                                                                                                                                                       |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                              | Type of<br>Change | Change Description                                                                                                                                                                                                                                            |
|-----------------------|------------------------------|-----------------------------------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID                   | AP                           | AP Bio<br>metric Da<br>ta Selec<br>tion                                           | Changed           | AP Biometric Data Selection now includes the control verification<br>of fingerprint images which was previously part of AP Unsupervised<br>Self-Service Fingerprint Acquisition System.                                                                       |
| GID                   | AP                           | AP Unsu<br>pervised<br>Self-Ser<br>vice Fin<br>gerprint<br>Acquisiti<br>on System | Changed           | The control verification of fingerprint images was moved from AP<br>Unsupervised Self-Service Fingerprint Acquisition System to AP Bio<br>metric Data Selection.                                                                                              |
| GID                   | AP                           | AP Super<br>vised Fin<br>gerprint<br>Acquisiti<br>on                              | Changed           | UI-FP-BSJ is no longer part of AP SUpervised Fingerprint Acquisiti<br>on, because in supervised scenarios, no feedback for biometric sub<br>jects is needed.                                                                                                  |
| GID                   | FM                           | COM-FI<br>JP2                                                                     | Changed           | The chip image shall have a file size of 17 kB including header infor<br>mation.                                                                                                                                                                              |
| ARE, BCL,<br>GID, IMA | PAP                          | Different<br>PAPs                                                                 | Changed           | HLBS has been included as a possible interface in all matching PAPs.<br>HLBS is optional when capturing facial images and fingerprints.<br>However, if HLBS is used, then the corresponding service definition<br>from Volume 2, Part 2 shall be implemented. |
| GID                   | AP                           | AP De<br>Mail                                                                     | Deleted           | Delivery of facial images via De-Mail is no longer permitted from<br>May 2025 on. Therefore, the corresponding Application Profile was<br>deleted.                                                                                                            |

**Table 1.4** Changelog BSI TR-03121, Part 3

#### <span id="page-7-0"></span>**1.2. Changelog Version 5.4-draft2**

This chapter includes all changes between Version 5.4-draft1 and Version 5.4-draft2.

#### **1.2.1. Changelog BSI TR-03121, General**

| Element Name | Type of<br>Change | Change Description   |
|--------------|-------------------|----------------------|
| NFIQ Version | Changed           | Use NFIQ Version 2.2 |

**Table 1.5** Changelog BSI TR-03121, General

#### **1.2.2. Changelog BSI TR-03121, Part 1**

| Element Name                                         | Type of<br>Change | Change Description                                          |
|------------------------------------------------------|-------------------|-------------------------------------------------------------|
| Organisation of<br>Partial Applicati<br>on Processes | Changed           | Added DEL (Delivery) to table of primary information items. |

**Table 1.6** Changelog BSI TR-03121, Part 1

#### **1.2.3. Changelog BSI TR-03121, Part 2, Volume HLBS**

| Element Name                     | Type of<br>Change | Change Description                                         |
|----------------------------------|-------------------|------------------------------------------------------------|
| Data Type Application<br>Profile | Changed           | Considered new application profile name of GID Basic FIAS. |

**Table 1.7** Changelog BSI TR-03121, Part 2

#### **1.2.4. Changelog BSI TR-03121, Part 3**

| TR Volume | Block /<br>Section /<br>Type | Name                                                  | Type of<br>Change | Change Description                                                                                                                                                                                                                                                                  |
|-----------|------------------------------|-------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID       | FM                           | AH-FI<br>ICS2, AH<br>FI-SSS2                          | Changed           | Added sitting position for SSS in context GID as alternative to stan<br>ding position. The biometric subject can now be standing upright in<br>front of the camera or sitting upright in front of the camera. In both<br>cases, a body height range of 140-200 cm shall be covered. |
| GID       | FM                           | AH-FI<br>ICS2                                         | Changed           | Added clarification, that adaption to environmental lighting condi<br>tions is only expected within common environmental setting and<br>with normal lighting conditions (no direct light from windows etc.).                                                                        |
| GID       | FM                           | QA-FI<br>GID                                          | Changed           | Inter-eye distance of scanned facial mages was set to (minimum) 120<br>pixels.                                                                                                                                                                                                      |
| GID       | AP                           | Facial<br>Image Di<br>gital De<br>livery via<br>Cloud | Changed           | Added clarification for requirements of facial images delivered via<br>cloud. Capture has to be conducted by natural person who ensures<br>quality of facial image and the exlusion of presenation attacks.                                                                         |
| GID       | AP                           | Facial<br>Image Di<br>gital De<br>livery via<br>Cloud | Changed           | Added clarification for requirements of facial images delivered via<br>cloud. Facial images taken be the enrolee him- or herself (selfie) and<br>facial images taken by a non-professional photographer shall not be<br>used.                                                       |
| GID       | AP                           | Self Ser<br>vice Sys<br>tems                          | Changed           | Application Profiles "Unsupervised Self-Service Facial Image Acqui<br>sition System" and "Unsupervised Self-Service Fingerprint Acquisiti<br>on System" were clarified to only be used for systems located within<br>agencies and connected directly to the agency's network.       |
| GID       | AP                           | Biometric<br>Data<br>Selection                        | Changed           | Added clarification on which sources of facial images exist.                                                                                                                                                                                                                        |
| All       | FM                           | PAD-FI<br>APP/APP1                                    | Changed           | Added requirement of 2% false-alarm-rate maximum.                                                                                                                                                                                                                                   |
| All       | FM                           | PAD-FP<br>APP/APP1                                    | Changed           | Added requirement of 2% false-alarm-rate maximum.                                                                                                                                                                                                                                   |
| GID       | FM                           | AH-FI<br>ICS2                                         | Changed           | For automated facial images acquisitions systems, the requirement<br>to display a feedback screen (digital mirror) was changed from man<br>datory to optional.                                                                                                                      |
| IMA       | FM                           | COD-ALL<br>IMA                                        | Changed           | Added alternative to log GSAT container as base64 encoded Binary<br>Record.                                                                                                                                                                                                         |
| ARE       | FM                           | COD-ALL<br>ARE                                        | Changed           | Changed Record to BinaryRecord (was renamed in schema).                                                                                                                                                                                                                             |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                        | Type of<br>Change | Change Description                                                                                                                                                                                                                                   |
|-----------------------|------------------------------|-------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID                   | FM                           | Different<br>FMs                                            | Changed           | Removed grey scale images for all live captured and cloud images.<br>Only in the case of scanning, grey scale photographs can be scanned<br>in grey scale (photographs in colour shall be scanned in colour, not<br>grey scale).                     |
| GID                   | AP                           | AP Super<br>vised Ba<br>sic Facial<br>Image Ac<br>quisition | Changed           | Renamed Application Profile "Supervised Facial Image Acquisition<br>with Digital Camera" to "Supervised Basic Facial Image Acquisition"<br>to clarify scope of AP.                                                                                   |
| GID                   | AP                           | AP Facial<br>Image De<br>livery by<br>Digital Ca<br>mera    | Added             | Added new Application Profile for Facial Image Delivery by Digital<br>Camera that is detached from the operators application.                                                                                                                        |
| GID                   | FM                           | COM-FI<br>JP2                                               | Changed           | Renamed to COM-FI-CHIP to make usage clearer.                                                                                                                                                                                                        |
| GID                   | FM                           | COD-FI<br>PRD                                               | Changed           | Changed image format to JPEG 2000. The facial image is coded as<br>JPEG 2000 before data transmission to the central document pro<br>duction. The highest possible quality level (i.e. the least compression<br>possible) shall be used.             |
| GID                   | General                      | Basics                                                      | Changed           | Changed introduction text to clarify that for fingerprints, a repeated<br>quality assessment at the counter is not necessary. For fingerprints,<br>quality assessment is only done during the enrolment process, not<br>during control verification. |
| GID                   | PAP                          | DEL-FI<br>SV-1                                              | Added             | Added new PAP for digital delivered facial images.                                                                                                                                                                                                   |
| GID                   | FM                           | LOG-ALL<br>GID                                              | Changed           | Changed ApplicationProfile entries according to name changes of<br>application profiles.                                                                                                                                                             |
| ARE, BCL,<br>GID, IMA | FM                           | UI-FI-OP                                                    | Changed           | Added requirements to display PAD warning and result the opera<br>tor if PAD was detected.                                                                                                                                                           |
| GID                   | FM                           | O-ALL<br>USV                                                | Changed           | Added requirement that within the application scenario GID, de<br>vice shall be set up in such a way that it can permanently obser<br>ved by an official.                                                                                            |
| GID                   | FM                           | AS-FI-FBS                                                   | Changed           | Requirement "no compression" was sharpened to the effect, that<br>apart from the compression of JPEG itself, no prior or further com<br>pression shall be applied.                                                                                   |
| GID                   | PAP                          | ACQ-FI<br>AUTO-1                                            | Changed           | Added distinction regarding time limits of the acquisition process:<br>Within the application context GID, the overall acquisition process<br>shall not exceed 30 seconds.                                                                           |
| GID                   | FM                           | QA-FI<br>GID                                                | Changed           | The dimensions of the images (width and height in pixels) may now<br>be +/- 10 pixels.                                                                                                                                                               |
| ARE                   | FM                           | LOG-ALL<br>ARE                                              | Changed           | Precised logging for facial images from CIR.                                                                                                                                                                                                         |
| BCL                   | FM                           | LOG-ALL<br>BCL                                              | Changed           | Adapted FM to current schema version.                                                                                                                                                                                                                |
| GID                   | FM                           | LOG-ALL<br>GID                                              | Changed           | Removed Processing for Document Production from Application<br>Profile list for logging.                                                                                                                                                             |
| GID                   | FM                           | LOG-FI<br>GID2                                              | Changed           | Adapted FM to current schema version.                                                                                                                                                                                                                |

| TR Volume        | Block /<br>Section /<br>Type | Name                                                     | Type of<br>Change | Change Description                                                                                                                                                                                                                                                                   |
|------------------|------------------------------|----------------------------------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID              | FM                           | LOG-FP<br>GID2                                           | Changed           | Adapted FM to current schema version.                                                                                                                                                                                                                                                |
| GID              | AP                           | Biometric<br>Data<br>Selection                           | Changed           | Clarified wording about the resolution of facial images. Also, post<br>processing of facial images (repeated rotation and cropping) is no<br>longer a step of the Facial Image Selection Procedure.                                                                                  |
| BCL, GID         | PAP Task                     | ACQ-FPP<br>USV-1                                         | Changed           | Simplified timeouts: Only one timeout.                                                                                                                                                                                                                                               |
| BCL, GID         | PAP Task                     | ACQ-FPS<br>USV-1                                         | Changed           | Simplified timeouts: Only one timeout.                                                                                                                                                                                                                                               |
| BCL, GID         | PAP Task                     | ACQ-FPS<br>USV-1                                         | Changed           | Add configurable number of retries, if wrong slap is detected.                                                                                                                                                                                                                       |
| GID              | General                      | Basics                                                   | Changed           | Changed text regarding sources of facial images because the intro<br>duction of AP Facial Image Delivery by Digital Camera. The distinc<br>tion between live images and delivered images is updated to cover all<br>possible image origins.                                          |
| GID              | FM                           | COD-FI<br>GID and<br>COD-FI<br>ROR                       | Changed           | Added requirement that the highest possible quality level (i.e. the<br>least compression possible) shall be used.                                                                                                                                                                    |
| GID              | FM                           | REF-FI<br>GID                                            | Changed           | Added requirements for storage of location where the facial image<br>was taken ("lichtbildaufnehmende Stelle").                                                                                                                                                                      |
| GID              | AP                           | Supervi<br>sed Facial<br>Image Ac<br>quisition<br>System | Changed           | Added clarification that system is not required to provide a manual<br>mode. In this case, other means to capture a facial image manually<br>must be available within the agency (Basic Facial Image Acquisition<br>System and/or Facial Image Digital Delivery via Digital Camera). |
| GID              | FM                           | COM-FI<br>CHIP                                           | Changed           | Deleted requirement of test interface as compression of JPEG2000<br>is no longer a task that performed within the agency but in docu<br>ment production only.                                                                                                                        |
| GID              | FM                           | LOG-FI<br>GID and<br>LOG-FI<br>GID2                      | Changed           | Renamed LOG-FI-GID to LOG-FI-CHIP to make usage in document<br>production clearer. Renamed LOG-FI-GID2 to LOG-FI-GID for con<br>sistency.                                                                                                                                            |
| GID              | FM                           | LOG-FP<br>GID and<br>LOG-FP<br>GID2                      | Changed           | Renamed LOG-FP-GID to LOG-FP-CHIP to make usage in document<br>production clearer. Renamed LOG-FP-GID2 to LOG-FP-GID for con<br>sistency.                                                                                                                                            |
| GID              | AP                           | Biometric<br>Data<br>Selection                           | Changed           | Added reference to AP Supervised Fingerprint Acquisition to be used<br>during control verification. When conducting a control verification,<br>no quality thresholds are to be applied during the repeated acquisiti<br>on of fingerprints.                                          |
| GID              | FM                           | AH-FI<br>DC2 and<br>AH-FI<br>ICS2                        | Changed           | Added reference to ICAO Technical Guideline "Portrait Quality". Wi<br>de-agle setting must not be used.                                                                                                                                                                              |
| ARE, BCL,<br>IMA | FM                           | AH-FI-DC<br>and AH<br>FI-ICS                             | Changed           | Added reference to ICAO Technical Guideline "Portrait Quality". Wi<br>de-agle setting must not be used.                                                                                                                                                                              |
| GID              | FM                           | AS-FI<br>ICS2                                            | Changed           | Clarified uniform background greyscale in case of elimination of the<br>original background.                                                                                                                                                                                         |

| TR Volume | Block /<br>Section /<br>Type | Name                           | Type of<br>Change      | Change Description                                                                                                                                                                                                                                                                                     |
|-----------|------------------------------|--------------------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID       | AP                           | Biometric<br>Data<br>Selection | Changed                | Modified the figure concerning the process of control verification of<br>fingerprints: added the operator's task to control biometric sub<br>ject's fingers in case of PAD alarms.                                                                                                                     |
| GID       | FM                           | EVA-* and<br>EVA-ALL<br>APP    | Deleted resp.<br>Added | Deleted current EVA-FMs from GID volume. The quality statistics<br>that are to be created by the document manufacturer shall be build<br>according to an annex of this TR in the future. This annex will be<br>specified in a future version of this TR. Added EVA-ALL-APP as link<br>to future annex. |

**Table 1.8** Changelog BSI TR-03121, Part 3

#### <span id="page-11-0"></span>**1.3. Changelog Version 6.0**

This chapter includes all changes between Version 5.4-draft2 and Version 6.0.

#### **1.3.1. Changelog BSI TR-03121, General**

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
|              |                   |                    |

**Table 1.9** Changelog BSI TR-03121, General

#### **1.3.2. Changelog BSI TR-03121, Part 1**

| Element Name | Type of<br>Change | Change Description |
|--------------|-------------------|--------------------|
|              |                   |                    |

**Table 1.10** Changelog BSI TR-03121, Part 1

#### **1.3.3. Changelog BSI TR-03121, Part 2, Volume HLBS**

| Element Name                                 | Type of<br>Change | Change Description            |
|----------------------------------------------|-------------------|-------------------------------|
| Service Definition Facial<br>Delivery System | Added             | Added new service definition. |

**Table 1.11** Changelog BSI TR-03121, Part 2

#### **1.3.4. Changelog BSI TR-03121, Part 3**

| TR Volume | Block /<br>Section /<br>Type | Name                           | Type of<br>Change | Change Description                                                                                                                    |
|-----------|------------------------------|--------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| GID       | FM                           | AS-FI<br>ICS3                  | Changed           | Replaced the distance measurement by a face recognition property:<br>process terminates if a face completely leaves the capture area. |
| GID       | AP                           | Biometric<br>Data<br>Selection | Changed           | Modified two figures to be compliant with the TR regulations.                                                                         |
| BCL, GID  | FM                           | O-ALL<br>USV                   | Changed           | Edited requirements to make specifications of 'visible' and 'observa<br>ble' clearer.                                                 |
| GID       | FM                           | AH-FI<br>SSS2                  | Changed           | Added the definition of Frankfurt Horizon.                                                                                            |

| TR Volume             | Block /<br>Section /<br>Type | Name                                                                          | Type of<br>Change | Change Description                                                                                                                                                                                                                       |  |
|-----------------------|------------------------------|-------------------------------------------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| GID                   | AP                           | Unsu<br>pervised<br>Self-Ser<br>vice Faci<br>al Image<br>Acquistion<br>System | Changed           | Added a clarifying footnote that the selection of acquired facial<br>images by the biometric subject is allowed under certain conditions.                                                                                                |  |
| GID                   | AP                           | Biometric<br>Data<br>Selection                                                | Changed           | Modified and simplified process flow of figure "Process Facial Image<br>Selection Procedure for German Identity Documents purposes". Ad<br>justed some wording.                                                                          |  |
| GID                   | AP                           | Biometric<br>Data<br>Selection                                                | Changed           | Modified and simplified process flow of figure "Overview Process of<br>Control Verification of Fingerprints".                                                                                                                            |  |
| GID                   | AP                           | Biometric<br>Data<br>Selection                                                | Changed           | Added required function modules to the table.                                                                                                                                                                                            |  |
| GID                   | AP                           | Biometric<br>Data<br>Selection                                                | Changed           | Rephrased and clarified text regarding Mandatory Process of Finger<br>print Images.                                                                                                                                                      |  |
| GID                   | FM                           | PAD-FI<br>APP1                                                                | Changed           | Deleted relation to fingerprints.                                                                                                                                                                                                        |  |
| GID                   | AP                           | Biometric<br>Data<br>Selection                                                | Changed           | Modified figure "Process Facial Image Selection Procedure for Ger<br>man Identity Documents purposes" regarding referenced FMs at first<br>task box. Added accidentally deleted text in Mandatory Process re<br>garding both modalities. |  |
| BCL, GID,<br>ARE, IMA | FM                           | LOG-FP<br>GENERIC                                                             | Changed           | Added configured pixel density of fingerprint scanner to log as Con<br>figurationInformation.                                                                                                                                            |  |
| GID                   | FM                           | LOG-FI<br>GID                                                                 | Changed           | Added configured pixel density to log for scanned images as Confi<br>gurationInformation.                                                                                                                                                |  |
| GID                   | AP                           | Unsuper<br>vised Self<br>Service<br>Finger<br>print Ac<br>quisition<br>System | Changed           | Removed unnecessary FM (FM UI-FP-OP) from table with Mandato<br>ry Function Modules.                                                                                                                                                     |  |
| GID                   | AP                           | Unsuper<br>vised Self<br>Service<br>Finger<br>print Ac<br>quisition<br>System | Changed           | Added necessary FM (FM COD-FP-CHIP) in table with Mandatory<br>Function Modules.                                                                                                                                                         |  |
| GID                   | General                      | Basics                                                                        | Changed           | Added an example how multiple processes can be reduced.                                                                                                                                                                                  |  |
| GID                   | FM                           | QA-FI<br>GENERIC                                                              | Changed           | Deleted the explicit mention of the file format JPEG2000.                                                                                                                                                                                |  |
| GID                   | FM                           | COD-FI<br>CHIP                                                                | Changed           | Added Source Type as information to be stored together with facial<br>image in the chip.                                                                                                                                                 |  |

| TR Volume             | Block /<br>Section /<br>Type | Name                                          | Type of<br>Change | Change Description                                                                                                                                                                 |  |
|-----------------------|------------------------------|-----------------------------------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| GID                   | FM                           | AH-FI<br>DC2, AH<br>FI-ICS2,<br>AS-FI<br>ICS2 | Changed           | Added reference to 'ICAO Technical Report Portrait Quality' regar<br>ding uniform background. Also, added recommendation that uni<br>form background should be grey.               |  |
| ARE, BCL,<br>IMA      | FM                           | AH-FI-DC                                      | Changed           | Added reference to 'ICAO Technical Report Portrait Quality' regar<br>ding uniform background. Also, added recommendation that uni<br>form background should be grey.               |  |
| GID                   | FM                           | QA-FI<br>GID                                  | Changed           | Removed range of +/- 10 pixels for image height and image width, as<br>there is no tolerance necessary for these criteria.                                                         |  |
| GID                   | General                      | ---                                           | Changed           | Renamed Register of Residents to Register of Documents.                                                                                                                            |  |
| GID                   | FM                           | LOG-ALL<br>GID                                | Changed           | Renamed RegisterOfResidents to RegisterOfDocuments.                                                                                                                                |  |
| GID                   | FM                           | LOG-ALL<br>GID                                | Changed           | Added information on StartTime and EndTime of enrolment ele<br>ment as well as the information that all collected data are to be<br>maintained if not explicitly stated otherwise. |  |
| GID                   | FM                           | LOG-FP<br>GID                                 | Changed           | Changed allowance of appreance Finger element to FingerAcqui<br>sition.                                                                                                            |  |
| GID                   | FM                           | COD-FI<br>ROR                                 | Changed           | Renamed to COD-FI-ROD (Register of Documents)                                                                                                                                      |  |
| GID                   | FM                           | REF-FI<br>GID                                 | Changed           | Added detailed information on the location, where the facial image<br>was captured (lichtbildaufnehmende Stelle).                                                                  |  |
| BCL, GID              | PAP Task                     | ACQ-FPS<br>USV-1                              | Changed           | Modified describing text to bring it in line with corresponding mo<br>del.                                                                                                         |  |
| BCL, GID              | PAP                          | ACQ-FI<br>SV-5                                | Changed           | Modified describing text regarding software based QA and manual<br>review of the operator to bring it in line with corresponding model.                                            |  |
| BCL, GID              | PAP                          | ACQ-FI<br>SV-5                                | Changed           | The support of a manual service mode is optional within the applica<br>tion context GID but mandatory otherweise.                                                                  |  |
| ARE                   | AP                           | Arrival At<br>testation<br>Document           | Changed           | Precised overview process and introduced PAP Supervised Facial<br>Image Digital Delivery.                                                                                          |  |
| ARE                   | AP                           | Arrival At<br>testation<br>Document           | Changed           | Precised overview process and introduced PAP Supervised Facial<br>Image Digital Delivery.                                                                                          |  |
| ARE, GID              | PAP                          | DEL-FI<br>SV-1                                | Changed           | Added interface requirements.                                                                                                                                                      |  |
| BCL                   | ---                          | Bibliogra<br>phy                              | Changed           | Updates EES Interface Control Document to version 0.7.2.                                                                                                                           |  |
| ARE                   | PAP                          | ACQ<br>FP442-<br>SV-2                         | Changed           | Modified model regarding addition of selection option right before<br>capture of thumbs.                                                                                           |  |
| BCL, GID,<br>ARE, IMA | FM                           | UI-FI-OP                                      | Changed           | Added requirements regarding displaying PAD alarms to the opera<br>tor.                                                                                                            |  |
| BCL                   | FM                           | QA-FI<br>BCL                                  | Changed           | Deleted ratio of image width and height of 3:4 as quality criterion.                                                                                                               |  |
| ARE, BCL,<br>GID, IMA | FM                           | BIP-FP<br>APP                                 | Changed           | Resolution of 1000 ppi was missing.                                                                                                                                                |  |

| TR Volume        | Block /<br>Section /<br>Type | Name                                                                                            | Type of<br>Change | Change Description                                                                                                                                                                                                                     |
|------------------|------------------------------|-------------------------------------------------------------------------------------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GID              | FM                           | AS-FI<br>ICS2                                                                                   | Changed           | Marked background elimination as full alternative for using a uni<br>form background (removed disclaimer).                                                                                                                             |
| GID              | AP                           | Biometric<br>Data<br>Selection                                                                  | Changed           | All biometric data from a SSS are to be retrieved together (not sepa<br>rated in facial images and fingerprints).                                                                                                                      |
| IMA              | APs                          | Multi<br>modal<br>Processing<br>in Immi<br>gration<br>Autho<br>rities for<br>EES and<br>for SIS | Changed           | Added FM AS-FP-SF for processes where single-finger scanner are<br>used as backup.                                                                                                                                                     |
| GID              | FM                           | PAD-FI<br>APP1                                                                                  | Changed           | Changed interpretation of PAD score. In dependence on the ISO/IEC<br>30107-2:2017 the value 0 is bona fide, 1 (not 100) an attack. The va<br>lue range/data type is kept to [0,1] and double, in order to keep more<br>interim values. |
| ARE, GID,<br>IMA | FM                           | PAD-FP<br>APP                                                                                   | Changed           | Changed interpretation of PAD score. In dependence on the ISO/IEC<br>30107-2:2017 the value 0 is bona fide, 1 (not 100) an attack. The va<br>lue range/data type is kept to [0,1] and double, in order to keep more<br>interim values. |
| BCL              | FM                           | PAD-FI<br>APP                                                                                   | Changed           | Changed interpretation of PAD score. In dependence on the ISO/IEC<br>30107-2:2017 the value 0 is bona fide, 1 (not 100) an attack. The va<br>lue range/data type is kept to [0,1] and double, in order to keep more<br>interim values. |
| BCL              | FM                           | PAD-FP<br>APP1                                                                                  | Changed           | Changed interpretation of PAD score. In dependence on the ISO/IEC<br>30107-2:2017 the value 0 is bona fide, 1 (not 100) an attack. The va<br>lue range/data type is kept to [0,1] and double, in order to keep more<br>interim values. |

**Table 1.12** Changelog BSI TR-03121, Part 3

## <span id="page-15-0"></span>**2. Introduction**

#### <span id="page-15-1"></span>**2.1. Motivation and Objectives of Technical Guideline Biometrics**

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

#### <span id="page-15-2"></span>**2.2. Target Audience and User**

Audience for this guideline are institutions that are dealing with projects using biometric characteristics in public sector applications. These include:

- **•** Agencies that are issuing identity documents or visas, e.g. passport agencies of the local authorities mis sions abroad of the Federal Foreign Office.
- **•** Public Authorities using biometric applications for identity verification of people, e.g. the German Federal Police (Polizeien des Bundes) or the Police of the Federal States (Polizeien der Länder), the German Customs Administration (Bundeszollverwaltung) or the Federal Administrative Office (Bundesverwaltungsamt).

Beside these users, this guideline also addresses vendors of biometric systems as well integrators and app lication developers.

#### <span id="page-16-0"></span>**2.3. Terminology**

The key words "MUST", MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this Technical Guideline are to be interpreted as described in [\[BIB\\_RFC2119\]](#page-27-1).

#### <span id="page-16-1"></span>**2.4. Business Process Modelling Notation (BPMN)**

<span id="page-16-2"></span>The processes in this Technical Guideline are modelled using the Business Process Modelling Notation (BPMN). [Figure 2.1](#page-16-2) gives an overview over the relevant icons herein.

![](_page_16_Figure_6.jpeg)

![](_page_16_Figure_7.jpeg)

### <span id="page-17-0"></span>**3. Structure of Technical Guideline Biometrics**

This Technical Guideline consists of the following parts:

**•** Part 1: Framework (TR-03121-1)

TR-03121-1 is the framework document of the guideline. It explains the concept and the relation between the different parts.

**•** Part 2: Software Architecture (TR-03121-2)

The [High Level Biometric Services \(HLBS\)](#page-26-4) as well as Service Definitions for specific use cases are specified here.

- **•** Part 3: Application Profiles, Function Modules and Processes (TR-03121-3)
	- **•** In the third part, the different Application Profiles with corresponding Partial Application Processes and Function Modules are defined. These contain the detailed technical requirements for each of com ponents.
		- **•** Application Profiles may reference Function Modules, Partial Processes and Service De finitions (refer to Part 2).
		- **•** Partial Application Processes may refer to Function Module Categories and may be comprised of *Tasks*. Tasks are processes which are part of more than one Partial Application Process.
	- **•** For practical purposes, this part is split up in different volumes to serve different user groups.
		- **•** [Border Control \(BCL\)](#page-26-5)
		- **•** [German Identity Documents \(GID\)](#page-26-6)
		- **•** [Alien Register Enrolment \(ARE\)](#page-26-7)
		- **•** [Immigration Authorities \(IMA\)](#page-26-8)

Please refer to [Figure 3.1](#page-18-0) for a class diagram of the structure described above.

<span id="page-18-0"></span>![](_page_18_Figure_1.jpeg)

**Figure 3.1.** Class Diagram of the Technical Guidelines

Additionally, the Technical Guideline BSI-TR 03122 "Conformance Test Specification for Technical Guideline TR-03121 Biometrics for Public Sector Applications" describes the requirements that are essential to declare conformance or to declare the absence of conformance. It consists of the following parts:

- **•** Part 1: Framework (TR-03122-1)
- **•** Part 3: Test Cases for Function Modules and Processes (TR-03122-3)

### <span id="page-19-0"></span>**4. How to use this Technical Guideline**

This chapter gives a short overview how to read and apply this guideline step by step.

- 1. The user chooses the desired Application Profile. With the help of the Application Profile the user can get a deeper insight into the application, the required software architecture components and the described functionality. TR-03121-2 offers further information about the software architecture component model.
- 2. Based on the Application Profile, the mandatory Partial Application Processes and Function Modules are identified. One profile can link to several Partial Application Processes and Function Modules due dif ferent kinds of underlying biometric characteristics or the fact that different technologies (e.g. scanners or digital cameras for the digitisation of a photo) are used.

Function Modules are referenced by an explicit identifier, e.g. AH-FP-GID. The first part identifies the requirement type (e.g. Hardware), the second part represents the biometric characteristic (e.g. fingerprint), and the last part denotes a further descriptor, typically the scope (e.g. German Identity Document).

Function Modules for different biometric characteristics are divided by a comma while a choice between different technologies is denoted by a slash (e.g. AH-FP-FTR, AH-PH-FBS/AH-PH-DC).

If a Function Module is denoted with a placeholder between a less-than and greater-than sign (< >) the actual referenced Function Module is dependant on the context in which the Function Module has been mentioned. For example the Function Module AH-FI-<VL> has been mentioned within a Partial Applica tion Process used in the [BCL volume, then the actual referenced Function Module is AH-FI-BCL. The sa](#page-26-5) me procedure holds for Application Profiles denoted as <AP> analogously. If no specific Function Module applies, then there are no further requirements defined for this context.

Partial Application Processes are referenced by an explicit identifier, refer to Partial Application Profile section.

3. On the basis of identifier according Function Module and Partial Application Processes can be ex amined. Every Function Module and Partial Application Process provides detailed technical requirements and recommendations. Note, each reference to a Function Module or Partial Application Processes is a link within the document.

### <span id="page-20-0"></span>**5. Logging scheme**

#### <span id="page-20-1"></span>**5.1. Use cases**

This chapter specifies a logging scheme, which allows to document all technical activities performed. The schema files contain additional and mandatory information on technical requirements. Such a logging sche me SHALL be used to measure the quality of the biometric processes across different systems, regardless of the used hard- or software. This enables the possibility of an operational monitoring for technical as well as functional processes and evaluations.

#### <span id="page-20-2"></span>**5.2. XML schemas**

The logging scheme is based on a transactional logging format which collects performance and evaluation results from the different application domains. The schema file trbio5v1.xsd imports all other schema files and as such the main file used for validation.

A separate XML schema definition exists for each volume of TR-03121-3, which SHALL be used within the respective application area. [Table 5.1](#page-20-3) gives an overview of the different XML schema files.

<span id="page-20-3"></span>

| Application domain             | Schemafile      | Namespace                         |
|--------------------------------|-----------------|-----------------------------------|
| Alien register enrolment       | are5v1.xsd      | http://trbio.bsi.bund.de/are/5    |
| Border control log             | bcl5v1.xsd      | http://trbio.bsi.bund.de/bcl/5    |
| Type definitions               | biotypes5v1.xsd | http://trbio.bsi.bund.de/base/5   |
| German identity documents      | gid5v1.xsd      | http://trbio.bsi.bund.de/gid/5    |
| High level biometric services  | hlbs5v1.xsd     | http://trbio.bsi.bund.de/hlbs/5   |
| Immigration authorities        | ima5v1.xsd      | http://trbio.bsi.bund.de/ima/5    |
| Conformance test specification | biocts5v1.xsd   | http://trbio.bsi.bund.de/biocts/5 |

**Table 5.1** Overview XML schema files

### <span id="page-21-0"></span>**6. Application Profiles**

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

### <span id="page-22-0"></span>**7. Organisation of the Function Modules**

Specific technical requirements are structured in Function Modules. They contain detailed require ments for the respective component. Function Modules are aligned to the products on the market and to the targets of evaluation. Every Function Module is built of one or more subclauses which are assigned to unique identifiers. Within the subclauses requirements and recommendations are specified in detail.

Function Modules are referenced by their ID, which can contain up to three information items pointing to its contents. The basic structure of an ID is: "FM AAA-BBB-CCC".

Here, *AAA* is the primary information item, pointing to the main contents. *BBB* and *CCC* are optional infor mation items, which can further specify the Function Module. These information items may be two to seven alphanumeric digits. [Table 7.1](#page-22-1) gives an overview of the different primary information items used for Func tion Module categories. [Table 7.2](#page-23-0) gives an overview of the different optional information items *BBB* used for Function Module categories.

<span id="page-22-1"></span>

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

<span id="page-23-0"></span>

| Optional Information Item | Function Module Category                        |
|---------------------------|-------------------------------------------------|
| ALL                       | Overall                                         |
| CCTV                      | Closed Circuit Television (Surveillance Camera) |

| Optional Information Item | Function Module Category |
|---------------------------|--------------------------|
| FI                        | Facial Image             |
| FP                        | Fingerprint              |

**Table 7.2** Overview FM Categories Optional Information Items

### <span id="page-25-0"></span>**8. Organisation of the Partial Application Processes**

Partial Application Processes are referenced by their ID, which can contain up to three information items pointing to its contents. The basic structure of an ID is: "PAP (Task) AAA-BBB-CCC-#".

Here, "Task" is optional and is only used if the *PAP* is a task. *AAA* is the primary information item, pointing to the main contents. *BBB* and *CCC* are optional information items, which can further specify the [PAP](#page-26-2). These information items may be one to six alphanumeric digits. The abbreviations used for the [PAP](#page-26-2) IDs are listed in [Table 8.1](#page-25-1) and [Table 8.2](#page-25-2). All [PAP](#page-26-2) IDs end with a number *#*. This number is usually 1, unless multiple IDs with similar preceding information items exist. In this case, they are enumerated increasingly.

<span id="page-25-1"></span>

| Primary Information Item | Description    |
|--------------------------|----------------|
| ACQ                      | Acquisition    |
| ASS                      | Assessment     |
| DEL                      | Delivery       |
| EVA                      | Evaluation     |
| ID                       | Identification |
| UPD                      | Update         |
| VER                      | Verification   |

**Table 8.1** Overview PAP ID Primary Information Items

<span id="page-25-2"></span>

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

### <span id="page-26-0"></span>**List of Abbreviations**

<span id="page-26-8"></span><span id="page-26-7"></span><span id="page-26-6"></span><span id="page-26-5"></span><span id="page-26-4"></span><span id="page-26-3"></span><span id="page-26-2"></span><span id="page-26-1"></span>

| Abbreviation | Description                   |
|--------------|-------------------------------|
| AP           | Application Profile           |
| ARE          | Alien Register Enrolment      |
| BCL          | Border Control                |
| FM           | Function Module               |
| GID          | German Identity Documents     |
| HLBS         | High Level Biometric Services |
| IMA          | Immigration Authorities       |
| PAP          | Partial Application Process   |

## <span id="page-27-0"></span> **Bibliography**

<span id="page-27-1"></span>[BIB\_RFC2119] *RFC 2119: Key words for use in RFCs to Indicate Requirement Levels.*
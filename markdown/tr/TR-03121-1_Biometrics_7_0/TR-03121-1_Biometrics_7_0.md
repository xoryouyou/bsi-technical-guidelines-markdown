## BSI Technical Guideline TR-03121-1 Biometrics for Public Sector Applications 

Part 1: Framework 

Version 7.0 

Federal Office for Information Security PO Box 20 03 63 53133 Bonn E-Mail: trbiometrics@bsi.bund.de Internet: https://www.bsi.bund.de © Federal Office for Information Security 2025 

BSI Technical Guideline TR-03121-1 

Federal Office for Information Security 

iii 

Table of Contents 

## Table of Contents 

|1|Changelog ..................................................................................................................................... 1|
|---|---|
|1.1|Changelog Version 7.0-draft1 .................................................................................................. 1|
|1.2|Changelog Version 7.0-draft2 .................................................................................................. 3|
|1.3|Changelog Version 7.0 ............................................................................................................ 5|
|2|Introduction .................................................................................................................................. 9|
|2.1|Motivation and Objectives of Technical Guideline Biometrics .................................................. 9|
|2.2|Target Audience and User ...................................................................................................... 9|
|2.3|Terminology .......................................................................................................................... 9|
|2.4|Business Process Modelling Notation (BPMN) ........................................................................ 10|
|3|Structure of Technical Guideline Biometrics ................................................................................. 11|
|4|How to use this Technical Guideline ............................................................................................. 13|
|5|Logging scheme ........................................................................................................................... 14|
|5.1|Use cases .............................................................................................................................. 14|
|5.2|XML schemas ....................................................................................................................... 14|
|6|Application Profiles ...................................................................................................................... 15|
|7|Organisation of the Function Modules .......................................................................................... 16|
|8|Organisation of the Partial Application Processes .......................................................................... 18|
||List of Abbreviations .................................................................................................................... 19|
||Bibliography ................................................................................................................................ 20|



Federal Office for Information Security 

iv 

List of Figures 

## List of Figures 

2.1. BPMN Symbols used for the Process Modelling ............................................................................. 10 3.1. Class Diagram of the Technical Guidelines .................................................................................... 12 

Federal Office for Information Security 

v 

List of Figures 

Federal Office for Information Security 

vi 

1 Changelog 

## 1 Changelog 

The following tables present the changes introduced to this Technical Guideline since version 6.0. The chan gelog lists the changes grouped per part of this Technical Guideline, and per building block (Application Pro file (AP), Partial Application Process (PAP), Task, Function Module (FM)) or element (section, table, figure): 

- _Added_ for new features 

- _Changed_ for changes in existing functionality 

- _Deprecated_ for soon-to-be removed features 

- _Removed_ for now removed features 

- _Fixed_ for any bug fixes 

- _Security_ in case of vulnerabilities 

## 1.1 Changelog Version 7.0-draft1 

This chapter includes all changes between Version 6.0 and Version 7.0-draft1. 

## 1.1.1 Changelog BSI TR-03121, General 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|Schema|Changed|Replace XMLRecord with BinaryRecord in are5v2_overall_example.xml.|



**Table 1.1** Changelog BSI TR-03121, General 

## 1.1.2 Changelog BSI TR-03121, Part 1 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|-|-|-|



**Table 1.2** Changelog BSI TR-03121, Part 1 

## 1.1.3 Changelog BSI TR-03121, Part 2, Volume HLBS 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|Service Definition "Rolled<br>Fingerprint Acquisition"|Changed|Changed unclear Service UUID to unique UUID|



**Table 1.3** Changelog BSI TR-03121, Part 2 

## 1.1.4 Changelog BSI TR-03121, Part 3 

|**TR Volume**|**Block /**<br>**Section /**<br>**Type**|**Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|---|---|
|GID|FM|REF-FI-<br>GID, LOG-<br>ALL-GID|Changed|Changed "Behördenkennziffer (BHKZ)" to "Behördenkennzahl<br>(BKZ)" to standardise the name.|
|BCL, GID,<br>VIS, ARE,<br>GIS, IMA|FM|AH-FI-DC,<br>AH-FI-<br>DC2|Changed|Added clarification for requirements of facial image cameras. Captu<br>re of full frontal facial image shall be possible and the camera shall<br>allow cropping of captured facial image.|
|BCL, GID,<br>VIS, ARE,<br>GIS, IMA|FM|UI-FP-OP,<br>UI-FI-OP|Changed|Added clarification for the case that no PAD result is available. This<br>information shall be displayed to the operator.|



Federal Office for Information Security 

1 

1 Changelog 

|**TR Volume**|**Block /**<br>**Section /**<br>**Type**|**Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|---|---|
|GID|FM|AS-FI-FBS|Changed|Removed the selection of the scanning mode for images in colour or<br>in grey scale.|
|ARE|AP|Arrival At<br>testation<br>Document|Changed|Replaced PAP ACQ-FI-SV-2 with PAP ACQ-FI-SV-4.|
|ARE|AP|Arrival At<br>testation<br>Document<br>in Special<br>Situations|Changed|Replaced PAP ACQ-FI-SV-2 with PAP ACQ-FI-SV-4.|
|ARE|AP|Arrival At<br>testation<br>Document|Changed|Marked PAP DEL-FI-SV-1 as optional.|
|ARE|AP|Arrival At<br>testation<br>Document<br>in Special<br>Situations|Changed|Marked PAP DEL-FI-SV-1 as optional.|
|ARE|AP|Registra<br>tion with<br>Biometric<br>Identifica<br>tion|Added|Added new Application Profile "Registration with Biometric Identifi<br>cation".|
|ARE|AP|Document<br>Issuing<br>with Bio<br>metric Ve<br>rification|Added|Added new Application Profile "Document Issuing with Biometric<br>Verification".|
|ARE|FM|COD-ALL-<br>ARE|Changed|Removed the alternative option of using BinaryRecord elements.|
|BCL, GID,<br>VIS, ARE,<br>GIS, IMA|FM|LOG-FI-<br>GENERIC,<br>LOG-FP-<br>GENERIC|Changed|Added the special case of canceled acquisition.|
|BCL, ARE,<br>IMA|FM|AS-FP-<br>SLP|Changed|Added the alternative of hardware-based detection.|
|GID|FM|COD-FI-<br>CHIP|Changed|Added footnote to ISO reference BIB_ISO_FACE (transition to<br>BIB_ISO_39794-5).|
|GID|FM|COD-FP-<br>CHIP|Changed|Added footnote to ISO references BIB_ISO_FINGER (transition to<br>BIB_ISO_39794-4).|
|GID|Basics for<br>German<br>Identi<br>ty Docu<br>ments|--|Changed|Added ISO/IEC 39794-4 and ISO/IEC 39794-5.|
|BCL|Volume<br>Border<br>Control|--|Changed|Added ISO/IEC 39794-4 and ISO/IEC 39794-5.|
|ARE|Volume<br>Alien Re<br>gister En<br>rolment|–|Changed|Added chapter for Application Profile combinations.|



Federal Office for Information Security 

2 

1 Changelog 

|**TR Volume**|**Block /**<br>**Section /**<br>**Type**|**Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|---|---|
|ARE|FM|LOG-ALL-<br>ARE|Changed|Added new Application Profiles.|



**Table 1.4** Changelog BSI TR-03121, Part 3 

## 1.2 Changelog Version 7.0-draft2 

This chapter includes all changes between Version 7.0-draft1 and Version 7.0-draft2. 

## 1.2.1 Changelog BSI TR-03121, General 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|Schema|Changed|Add the attribute selected for bio:FaceCapture.|
|Schema|Changed|Add PGM and PNM data type to type.record.type.|
|Schema|Changed|Add result attribute to FingerDelivery and FaceDelivery.|



**Table 1.5** Changelog BSI TR-03121, General 

## 1.2.2 Changelog BSI TR-03121, Part 1 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|-|-|-|



**Table 1.6** Changelog BSI TR-03121, Part 1 

## 1.2.3 Changelog BSI TR-03121, Part 2, Volume HLBS 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|Service Definition "Rolled<br>Fingerprint Acquisition"|Changed|Changed unclear Version value of ServiceInformation to acutal version of the cur<br>rent BSI TR-03121.|
|Service Definition "Facial<br>Image Delivery Acquisiti<br>on"|Changed|Changed unclear Version value of ServiceInformation to acutal version of the cur<br>rent BSI TR-03121.|
|Service Definition "Facial<br>Image Delivery System"|Changed|Configuration Parameter FacialImages: hlbs:Image SHALL contain bio:Origin wit<br>hin xmlParameters; image format according to Application Profile.|
|Service Definition "Facial<br>Image Delivery System"|Changed|User Command Parameter CropManually: added ImageListItem to specify the<br>image to crop.|
|Service Definition "Facial<br>Image Delivery System"|Changed|User Command Parameter RotateManually: added ImageListItem to specify the<br>image to rotate manually.|
|Service Definition "Facial<br>Image Delivery System"|Changed|User Command Parameter AcceptImage: added ImageListItem to specify the image<br>to accept.|
|Service Definition "Facial<br>Image Delivery System"|Changed|User Command Parameter RejectImage: renamed to RejectAllImages.|
|Service Definition "Facial<br>Image Delivery System"|Changed|Feedback Parameter QAFeedback: renamed to QAFeedbackList, changed type to<br>hlbs:StringList.|
|Service Definition "Facial<br>Image Delivery System"|Changed|Feedback Parameter QAEntireFacialImage: renamed to QAEntireFacialImageList,<br>changed type to hlbs:ImageList; image format according to Application Profile.|
|Service Definition "Facial<br>Image Delivery System"|Changed|Feedback Parameter QACroppedFacialImage: renamed to QACroppedFacialImage<br>List, changed type to hlbs:ImageList; image format according to Application Profile.|



Federal Office for Information Security 

3 

1 Changelog 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|Service Definition "Facial<br>Image Delivery System"|Changed|Feedback Parameter QACroppedFacialImageRotation: renamed to QACroppedFaci<br>alImageRotationList, changed type to hlbs:StringList.|
|Service Definition "Facial<br>Image Delivery System"|Changed|Results Parameter FaceAcquisition: renamed to FaceDelivery.|
|Service Definition "Faci<br>al Image Acquisition Sys<br>tem"|Changed|Changed unclear Version value of ServiceInformation to acutal version of the cur<br>rent BSI TR-03121.|
|Service Definition "Basic<br>Facial Image Acquisition<br>System"|Changed|Changed unclear Version value of ServiceInformation to acutal version of the cur<br>rent BSI TR-03121.|
|Service Definition "Fin<br>gerprint Acquisition"|Changed|Changed unclear Version value of ServiceInformation to acutal version of the cur<br>rent BSI TR-03121.|
|Service Definition "Self-<br>Service System"|Changed|Changed unclear Version value of ServiceInformation to acutal version of the cur<br>rent BSI TR-03121 for both Automated Acquisition of Slap Fingerprints and Auto<br>mated Acquisition of Facial Images .|



**Table 1.7** Changelog BSI TR-03121, Part 2 

## 1.2.4 Changelog BSI TR-03121, Part 3 

|**TR Volume**|**Block /**<br>**Section /**<br>**Type**|**Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|---|---|
|GID|FM|LOG-FI-<br>GID|Changed|Restricted the Exif data to printable ASCII characters.|
|GID|FM|AS-FI-<br>DC2, AH-<br>FI-DC2|Changed|Restricted the dispensing with a uniform background.|
|ARE|AP|Document<br>Issuing<br>with Bio<br>metric Ve<br>rificati<br>on, Arrival<br>Attestati<br>on Docu<br>ment, Ar<br>rival At<br>testation<br>Document<br>in Special<br>Situations|Changed|Changed order of printing and logging.|
|ARE|AP|Document<br>Issuing<br>with Bio<br>metric Ve<br>rification,<br>Arrival At<br>testation<br>Document|Changed|Verification is included in PAP Task.|
|GID|AP|Biometric<br>Data<br>Selection|Changed|Added a clarification for the resolution of non-scanned facial<br>images.|
|GID|FM|COD-FI-<br>GID|Changed|Fixed the image resolution to 1244x1600 pixels.|



Federal Office for Information Security 

4 

1 Changelog 

|**TR Volume**|**Block /**<br>**Section /**<br>**Type**|**Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|---|---|
|GID|FM|COD-FI-<br>ROD|Changed|Fixed the image resolution to 1244x1600 pixels.|
|GID|FM|COD-FP-<br>CHIP|Changed|The ICAO-CBEFF container will be omitted in the future.|
|GID|AP|Biometric<br>Data<br>Selection|Changed|Added required FM LOG-ALL-BDS|
|GID|FM|LOG-ALL-<br>GID|Changed|Moved parts to FM LOG-ALL-BDS|
|GID|FM|LOG-ALL-<br>BDS|Added|Created new FM with parts of FM LOG-ALL-GID|
|GID|Basics for<br>German<br>Identi<br>ty Docu<br>ments|-|Changed|Changed ISO references and added footnotes to the ISO/IEC 39794<br>series.|
|BCL|Volume<br>Border<br>Control|-|Changed|Changed ISO references and added footnotes to the ISO/IEC 39794<br>series.|



**Table 1.8** Changelog BSI TR-03121, Part 3 

## 1.3 Changelog Version 7.0 

This chapter includes all changes between Version 7.0-draft2 and Version 7.0. 

## 1.3.1 Changelog BSI TR-03121, General 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|Bibliography|Changed|[BIB_EES_ICD_Annex5] Renamed from [BIB_EES_ICD] as it refers to Annex 5 and updated<br>from Version 0.7.2 to Version 00_07_06_errata2|
|Bibliography|Changed|[BIB_EES_ICD] Updated from Version 0.7.2 to Version 00_07_06_errata2|
|Schema|Changed|_Changes to the XML schema are recorded in the schema changelog (CHANGELOG.md)._<br>However, we would like to highlight a minor change in the XML Schema which has larger<br>impact to the XML-logs to be written: The`copyReasons`attribute of`XMLRecord`and`Bi`<br>`naryRecord`SHALL now be used within the copied record (like the already used`copyRe`<br>`ferences`attribute), instead of being written down to the original record.|
|Schema|Changed|Introduce new schema version 6v1 for all volumes.|



**Table 1.9** Changelog BSI TR-03121, General 

## 1.3.2 Changelog BSI TR-03121, Part 1 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|-|-|-|



**Table 1.10** Changelog BSI TR-03121, Part 1 

Federal Office for Information Security 

5 

1 Changelog 

## 1.3.3 Changelog BSI TR-03121, Part 2, Volume HLBS 

|**Element Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|
|Service Definition "Rolled<br>Fingerprint Acquisition"|Changed|Added "DiscardAll" to possible values of parameter ID "Result" of result elements.|



**Table 1.11** Changelog BSI TR-03121, Part 2 

## 1.3.4 Changelog BSI TR-03121, Part 3 

|**TR Volume**|**Block /**<br>**Section /**<br>**Type**|**Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|---|---|
|ARE|FM|LOG-ALL-<br>ARE|Changed|Listed root elements and sub-elements to log|
|BCL|FM|LOG-ALL-<br>BCL|Changed|Listed root elements and sub-elements to log|
|GID|FM|LOG-ALL-<br>GID|Changed|Listed root elements and sub-elements to log|
|GID|FM|LOG-FI-<br>GID|Changed|Changed MultiModalAcquisition to MultiModalProcess|
|GID|FM|LOG-FP-<br>GID|Changed|Changed MultiModalAcquisition to MultiModalProcess|
|ARE, BCL,<br>GID|FM|LOG-FI-<br>GENERIC|Changed|Changed MultiModalAcquisition to MultiModalProcess|
|ARE, BCL,<br>GID|FM|LOG-FP-<br>GENERIC|Changed|Changed MultiModalAcquisition to MultiModalProcess|
|GID|FM|LOG-ALL-<br>BDS|Changed|Added footnote preview for logging fingerprint data during the ISO<br>transition phase|
|BCL, IMA|FM|COD-FI-<br>EES|Changed|Changed requirements according to new EES ICD version.|
|BCL, IMA|FM|COD-FP-<br>EES|Changed|Changed requirements according to new EES ICD version.|
|BCL|FM|COM-FI-<br>BCL|Changed|Changed requirements according to new EES ICD version.|
|BCL|FM|COM-FP-<br>BCL|Changed|Changed requirements according to new EES ICD version.|
|IMA|FM|COM-FI-<br>IMA|Changed|Changed requirements according to new EES ICD version.|
|IMA|FM|COM-FP-<br>IMA|Changed|Changed requirements according to new EES ICD version.|
|GID|FM|COD-<br>FI-ROD,<br>COD-<br>FI-PRD,<br>COD-FI-<br>GID|Changed|The resulting scanned facial image shall be a color image (24 bit<br>sRGB).|
|ARE,<br>BCL,GID,<br>IMA|FM|AS-FP-MF|Changed|List of requirements with respect to acquisition setting levels.|
|BCL, GID|FM|O-ALL-<br>USV|Changed|Maximum visual angle is set to 50°.|
|GID|FM|PAD-FI-<br>APP1|Changed|In case of a PAD alarm, all facial images within an acquisition shall<br>be forwarded.|



Federal Office for Information Security 

6 

1 Changelog 

|**TR Volume**|**Block /**<br>**Section /**<br>**Type**|**Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|---|---|
|ARE, BCL,<br>GID, IMA|FM|UI-FI-OP|Changed|Changed wording and added requirements in the case of a PAD<br>alarm.|
|BCL, GID|FM|O-ALL-<br>USV|Changed|Added requirements for the product documentation.|
|ARE|AP|Registra<br>tion with<br>Biometric<br>Identifica<br>tion|Changed|Added Function Modules for the case of supervised SSS.|
|GID|FM|AH-FI-<br>SSS2|Changed|Clarified the range of the optical path.|
|ARE|AP|Document<br>Issuing<br>with Bio<br>metric Ve<br>rification|Changed|Updated Process Issuing with Biometric Verification in order to al<br>low re-capture of plain and/or rolled fingerprints. Included FMs ac<br>cordingly.|
|GID|FM|AS-FI-FBS|Changed|Added color requirements.|
|GID|PAP|ACQ-FI-<br>SV-4|Changed|Added clarification about manual capture mode.|
|GID|PAP|ACQ-FI-<br>SV-4|Changed|Added automatic mode with capture after fixed time interval.|
|GID|PAP|ACQ-FI-<br>SV-5|Changed|Added description for manual trigger in automated mode.|
|ARE|AP|Arrival At<br>testation<br>Document<br>(Single<br>Process at<br>Counter)|Changed|Updated Arrival Attestation Document (Single Process at Counter) to<br>allow re-capture of plain and/or rolled fingerprints.|
|GID|PAP|ACQ-FI-<br>AUTO-1|Changed|Excluded background replacement in the overall GID timeout.|
|GID|FM|AS-FI-<br>DC2|Changed|Rephrased requirements regarding (uniform) background.|
|GID|FM|AS-FI-<br>ICS2|Changed|Rephrased requirements regarding (uniform) background.|
|GID|FM|AH-FI-<br>DC2|Changed|Rephrased requirements regarding (uniform) background.|
|GID|FM|COD-FI-<br>PRD|Changed|Added clarification about lossless compression.|
|GID|FM|AH-FI-<br>ICS2|Changed|Rephrased requirements regarding (uniform) background.|
|GID|PAP|ACQ-FI-<br>AUTO-1|Changed|Clarified the timeout start in the figure.|
|ARE|AP|Registra<br>tion with<br>Biometric<br>Identifica<br>tion|Changed|Skip fingerprint acquisition if legal requirements are not given.|



Federal Office for Information Security 

7 

1 Changelog 

|**TR Volume**|**Block /**<br>**Section /**<br>**Type**|**Name**|**Type of**<br>**Change**|**Change Description**|
|---|---|---|---|---|
|ARE|AP|Document<br>Issuing<br>with Bio<br>metric Ve<br>rification|Changed|Skip fingerprint acquisition if legal requirements are not given.|
|ARE|AP|Arrival At<br>testation<br>Document|Changed|Skip fingerprint acquisition if legal requirements are not given.|
|ARE|AP|Arrival At<br>testation<br>Document<br>in Special<br>Situations|Changed|Skip fingerprint acquisition if legal requirements are not given.|
|ARE|AP|Arrival At<br>testtattion<br>Document<br>(Single<br>Process at<br>Counter)|Changed|Receive trigger for total re-acquisition from PAP ACQ-FP10R-SV-1<br>and remove duplicate control verification (as already implemented<br>in PAP Task ACQ-FPR-1).|
|ARE|AP|Document<br>Issuing<br>with Bio<br>metric Ve<br>rification|Changed|Receive trigger for total re-acquisition from PAP ACQ-FP10R-SV-1<br>and remove duplicate control verification (as already implemented<br>in PAP Task ACQ-FPR-1).|
|ARE|PAP|ACQ-<br>FP10R-<br>SV-1|Changed|Implement loop for capture sequence and receive trigger from PAP<br>Task ACQ-FPR-1.|
|ARE|PAP Task|ACQ-<br>FPR-1|Changed|Optimized process for captures with insufficient quality and re-desi<br>gned operator's decision tree for successful and non-successful cap<br>tures.|
|GID|FM|BIP-FI-<br>GID|Changed|Added, that padding SHALL NOT be used.|
|ARE|FM|BIP-FI-<br>DC-HQ|Changed|Added, that padding SHALL NOT be used.|
|GID|FM|O-ALL-<br>USV|Changed|Added description and figure regarding obstruction angles.|



**Table 1.12** Changelog BSI TR-03121, Part 3 

Federal Office for Information Security 

8 

2 Introduction 

## 2 Introduction 

## 2.1 Motivation and Objectives of Technical Guideline Biometrics 

Biometric methods are used in many different areas of applications. The solutions and systems available on the market are able to serve a broad range regarding performance, security, usability and standard confor mance. For public sector applications, it is necessary to define precise requirements and general conditions. Furthermore, the systems have to be defined in a way which allows for extension in future developments. 

The objective of this Technical Guideline (TR Biometrics) is to offer a basis for a consistent and comparable quality of public sector applications and for building a common architecture. 

This guideline has the following objectives: 

- _Modularity:_ The complete guideline is built from several single guideline modules. For a single application area only the respective modules have to be taken into account. This is done in order to avoid side effects between different kinds of applications which would occur due to changes of special functions. 

- _Clarity:_ The concept of this guideline follows a well structured framework. With this framework it is easily understandable which kind of guideline modules are valid for the respective application scenario. 

- _Expandability:_ Modularity is the key component of expandability in the scope of this guideline. This is valid regarding new applications as well as new functional units. 

- _Standard conformance:_ The Technical Guideline takes national and international standards and guidelines into account and deploys them for governmental applications. 

- _Conformance and certification:_ The guideline modules are designed in such a way that requirements and conditions for single functional units are clearly separated from each other. Products for single functional units are clearly defined regarding the interfaces and the range of their functionality so that they can be tested for conformance with this guideline and certified. 

- _Ability to reference:_ The use of functional units allows to specify precise requirements for products that are used in according application scenarios. Therefore, this guideline can be used as a reference e.g. for tenders. 

- _Market orientation:_ The definition of functional units is related to the products that can be found on the market. Requirements of the guideline can be unambiguously assigned to the respective systems and com ponents. 

It should be noted that the content of this guideline is limited to the aspects of biometric characteristics. In terfaces to further technologies (e.g. connection of optical or electronic document readers) are out of scope of this document. 

## 2.2 Target Audience and User 

Audience for this guideline are institutions that are dealing with projects using biometric characteristics in public sector applications. These include: 

- Agencies that are issuing identity documents or visas, e.g. passport agencies of the local authorities or mis sions abroad of the Federal Foreign Office. 

- Public Authorities using biometric applications for identity verification of people, e.g. the German Federal Police (Polizeien des Bundes) or the Police of the Federal States (Polizeien der Länder), the German Customs Administration (Bundeszollverwaltung) or the Federal Administrative Office (Bundesverwaltungsamt). 

Beside these users, this guideline also addresses vendors of biometric systems as well as integrators and app lication developers. 

## 2.3 Terminology 

The key words "MUST", MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this Technical Guideline are to be interpreted as described in [BIB_RFC2119]. 

Federal Office for Information Security 

9 

2 Introduction 

## 2.4 Business Process Modelling Notation (BPMN) 

The processes in this Technical Guideline are modelled using the Business Process Modelling Notation (BPMN). Figure 2.1 gives an overview over the relevant icons herein. 


![](markdown/tr/TR-03121-1_Biometrics_7_0/TR-03121-1_Biometrics_7_0.pdf-0016-03.png)


**----- Start of picture text -----**<br>
Start Manual Opening or ClosingEither-Or-Gateway<br>Operator Task<br>Schedule-Based<br>Start<br>Opening or Closing<br>Parallel Gateway<br>Biometric<br>Event/Message- Subject Task<br>Based Start<br>Opening or Closing<br>End of process  Complex Gateway<br>ow. If other ows (Multiple Exclusive<br>run in parallel in  Options)<br>the same diagram,  Automated Task<br>they continue.<br>Opening or Closing<br>Event Based<br>Intermediate  Gateway (Multiple<br>Exclusive Options<br>process Collapsed<br>triggerd by<br>Process with  messages)<br>Subtasks<br>Terminates whole<br>process ow,<br>Opening or Closing<br>including other<br>Inclusive Gateway<br>ows still running<br>(Or-Gateway where<br>in parallel in this<br>one or more paths<br>diagram.<br>are chosen)<br>Process jumps to a<br>compensate step.<br>Database or Cache<br>Error occured<br>during task.<br>Process ends with<br>error.<br>Ad hoc Process<br>(Expanded process, gathering all kind of subtasks which might be<br>called within this process in no specic order)<br>Process ends with a<br>message.<br>**----- End of picture text -----**<br>


**Figure 2.1.** BPMN Symbols used for the Process Modelling 

Federal Office for Information Security 

10 

3 Structure of Technical Guideline Biometrics 

## 3 Structure of Technical Guideline Biometrics 

This Technical Guideline consists of the following parts: 

- Part 1: Framework (TR-03121-1) 

TR-03121-1 is the framework document of the guideline. It explains the concept and the relation between the different parts. 

- Part 2: Software Architecture (TR-03121-2) 

The High Level Biometric Services (HLBS) as well as Service Definitions for specific use cases are specified here. 

- Part 3: Application Profiles, Function Modules and Processes (TR-03121-3) 

   - In the third part, the different Application Profiles with corresponding Partial Application Processes and Function Modules are defined. These contain the detailed technical requirements for each of the com ponents. 

      - Application Profiles may reference Function Modules, Partial Application Processes and Service De finitions (refer to Part 2). 

      - Partial Application Processes may refer to Function Module Categories and may be comprised of _Tasks_ Tasks are processes which are part of more than one Partial Application Process. 

   - For practical purposes, this part is split up in different volumes to serve different user groups. 

      - Border Control (BCL) 

      - German Identity Documents (GID) 

      - Alien Register Enrolment (ARE) 

      - Immigration Authorities (IMA) 

Please refer to Figure 3.1 for a class diagram of the structure described above. 

Federal Office for Information Security 

11 

3 Structure of Technical Guideline Biometrics 


![](markdown/tr/TR-03121-1_Biometrics_7_0/TR-03121-1_Biometrics_7_0.pdf-0018-01.png)


**----- Start of picture text -----**<br>
TRBiom etrics<br>BSI TR-03121<br>composed of<br>«abstract»<br>P a rts<br>specialises specialises specialises<br>P a rt1 P a rt2 P a rt3<br>describes describes<br>Volumes within Part3<br>Volumes_Part2 «abstract» Volumes_Part3 «abstract» Volumes within Part2 ---- Volume 1: BCLVolume 2: GID ----<br>Volume 2: HLBS<br>Volume 4: ARE<br>Volume 6: IMA<br>describes describes<br>ServiceDenition Test Cases in ApplicationProle<br>BSI TR-03122 Part 2 u s e s<br>im plem ents u s e s im plem ents<br>SpecicInterface PartialApplicationProcesses Test Cases in RealWorldApplication<br>u s e s BSI TR-03122 Part 3<br>contains u s e s<br>PAP_Tasks<br>u s e s<br>u s e s<br>FunctionModules Test Cases in<br>BSI TR-03122 Part 3<br>**----- End of picture text -----**<br>


**Figure 3.1.** Class Diagram of the Technical Guidelines 

Additionally, the Technical Guideline BSI-TR 03122 "Conformance Test Specification for Technical Guideline TR-03121 Biometrics for Public Sector Applications" describes the requirements that are essential to declare conformance or to declare the absence of conformance. It consists of the following parts: 

- Part 1: Framework (TR-03122-1) 

- Part 3: Test Cases for Function Modules and Processes (TR-03122-3) 

Federal Office for Information Security 

12 

4 How to use this Technical Guideline 

## 4 How to use this Technical Guideline 

This chapter gives a short overview how to read and apply this guideline step by step. 

1. The user chooses the desired Application Profile. With the help of the Application Profile the user can get a deeper insight into the application, the required software architecture components and the described functionality. TR-03121-2 offers further information about the software architecture component model. 

2. Based on the Application Profile, the mandatory Partial Application Processes and Function Modules are identified. One profile can link to several Partial Application Processes and Function Modules due to dif ferent kinds of underlying biometric characteristics or the fact that different technologies (e.g. scanners or digital cameras for the digitisation of a photo) are used. 

Function Modules are referenced by an explicit identifier, e.g. AH-FP-GID. The first part identifies the requirement type (e.g. Hardware), the second part represents the biometric characteristic (e.g. fingerprint), and the last part denotes a further descriptor, typically the scope (e.g. German Identity Document). 

Function Modules for different biometric characteristics are divided by a comma while a choice between different technologies is denoted by a slash (e.g. AH-FP-FTR, AH-PH-FBS/AH-PH-DC). 

If a Function Module is denoted with a placeholder between a less-than and greater-than sign (< >) the actual referenced Function Module is dependant on the context in which the Function Module has been mentioned. For example the Function Module AH-FI-<VL> has been mentioned within a Partial Applica tion Process used in the BCL volume, then the actual referenced Function Module is AH-FI-BCL. The sa me procedure holds for Application Profiles denoted as <AP> analogously. If no specific Function Module applies, then there are no further requirements defined for this context. 

Partial Application Processes are referenced by an explicit identifier, refer to Partial Application Profile section. 

3. On the basis of the identifier the according Function Module and Partial Application Processes can be ex amined. Every Function Module and Partial Application Process provides detailed technical requirements and recommendations. Note, each reference to a Function Module or Partial Application Processes is a link within the document. 

Federal Office for Information Security 

13 

5 Logging scheme 

## 5 Logging scheme 

## 5.1 Use cases 

This chapter specifies a logging scheme, which allows to document all technical activities performed. The schema files contain additional and mandatory information on technical requirements. Such a logging sche me SHALL be used to measure the quality of the biometric processes across different systems, regardless of the used hard- or software. This enables the possibility of an operational monitoring for technical as well as functional processes and evaluations. 

## 5.2 XML schemas 

The logging scheme is based on a transactional logging format which collects performance and evaluation results from the different application domains. The schema file `trbio6v1.xsd` imports all other schema files and as such the main file used for validation. 

A separate XML schema definition exists for each volume of TR-03121-3, which SHALL be used within the respective application area. Table 5.1 gives an overview of the different XML schema files. 

|**Application domain**|**Schemafile**|**Namespace**|
|---|---|---|
|Alien register enrolment|are6v1.xsd|http://trbio.bsi.bund.de/are/6|
|Border control log|bcl6v1.xsd|http://trbio.bsi.bund.de/bcl/6|
|Type definitions|biotypes6v1.xsd|http://trbio.bsi.bund.de/base/6|
|German identity documents|gid6v1.xsd|http://trbio.bsi.bund.de/gid/6|
|High level biometric services|hlbs6v1.xsd|http://trbio.bsi.bund.de/hlbs/6|
|Immigration authorities|ima6v1.xsd|http://trbio.bsi.bund.de/ima/6|
|Conformance test specification|biocts6v1.xsd|http://trbio.bsi.bund.de/biocts/6|



**Table 5.1** Overview XML schema files 

Federal Office for Information Security 

14 

6 Application Profiles 

## 6 Application Profiles 

Different areas in which this guideline can be used are defined in separate Application Profiles. Application Profiles can have mandatory status, e.g. through published regulations and laws or by requirements given in tenders. Besides, such Application Profiles can also be considered as Best Practices. Thus, the certification process SHALL use one or more seperate Application Profiles. 

An Application Profile is described with the following items: 

- Introduction (legal requirements) 

- Process overview 

   - Target audience 

   - Users 

- Relevant standards and conditions 

- List of 

   - required Function Modules 

   - required Partial Application Processes 

Federal Office for Information Security 

15 

7 Organisation of the Function Modules 

## 7 Organisation of the Function Modules 

Specific technical requirements are structured in Function Modules. They contain detailed technical require ments for the respective component. Function Modules are aligned to the products on the market and to the targets of evaluation. Every Function Module is built of one or more subclauses which are assigned to unique identifiers. Within the subclauses requirements and recommendations are specified in detail. 

Function Modules are referenced by their ID, which can contain up to three information items pointing to its contents. The basic structure of an ID is: "FM AAA-BBB-CCC". 

Here, _AAA_ is the primary information item, pointing to the main contents. _BBB_ and _CCC_ are optional infor mation items, which can further specify the Function Module. These information items may be two to seven alphanumeric digits. Table 7.1 gives an overview of the different primary information items used for Func tion Module categories. Table 7.2 gives an overview of the different optional information items _BBB_ used for Function Module categories. 

|**Primary Information Item**|**Function Module Category**|**Description**|
|---|---|---|
|AH|Acquisition Hardware|Devices that are used for digitising phy<br>sical representable biometric characte<br>ristics are called Acquisition Hardware.<br>Scanners for capturing photographs, di<br>gital cameras to capture facial images,<br>fingerprint sensors, or signature tablets<br>can be named as examples.|
|AS|Acquisition Software|Acquisition Software encapsulates all<br>functionality regarding image proces<br>sing except for biometric purposes. The<br>refore, this module usually contains de<br>vice driver software for the Acquisiti<br>on Hardware or in general software that<br>is very close to the physical hardware.<br>Furthermore, colour management and<br>image enhancement mechanisms are<br>often part of this software layer.|
|BIP|Biometric Image Processing|The module Biometric Image Proces<br>sing provides the extraction of all rele<br>vant biometric information from the<br>data, which is provided by the Acquisi<br>tion Hardware or the Acquisition Soft<br>ware layer. Thus, a proprietary data<br>block is transformed to a digital image<br>of a biometric characteristic. In gene<br>ral, specific image processing for bio<br>metric characteristics is addressed he<br>re e.g. provision of full frontal images or<br>segmentation of fingerprints.|
|CMP|Biometric Comparison|The module Biometric Comparison en<br>closes the mechanisms and algorithms<br>to verify or identify an identity based on<br>a one-to-one or one-to-many biometric<br>comparison between reference data and<br>a current biometric sample (usually a<br>live presented image) no matter where<br>the reference is stored.|
|COD|Coding|This module contains the procedures to<br>code logging data as well as biometric<br>data in defined formats. Interoperability<br>is provided by means of standard comp<br>liant coding.|



Federal Office for Information Security 

16 

7 Organisation of the Function Modules 

|**Primary Information Item**|**Function Module Category**|**Description**|
|---|---|---|
|COM|Compression|The objective of the module Compres<br>sion is to keep the biometric data be<br>low a feasible size without losing too<br>much quality for biometric verification<br>or identification.|
|EVA|Evaluation|Methods and interfaces which are used<br>in the scope of evaluation are the con<br>tent of this module.|
|LOG|Logging|The module Logging contains require<br>ments how and in which modality data<br>has to be logged.|
|O|Operation|Within the module Operation, the<br>working process is specified for the re<br>spective operator.|
|PAD|Presentation Attack Detection|The Presentation Attack Detection mo<br>dules give requirements on fake detec<br>tion. This encloses, among other things,<br>functionality and certification require<br>ments.|
|QA|Quality Assessment|This module contains all kinds of me<br>chanisms and procedures to check the<br>quality of the biometric data or to select<br>the best quality data out of multiple in<br>stances. Quality Assessment is typical<br>ly used in evaluation of an application's<br>performance over time.|
|REF|Reference Storage|The objective of this module is to store<br>biometric data in a way that it can be<br>used for reference purposes later on.|
|UI|User Interface|The User Interface modules give requi<br>rements on visualization and user in<br>teraction. This encloses, among other<br>things, functionality, quality assurance<br>information, and veto messages.|



**Table 7.1** Overview FM Categories Primary Information Items 

|**Optional Information Item**|**Function Module Category**|
|---|---|
|ALL|Overall|
|CCTV|Closed Circuit Television (Surveillance Camera)|
|FI|Facial Image|
|FP|Fingerprint|



**Table 7.2** Overview FM Categories Optional Information Items 

Federal Office for Information Security 

17 

8 Organisation of the Partial Application Processes 

## 8 Organisation of the Partial Application Processes 

Partial Application Processes are referenced by their ID, which can contain up to three information items pointing to its contents. The basic structure of an ID is: "PAP (Task) AAA-BBB-CCC-#". 

Here, "Task" is optional and is only used if the _PAP_ is a task. _AAA_ is the primary information item, pointing to the main contents. _BBB_ and _CCC_ are optional information items, which can further specify the PAP. These information items may be one to six alphanumeric digits. The abbreviations used for the PAP IDs are listed in Table 8.1 and Table 8.2. All PAP IDs end with a number _#_ . This number is usually 1, unless multiple IDs with similar preceding information items exist. In this case, they are enumerated increasingly. 

|**Primary Information Item**|**Description**|
|---|---|
|ACQ|Acquisition|
|ASS|Assessment|
|DEL|Delivery|
|EVA|Evaluation|
|ID|Identification|
|UPD|Update|
|VER|Verification|



**Table 8.1** Overview PAP ID Primary Information Items 

|**Optional Information Item**|**Description**|
|---|---|
|ALL|Overall|
|AUTO|Automated|
|B|Biometrics (fingerprints and facial images)|
|EES|Entry-Exit-System|
|FI|Facial Image|
|FP10R|Fingerprint 10 Finger Rolled|
|FP2P|2 Plain Fingerprints|
|FP4141|Fingerprint 4-1-4-1|
|FP442|Fingerprint 4-4-2|
|FPS|Single Slap Fingerprint Image|
|ID|Identification|
|nCIR|no Connected Identity Register|
|SV|Supervised|
|USV|Unsupervised|
|VER|Verification|
|wCIR|with Connected Identity Register|



**Table 8.2** Overview PAP ID Optional Information Items 

Federal Office for Information Security 

18 

List of Abbreviations 

## List of Abbreviations 

|**Abbreviation**|**Description**|
|---|---|
|AP|Application Profile|
|ARE|Alien Register Enrolment|
|BCL|Border Control|
|FM|Function Module|
|GID|German Identity Documents|
|HLBS|High Level Biometric Services|
|IMA|Immigration Authorities|
|PAP|Partial Application Process|



Federal Office for Information Security 

19 

Bibliography 

## Bibliography 

[BIB_RFC2119] _RFC 2119: Key words for use in RFCs to Indicate Requirement Levels._ 

Federal Office for Information Security 

20 


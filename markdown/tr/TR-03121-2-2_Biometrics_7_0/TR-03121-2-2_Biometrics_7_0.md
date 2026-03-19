BSI Technical Guideline TR-03121-2 

## Biometrics for Public Sector Applications 

Part 2: Software Architecture 

Volume 2: High Level Biometric Services (HLBS) 

Version 7.0 

Federal Office for Information Security PO Box 20 03 63 53133 Bonn E-Mail: trbiometrics@bsi.bund.de Internet: https://bsi.bund.de © Federal Office for Information Security 2025 

BSI Technical Guideline TR-03121-2 

Federal Office for Information Security 

iii 

Table of Contents 

## Table of Contents 

|1|Volume High Level Biometric Services ........................................................................................... 1|
|---|---|
|2|Architecture for Biometric Applications .......................................................................................... 2|
|2.1|Client-Server Architecture ...................................................................................................... 2|
|3|Document Overview ...................................................................................................................... 3|
|3.1|Terminology .......................................................................................................................... 3|
|3.2|Naming Conventions .............................................................................................................. 3|
|3.3|Namespaces ........................................................................................................................... 3|
|3.4|XML Schema and Web Service Definition ................................................................................ 4|
|3.5|Interoperability ...................................................................................................................... 4|
|4|Interface Overview ........................................................................................................................ 5|
|4.1|High-Level Biometric Services ................................................................................................ 5|
|4.2|Error Handling ....................................................................................................................... 5|
|5|High Level Biometric Services API .................................................................................................. 6|
|5.1|Namespaces ........................................................................................................................... 6|
|5.2|Data Types ............................................................................................................................. 6|
|5.3|Fault Types .......................................................................................................................... 21|
|5.4|Operations ........................................................................................................................... 25|
|5.5|Service-Device Description Schema ....................................................................................... 33|
|6|Example (Non-Normative) ............................................................................................................ 58|
|6.1|Service-Device Description ................................................................................................... 58|
|7|Client-Server Connection Scenarios .............................................................................................. 60|
|7.1|Connection via TCP/IP ......................................................................................................... 60|
|7.2|Connection via USB .............................................................................................................. 61|
|8|Service Definitions ....................................................................................................................... 63|
|8.1|Service Definition Facial Image Acquisition System ............................................................... 63|
|8.2|Service Definition Basic Facial Image Acquisition System ....................................................... 69|
|8.3|Service Definition Facial Image Delivery System .................................................................... 74|
|8.4|Service Definition Fingerprint Acquisition ............................................................................. 78|
|8.5|Service Definition Rolled Fingerprint Acquisition .................................................................. 82|
|8.6|Service Definition for Self-Service System ............................................................................. 87|
||List of Abbreviations .................................................................................................................... 94|
||Bibliography ................................................................................................................................ 95|



Federal Office for Information Security 

iv 

List of Figures 

## List of Figures 

2.1. Client-Side Process ........................................................................................................................ 2 7.1. HLBS Architecture ....................................................................................................................... 60 7.2. Architecture via TCP/IP ............................................................................................................... 61 7.3. Architecture via USB .................................................................................................................... 62 

Federal Office for Information Security 

v 

List of Figures 

Federal Office for Information Security 

vi 

1 Volume High Level Biometric Services 

## 1 Volume High Level Biometric Services 

This Technical Guideline specifies a web service called High Level Biometric Services (HLBS) that provides a high level interface for executing and visualising biometric services. 

The BSI TR-03121-3 defines workflows for some standard scenarios in public sector applications. Due to limi tations of Biometric Application Programming Interface (BioAPI) 2.0, the graphical user interfaces (GUIs) for these workflows are usually implemented directly in the Biometric Service Providers (BSPs), which make a seamless integration into the application impossible. BioAPI 2.1 introduces so called BioGUI callbacks, which allow the transfer of process information (e.g. live images, process states, …) but implementing these callbacks in the application proved to be very tedious. 

The goal of this document is to provide a high-level webservice interface that reduces the programming effort to integrate the visualisation of status information and the interaction with biometric workflows into appli cations. The interface is explicitly designed to be independent of the BioAPI standard in terms of terminology and functionality so that webservice implementations are not bound to the BioAPI standard. 

Federal Office for Information Security 

1 

2 Architecture for Biometric Applications 

## 2 Architecture for Biometric Applications 

## 2.1 Client-Server Architecture 

To separate responsibilities and increase flexibility, a client-server approach is introduced in this Technical Guideline. While the server side is responsible for implementing the specific biometric workflow and the com munication with biometric devices, the client side is responsible for displaying the workflow feedback and providing possibilities for the user to interact with the service. The client does not need to care about the exact process behind a service, so that there is a clear separation between user interface and workflow. This allows a very flexible and seamless integration of the same biometric process into different applications. 

In this Technical Guideline the term "biometric service" refers to the general process to accomplish a certain biometric task. For example one such process for fingerprint enrolment could be to capture the fingerprints, do quality computations and repeat the capturing up to three times if the quality components are not met. It is important to note that these processes can greatly be influenced by the available biometric devices. If a 4-finger scanner is available, the process to capture the fingerprints would be a standard 4-4-2 approach. If only a 1-finger scanner is available each finger has to be captured separately. So, although the general process stays the same, details can change depending on the used device. This is why in the following we need to select service-device-combinations instead of only selecting services. Of course, it is possible though that some services do not need devices at all (e.g. a simple face image comparison service), so the device-selection might be optional for some services. 

The server provides a list of service-device-descriptions out of which the client can choose the one that is most appropriate for him. Each description is detailed enough to provide enough information for the application programmer in order to design it's user interface without knowing the exact logic behind the process. The description is standardized through an XML schema so that the application can even analyse the description to automatically adjust the user interface. 

Each service allows interaction with so called user commands. In the feedback loop the service provides in formation about which user commands are allowed to be signalled at the moment and which are not. The application can reflect that by enabling/disabling the corresponding buttons for example. 

After the service execution has finished, one or more results can be retrieved from the service. The service description lists all generated results so that the application knows beforehand which results can be expected. 


![](markdown/tr/TR-03121-2-2_Biometrics_7_0/TR-03121-2-2_Biometrics_7_0.pdf-0008-08.png)


**----- Start of picture text -----**<br>
No<br>Acquire service-device  Congure service Start service execution feedback elementFetch one  Update user interface Yes Fetch results Release service-device<br>combination combination<br>Start End<br>Finished?<br>Signal user<br>command to<br>server<br>Button pressed<br>**----- End of picture text -----**<br>


**Figure 2.1.** Client-Side Process 

Figure 2.1 visualises the service execution process from the client side. After a service-device-combination is reserved for use, it can be configured and started. The client processes the service feedback in a loop and updates the user interface accordingly. If a user command should be signalled (e.g. because the user clicked a button), the client sends an appropriate message to the server. After the service execution has finished, the client fetches the results and releases the acquired service-device-combination. 

Federal Office for Information Security 

2 

3 Document Overview 

## 3 Document Overview 

## 3.1 Terminology 

The key words "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BIB_RFC2119]. 

## 3.2 Naming Conventions 

## 3.2.1 Multiplicity 

Generally, XML elements and attributes listed in this document are required, i.e. the respective parent element SHALL contain exactly one such element. Elements and attributes that deviate from this baseline are denoted in this document by a symbol which is appended to the element/attribute name. The symbols are listed in Table 3.1. 

|**Appended Sym**<br>**bol**|**Meaning**|
|---|---|
|?|Zero or one|
|*|Zero or more|
|+|One or more|



**Table 3.1** Multiplicity Symbols 

## 3.2.2 SOAP Interfaces 

All operations of this interface follow the request/response model, i.e., communication is initiated by the client by sending a Simple Object Access Protocol (SOAP) message to the server (request). For each request, the server replies with a SOAP message containing the result of the requested operation (response) or, in case of error, a fault. 

The body of each SOAP message consists of a single part which is named according to the corresponding operation. For requests, the part name is identical to the name of the operation. For responses, the part name is identical to the name of the operation plus the suffix "Response" (see Table 3.2). 

|**Message Type**|**Part Name**|
|---|---|
|Request|<operation_name>|
|Response|<operation_name>Response|



**Table 3.2** Naming Conventions for SOAP Messages 

## _Example: Naming Convention_ 

- Operation: `getAllServices` 

- Request: `getAllServices` 

- Response: `getAllServicesResponse` 

Both request and response elements exclusively contain zero or more child elements according to the detailed description in this guideline. They do not carry any attributes. 

## 3.3 Namespaces 

|**Prefix**|**Description**|**URI**|
|---|---|---|
|`hlbs`|HLBS|http://trbio.bsi.bund.de/hlbs/1|
|`xsd`|XML Schema|http://www.w3.org/2001/XMLSchema|



**Table 3.3** Namespaces 

Federal Office for Information Security 

3 

3 Document Overview 

## 3.4 XML Schema and Web Service Definition 

The following XML Schema Definition ( `.xsd` ) and Web Service Definition ( `.wsdl` ) files are provided with this Technical Guideline in the current version 1v1: 

|**File**|**Description**|
|---|---|
|`HLBS1v1.wsdl`|HLBS web service definition (<br>Chapter 5)|
|`hlbs_service1v1.xsd`|XML Schema Definition for service descriptions (<br>Section 5.5)|



**Table 3.4** XML Schema and Web Service Definition 

Both files can be found in TR-03121 XML Schema. 

## 3.5 Interoperability 

To ensure trouble-free interoperability between different SOAP implementations, both client and server im plementations SHOULD fulfil the WS-I Basic Profile 1.1. 

Federal Office for Information Security 

4 

4 Interface Overview 

## 4 Interface Overview 

## 4.1 High-Level Biometric Services 

## 4.1.1 Objective 

The HLBS interface provides execution and feedback delivery of biometric services. 

## 4.1.2 Service and Device Management 

- The function `getAllServices` provides a list of all biometric services that are available on the server. For each biometric service there is a list of available devices provided. 

- The function `getServiceDescription` provides an XML description of a service-device-combination descri bing the supported configuration, feedback elements, user commands and results. The XML schema is de scribed in Section 5.5. 

## 4.1.3 Service Execution 

- The function `acquireService` reserves a service-device-combination for use. The function returns a session handle which SHALL be used by the client in subsequent calls. The client MAY provide his own session id to the function. 

- The service-device-combination MAY be configured by calling `configureService` . 

- The function `beginServiceExecution` starts the service execution and returns the initial feedback which SHOULD be used by the client to initialize the GUI. 

- The client SHOULD inform the server that client-side processing has finished by calling `endServiceExe cution` . 

- The client SHALL release the service-device-combination by calling `releaseService` . 

## 4.1.4 Service Execution Feedback and Results 

- The function `getServiceFeedback` provides the next available feedback elements 

- The client MAY signal user commands by calling the function `signalUserCommand` . 

- The function `getResults` returns the final results generated by the service execution. It SHALL be called after the service execution has been finished or cancelled. 

## 4.2 Error Handling 

If errors occur during processing of a web service request, a SOAP fault is generated according to the SOAP 1.1 specification. SOAP faults are comparable to exceptions in programming languages such as C++, C# or Java insofar as they allow reporting of errors without the need to account for error codes in function signatures. 

SOAP faults are returned in place of the SOAP response. Depending on the type of an error, the fault message MAY contain additional information about the error. The faults that are specific to the web services in this document are specified in the respective chapters and listed with every function that MAY generate them. Faults originating from other causes such as network connection problems or validation errors are beyond the scope of this document as they depend on the specific SOAP implementation. 

Federal Office for Information Security 

5 

5 High Level Biometric Services API 

## 5 High Level Biometric Services API 

The HLBS Application Programming Interface (API) contains functions to execute and visualize biometric services. The client defines the User Interface (UI) layout and updates it with the feedback it gets from the server. The server implements the process/workflow and continuously delivers feedback about the process state to the client. User interaction is supported by signalling user commands to the server. 

The definitions of the HLBS API are provided in `HLBS1v1.wsdl` . The schema for the service-device description is provided in `hlbs_service1v1.xsd` . 

A complete example can be found in Section 6.1. 

## 5.1 Namespaces 

The elements of the server- and client-side APIs and the service-device descriptions are members of the na mespace http://trbio.bsi.bund.de/hlbs/1, which is aliased by `hlbs` . 

## 5.2 Data Types 

In addition to simple XSD types, the SOAP interface uses custom data types, which are described in the fol lowing. 

## 5.2.1 ServiceType 

Represents the type of task a biometric service provides. Each service is bound to exactly one service type. Derived from `xsd:string` . 

## 5.2.1.1 Values 

|**Value**|**Description**|
|---|---|
|`enrolment`|The service is used for enrolment.|
|`verification`|The service is used for verification.|
|`identification`|The service is used for identification.|
|`comparison`|The service is used for comparison of two biometric templates.|
|`other`|The service is used for another purpose.|



**Table 5.1** ServiceType Values 

## 5.2.1.2 WSDL Definition 

```
<simpleTypename="ServiceType">
<restrictionbase="xsd:string">
<enumerationvalue="enrolment"/>
<enumerationvalue="verification"/>
<enumerationvalue="identification"/>
<enumerationvalue="comparison"/>
<enumerationvalue="other"/>
</restriction>
</simpleType>
```

## 5.2.2 BiometricType 

Represents the type of a biometric modality. Derived from `xsd:string` . 

## 5.2.2.1 Values 

|**Value**|**Description**|
|---|---|
|`finger`|Fingerprint|
|`face`|Face|



Federal Office for Information Security 

6 

5 High Level Biometric Services API 

|**Value**|**Description**|
|---|---|
|`iris`|Iris|
|`vein`|Vein|
|`signature`|Signature|
|`gait`|Gait|
|`retina`|Retina Scan|
|`hand-geom`|Geometry of hand|
|`voice`|Voice|
|`palm`|Palm|
|`other`|Other modality|



**Table 5.2** BiometricType Values 

## 5.2.2.2 WSDL Definition 

```
<simpleTypename="BiometricType">
<restrictionbase="xsd:string">
<enumerationvalue="finger"/>
<enumerationvalue="face"/>
<enumerationvalue="iris"/>
<enumerationvalue="vein"/>
<enumerationvalue="signature"/>
<enumerationvalue="gait"/>
<enumerationvalue="retina"/>
<enumerationvalue="hand-geom"/>
<enumerationvalue="voice"/>
<enumerationvalue="palm"/>
<enumerationvalue="other"/>
</restriction>
</simpleType>
```

## 5.2.3 FeedbackStatus 

Represents the type of the service execution status. Derived from `xsd:string` . 

## 5.2.3.1 Values 

|**Value**|**Description**|
|---|---|
|`not-started`|The service has not been started yet.|
|`running`|The service is running.|
|`waiting-for-input`|The service is waiting for user input to decide how to continue.|
|`finished`|The service has finished.|
|`cancelled`|The service was cancelled.|



**Table 5.3** FeedbackStatus Values 

## 5.2.3.2 WSDL Definition 

```
<simpleTypename="FeedbackStatus">
<restrictionbase="xsd:string">
<enumerationvalue="not-started"/>
<enumerationvalue="running"/>
<enumerationvalue="waiting-for-input"/>
<enumerationvalue="finished"/>
<enumerationvalue="cancelled"/>
</restriction>
</simpleType>
```

Federal Office for Information Security 

7 

5 High Level Biometric Services API 

## 5.2.4 UserCommandStatus 

Specifies whether a user command is allowed to be signalled at the moment or not. User interfaces SHOULD disable/enable the buttons bound to the corresponding user commands based on this status. Derived from `xsd:string` . 

## 5.2.4.1 Values 

|**Value**|**Description**|
|---|---|
|`allowed`|The user command is allowed to be fired.|
|`not-allowed`|The user command is not allowed to be fired.|



**Table 5.4** UserCommandStatus Values 

## 5.2.4.2 WSDL Definition 

```
<simpleTypename="UserCommandStatus">
<restrictionbase="xsd:string">
<enumerationvalue="allowed"/>
<enumerationvalue="not-allowed"/>
</restriction>
</simpleType>
```

## 5.2.5 Iso19794FingerImpression 

Represents the impression type as specified in [BIB_ISO_19794_FINGER] (e.g. finger or palm). Derived from `xsd:unsignedInt` . 

## 5.2.5.1 Format Restrictions 

The impression type according to [BIB_ISO_19794_FINGER] (e.g. finger or palm) is specified as an unsigned integer where the following values are allowed: 

|**Impression Code**|**Description**|
|---|---|
|`0`|Live-scan plain|
|`1`|Live-scan rolled|
|`2`|Nonlive-scan plain|
|`3`|Nonlive-scan rolled|
|`4`|Latent impression|
|`5`|Latent tracing|
|`6`|Latent photo|
|`7`|Latent lift|
|`8`|Live-scan swipe|
|`9`|Live-scan vertical roll|
|`10`|Live-scan palm|
|`11`|Nonlive-scan palm|
|`12`|Latent palm impression|
|`13`|Latent palm tracing|
|`14`|Latent palm photo|
|`15`|Latent palm lift|
|`20`|Reserved for future use|
|`21`|Reserved for future use|
|`22`|Reserved for future use|



Federal Office for Information Security 

8 

5 High Level Biometric Services API 

|**Impression Code**|**Description**|
|---|---|
|`23`|Reserved for future use|
|`24`|Live-scan optical contactless plain|
|`25`|Reserved for future use|
|`26`|Reserved for future use|
|`27`|Reserved for future use|
|`28`|Other|
|`29`|Unknown|



**Table 5.5** Iso19794FingerImpression Format Restrictions 

## 5.2.5.2 WSDL Definition 

```
<simpleTypename="Iso19794FingerImpression">
<restrictionbase="xsd:unsignedInt">
<patternvalue="[0-9]|1[0-5]|2[0-9]"/>
</restriction>
</simpleType>
```

## 5.2.6 Iso19794FingerCode 

A code as defined in [BIB_ISO_19794_FINGER] (e.g. finger or palm). Derived from `xsd:unsignedInt` . 

## 5.2.6.1 Format Restrictions 

The code is specified as an unsigned integer where the following values are allowed according to [BIB_ISO_19794_FINGER]: 

|**Finger Code**|**Finger/Palm Position**|
|---|---|
|`0`|Unknown|
|`1`|Right thumb|
|`2`|Right index finger|
|`3`|Right middle finger|
|`4`|Right ring finger|
|`5`|Right little finger|
|`6`|Left thumb|
|`7`|Left index finger|
|`8`|Left middle finger|
|`9`|Left ring finger|
|`10`|Left little finger|
|`13`|Plain right four fingers|
|`14`|Plain left four fingers|
|`15`|Plain thumbs (2)|
|`20`|Unknown palm|
|`21`|Right full palm|
|`22`|Right writer's palm|
|`23`|Left full palm|
|`24`|Left writer's palm|
|`25`|Right lower palm|



Federal Office for Information Security 

9 

5 High Level Biometric Services API 

|**Finger Code**|**Finger/Palm Position**|
|---|---|
|`26`|Right upper palm|
|`27`|Left lower palm|
|`28`|Left upper palm|
|`29`|Right other|
|`30`|Left other|
|`31`|Right interdigital|
|`32`|Right thenar|
|`33`|Right hypothenar|
|`34`|Left interdigital|
|`35`|Left hemar|
|`36`|Left hypothenar|
|`40`|Right index and middle|
|`41`|Right middle and ring|
|`42`|Right ring and little|
|`43`|Left index and middle|
|`44`|Left middle and ring|
|`45`|Left ring and little|
|`46`|Right index and left index|
|`47`|Right index and middle and ring|
|`48`|Right middle and ring and little|
|`49`|Left index and middle and ring|
|`50`|Left middle and ring and little|



**Table 5.6** Iso19794FingerCode Format Restrictions 

## 5.2.6.2 WSDL Definition 

```
<simpleTypename="Iso19794FingerCode">
<restrictionbase="xsd:unsignedInt">
<patternvalue="[0-9]|10|1[3-5]|2[0-9]|3[0-6]|4[0-9]|50"/>
</restriction>
</simpleType>
```

## 5.2.7 Iso19794FaceImageCode 

Represents a face image code in the format specified in [BIB_ISO_19794_FACE]. Derived from `xsd:unsignedInt` . 

## 5.2.7.1 Format Restrictions 

The face code is specified as an unsigned integer between 0 and 255 with the following meanings: 

|**Face Image Code**|**Description**|
|---|---|
|`0`|Basic face image|
|`1`|Full frontal image|
|`2`|Token frontal image|
|`3`|Post-processed frontal image|
|`4-127`|Reserved by SC 37 for future use|
|`128`|Basic 3D face image|



Federal Office for Information Security 

10 

5 High Level Biometric Services API 

|**Face Image Code**|**Description**|
|---|---|
|`129`|Full frontal 3D face image|
|`130`|Token frontal 3D face image|
|`131-255`|Reserved by SC 37 for future use|



**Table 5.7** Iso19794FaceImageCode Format Restrictions 

## 5.2.7.2 WSDL Definition 

```
<simpleTypename="Iso19794FaceImageCode">
<restrictionbase="xsd:unsignedInt">
<minInclusivevalue="0"/>
<maxInclusivevalue="255"/>
</restriction>
</simpleType>
```

## 5.2.8 Iso19794IrisImageCode 

Represents an iris code in the format specified in [BIB_ISO_IRIS]. Derived from `xsd:unsignedInt` . 

## 5.2.8.1 Format Restrictions 

The iris code is specified as an unsigned integer between 0 and 2 with the following meanings: 

|**Iris Image Code**|**Description**|
|---|---|
|`0`|Unknown|
|`1`|Right iris|
|`2`|Left iris|



**Table 5.8** Iso19794IrisImageCode Format Restrictions 

## 5.2.8.2 WSDL Definition 

```
<simpleTypename="Iso19794IrisImageCode">
<restrictionbase="xsd:unsignedInt">
<minInclusivevalue="0"/>
<maxInclusivevalue="2"/>
</restriction>
</simpleType>
```

## 5.2.9 DataFormat 

Represents an identifier for a data format. Derived from `xsd:string` . 

## 5.2.9.1 Format Restrictions 

The data format is represented as a non-empty string. The following values SHOULD be supported by the implementation. 

|**Data Format String**|**Description**|
|---|---|
|`data_format_not_set`|Dataformat was not set|
|`opaque`|Opaque data format which can be used when the real data format is unk<br>nown or unimportant.|
|`iso19794_2`|Finger minutiae according to [BIB_ISO_MINUTIAE]|
|`iso19794_4`|Finger image according to [BIB_ISO_19794_FINGER]|
|`iso19794_5`|Face image according to [BIB_ISO_19794_FACE]|
|`icao_lds_dg1`|ICAO LDS datagroup 1|
|`icao_lds_dg2`|ICAO LDS datagroup 2 (face image)|



Federal Office for Information Security 

11 

5 High Level Biometric Services API 

|**Data Format String**|**Description**|
|---|---|
|`icao_lds_dg3`|ICAO LDS datagroup 3 (fingerprint images)|
|`icao_lds_dg4`|ICAO LDS datagroup 4 (iris images)|
|`icao_lds_dg5`|ICAO LDS datagroup 5|
|`icao_lds_dg6`|ICAO LDS datagroup 6|
|`icao_lds_dg7`|ICAO LDS datagroup 7 (signature)|
|`icao_lds_dg8`|ICAO LDS datagroup 8|
|`icao_lds_dg9`|ICAO LDS datagroup 9|
|`icao_lds_dg10`|ICAO LDS datagroup 10|
|`icao_lds_dg11`|ICAO LDS datagroup 11|
|`icao_lds_dg12`|ICAO LDS datagroup 12|
|`icao_lds_dg13`|ICAO LDS datagroup 13|
|`icao_lds_dg14`|ICAO LDS datagroup 14|
|`icao_lds_dg15`|ICAO LDS datagroup 15|
|`icao_lds_dg16`|ICAO LDS datagroup 16|
|`wsq`|Image in WSQ format|
|`bmp`|Image in BMP format|
|`jpeg`|Image in JPEG format|
|`jpeg2000`|Image in JPEG2000 format|
|`png`|Image in PNG format|
|`rgb`|Image in RGB format|
|`tiff`|Image in TIFF format|
|`yuv422`|Image in YUV422 format|
|`bioapi_bir`|BioAPI 2.0 Biometric Information Record|
|`ansi_nist_itl`|ANSI/NIST ITL container|
|`bit`|CBEFF Biometric Information Template|



**Table 5.9** DataFormat Format Restrictions 

## 5.2.9.2 WSDL Definition 

```
<simpleTypename="DataFormat">
<restrictionbase="xsd:string">
<minLengthvalue="1"/>
<maxLengthvalue="255"/>
</restriction>
</simpleType>
```

## 5.2.10 ApplicationProfile 

Represents an Application Profile of the TR-03121 Part 3. It is hereby defined which requirements (e.g. regar ding quality thresholds, data formats, compression or processes) apply to a generalised HLBS service where the Application Profile is configurable. A generalised system using HLBS MAY not support all Application Profiles (e.g. because the system is only used in specific contexts or the system uses a different modality than used within the Application Profile). Derived from `xsd:string` . 

## 5.2.10.1 Format Restrictions 

The application profile is represented as a non-empty string. Whether a service definition SHALL support a specific Application Profile, is defined in the respective service definition itself. 

Federal Office for Information Security 

12 

5 High Level Biometric Services API 

|**Data Format String**|**Description**|
|---|---|
|`BCL_ManualBorderControl`|Volume BCL, Application Pro<br>file Manual Border Control|
|`BCL_SemiMobileManualBorderControl`|Volume BCL, Application Pro<br>file Semi-Mobile Manual Bor<br>der Control|
|`BCL_SelfServiceSystem`|Volume BCL, Application Pro<br>file Self-Service System|
|`GID_UnsupervisedSelfServiceFacialImageAcquitistionSystem`|Volume GID, Application Pro<br>file Unsupervised Self-Service<br>Facial Image Acquisition Sys<br>tem|
|`GID_SupervisedFacialImageAcquisitionSystem`|Volume GID, Application Pro<br>file Supervised Facial Image<br>Acquisition System|
|`GID_SupervisedBasicFacialImageAcquisitionSystem`|Volume GID, Application Pro<br>file Supervised Basic Facial<br>Image Acquisition System|
|`GID_UnsupervisedSelfServiceFingerprintAcquisitionSystem`|Volume GID, Application Pro<br>file Unsupervised Self-Service<br>Fingerprint Acquisition Sys<br>tem|
|`GID_SupervisedFingerprintAcquisition`|Volume GID, Application Pro<br>file Supervised Fingerprint Ac<br>quisition|
|`ARE_ArrivalAttestationDocument`|Volume ARE, Application Pro<br>file Arrival Attestation Docu<br>ment|
|`ARE_ArrivalAttestationDocumentInSpecialSituations`|Volume ARE, Application Pro<br>file Arrival Attestation Docu<br>ment in Special Situations|
|`IMA_MultiModalProcessingImmigrationAuthoritiesEES`|Volume IMA, Application Pro<br>file Multimodal Processing in<br>Immigration Authorities for<br>EES|
|`IMA_MultiModalProcessingImmigrationAuthoritiesSIS`|Volume IMA, Application Pro<br>file Multimodal Processing in<br>Immigration Authorities for<br>SIS|



**Table 5.10** DataFormat Format Restrictions 

## 5.2.10.2 WSDL Definition 

```
<simpleTypename="DataFormat">
<restrictionbase="xsd:string">
<minLengthvalue="1"/>
<maxLengthvalue="255"/>
</restriction>
</simpleType>
```

## 5.2.11 DeviceInformation 

Contains information about a biometric device. 

Federal Office for Information Security 

13 

5 High Level Biometric Services API 

## 5.2.11.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`id`|`xsd:string`<br>Unique ID of this device.|
|`vendor`|`xsd:string`<br>The name of the device vendor.|
|`name`|`xsd:string`<br>The name of the device.|
|`version?`|`xsd:string`<br>The version of the device (if available).|
|`firmwareVersion?`|`xsd:string`<br>The firmware version used in the device (if available).|
|`deviceID?`|`xsd:string`<br>The internal id of the device, e.g. the serial number (if available).|
|`biometricType`|`hlbs:BiometricType?`<br>The biometric modality this device can capture (if available).|
|`properties`|`hlbs:KeyValue`<br>The specific properties of the device.|



**Table 5.11** DeviceInformation Elements 

## 5.2.11.2 WSDL Definition 

```
<complexTypename="DeviceInformation">
<sequence>
<elementname="id"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="vendor"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="name"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="version"type="xsd:string"minOccurs="0"maxOccurs="1"nillable="true"/>
<elementname="firmwareVersion"type="xsd:string"minOccurs="0"maxOccurs="1"nillable="true"/>
<elementname="deviceID"type="xsd:string"minOccurs="0"maxOccurs="1"nillable="true"/>
<elementname="biometricType"type="hlbs:BiometricType"minOccurs="0"maxOccurs="1"
nillable="true"/>
```

```
<elementname="properties"type="hlbs:KeyValue"minOccurs="0"maxOccurs="unbounded"
nillable="true"/>
</sequence>
</complexType>
```

## 5.2.12 ServiceInformation 

Contains information about a biometric service. 

## 5.2.12.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`id`|`xsd:string`<br>Unique ID of this service.|
|`type`|`hlbs:ServiceType`<br>The type of purpose this service can be used for.|
|`vendor`|`xsd:string`<br>The vendor of the service.|
|`name`|`xsd:string`<br>The name of the service.|
|`version?`|`xsd:string`<br>The version of the service (if available).|



Federal Office for Information Security 

14 

5 High Level Biometric Services API 

**Element Name Description** `devices* hlbs:DeviceInformation` A list of devices which are connected and can be used in combination with this service. MAY be empty if no devices are connected or when the service doesn't need any devices for its functionality. 

**Table 5.12** ServiceInformation Elements 

## 5.2.12.2 WSDL Definition 

```
<complexTypename="ServiceInformation">
<sequence>
<elementname="id"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="type"type="hlbs:ServiceType"minOccurs="1"maxOccurs="1"/>
<elementname="vendor"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="name"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="version"type="xsd:string"minOccurs="0"maxOccurs="1"nillable="true"/>
<elementname="devices"type="hlbs:DeviceInformation"minOccurs="0"maxOccurs="unbounded"/>
</sequence>
</complexType>
```

## 5.2.13 BiometricImpression 

Contains the description of a biometric impression type. It can be used to distinguish between "plain" and "rolled" fingerprint captures for example. At the moment only finger impression types are supported. 

## 5.2.13.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`fingerImpression`|`hlbs:Iso19794FingerImpression`<br>Represents an impression type according to [BIB_ISO_19794_FINGER]|



**Table 5.13** BiometricImpression Elements 

## 5.2.13.2 WSDL Definition 

```
<complexTypename="BiometricImpression">
<choice>
<elementname="fingerImpression"type="hlbs:Iso19794FingerImpression"minOccurs="1"maxOccurs="1"/
>
</choice>
</complexType>
```

## 5.2.14 BiometricCode 

Contains the description of a biometric modality. This could be, for example, the specific finger code of a finger which is shown in an image or the description of which kind of facial image should be enrolled. 

## 5.2.14.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`fingerCode`|`hlbs:Iso19794FingerCode`<br>Represents a finger or palm code according to [BIB_ISO_19794_FINGER]|
|`faceImageCode`|`hlbs:Iso19794FaceImageCode`<br>Represents a face image code according to [BIB_ISO_19794_FACE]|
|`irisCode`|`hlbs:Iso19794IrisImageCode`<br>Represents an iris image code according to [BIB_ISO_IRIS]|



**Table 5.14** BiometricCode Elements 

## 5.2.14.2 WSDL Definition 

```
<complexTypename="BiometricCode">
```

Federal Office for Information Security 

15 

5 High Level Biometric Services API 

```
<choice>
```

```
<elementname="fingerCode"type="hlbs:Iso19794FingerCode"minOccurs="1"maxOccurs="1"/>
<elementname="faceImageCode"type="hlbs:Iso19794FaceImageCode"minOccurs="1"maxOccurs="1"/>
<elementname="irisCode"type="hlbs:Iso19794IrisImageCode"minOccurs="1"maxOccurs="1"/>
</choice>
</complexType>
```

## 5.2.15 BiometricCodeList 

Contains a list of biometric codes. Can be used for example to represent an arbitrary combination of single fingers. Although it is theoretically possible to mix modalities in this list (e.g. finger and iris), this SHOULD be avoided if possible. 

## 5.2.15.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`values*`|`hlbs:BiometricCode`<br>List of biometric codes.|



**Table 5.15** BiometricCodeList Elements 

## 5.2.15.2 WSDL Definition 

```
<complexTypename="BiometricCodeList">
<sequence>
<elementname="values"type="hlbs:BiometricCode"minOccurs="0"maxOccurs="unbounded"/>
</sequence>
</complexType>
```

## 5.2.16 StringList 

Represents a list of strings. 

## 5.2.16.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`items*`|`xsd:string`<br>The items of the string list.|



**Table 5.16** StringList Elements 

## 5.2.16.2 WSDL Definition 

```
<complexTypename="StringList">
<sequence>
<elementname="values"type="xsd:string"minOccurs="0"maxOccurs="unbounded"/>
</sequence>
</complexType>
```

## 5.2.17 UserCommandInfo 

Contains information about the current state of a user command. It indicates whether a specific user com mand can be signalled at the moment (allowed) or not (not-allowed). This information SHOULD be used by the user interface to disable/enable the button/element associated with the command. 

## 5.2.17.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`userCommandId`|`xsd:string`<br>The ID of the user command.|



Federal Office for Information Security 

16 

5 High Level Biometric Services API 

|**Element Name**|**Description**|
|---|---|
|`status`|`hlbs:UserCommandStatus`<br>The current status of the user command.|



**Table 5.17** UserCommandInfo Elements 

## 5.2.17.2 WSDL Definition 

```
<complexTypename="UserCommandInfo">
<sequence>
<elementname="userCommandId"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="status"type="hlbs:UserCommandStatus"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
```

## 5.2.18 Image 

Represents an image. 

## 5.2.18.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`imageData`|`xsd:base64Binary`<br>The image data.|
|`format?`|`hlbs:DataFormat`<br>The image format (if available).|
|`width?`|`xsd:int`<br>The width of the image (if available).|
|`height?`|`xsd:int`<br>The height of the image (if available).|
|`biometricCodeList?`|`hlbs:BiometricCodeList`<br>A list of biometric codes representing what is shown in the image (if available).|
|`biometricImpression?`|`hlbs:BiometricImpression`<br>A biometric impression type describing the type of the image (e.g. "plain" or "rol<br>led" - only if available).|
|`imageRegion*`|`hlbs:ImageRegion`<br>Region(s) within the image.|
|`xmlParameter?`|`xsd:string`<br>Application specific metadata for the given image.|



**Table 5.18** Image Elements 

## 5.2.18.2 WSDL Definition 

```
<complexTypename="Image">
<sequence>
```

```
<elementname="imageData"type="xsd:base64Binary"minOccurs="1"maxOccurs="1"nillable="true"/>
<elementname="format"type="hlbs:DataFormat"minOccurs="0"maxOccurs="1"nillable="true"/>
<elementname="width"type="xsd:int"minOccurs="0"maxOccurs="1"nillable="true"/>
<elementname="height"type="xsd:int"minOccurs="0"maxOccurs="1"nillable="true"/>
<elementname="biometricCodeList"type="hlbs:BiometricCodeList"minOccurs="0"maxOccurs="1"
nillable="true"/>
```

```
<elementname="biometricImpression"type="hlbs:BiometricImpression"minOccurs="0"maxOccurs="1"
nillable="true"/>
```

```
<elementname="imageRegion"type="hlbs:ImageRegion"minOccurs="0"maxOccurs="unbounded"
nillable="true"/>
```

```
<elementname="xmlParameter"type="xsd:string"minOccurs="0"maxOccurs="1"nillable="true"/>
</sequence>
```

```
</complexType>
```

Federal Office for Information Security 

17 

5 High Level Biometric Services API 

## 5.2.19 Point 

Represents a point. 

## 5.2.19.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`x`|`xsd:int`<br>The x-coordinate of the point.|
|`y`|`xsd:int`<br>The y-coordinate of the point.|



**Table 5.19** Point Elements 

## 5.2.19.2 WSDL Definition 

```
<complexTypename="Point">
<sequence>
<elementname="x"type="xsd:int"minOccurs="1"maxOccurs="1"/>
<elementname="y"type="xsd:int"minOccurs="1"maxOccurs="1"/>
<sequence>
</complexType>
```

## 5.2.20 ImageRegion 

Represents a rectangular region within an image. 

## 5.2.20.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`p1`|`hlbs:Point`<br>The top left point of an rectangular region within an image.|
|`p2`|`hlbs:Point`<br>The bottom right point of an rectangular region within an image.|



**Table 5.20** Image Elements 

## 5.2.20.2 WSDL Definition 

```
<complexTypename="ImageRegion">
<sequence>
<elementname="p1"type="hlbs:Point"minOccurs="1"maxOccurs="1"/>
<elementname="p2"type="hlbs:Point"minOccurs="1"maxOccurs="1"/>
<sequence>
</complexType>
```

## 5.2.21 ImageList 

Represents a list of images. 

## 5.2.21.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`images`*|`hlbs:Image`<br>The sequence of images.|



**Table 5.21** ImageList Elements 

## 5.2.21.2 WSDL Definition 

```
<complexTypename="ImageList">
<sequence>
<elementname="images"type="hlbs:Image"minOccurs="0"maxOccurs="unbounded"/>
```

Federal Office for Information Security 

18 

5 High Level Biometric Services API 

```
</sequence>
</complexType>
```

## 5.2.22 Binary 

Represents binary data. 

## 5.2.22.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`format`|`hlbs:DataFormat`<br>The dataformat of the binary data.|
|`data`|`xsd:base64Binary`<br>The data.|



**Table 5.22** Binary Elements 

## 5.2.22.2 WSDL Definition 

```
<complexTypename="Binary">
<sequence>
<elementname="format"type="hlbs:DataFormat"minOccurs="1"maxOccurs="1"/>
<elementname="data"type="xsd:base64Binary"minOccurs="1"maxOccurs="1"nillable="true"/>
</sequence>
</complexType>
```

## 5.2.23 KeyValue 

Represents a key-value-pair. This element is used to describe and distinguish the different configuration, feed back and result values. 

## 5.2.23.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`key`|`xsd:string`<br>The unique identifier which specifies the key of the key-value-pair.|
|`boolValue`|`xsd:boolean`<br>A bool value.|
|`intValue`|`xsd:int`<br>An integer value.|
|`floatValue`|`xsd:float`<br>A float value.|
|`stringValue`|`xsd:string`<br>A string value.|
|`biometricImpressionValue`|`hlbs:BiometricImpression`<br>A biometric impression type value.|
|`biometricCodeValue`|`hlbs:BiometricCode`<br>A biometric code value.|
|`biometricCodeListValue`|`hlbs:BiometricCodeList`<br>A biometric code list value.|
|`imageValue`|`hlbs:Image`<br>An image value.|
|`dataFormatValue`|`hlbs:DataFormat`<br>A data format value.|
|`binaryValue`|`hlbs:Binary`<br>A binary value.|



Federal Office for Information Security 

19 

5 High Level Biometric Services API 

|**Element Name**|**Description**|
|---|---|
|`stringListValue`|`hlbs:StringList`<br>A string list value.|
|`imageListValue`|`hlbs:ImageList`<br>An image list value.|



**Table 5.23** KeyValue Elements 

## 5.2.23.2 WSDL Definition 

```
<complexTypename="KeyValue">
<sequence>
<elementname="key"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<choice>
```

```
<elementname="boolValue"type="xsd:boolean"minOccurs="1"maxOccurs="1"/>
```

```
<elementname="intValue"type="xsd:int"minOccurs="1"maxOccurs="1"/>
```

```
<elementname="floatValue"type="xsd:float"minOccurs="1"maxOccurs="1"/>
```

```
<elementname="stringValue"type="xsd:string"minOccurs="1"maxOccurs="1"nillable="true"/>
<elementname="biometricImpressionValue"type="hlbs:BiometricImpression"minOccurs="1"
maxOccurs="1"nillable="true"/>
```

```
<elementname="biometricCodeValue"type="hlbs:BiometricCode"minOccurs="1"maxOccurs="1"
nillable="true"/>
```

- `<element name=` **`"biometricCodeListValue"`** `type=` **`"hlbs:BiometricCodeList"`** `minOccurs=` **`"1"`** `maxOccurs=` **`"1"`** 

- `nillable=` **`"true"`** `/>` 

- `<element name=` **`"imageValue"`** `type=` **`"hlbs:Image"`** `minOccurs=` **`"1"`** `maxOccurs=` **`"1"`** `nillable=` **`"true"`** `/> <element name=` **`"dataFormatValue"`** `type=` **`"hlbs:DataFormat"`** `minOccurs=` **`"1"`** `maxOccurs=` **`"1"`** 

- `nillable=` **`"true"`** `/>` 

- `<element name=` **`"binaryValue"`** `type=` **`"hlbs:Binary"`** `minOccurs=` **`"1"`** `maxOccurs=` **`"1"`** `nillable=` **`"true"`** `/> <element name=` **`"stringListValue"`** `type=` **`"hlbs:StringList"`** `minOccurs=` **`"1"`** `maxOccurs=` **`"1"`** 

- `nillable=` **`"true"`** `/>` 

```
<elementname="imageListValue"type="hlbs:ImageList"minOccurs="1"maxOccurs="1"nillable="true"/
>
```

```
</choice>
</sequence>
</complexType>
```

## 5.2.24 UserCommand 

Represents a user command, which can be signaled by the application. A user command MAY contain para meters which reveal further details about the command. It depends on the concrete service whether parame ters for certain commands are supported or not. 

## 5.2.24.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`userCommandId`|`xsd:string`<br>The ID if the user command which is signalled.|
|`parameters*`|`hlbs:KeyValue`<br>A list of key-value-pairs describing further details about the command (OPTIONAL).|



**Table 5.24** UserCommand Elements 

## 5.2.24.2 WSDL Definition 

```
<complexTypename="UserCommand">
<sequence>
<elementname="userCommandId"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="parameters"type="hlbs:KeyValue"minOccurs="0"maxOccurs="unbounded"/>
</sequence>
</complexType>
```

Federal Office for Information Security 

20 

5 High Level Biometric Services API 

## 5.2.25 Feedback 

Represents the current state of the service execution including information about the user command states, live feedback and the general execution state. An implementation SHOULD only transfer feedback to the user that has changed since the last feedback delivery for performance reasons. However, it SHALL NOT lead to an error in the client if the server sends equal feedback elements in successive calls. 

## 5.2.25.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`status`|`hlbs:FeedbackStatus`<br>The current state of the service execution (running, finished, cancelled, ...).|
|`userCommands*`|`hlbs:UserCommandInfo`<br>A list of user command info which represent the current state of the user com<br>mands.|
|`feedbackElements*`|`hlbs:KeyValue`<br>A list of feedback elements with live information about the service execution.|



**Table 5.25** Feedback Elements 

## 5.2.25.2 WSDL Definition 

```
<complexTypename="Feedback">
<sequence>
<elementname="status"type="hlbs:FeedbackStatus"minOccurs="1"maxOccurs="1"/>
<elementname="userCommands"type="hlbs:UserCommandInfo"minOccurs="0"maxOccurs="unbounded"/>
<elementname="feedbackElements"type="hlbs:KeyValue"minOccurs="0"maxOccurs="unbounded"/>
</sequence>
</complexType>
```

## 5.2.26 Results 

Represents the results of a service execution. Results can be retrieved as soon as the service execution has finished or was cancelled. 

## 5.2.26.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`resultElements*`|`hlbs:KeyValue`<br>A list of key-value-pairs representing the results of the service execution.|



**Table 5.26** Results Elements 

## 5.2.26.2 WSDL Definition 

```
<complexTypename="Results">
<sequence>
<elementname="resultElements"type="hlbs:KeyValue"minOccurs="0"maxOccurs="unbounded"/>
</sequence>
</complexType>
```

## 5.3 Fault Types 

This section specifies the SOAP faults that are specific to this SOAP API. No fault has any attributes. 

## 5.3.1 InvalidId 

Base type of other faults which are returned when an invalid id is specified in a call. 

Federal Office for Information Security 

21 

5 High Level Biometric Services API 

## 5.3.1.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`id`|`xsd:string`<br>The value of the invalid id.|



**Table 5.27** InvalidId Elements 

## 5.3.1.2 WSDL Definition 

```
<complexTypename="InvalidId">
<sequence>
<elementname="id"type="xsd:string"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
```

## 5.3.2 InvalidServiceId 

Returned when no service with the given ID is found. Derived from `hlbs:InvalidId` . 

## 5.3.2.1 Elements 

None. 

## 5.3.2.2 WSDL Definition 

```
<complexTypename="InvalidServiceId">
<complexContent>
<extensionbase="hlbs:InvalidId">
<sequence>
</sequence>
</extension>
</complexContent>
</complexType>
```

## 5.3.3 InvalidDeviceId 

Returned when no device with the given ID is supported by the respective service. Derived from `hlbs:Inva lidId` . 

## 5.3.3.1 Elements 

None. 

## 5.3.3.2 WSDL Definition 

```
<complexTypename="InvalidDeviceId">
<complexContent>
<extensionbase="hlbs:InvalidId">
<sequence>
</sequence>
</extension>
</complexContent>
</complexType>
```

## 5.3.4 InvalidSessionHandle 

Returned when an unknown session handle is specified. 

## 5.3.4.1 Elements 

None. 

Federal Office for Information Security 

22 

5 High Level Biometric Services API 

## 5.3.4.2 WSDL Definition 

```
<complexTypename="InvalidSessionHandle">
<complexContent>
<extensionbase="hlbs:InvalidId">
<sequence>
</sequence>
</extension>
</complexContent>
</complexType>
```

## 5.3.5 InvalidParameterKey 

Returned when an unknown parameter key is specified in a key-value-pair. 

## 5.3.5.1 Elements 

None. 

## 5.3.5.2 WSDL Definition 

```
<complexTypename="InvalidParameterKey">
<complexContent>
<extensionbase="hlbs:InvalidId">
<sequence>
</sequence>
</extension>
</complexContent>
</complexType>
```

## 5.3.6 InvalidParameterValue 

Returned when the value assoicated with a parameter key is not valid. This could happen for example if the specified value is out of the valid range or of an invalid type. 

## 5.3.6.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`parameterKey`|`xsd:string`<br>The name of the parameter key whose value is considered invalid.|



**Table 5.28** InvalidParameterValue Elements 

## 5.3.6.2 WSDL Definition 

```
<complexTypename="InvalidParameterValue">
<sequence>
<elementname="parameterKey"type="xsd:string"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
```

## 5.3.7 AlreadyInUse 

Returned when a service-device-combination is acquired when it is currently already acquired by someone else. 

## 5.3.7.1 Elements 

|**Element Name**|**Description**|
|---|---|
|`serviceId`|`xsd:string`<br>The ID of the service whose acquirement failed.|



Federal Office for Information Security 

23 

5 High Level Biometric Services API 

|**Element Name**|**Description**|
|---|---|
|`deviceId`|`xsd:string`<br>The ID of the device whose acquirement failed.|



**Table 5.29** AlreadyInUse Elements 

## 5.3.7.2 WSDL Definition 

```
<complexTypename="AlreadyInUse">
<sequence>
<elementname="serviceId"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="deviceId"type="xsd:string"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
```

## 5.3.8 TimeoutOccured 

Returned when a function timed out. 

## 5.3.8.1 Elements 

None. 

## 5.3.8.2 WSDL Definition 

```
<complexTypename="TimeoutOccured">
<sequence>
</sequence>
</complexType>
```

## 5.3.9 InvalidUserCommandId 

Returned when an unknown user command is signalled. 

## 5.3.9.1 Elements 

None. 

## 5.3.9.2 WSDL Definition 

```
<complexTypename="InvalidUserCommandId">
<complexContent>
<extensionbase="hlbs:InvalidId">
<sequence>
</sequence>
</extension>
</complexContent>
</complexType>
```

## 5.3.10 NotFinishedYet 

Returned when results should be retrieved, but the service execution has not finished yet. 

## 5.3.10.1 Elements 

None. 

## 5.3.10.2 WSDL Definition 

```
<complexTypename="NotFinishedYet">
<sequence>
</sequence>
</complexType>
```

Federal Office for Information Security 

24 

5 High Level Biometric Services API 

## 5.3.11 MTOMNotSupported 

Return when MTOM attachments are requested for feedback delivery but are not supported by the server. 

## 5.3.11.1 Elements 

None. 

## 5.3.11.2 WSDL Definition 

```
<complexTypename="MTOMNotSupported">
<sequence>
</sequence>
</complexType>
```

## 5.3.12 AlreadyRunning 

Returned when a service-device-combination should be executed but has already been started before. 

## 5.3.12.1 Elements 

None. 

## 5.3.12.2 WSDL Definition 

```
<complexTypename="AlreadyRunning">
<sequence>
</sequence>
</complexType>
```

## 5.4 Operations 

## 5.4.1 getAllServices 

Returns a list of all available services. Each service description contains a list devices which can be selected for the service execution. 

## 5.4.1.1 Request Elements 

None. 

## 5.4.1.2 Response Elements 

|**Element Name**|**Description**|
|---|---|
|`service*`|`hlbs:ServiceInformation`<br>List of service information.|



**Table 5.30** getAllServices Response Elements 

## 5.4.1.3 Faults 

None. 

## 5.4.1.4 WSDL Definition 

```
<elementname="getAllServices">
<complexType>
<sequence>
</sequence>
</complexType>
</element>
<elementname="getAllServicesResponse">
<complexType>
<sequence>
<elementname="service"type="hlbs:ServiceInformation"minOccurs="0"maxOccurs="unbounded"/>
</sequence>
```

Federal Office for Information Security 

25 

5 High Level Biometric Services API 

```
</complexType>
</element>
```

## 5.4.2 getServiceDescription 

Returns an XML description of a service-device-combination. The XML schema is defined in Section 5.5 and contains a description of the possible configuration values, feedback values, user commands and results. The primary purpose of the description is to give the application programmer an overview of the service and help him to implement the application. But of course it is also possible to parse the description in the application and, for example, dynamically generate or adjust the user interface for the specific service-device-combina tion. 

## 5.4.2.1 Request Elements 

|**Element Name**|**Description**|
|---|---|
|`serviceID`|`xsd:string`<br>The ID of the service.|
|`deviceID?`|`xsd:string`<br>The ID of the device (OPTIONAL).|



**Table 5.31** getAllServices Request Elements 

## 5.4.2.2 Response Elements 

|**Element Name**|**Description**|
|---|---|
|`serviceDescriptionXML`|`xsd:string`<br>The description of the service-device-combination as XML. The XML schema is<br>defined in<br>Section 5.5.|



**Table 5.32** getServiceDescription Response Elements 

## 5.4.2.3 Faults 

|**Fault**|**Cause**|
|---|---|
|`InvalidServiceId`|The specified service id is unknown.|
|`InvalidDeviceId`|The specified device id is unknown or is not supported by the selected service.|



**Table 5.33** getServiceDescription Faults 

## 5.4.2.4 WSDL Definition 

```
<elementname="getServiceDescription">
<complexType>
<sequence>
<elementname="serviceID"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="deviceID"type="xsd:string"minOccurs="0"maxOccurs="1"/>
</sequence>
</complexType>
</element>
<elementname="getServiceDescriptionResponse">
<complexType>
<sequence>
<elementname="serviceDescriptionXML"type="xsd:string"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
```

## 5.4.3 acquireService 

Exclusively reserves a service-device-combination for use. Each service-device-combination can only be ac quired once at the same time. To release the lock, the function releaseService SHALL be called. 

Federal Office for Information Security 

26 

5 High Level Biometric Services API 

## 5.4.3.1 Request Elements 

|**Element Name**|**Description**|
|---|---|
|`serviceID`|`xsd:string`<br>The ID of the service to acquire.|
|`deviceID?`|`xsd:string`<br>The ID of the device to acquire (OPTIONAL). If no device ID is specified, the function only<br>succeeds if the service can be executed without a device.|
|`sessionHandle?`|`xsd:string`<br>If specified, this sessionHandle is used instead of an automatically generated one.|



**Table 5.34** acquireService Request Elements 

## 5.4.3.2 Response Elements 

|**Element Name**|**Description**|
|---|---|
|`sessionHandle`|`xsd:string`<br>The session handle which SHALL be used in consecutive calls. If a session handle was speci<br>fied in the request, the returned handle equals the one from the request.|



**Table 5.35** acquireService Response Elements 

## 5.4.3.3 Faults 

|**Fault**|**Cause**|
|---|---|
|`AlreadyInUse`|The service-device-combination is already acquired. It can only be REQUIRED if<br>it is released before.|
|`InvalidServiceId`|The specified service ID is unkown.|
|`InvalidDeviceId`|The specified device ID is unknown or is not supported by this service.|



**Table 5.36** acquireService Faults 

## 5.4.3.4 WSDL Definition 

```
<elementname="acquireService">
<complexType>
<sequence>
<elementname="serviceID"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="deviceID"type="xsd:string"minOccurs="0"maxOccurs="1"/>
<elementname="sessionHandle"type="xsd:string"minOccurs="0"maxOccurs="1"/>
</sequence>
</complexType>
</element>
<elementname="acquireServiceResponse">
<complexType>
<sequence>
<elementname="sessionHandle"type="xsd:string"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
```

## 5.4.4 configureService 

Sets configuration values for a service-device-combination which can influence the service behaviour or feed back delivery. It SHALL be possible to call this function multiple times for the same session handle. Newer configuration values SHALL overwrite values which were set in previous calls. It SHALL be possible to call this method before `beginServiceExceution` is called. It SHOULD be possible to call this method even after `be ginServiceExecution` was called. 

Federal Office for Information Security 

27 

5 High Level Biometric Services API 

## 5.4.4.1 Request Elements 

|**Element Name**|**Description**|
|---|---|
|`sessionHandle`|`xsd:string`<br>The session handle belonging to the service-device-combination which should be confi<br>gured.|
|`Parameters+`|`hlbs:KeyValue`<br>List of key-value-pairs containing the configuration values to be set.|



**Table 5.37** configureService Request Elements 

## 5.4.4.2 Response Elements 

None. 

## 5.4.4.3 Faults 

|**Fault**|**Cause**|
|---|---|
|`InvalidSessionHandle`|The specified session handle is not valid.|
|`InvalidParameterKey`|One of the specified parameter keys is not supported by the service.|
|`InvalidParameterValue`|One of the specified parameter values is not valid (e.g. because it is out<br>of range or of invalid type).|



**Table 5.38** configureService Faults 

## 5.4.4.4 WSDL Definition 

```
<elementname="configureService">
<complexType>
<sequence>
<elementname="sessionHandle"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="parameters"type="hlbs:KeyValue"minOccurs="1"maxOccurs="unbounded"/>
</sequence>
</complexType>
</element>
<elementname="configureServiceResponse">
<complexType>
<sequence>
</sequence>
</complexType>
</element>
```

## 5.4.5 beginServiceExecution 

Starts the execution of an acquired service-device-combination. The response of this method contains the initial state of the service execution which SHOULD be used to initialize the user interface. After this call the service process starts and the application SHOULD update the user interface by calling the function `getSer viceFeedback` in a loop until the service execution finished. 

## 5.4.5.1 Request Elements 

|**Element Name**|**Description**|
|---|---|
|`sessionHandle`|`xsd:string`<br>The session handle belonging to the acquired service-device-combination which should be<br>started.|
|`useMTOM?`|`xsd:boolean`<br>If true and supported by the server, all binary data in the feedback and result queries are retur<br>ned as MTOM attachments. Otherwise, all binary data is returned as normal base64 encoded<br>strings. It is recommended to use MTOM attachments because of improved performance.|



**Table 5.39** beginServiceExecution Request Elements 

Federal Office for Information Security 

28 

5 High Level Biometric Services API 

## 5.4.5.2 Response Elements 

|**Element Name**|**Description**|
|---|---|
|`feedback`|`hlbs:Feedback`<br>Feedback which describes the initial state of the service execution.|



**Table 5.40** beginServiceExecution Response Elements 

## 5.4.5.3 Faults 

|**Fault**|**Cause**|
|---|---|
|`InvalidSessionHandle`|The specified session handle is unknown.|
|`AlreadyRunning`|The service execution has already been started.|
|`MTOMNotSupported`|The server doesn't support MTOM attachments.|



**Table 5.41** beginServiceExecution Faults 

## 5.4.5.4 WSDL Definition 

```
<elementname="beginServiceExecution">
<complexType>
<sequence>
<elementname="sessionHandle"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="useMTOM"type="xsd:boolean"minOccurs="0"maxOccurs="1"nillable="true"/>
</sequence>
</complexType>
</element>
<elementname="beginServiceExecutionResponse">
<complexType>
<sequence>
<elementname="feedback"type="hlbs:Feedback"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
```

## 5.4.6 getServiceFeedback 

Returns the current state of the service execution. The server SHOULD only return feedback elements which have changed since the last call of this function. It is assumed that feedback elements which are not present in the response haven't changed. If the function runs into a timeout the application SHOULD still continue the feedback loop. 

## 5.4.6.1 Request Elements 

|**Element Name**|**Description**|
|---|---|
|`sessionHandle`|`xsd:string`<br>The session handle of the service execution for which the next feedback should be retrie<br>ved.|
|`timeout-ms`|`xsd:int`<br>Timeout in ms after which the function returns if no new feedback is available. If the value<br>is smaller than 0, no timeout will be set.|



**Table 5.42** getServiceFeedback Request Elements 

## 5.4.6.2 Response Elements 

|**Element Name**|**Description**|
|---|---|
|`feedback`|`hlbs:Feedback`<br>The feedback elements.|



**Table 5.43** getServiceFeedback Response Elements 

Federal Office for Information Security 

29 

5 High Level Biometric Services API 

## 5.4.6.3 Faults 

|**Fault**|**Cause**|
|---|---|
|`InvalidSessionHandle`|The specified session handle is unknown.|
|`TimeoutOccured`|The timeout has expired and no changed feedback elements were<br>found.|



**Table 5.44** getServiceFeedback Faults 

## 5.4.6.4 WSDL Definition 

```
<elementname="getServiceFeedback">
<complexType>
<sequence>
<elementname="sessionHandle"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="timeout-ms"type="xsd:int"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
<elementname="getServiceFeedbackResponse">
<complexType>
<sequence>
<elementname="feedback"type="hlbs:Feedback"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
```

## 5.4.7 signalUserCommand 

Signals a user command with OPTIONAL additional parameters. This function is typically called when a user executes a command in the user interface, like clicking a button for example. The function will return an error when the signalled user command is not allowed by the service at the moment. 

## 5.4.7.1 Request Elements 

|**Element Name**|**Description**|
|---|---|
|`sessionHandle`|`xsd:string`<br>The session handle for which this user command is signalled.|
|`userCommand`|`hlbs:UserCommand`<br>The user command to be signalled.|



**Table 5.45** signalUserCommand Request Elements 

## 5.4.7.2 Response Elements 

None. 

## 5.4.7.3 Faults 

|**Fault**|**Cause**|
|---|---|
|`InvalidSessionHandle`|The specified session handle is unknown.|
|`InvalidUserCommandId`|The specified user command id is unknown or not allowed at the mo<br>ment.|
|`InvalidParameterKey`|One of the command parameters has an unknown key.|
|`InvalidParameterValue`|One of the command parameters has an invalid value (e.g. out of ran<br>ge or of invalid type).|



**Table 5.46** signalUserCommand Faults 

## 5.4.7.4 WSDL Definition 

```
<elementname="signalUserCommand">
```

Federal Office for Information Security 

30 

5 High Level Biometric Services API 

```
<complexType>
<sequence>
<elementname="sessionHandle"type="xsd:string"minOccurs="1"maxOccurs="1"/>
<elementname="userCommand"type="hlbs:UserCommand"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
<elementname="signalUserCommandResponse">
<complexType>
<sequence>
</sequence>
</complexType>
</element>
```

## 5.4.8 endServiceExecution 

Stops the service execution. This call is OPTIONAL because it is also implicitly called when `releaseService` is called. However, it is recommended to call this function before the function getResults is called to ensure that service execution has finished. 

## 5.4.8.1 Request Elements 

|**Element Name**|**Description**|
|---|---|
|`sessionHandle`|`xsd:string`<br>The session handle whose execution should be stopped.|



**Table 5.47** endServiceExecution Request Elements 

## 5.4.8.2 Response Elements 

None. 

## 5.4.8.3 Faults 

|**Fault**|**Cause**|
|---|---|
|`InvalidSessionHandle`|The specified session handle is unknown.|



**Table 5.48** endServiceExecution Faults 

## 5.4.8.4 WSDL Definition 

```
<elementname="endServiceExecution">
<complexType>
<sequence>
<elementname="sessionHandle"type="xsd:string"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
<elementname="endServiceExecutionResponse">
<complexType>
<sequence>
</sequence>
</complexType>
</element>
```

## 5.4.9 getResults 

Returns the results generated by the service execution. The service execution SHALL have finished before this function can be called. Even if the execution was cancelled or ran into an error the function `getResults` SHOULD still be called to get intermediate results or log data describing the errors. 

Federal Office for Information Security 

31 

5 High Level Biometric Services API 

## 5.4.9.1 Request Elements 

|**Element Name**|**Description**|
|---|---|
|`sessionHandle`|`xsd:string`<br>The session handle for which the results are requested.|



**Table 5.49** getResults Request Elements 

## 5.4.9.2 Response Elements 

|**Element Name**|**Description**|
|---|---|
|`results`|`hlbs:Results`<br>The results generated by the service execution|



**Table 5.50** getResults Response Elements 

## 5.4.9.3 Faults 

|**Fault**|**Cause**|
|---|---|
|`InvalidSessionHandle`|The specified session handle is unknown.|
|`NotFinishedYet`|The service execution has not been finished yet.|



**Table 5.51** getResults Faults 

## 5.4.9.4 WSDL Definition 

```
<elementname="getResults">
<complexType>
<sequence>
<elementname="sessionHandle"type="xsd:string"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
<elementname="getResultsResponse">
<complexType>
<sequence>
<elementname="results"type="hlbs:Results"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
```

## 5.4.10 releaseService 

Releases an acquired service-device-combination and makes this combination available for new acquire ments. Implicitly calls `endServiceExecution` to make sure that the service execution has finished before the lock is released. After the call the session handle is invalid. 

## 5.4.10.1 Request Elements 

|**Element Name**|**Description**|
|---|---|
|`sessionHandle`|`xsd:string`<br>The session handle to be released.|



**Table 5.52** releaseService Request Elements 

## 5.4.10.2 Response Elements 

None. 

Federal Office for Information Security 

32 

5 High Level Biometric Services API 

## 5.4.10.3 Faults 

|**Fault**|**Cause**|
|---|---|
|`InvalidSessionHandle`|The specified session handle is unknown.|



**Table 5.53** releaseService Faults 

## 5.4.10.4 WSDL Definition 

```
<elementname="releaseService">
<complexType>
<sequence>
<elementname="sessionHandle"type="xsd:string"minOccurs="1"maxOccurs="1"/>
</sequence>
</complexType>
</element>
<elementname="releaseServiceResponse">
<complexType>
<sequence>
</sequence>
</complexType>
</element>
```

## 5.5 Service-Device Description Schema 

The XML schema for the HLBS service-device description can be found in the file `hlbs_service_v1.xsd` . The namespace of the definition is http://trbio.bsi.bund.de/hlbs/1. 

An example can be found in Section 6.1. 

## 5.5.1 Self-Device Description Document 

XML document that provides the following information about a service-device-combination: 

- General information about the service 

- General information about the device 

- Information about possible configuration values 

- Information about available user commands 

- Information about provided feedback 

- Information about provided results 

## 5.5.1.1 Root Element 

|**Element Name**|**Description**|
|---|---|
|`Service`|`hlbs:type.service`<br>Root element of the service-device description.|



**Table 5.54** Root Element 

## 5.5.1.2 XSD Definition 

```
<xs:elementname="Service"type="hlbs:type.service"/>
```

## 5.5.2 type.service 

Root element of a HLBS service-device description. 

Federal Office for Information Security 

33 

5 High Level Biometric Services API 

## 5.5.2.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`schemaVersion`|`xsd:integer`<br>The`schemaVersion`currently has the value 1.|



**Table 5.55** type.service Attributes 

## 5.5.2.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`Information`|`hlbs:type.information`<br>General information about the service and device.|
|`Configuration?`|`hlbs:type.configuration`<br>Information about possible configuration values (if available).|
|`UserCommands?`|`hlbs:type.user.commands`<br>Information about possible user commands (if available).|
|`FeedbackElements?`|`hlbs:type.feedback`<br>Information about possible feedback elements (if available).|
|`Results`|`hlbs:type.feedback`<br>Information about possible results.|



**Table 5.56** type.service Elements 

## 5.5.2.3 XSD Definition 

```
<xs:complexTypename="type.service">
```

```
<xs:sequence>
```

```
<xs:elementname="Information"type="hlbs:type.information"minOccurs="1"maxOccurs="1" />
<xs:elementname="Configuration"type="hlbs:type.configuration"minOccurs="0"maxOccurs="1" />
<xs:elementname="UserCommands"type="hlbs:type.user.commands"minOccurs="0"maxOccurs="1" />
<xs:elementname="FeedbackElements"type="hlbs:type.feedback"minOccurs="0"maxOccurs="1" />
<xs:elementname="Results"type="hlbs:type.feedback"minOccurs="1"maxOccurs="1" />
</xs:sequence>
```

```
<xs:attributename="schemaVersion"type="xs:integer"use="required" />
</xs:complexType>
```

## 5.5.3 type.information 

Provides general information about the service and the corresponding device. 

## 5.5.3.1 Attributes 

None. 

## 5.5.3.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`Id`|`xs:string`<br>Unique ID of this service.|
|`Vendor?`|`xs:string`<br>Name of the vendor of the service (if available).|
|`Name`|`xs:string`<br>Name of the service.|
|`Version?`|`xs:string`<br>Version of the service (if available).|
|`Description?`|`xs:string`<br>Textual description of the service (if available).|



Federal Office for Information Security 

34 

5 High Level Biometric Services API 

|**Element Name**|**Description**|
|---|---|
|`Type`|`hlbs:type.information.service.type`<br>Purpose/Type of this service.|
|`Device?`|`hlbs:type.information.devices.device`<br>Information about the device (if available).|



**Table 5.57** type.information Elements 

## 5.5.3.3 XSD Definition 

```
<xs:complexTypename="type.information">
<xs:sequence>
<xs:elementname="Id"minOccurs="1"maxOccurs="1"type="xs:string" />
<xs:elementname="Vendor"minOccurs="0"maxOccurs="1"type="xs:string" />
<xs:elementname="Name"minOccurs="1"maxOccurs="1"type="xs:string"/>
<xs:elementname="Version"minOccurs="0"maxOccurs="1"type="xs:string"/>
<xs:elementname="Description"minOccurs="0"maxOccurs="1"type="xs:string"/>
<xs:elementname="Type"minOccurs="1"maxOccurs="1"type="hlbs:type.information.service.type" /
>
<xs:elementname="Device"minOccurs="0"maxOccurs="1"type="hlbs:type.information.devices.device"
 />
</xs:sequence>
</xs:complexType>
```

## 5.5.4 type.information.service.type 

Represents the purpose of the service. Derived from `xs:string` . 

## 5.5.4.1 Values 

|**Value**|**Description**|
|---|---|
|`Enrolment`|The service is used for enrolment.|
|`Verification`|The service is used for verification.|
|`Comparison`|The service is used for comparison of two biometric templates.|
|`Other`|The service is used for another purpose.|



**Table 5.58** type.information.service.type Values 

## 5.5.4.2 XSD Definition 

```
<xs:simpleTypename="type.information.service.type">
<xs:restrictionbase="xs:string">
<xs:enumerationvalue="Enrolment" />
<xs:enumerationvalue="Verification" />
<xs:enumerationvalue="Comparison" />
<xs:enumerationvalue="Other" />
</xs:restriction>
</xs:simpleType>
```

## 5.5.5 type.information.devices.device 

Provides general information about the selected device. 

## 5.5.5.1 Attributes 

None. 

## 5.5.5.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`Id`|`xs:string`<br>Unique ID of this service.|



Federal Office for Information Security 

35 

5 High Level Biometric Services API 

|**Element Name**|**Description**|
|---|---|
|`Vendor?`|`xs:string`<br>Name of the vendor of the device (if available).|
|`Name`|`xs:string`<br>Name of the device.|
|`Version?`|`xs:string`<br>Version of the device (if available).|
|`FirmwareVersion?`|`xs:string`<br>Firmware version of the device (if available).|
|`DeviceId?`|`xs:string`<br>The device id (if available, e.g. the serial number).|
|`BiometricType?`|`hlbs:type.device.biometric.type`<br>The biometric modality this device can capture (if available).|
|`Properties?`|`hlbs:type.device.properties`<br>Specific properties of the device (if available).|



**Table 5.59** type.information.devices.device Elements 

## 5.5.5.3 XSD Definition 

## `<xs:complexType name=` **`"type.information.devices.device"`** `>` 

```
<xs:sequence>
```

```
<xs:elementname="Id"minOccurs="1"maxOccurs="1"type="xs:string" />
```

- `<xs:element name=` **`"Vendor"`** `minOccurs=` **`"0"`** `maxOccurs=` **`"1"`** `type=` **`"xs:string"`** `/>` 

- `<xs:element name=` **`"Name"`** `minOccurs=` **`"1"`** `maxOccurs=` **`"1"`** `type=` **`"xs:string"`** `/>` 

- `<xs:element name=` **`"Version"`** `minOccurs=` **`"0"`** `maxOccurs=` **`"1"`** `type=` **`"xs:string"`** `/>` 

- `<xs:element name=` **`"FirmwareVersion"`** `minOccurs=` **`"0"`** `maxOccurs=` **`"1"`** `type=` **`"xs:string"`** `/>` 

- `<xs:element name=` **`"DeviceID"`** `minOccurs=` **`"0"`** `maxOccurs=` **`"1"`** `type=` **`"xs:string"`** `/>` 

```
<xs:elementname="BiometricType"minOccurs="0"maxOccurs="1"
```

```
type="hlbs:type.device.biometric.type" />
```

- `<xs:element name=` **`"Properties"`** `minOccurs=` **`"0"`** `maxOccurs=` **`"1"`** `type=` **`"hlbs:type.device.properties"`** `/>` 

- `</xs:sequence>` 

```
</xs:complexType>
```

## 5.5.6 type.device.biometric.type 

Represents the biometric modality a device can capture. Derived from `xs:string` . 

## 5.5.6.1 Values 

|**Value**|**Description**|
|---|---|
|`Finger`|Fingerprints|
|`Face`|Face|
|`Iris`|Iris|
|`Vein`|Vein|
|`Signature`|Signature|
|`Gait`|Gait|
|`Retina`|Retina|
|`HandGeometry`|HandGeometry|
|`Voice`|Voice|
|`Palm`|Palm|
|`Other`|Other|



**Table 5.60** type.device.biometric.type Values 

Federal Office for Information Security 

36 

5 High Level Biometric Services API 

## 5.5.6.2 XSD Definition 

```
<xs:simpleTypename="type.device.biometric.type">
<xs:restrictionbase="xs:string">
<xs:enumerationvalue="Finger" />
<xs:enumerationvalue="Face" />
<xs:enumerationvalue="Iris" />
<xs:enumerationvalue="Vein" />
<xs:enumerationvalue="Signature" />
<xs:enumerationvalue="Gait" />
<xs:enumerationvalue="Retina" />
<xs:enumerationvalue="HandGeometry" />
<xs:enumerationvalue="Voice" />
<xs:enumerationvalue="Palm" />
<xs:enumerationvalue="Other" />
</xs:restriction>
</xs:simpleType>
```

## 5.5.7 type.device.properties 

## 5.5.7.1 Attributes 

None. 

## 5.5.7.2 Elements 

A list of one or more of the following elements: 

|**Element Name**|**Description**|
|---|---|
|`Boolean`|`hlbs:type.device.properties.boolean`<br>A Boolean device property value.|
|`Integer`|`hlbs:type.device.properties.integer`<br>An integer device property value.|
|`String`|`hlbs:type.device.properties.string`<br>A string device property value.|
|`Float`|`hlbs:type.device.properties.float`<br>A float device property value.|



**Table 5.61** type.device.properties Elements 

## 5.5.7.3 XSD Definition 

```
<xs:complexTypename="type.device.properties">
<xs:choiceminOccurs="1"maxOccurs="unbounded">
<xs:elementname="Boolean"type="hlbs:type.device.properties.boolean" />
<xs:elementname="Integer"type="hlbs:type.device.properties.integer" />
<xs:elementname="String"type="hlbs:type.device.properties.string" />
<xs:elementname="Float"type="hlbs:type.device.properties.float" />
</xs:choice>
</xs:complexType>
```

## 5.5.8 type.device.properties.base 

Base type that contains data which is shared among all device property values. 

## 5.5.8.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`id`|`xs:string`<br>The id of the device property value.|



**Table 5.62** type.configuration.base Attributes 

Federal Office for Information Security 

37 

5 High Level Biometric Services API 

## 5.5.8.2 Elements 

None. 

## 5.5.8.3 XSD Definition 

```
<xs:complexTypename="type.device.properties.base">
<xs:attributename="id"type="xs:string"use="required"/>
</xs:complexType>
```

## 5.5.9 type.device.properties.boolean 

A Boolean device property value. Derived from `hlbs:type.device.properties.base` . 

## 5.5.9.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`value`|`xs:boolean`<br>Value of this device property.|



**Table 5.63** type.device.properties.boolean Attributes 

## 5.5.9.2 Elements 

None. 

## 5.5.9.3 XSD Definition 

```
<xs:complexTypename="type.device.properties.boolean">
<xs:complexContent>
<xs:extensionbase="hlbs:type.device.properties.base">
<xs:attributename="value"type="xs:boolean"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.10 type.device.properties.integer 

An integer device property value. Derived from `hlbs:type.device.properties.base` . 

## 5.5.10.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`value`|`xs:integer`<br>Value of this device property.|



**Table 5.64** type.device.properties.integer Attributes 

## 5.5.10.2 Elements 

None. 

## 5.5.10.3 XSD Definition 

```
<xs:complexTypename="type.device.properties.integer">
<xs:complexContent>
<xs:extensionbase="hlbs:type.device.properties.base">
<xs:attributename="value"type="xs:integer"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.11 type.device.properties.string 

A string device property value. Derived from `hlbs:type.device.properties.base` . 

Federal Office for Information Security 

38 

5 High Level Biometric Services API 

## 5.5.11.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`value`|`xs:string`<br>Value of this device property.|



**Table 5.65** type.device.properties.string Attributes 

## 5.5.11.2 Elements 

None. 

## 5.5.11.3 XSD Definition 

```
<xs:complexTypename="type.device.properties.string">
<xs:complexContent>
<xs:extensionbase="hlbs:type.device.properties.base">
<xs:attributename="value"type="xs:string"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.12 type.device.properties.float 

A float device property value. Derived from `hlbs:type.device.properties.base` . 

## 5.5.12.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`value`|`xs:float`<br>Value of this device property.|



**Table 5.66** type.device.properties.float Attributes 

## 5.5.12.2 Elements 

None. 

## 5.5.12.3 XSD Definition 

```
<xs:complexTypename="type.device.properties.float">
<xs:complexContent>
<xs:extensionbase="hlbs:type.device.properties.base">
<xs:attributename="value"type="xs:float"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.13 type.configuration 

Provides information about all possible configuration values. 

## 5.5.13.1 Attributes 

None. 

## 5.5.13.2 Elements 

A list of one or more of the following elements: 

|**Element Name**|**Description**|
|---|---|
|`Boolean`|`hlbs:type.configuration.boolean`<br>A Boolean configuration value.|



Federal Office for Information Security 

39 

5 High Level Biometric Services API 

|**Element Name**|**Description**|
|---|---|
|`Integer`|`hlbs:type.configuration.integer`<br>An integer configuration value.|
|`String`|`hlbs:type.configuration.string`<br>A string configuration value.|
|`Float`|`hlbs:type.configuration.float`<br>A float configuration value.|
|`BiometricCode`|`hlbs:type.configuration.biometricCode`<br>A biometric code configuration value.|
|`BiometricCodeList`|`hlbs:type.configuration.biometricCodeList`<br>A list of biometric codes configuration value.|
|`BiometricImpression`|`hlbs:type.configuration.biometricImpression`<br>A biometric impression type configuration value.|
|`Image`|`hlbs:type.configuration.image`<br>An image configuration value.|
|`ImageList`|`hlbs:type.configuration.image`<br>An image list configuration value.|
|`DataFormat`|`hlbs:type.configuration.dataformat`<br>A data format value configuration value.|
|`Binary`|`hlbs:type.configuration.binary`<br>A binary data value configuration value.|



**Table 5.67** type.configuration Elements 

## 5.5.13.3 XSD Definition 

```
<xs:complexTypename="type.configuration">
```

```
<xs:choiceminOccurs="1"maxOccurs="unbounded">
```

- `<xs:element name=` **`"Boolean"`** `type=` **`"hlbs:type.configuration.boolean"`** `/>` 

- `<xs:element name=` **`"Integer"`** `type=` **`"hlbs:type.configuration.integer"`** `/>` 

- `<xs:element name=` **`"String"`** `type=` **`"hlbs:type.configuration.string"`** `/>` 

- `<xs:element name=` **`"Float"`** `type=` **`"hlbs:type.configuration.float"`** `/>` 

- `<xs:element name=` **`"BiometricCode"`** `type=` **`"hlbs:type.configuration.biometricCode"`** `/>` 

- `<xs:element name=` **`"BiometricCodeList"`** `type=` **`"hlbs:type.configuration.biometricCodeList"`** `/>` 

- `<xs:element name=` **`"BiometricImpression"`** `type=` **`"hlbs:type.configuration.biometricImpression"`** `/>` 

- `<xs:element name=` **`"Image"`** `type=` **`"hlbs:type.configuration.image"`** `/>` 

- `<xs:element name=` **`"ImageList"`** `type=` **`"hlbs:type.configuration.image"`** `/>` 

- `<xs:element name=` **`"DataFormat"`** `type=` **`"hlbs:type.configuration.dataformat"`** `/>` 

```
<xs:elementname="Binary"type="hlbs:type.configuration.binary" />
</xs:choice>
</xs:complexType>
```

## 5.5.14 type.configuration.base 

Base type that contains data which is shared among all configuration values. 

## 5.5.14.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`id`|`xs:string`<br>The id of the configuration value.|
|`mandatory?`|`xs:boolean`<br>If true, this configuration value SHALL be provided before the service execution starts. Default:<br>false|
|`modifiable?`|`xs:string`<br>Name of the service.|



Federal Office for Information Security 

40 

5 High Level Biometric Services API 

|**Attribute Name**|**Description**|
|---|---|
|`Version?`|`xs:boolean`<br>If true, this configuration value can be changed by the application. Otherwise the value is only<br>listed for information. Default: true|



**Table 5.68** type.configuration.base Attributes 

## 5.5.14.2 Elements 

None. 

## 5.5.14.3 XSD Definition 

```
<xs:complexTypename="type.configuration.base">
<xs:attributename="id"type="xs:string"use="required"/>
<xs:attributename="mandatory"type="xs:boolean"default="false" />
<xs:attributename="modifiable"type="xs:boolean"default="true" />
</xs:complexType>
```

## 5.5.15 type.configuration.boolean 

A Boolean configuration value. Derived from `hlbs:type.configuration.base` . 

## 5.5.15.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`default`|`xs:boolean`<br>Default value of this configuration entry which is used if the value is not overriden by the app<br>lication.|



**Table 5.69** type.configuration.boolean Attributes 

## 5.5.15.2 Elements 

None. 

## 5.5.15.3 XSD Definition 

```
<xs:complexTypename="type.configuration.boolean">
<xs:complexContent>
<xs:extensionbase="hlbs:type.configuration.base">
<xs:attributename="default"type="xs:boolean"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.16 type.configuration.integer 

An integer configuration value. Derived from `hlbs:type.configuration.base` . 

## 5.5.16.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`default`|`xs:integer`<br>Default value of this configuration entry which is used if the value is not overriden by the appli<br>cation.|
|`min?`|`xs:integer`<br>Minimal allowed value for this configuration value. If omitted, there is no lower limit..|
|`max?`|`xs:integer`<br>Maximal allowed value for this configuration value. If omitted, there is no upper limit.|



**Table 5.70** type.configuration.integer Attributes 

Federal Office for Information Security 

41 

5 High Level Biometric Services API 

## 5.5.16.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`AllowedValue*`|`xs:integer`<br>A list of allowed values (OPTIONAL).|



**Table 5.71** type.configuration.integer Elements 

## 5.5.16.3 XSD Definition 

```
<xs:complexTypename="type.configuration.integer">
<xs:complexContent>
<xs:extensionbase="hlbs:type.configuration.base">
<xs:sequence>
<xs:elementname="AllowedValue"type="xs:integer"minOccurs="0"maxOccurs="unbounded"/>
</xs:sequence>
<xs:attributename="default"type="xs:integer"use="required"/>
<xs:attributename="min"type="xs:integer"/>
<xs:attributename="max"type="xs:integer"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.17 type.configuration.string 

A string configuration value. Derived from `hlbs:type.configuration.base` . 

## 5.5.17.1 Attributes 

|**Attribute Name**<br>|**Description**|
|---|---|
|`default`<br><br> <br>|`xs:string`<br>Default value of this configuration entry which is used if the value is not overriden by the app<br>lication.|
|**Table 5.72**type.configuration.string Attributes<br>5.5.17.2 Elements||
|**Element Name**|**Description**|
|`AllowedValue*`|`xs:string`<br>A list of allowed values (OPTIONAL).|



**Table 5.73** type.configuration.string Elements 

## 5.5.17.3 XSD Definition 

```
<xs:complexTypename="type.configuration.string">
<xs:complexContent>
<xs:extensionbase="hlbs:type.configuration.base">
<xs:sequence>
<xs:elementname="AllowedValue"type="xs:string"minOccurs="0"maxOccurs="unbounded"/>
</xs:sequence>
<xs:attributename="default"type="xs:string"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.18 type.configuration.float 

A float configuration value. Derived from `hlbs:type.configuration.base` . 

Federal Office for Information Security 

42 

5 High Level Biometric Services API 

## 5.5.18.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`default`|`xs:float`<br>Default value of this configuration entry which is used if the value is not overriden by the app<br>lication.|
|`min?`|`xs:float`<br>Minimal allowed value for this configuration value. If omitted, there is no lower limit.|
|`max?`|`xs:float`<br>Maximal allowed value for this configuration value. If omitted, there is no upper limit.|



**Table 5.74** type.configuration.float Attributes 

## 5.5.18.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`AllowedValue*`|`xs:float`<br>A list of allowed values (OPTIONAL).|



**Table 5.75** type.configuration.float Elements 

## 5.5.18.3 XSD Definition 

```
<xs:complexTypename="type.configuration.float">
<xs:complexContent>
<xs:extensionbase="hlbs:type.configuration.base">
<xs:sequence>
<xs:elementname="AllowedValue"type="xs:float"minOccurs="0"maxOccurs="unbounded"/>
</xs:sequence>
<xs:attributename="default"type="xs:float"use="required"/>
<xs:attributename="min"type="xs:float"/>
<xs:attributename="max"type="xs:float"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.19 type.iso19794FingerImpressionType 

An impression type as defined in [BIB_ISO_19794_FINGER] (e.g. finger or palm). Derived from `xs:unsignedInt` . 

## 5.5.19.1 Format Restrictions 

The same restrictions as Section 5.2.5 in apply. 

## 5.5.19.2 XSD Definition 

```
<xs:simpleTypename="type.iso19794FingerImpressionType">
<xs:restrictionbase="xs:unsignedInt">
<xs:patternvalue="[0-9]|1[0-9]|2[0-9]"/>
</xs:restriction>
</xs:simpleType>
```

## 5.5.20 type.iso19794FingerCode 

A code as defined in [BIB_ISO_19794_FINGER] (e.g. finger or palm). Derived from `xs:unsignedInt` . 

## 5.5.20.1 Format Restrictions 

The same restrictions as in Section 5.2.6 apply. 

## 5.5.20.2 XSD Definition 

```
<xs:simpleTypename="type.iso19794FingerCode">
<xs:restrictionbase="xs:unsignedInt">
```

Federal Office for Information Security 

43 

5 High Level Biometric Services API 

```
<xs:patternvalue="[0-9]|10|1[3-5]|2[0-9]|3[0-6]|4[0-9]|50"/>
</xs:restriction>
</xs:simpleType>
```

## 5.5.21 type.iso19794FaceImageType 

A face image type as defined in [BIB_ISO_19794_FACE]. Derived from `xs:unsignedInt` . 

## 5.5.21.1 Format Restrictions 

The same restrictions as in Section 5.2.7 apply. 

## 5.5.21.2 XSD Definition 

```
<xs:simpleTypename="type.iso19794FaceImageType">
<xs:restrictionbase="xs:unsignedInt">
<xs:minInclusivevalue="0"/>
<xs:maxInclusivevalue="255"/>
</xs:restriction>
</xs:simpleType>
```

## 5.5.22 type.iso19794IrisCode 

A iris code as defined in [BIB_ISO_IRIS]. Derived from `xs:unsignedInt` . 

## 5.5.22.1 Format Restrictions 

The same restrictions as in Section 5.2.8 apply. 

## 5.5.22.2 XSD Definition 

```
<xs:simpleTypename="type.iso19794IrisCode">
<xs:restrictionbase="xs:unsignedInt">
<xs:minInclusivevalue="0"/>
<xs:maxInclusivevalue="2"/>
</xs:restriction>
</xs:simpleType>
```

## 5.5.23 type.biometricImpression 

A biometric impression type. 

## 5.5.23.1 Attributes 

None. 

## 5.5.23.2 Elements 

One of the following elements: 

|**Element Name**|**Description**|
|---|---|
|`FingerImpression`|`hlbs:type.iso19794FingerImpressionType`<br>A finger impression type (may also contain a palm).|



**Table 5.76** type.biometricImpression Elements 

## 5.5.23.3 XSD Definition 

```
<xs:complexTypename="type.biometricImpression">
<xs:choice>
<xs:elementname="FingerImpression"type="hlbs:type.iso19794FingerImpressionType"/>
</xs:choice>
</xs:complexType>
```

Federal Office for Information Security 

44 

5 High Level Biometric Services API 

## 5.5.24 type.configuration.biometricImpression 

A biometric impression type configuration value. Derived from `hlbs:type.configuration.base` . 

## 5.5.24.1 Attributes 

None. 

## 5.5.24.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`Default`|`hlbs:type.biometricImpression`<br>Default value of this configuration entry which is used if the value is not overriden by the application.|
|`Allowed*`|`hlbs:type.biometricImpression`<br>List of allowed values. If omitted, all values are allowed.|



**Table 5.77** type.configuration.biometricImpression Elements 

## 5.5.24.3 XSD Definition 

```
<xs:complexTypename="type.configuration.biometricImpression">
<xs:complexContent>
<xs:extensionbase="hlbs:type.configuration.base">
<xs:sequence>
```

```
<xs:elementname="Default"type="hlbs:type.biometricImpression"minOccurs="1"maxOccurs="1"/>
<xs:elementname="Allowed"type="hlbs:type.biometricImpression"minOccurs="0"
maxOccurs="unbounded"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.25 type.biometricCode 

A biometric code. 

## 5.5.25.1 Attributes 

None. 

## 5.5.25.2 Elements 

One of the following elements: 

|**Element Name**|**Description**|
|---|---|
|`FingerCode`|`hlbs:type.iso19794FingerCode`<br>A finger code (may also contain a palm code).|
|`FaceImageType`|`hlbs:type.iso19794FaceImageType`<br>A face image type.|
|`IrisCode`|`hlbs:type.iso19794IrisCode`<br>An iris code.|



**Table 5.78** type.biometricCode Elements 

## 5.5.25.3 XSD Definition 

```
<xs:complexTypename="type.biometricCode">
<xs:choice>
<xs:elementname="FingerCode"type="hlbs:type.iso19794FingerCode"/>
<xs:elementname="FaceImageType"type="hlbs:type.iso19794FaceImageType"/>
<xs:elementname="IrisCode"type="hlbs:type.iso19794IrisCode"/>
</xs:choice>
</xs:complexType>
```

Federal Office for Information Security 

45 

5 High Level Biometric Services API 

## 5.5.26 type.configuration.biometricCode 

A biometric code configuration value. Derived from `hlbs:type.configuration.base` . 

## 5.5.26.1 Attributes 

None. 

## 5.5.26.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`Default`|`hlbs:type.biometricCode`<br>Default value of this configuration entry which is used if the value is not overriden by the applicati<br>on.|
|`Allowed*`|`hlbs:type.biometricCode`<br>List of allowed values. If omitted, all values are allowed.|



**Table 5.79** type.configuration.biometricCode Elements 

## 5.5.26.3 XSD Definition 

```
<xs:complexTypename="type.configuration.biometricCode">
<xs:complexContent>
<xs:extensionbase="hlbs:type.configuration.base">
<xs:sequence>
<xs:elementname="Default"type="hlbs:type.biometricCode"minOccurs="1"maxOccurs="1"/>
```

```
<xs:elementname="Allowed"type="hlbs:type.biometricCode"minOccurs="0"maxOccurs="unbounded"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.27 type.configuration.biometricCodeList 

A biometric code list configuration value. Derived from `hlbs:type.configuration.base` . 

## 5.5.27.1 Attributes 

None. 

## 5.5.27.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`Default*`|`hlbs:type.biometricCode`<br>Default value of this configuration entry which is used if the value is not overriden by the applicati<br>on.|



**Table 5.80** type.configuration.biometricCodeList Elements 

## 5.5.27.3 XSD Definition 

```
<xs:complexTypename="type.configuration.biometricCodeList">
<xs:complexContent>
<xs:extensionbase="hlbs:type.configuration.base">
<xs:sequence>
```

```
<xs:elementname="Default"type="hlbs:type.biometricCode"minOccurs="0"maxOccurs="unbounded"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

Federal Office for Information Security 

46 

5 High Level Biometric Services API 

## 5.5.28 type.configuration.dataformat 

A data format configuration value. Derived from `hlbs:type.configuration.base` . 

## 5.5.28.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`default`|`hlbs:type.dataformat`<br>Default value of this configuration entry which is used if the value is not overriden by the applica<br>tion.|



**Table 5.81** type.configuration.dataformat Attributes 

## 5.5.28.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`AllowedValue*`|`hlbs:DataFormat`<br>A list of allowed values (OPTIONAL).|



**Table 5.82** type.configuration.dataformat Elements 

## 5.5.28.3 XSD Definition 

```
<xs:complexTypename="type.configuration.dataformat">
<xs:complexContent>
```

```
<xs:extensionbase="hlbs:type.configuration.base">
```

```
<xs:sequence>
```

```
<xs:elementname="AllowedValue"type="hlbs:type.dataformat"minOccurs="0"maxOccurs="unbounded"/
>
```

```
</xs:sequence>
<xs:attributename="default"type="hlbs:type.dataformat"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.29 type.dataformat 

A data format. Derived from `xs:string` . 

## 5.5.29.1 Values 

No restrictions. For a list of currently supported formats see Section 5.2.9. 

## 5.5.29.2 XSD Definition 

```
<xs:simpleTypename="type.dataformat">
<xs:restrictionbase="xs:string" />
</xs:simpleType>
```

## 5.5.30 type.configuration.image 

An image configuration value. Derived from `hlbs:type.configuration.base` . 

## 5.5.30.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`format`|`hlbs:type.dataformat`<br>The REQUIRED dataformat of the image.|



**Table 5.83** type.configuration.image Attributes 

## 5.5.30.2 Elements 

None. 

Federal Office for Information Security 

47 

5 High Level Biometric Services API 

## 5.5.30.3 XSD Definition 

```
<xs:complexTypename="type.configuration.image">
<xs:complexContent>
<xs:extensionbase="hlbs:type.configuration.base">
<xs:attributename="format"type="hlbs:type.dataformat"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.31 type.configuration.binary 

A binary configuration value. Derived from `hlbs:type.configuration.base` . 

## 5.5.31.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`format`|`hlbs:type.dataformat`<br>The REQUIRED dataformat of the binary data.|



**Table 5.84** type.configuration.binary Attributes 

## 5.5.31.2 Elements 

None. 

## 5.5.31.3 XSD Definition 

```
<xs:complexTypename="type.configuration.binary">
<xs:complexContent>
<xs:extensionbase="hlbs:type.configuration.base">
<xs:attributename="format"type="hlbs:type.dataformat"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.32 type.user.commands 

Provides information about all possible user commands that can be send to the service. 

## 5.5.32.1 Attributes 

None. 

## 5.5.32.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`UserCommand+`|`hlbs:type.user.command`<br>A list of possible user commands.|



**Table 5.85** type.user.commands Elements 

## 5.5.32.3 XSD Definition 

```
<xs:complexTypename="type.user.commands">
<xs:sequence>
<xs:elementname="UserCommand"type="hlbs:type.user.command"minOccurs="1"maxOccurs="unbounded"/
>
</xs:sequence>
</xs:complexType>
```

## 5.5.33 type.user.command 

A user command. 

Federal Office for Information Security 

48 

5 High Level Biometric Services API 

## 5.5.33.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`id`|`xs:string`<br>The ID of the user command.|
|`mandatory`|`xs:boolean`<br>If true, this user command SHALL be supported by the application because otherwise the service<br>won't be able to work. Default: false|



**Table 5.86** type.user.command Attributes 

## 5.5.33.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`Configuration*`|`hlbs:type.configuration`<br>A list of configuration values allowed for this user command (if available).|



**Table 5.87** type.user.command Elements 

## 5.5.33.3 XSD Definition 

```
<xs:complexTypename="type.user.command">
<xs:sequence>
```

```
<xs:elementname="Configuration"type="hlbs:type.configuration"minOccurs="0"maxOccurs="1"/>
</xs:sequence>
<xs:attributename="id"type="xs:string"use="required" />
<xs:attributename="mandatory"type="xs:boolean"default="false"/>
</xs:complexType>
```

## 5.5.34 type.feedback 

Provides information about all possible feedback elements that can be provided by the service. The following table provides the mapping of feedback elements in the service description to the elements which SHALL be used in the SOAP-API feedback type defined in Section 5.2.23. There is no one-to-one mapping, because the elements in the description focus on their semantic meanings while the types in the SOAP API are reduced to the technical minimum. 

|**Feedback-Element in Description**|**Feedback-Element in SOAP-API**|
|---|---|
|`Boolean`|`boolValue`|
|`Integer`|`intValue`|
|`Float`|`floatValue`|
|`FloatList`|`floatListValue`|
|`BiometricCode`|`biometricCodeValue`|
|`BiometricCodeList`|`biometricCodeListValue`|
|`Binary`|`binaryValue`|
|`Image`|`imageValue`|
|`ImageList`|`imageListValue`|
|`Progress`|`intValue`|
|`Icon`|`stringValue`|
|`Icons`|`stringListValue`|
|`Text`|`stringValue`|
|`XML`|`stringValue`|
|`Score`|`floatValue`|



**Table 5.88** Feedback-Element Mapping 

Federal Office for Information Security 

49 

5 High Level Biometric Services API 

Icons and text SHALL be represented by Ids instead of binary data, because the service only defines the process and the application SHALL define the concrete look and feel and localisation. 

## 5.5.34.1 Attributes 

None. 

## 5.5.34.2 Elements 

A list of one or more of the following elements: 

|**Element Name**|**Description**|
|---|---|
|`Boolean`|`hlbs:type.feedback.boolean`<br>A Boolean feedback element.|
|`Integer`|`hlbs:type.feedback.integer`<br>An integer feedback element.|
|`Float`|`hlbs:type.feedback.float`<br>An float feedback element.|
|`FloatList`|`hlbs:type.feedback.floatList`<br>An float list feedback element.|
|`BiometricCode`|`hlbs:type.feedback.biometricCode`<br>A biometric code feedback element.|
|`BiometricCodeList`|`hlbs:type.feedback.biometricCodeList`<br>A biometric code list feedback element.|
|`Binary`|`hlbs:type.feedback.binary`<br>A binary data feedback element.|
|`Image`|`hlbs:type.feedback.image`<br>An image feedback element.|
|`ImageList`|`hlbs:type.feedback.image`<br>An image list feedback element.|
|`Progress`|`hlbs:type.feedback.progress`<br>A progress feedback element.|
|`Icon`|`hlbs:type.feedback.icon`<br>An icon feedback element.|
|`Icons`|`hlbs:type.feedback.icons`<br>An icon list feedback element.|
|`Text`|`hlbs:type.feedback.text`<br>A text feedback element.|
|`XML`|`hlbs:type.feedback.xml`<br>An XML feedback element.|
|`Score`|`hlbs:type.feedback.score`<br>A score feedback element.|



**Table 5.89** type.feedback Elements 

## 5.5.34.3 XSD Definition 

```
<xs:complexTypename="type.feedback">
```

```
<xs:choiceminOccurs="1"maxOccurs="unbounded">
```

```
<xs:elementname="Boolean"type="hlbs:type.feedback.boolean" />
```

```
<xs:elementname="Integer"type="hlbs:type.feedback.integer" />
```

- `<xs:element name=` **`"Float"`** `type=` **`"hlbs:type.feedback.float"`** `/>` 

- `<xs:element name=` **`"FloatList"`** `type=` **`"hlbs:type.feedback.floatList"`** `/>` 

- `<xs:element name=` **`"BiometricCode"`** `type=` **`"hlbs:type.feedback.biometricCode"`** `/>` 

- `<xs:element name=` **`"BiometricCodeList"`** `type=` **`"hlbs:type.feedback.biometricCodeList"`** `/>` 

- `<xs:element name=` **`"Binary"`** `type=` **`"hlbs:type.feedback.binary"`** `/>` 

- `<xs:element name=` **`"Image"`** `type=` **`"hlbs:type.feedback.image"`** `/>` 

- `<xs:element name=` **`"ImageList"`** `type=` **`"hlbs:type.feedback.image"`** `/>` 

- `<xs:element name=` **`"Progress"`** `type=` **`"hlbs:type.feedback.progress"`** `/>` 

Federal Office for Information Security 

50 

5 High Level Biometric Services API 

```
<xs:elementname="Icon"type="hlbs:type.feedback.icon" />
```

```
<xs:elementname="Icons"type="hlbs:type.feedback.icons" />
```

```
<xs:elementname="Text"type="hlbs:type.feedback.text" />
```

```
<xs:elementname="XML"type="hlbs:type.feedback.xml" />
<xs:elementname="Score"type="hlbs:type.feedback.score" />
</xs:choice>
</xs:complexType>
```

## 5.5.35 type.feedback.base 

Base type that contains data which is shared among all feedback elements. 

## 5.5.35.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`id`|`xs:string`<br>The id of the feedback element.|
|`mandatory?`|`xs:boolean`<br>If true, this feedback element SHALL be supported by the application because its display is con<br>sidered critical for the process. Default: false|



**Table 5.90** type.feedback.base Attributes 

## 5.5.35.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`Configuration?`|`hlbs:type.configuration`<br>Possible configuration values for this feedback element (if available).|



**Table 5.91** type.feedback.base Elements 

## 5.5.35.3 XSD Definition 

```
<xs:complexTypename="type.feedback.base">
<xs:sequence>
<xs:elementname="Configuration"type="hlbs:type.configuration"minOccurs="0"maxOccurs="1"/>
</xs:sequence>
<xs:attributename="id"type="xs:string"use="required" />
<xs:attributename="mandatory"type="xs:boolean"default="false"/>
</xs:complexType>
```

## 5.5.36 type.feedback.boolean 

A Boolean feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.36.1 Attributes 

None. 

## 5.5.36.2 Elements 

None. 

## 5.5.36.3 XSD Definition 

```
<xs:complexTypename="type.feedback.boolean">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.37 type.feedback.integer 

An integer feedback element. Derived from `hlbs:type.feedback.base` . 

Federal Office for Information Security 

51 

5 High Level Biometric Services API 

## 5.5.37.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`min?`|`xs:int`<br>Minimal possible returned value. If omitted, there is no lower limit.|
|`max?`|`xs:int`<br>Maximal possible returned value. If omitted, there is no upper limit.|



**Table 5.92** type.feedback.integer Attributes 

## 5.5.37.2 Elements 

None. 

## 5.5.37.3 XSD Definition 

```
<xs:complexTypename="type.feedback.integer">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:attributename="min"type="xs:int"/>
<xs:attributename="max"type="xs:int"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.38 type.feedback.float 

A float feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.38.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`min?`|`xs:float`<br>Minimal possible returned value. If omitted, there is no lower limit.|
|`max?`|`xs:float`<br>Maximal possible returned value. If omitted, there is no upper limit.|



**Table 5.93** type.feedback.float Attributes 

## 5.5.38.2 Elements 

None. 

## 5.5.38.3 XSD Definition 

```
<xs:complexTypename="type.feedback.float">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:attributename="min"type="xs:float"/>
<xs:attributename="max"type="xs:float"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.39 type.feedback.floatList 

A float list feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.39.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`min?`|`xs:float`<br>Minimal possible returned value. If omitted, there is no lower limit.|



Federal Office for Information Security 

52 

5 High Level Biometric Services API 

|**Attribute Name**|**Description**|
|---|---|
|`max?`|`xs:float`<br>Maximal possible returned value. If omitted, there is no upper limit.|



**Table 5.94** type.feedback.floatList Attributes 

## 5.5.39.2 Elements 

None. 

## 5.5.39.3 XSD Definition 

```
<xs:complexTypename="type.feedback.floatList">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:attributename="min"type="xs:float"/>
<xs:attributename="max"type="xs:float"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.40 type.feedback.biometricCode 

A biometric code feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.40.1 Attributes 

None. 

## 5.5.40.2 Elements 

None. 

## 5.5.40.3 XSD Definition 

```
<xs:complexTypename="type.feedback.biometricCode">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.41 type.feedback.biometricCodeList 

A biometric code list feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.41.1 Attributes 

None. 

## 5.5.41.2 Elements 

None. 

## 5.5.41.3 XSD Definition 

```
<xs:complexTypename="type.feedback.biometricCodeList">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.42 type.feedback.binary 

A binary data feedback element. Derived from `hlbs:type.feedback.base` . 

Federal Office for Information Security 

53 

5 High Level Biometric Services API 

## 5.5.42.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`format?`|`hlbs:type.dataformat`<br>Format of the provided binary data.|



**Table 5.95** type.feedback.binary Attributes 

## 5.5.42.2 Elements 

None. 

## 5.5.42.3 XSD Definition 

```
<xs:complexTypename="type.feedback.binary">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:attributename="format"type="hlbs:type.dataformat"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.43 type.feedback.image 

An image data feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.43.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`format?`|`hlbs:type.dataformat`<br>Format of the provided image data.|
|`width?`|`xs:unsignedInt`<br>Width of the provided image.|
|`height?`|`xs:unsignedInt`<br>Height of the provided image.|



**Table 5.96** type.feedback.image Attributes 

## 5.5.43.2 Elements 

None. 

## 5.5.43.3 XSD Definition 

```
<xs:complexTypename="type.feedback.image">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:attributename="format"type="hlbs:type.dataformat"/>
<xs:attributename="width"type="xs:unsignedInt"/>
<xs:attributename="height"type="xs:unsignedInt"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.44 type.feedback.progress 

A progress feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.44.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`min?`|`xs:unsignedInt`<br>Minimal possible returned value. If omitted, there is no lower limit.|



Federal Office for Information Security 

54 

5 High Level Biometric Services API 

|**Attribute Name**|**Description**|
|---|---|
|`max?`|`xs:unsignedInt`<br>Maximal possible returned value. If omitted, there is no upper limit.|



**Table 5.97** type.feedback.progress Attributes 

## 5.5.44.2 Elements 

None. 

## 5.5.44.3 XSD Definition 

```
<xs:complexTypename="type.feedback.progress">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:attributename="min"type="xs:unsignedInt"use="required"/>
<xs:attributename="max"type="xs:unsignedInt"use="required"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.45 type.feedback.icon 

An icon feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.45.1 Attributes 

None. 

## 5.5.45.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`PossibleValue*`|`xs:string`<br>Possible provided values for this feedback element.|



**Table 5.98** type.feedback.icon Elements 

## 5.5.45.3 XSD Definition 

```
<xs:complexTypename="type.feedback.icon">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:sequence>
<xs:elementname="PossibleValue"type="xs:string"minOccurs="0"maxOccurs="unbounded"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.46 type.feedback.icons 

An icon list feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.46.1 Attributes 

None. 

## 5.5.46.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`PossibleValue*`|`xs:string`<br>Possible provided values for this feedback element.|



**Table 5.99** type.feedback.icons Elements 

Federal Office for Information Security 

55 

5 High Level Biometric Services API 

## 5.5.46.3 XSD Definition 

```
<xs:complexTypename="type.feedback.icons">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:sequence>
<xs:elementname="PossibleValue"type="xs:string"minOccurs="0"maxOccurs="unbounded"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.47 type.feedback.text 

A text feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.47.1 Attributes 

None. 

## 5.5.47.2 Elements 

|**Element Name**|**Description**|
|---|---|
|`PossibleValue*`|`xs:string`<br>Possible provided values for this feedback element.|



**Table 5.100** type.feedback.text Elements 

## 5.5.47.3 XSD Definition 

```
<xs:complexTypename="type.feedback.text">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:sequence>
<xs:elementname="PossibleValue"type="xs:string"minOccurs="0"maxOccurs="unbounded"/>
</xs:sequence>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.48 type.feedback.xml 

An XML feedback element. Derived from `hlbs:type.feedback.base` . 

## 5.5.48.1 Attributes 

None. 

## 5.5.48.2 Elements 

None. 

## 5.5.48.3 XSD Definition 

```
<xs:complexTypename="type.feedback.xml">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

## 5.5.49 type.feedback.score 

A score feedback element. Derived from `hlbs:type.feedback.base` . 

Federal Office for Information Security 

56 

5 High Level Biometric Services API 

## 5.5.49.1 Attributes 

|**Attribute Name**|**Description**|
|---|---|
|`min?`|`xs:float`<br>Minimal possible returned value. If omitted, there is no lower limit.|
|`max?`|`xs:float`<br>Maximal possible returned value. If omitted, there is no upper limit.|



**Table 5.101** type.feedback.score Attributes 

## 5.5.49.2 Elements 

None. 

## 5.5.49.3 XSD Definition 

```
<xs:complexTypename="type.feedback.score">
<xs:complexContent>
<xs:extensionbase="hlbs:type.feedback.base">
<xs:attributename="min"type="xs:float"/>
<xs:attributename="max"type="xs:float"/>
</xs:extension>
</xs:complexContent>
</xs:complexType>
```

Federal Office for Information Security 

57 

6 Example (Non-Normative) 

## 6 Example (Non-Normative) 

## 6.1 Service-Device Description 

This section presents an example of a simple service-device-description. 

```
<?xml version="1.0" encoding="utf-8"?>
<ServiceschemaVersion="1"xmlns="http://trbio.bsi.bund.de/hlbs/1">
<Information>
<Id>301678f1-6c9e-442d-827b-f3ba2cd67cba</Id>
<Vendor>Example Vendor</Vendor>
<Name>Capture Service</Name>
<Version>1.1</Version>
<Description>Generic Capture Service</Description>
<Type>Enrolment</Type>
<Device>
<Id>979d3850-1e32-42ae-a209-1693675600ad</Id>
<Vendor>Example Vendor</Vendor>
<Name>Fingerprint Scanner</Name>
<BiometricType>Finger</BiometricType>
</Device>
</Information>
```

This service can be used for enrolment and uses a fingerprint scanner. 

```
<Configuration>
<Integerid="TimeoutMs"default="0"/>
</Configuration>
```

One value that can be configured is the timeout after which the service execution automatically stops if not hing has been captured until then. The default value of 0 indicates by convention that the service normally doesn't automatically stop after a certain time. 

```
<UserCommands>
<UserCommandid="Cancel"/>
<UserCommandid="ManualCapture"/>
</UserCommands>
```

During the execution of the service the commands "Cancel" and "ManualCapture" are allowed. 

```
<FeedbackElements>
<Imageid="LiveImage">
<Configuration>
<DataFormatid="LiveImage.Format"default="bmp"modifiable="true" />
</Configuration>
</Image>
<Textid="State">
<PossibleValue>CAPTURE</PossibleValue>
<PossibleValue>ERROR_CAPTURE_FAILED</PossibleValue>
</Text>
</FeedbackElements>
```

The service provides live images via the feedback id "LiveImage". The format of the live image is "bmp" by de fault but this format can be changed by setting a different value for the configuration key "LiveImage.Format". Furthermore the service reports its state through a text element with id "State" which can be either "CAPTU RE" or "ERROR_CAPTURE_FAILED". 

```
<Results>
<Imageid="ResultImage">
<Configuration>
<DataFormatid="ResultImage.Format"default="bmp"modifiable="true" />
</Configuration>
```

Federal Office for Information Security 

58 

6 Example (Non-Normative) 

```
</Image>
</Results>
</Service>
```

As result the service returns the captured image with format "bmp" by default. The result format can be chan ged by setting a value for the configuration key "ResultImage.Format". 

Federal Office for Information Security 

59 

7 Client-Server Connection Scenarios 

## 7 Client-Server Connection Scenarios 

Two connection scenarios exist regarding the connection between client and server. Both scenarios are intro duced in the following sections. The logical architecture is depicted in Figure 7.1. Within this architecture the HLBS represents the interface between the middleware and the application with two physical connection scenarios described hereafter. 


![](markdown/tr/TR-03121-2-2_Biometrics_7_0/TR-03121-2-2_Biometrics_7_0.pdf-0066-03.png)


**Figure 7.1.** HLBS Architecture 

## 7.1 Connection via TCP/IP 

In the Transmission Control Protocol/Internet Protocol (TCP/IP) connection scenario the system that is using HLBS is one autarkic unit that is connected via an ethernet cable with the client computer. This architecture is also shown in Figure 7.2. Whether the connection is established directly or indirectly via one or multiple switches does not matter here. However, if the connection via TCP/IP is chosen, the following configuration SHALL be possible within the unit without the need of calling the `configureService` operation: 

- customizable device name 

- Dynamic Host Configuration Protocol (DHCP) and manual mode 

- Internet Protocol Version 4 (IPv4) and Internet Protocol Version 6 (IPv6) configuration 

- subnet configuration 

- Transport Layer Security (TLS) 1.2 end-to-end encryption between client and server 

- mutual client and server authentication 

- customizable port on which the HLBS runs 

Federal Office for Information Security 

60 

7 Client-Server Connection Scenarios 


![](markdown/tr/TR-03121-2-2_Biometrics_7_0/TR-03121-2-2_Biometrics_7_0.pdf-0067-01.png)


**----- Start of picture text -----**<br>
C lie n t P C<br>HLBS Client<br>TCP/IP<br>HLBS Device<br>HLBS Service<br>«im plem ents» «im plem ents»<br>HLBS API HLBS Service Denition<br>Middleware<br>Device Driver<br>Capture Device<br>**----- End of picture text -----**<br>


**Figure 7.2.** Architecture via TCP/IP 

## 7.2 Connection via USB 

In the Universal Serial Bus (USB) connection scenario the system that is using HLBS is split into two compo nents. The first component is the actual unit which processes the request (e.g. acquisition of a facial image). This unit is connected via an USB-cable to the client computer where the second component of the system resides. The component on the client computer acts as a driver and implements the HLBS. This architecture is also shown in Figure 7.3. The component on the client computer SHALL have support for configuring the port on which the HLBS runs without the need to call `configureService` . The set port SHALL only be available as loopback interface. 

Federal Office for Information Security 

61 

7 Client-Server Connection Scenarios 


![](markdown/tr/TR-03121-2-2_Biometrics_7_0/TR-03121-2-2_Biometrics_7_0.pdf-0068-01.png)


**----- Start of picture text -----**<br>
C lie n t P C<br>HLBS Client<br>HLBS Service<br>«im plem ents» «im plem ents»<br>HLBS API HLBS Service Denition<br>Middleware<br>Device Driver<br>U S B<br>Device<br>Capture Device<br>**----- End of picture text -----**<br>


**Figure 7.3.** Architecture via USB 

Federal Office for Information Security 

62 

8 Service Definitions 

## 8 Service Definitions 

Due to the generic structure of HLBS (e.g. support for custom user commands implemented by developers) it is necessary to define Service Definitions. These Service Definitions show different characteristics for each individual service including their minimum requirements. 

## 8.1 Service Definition Facial Image Acquisition System 

This Service Definition specifies requirements for a Facial Image Acqisition System (FIAS) that implements HLBS as communication interface. 

There are two operation modes that SHALL be supported by the FIAS. These modes are the automated mode and the manual mode. Both modes SHALL be implemented within the following service definition. 

## 8.1.1 ServiceInformation 

When the `getAllServices` operation is requested at least the `ServiceInformation` shown in Table 8.1 SHALL be returned. Further parameters are vendor specific and SHALL be set as well. 

|**Parameter ID**|**Description**|**Type**|**Value**|
|---|---|---|---|
|`Id`|Unique UUID of the service.|`xsd:`<br>`string`|`1411ad9f-58e6-4d3c-`<br>`816d-7fe9d7b67336`|
|`Name`|Name of the service.|`xsd:`<br>`string`|`Facial Image Acquisition`<br>`System`|
|`Version`|Version of BSI TR-03121 of<br>the implemented service.|`xsd:`<br>`string`|`7.0`|



**Table 8.1** FIAS ServiceInformation 

## 8.1.2 Configuration 

At least the configuration options listed in Table 8.2 SHALL be available for the `configureService` ope ration. These configuration options including their allowed and default values SHALL also be part of the `ser viceDescriptionXML` that is returned with the `getServiceDescription` operation. 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Purpose`|The purpose of the facial<br>image acquisition.|`hlbs:`<br>`ServiceType`|`enrolment`,<br>`identification`,<br>`verification`,<br>`other` _(e.g. purpose is ambi_<br>_guous)_|
|`ApplicationProfile`|Relevant Application Profile<br>to be used for the acquisition<br>process and its results.|`hlbs:`<br>`Application`<br>`Profile`|_Choice of the implemen_<br>_ted Application Profiles (e.g._<br>`BCL_`<br>`ManualBorderControl`_)_|
|`InitialVerticalPosition`|Sets the initial absolute ver<br>tical position of the camera's<br>field of view. In case a mul<br>ti camera solution is used, it<br>SHALL NOT be possible to<br>set the camera's field of view<br>to a position where a merge<br>image of two or more came<br>ras is created.|`xsd:float`|Range:`[0, ..., 1]`<br>Lowest position:`0`<br>Middle position:`0.5`<br>Highest position:`1`|
|`InitialIlluminationLevel`|Sets the initial absolute illu<br>mination brightness.|`xsd:float`|Range:`[0, ..., 1]`<br>Lowest position:`0`<br>Middle position:`0.5`<br>Highest position:`1`|



Federal Office for Information Security 

63 

8 Service Definitions 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`InitialOperationMode`|Sets the operation mode that<br>SHALL be used, once the ser<br>vice has been started.|`xsd:string`|`automated`,`manual`|
|`TimeOut`|Sets the timeout for acquisi<br>tions in milliseconds for the<br>automated operation mode.|`xsd:int`|_Arbitrary Value_<br>Default:`0`(no timeout)|



**Table 8.2** FIAS Configuration 

## 8.1.3 User Commands 

When the `signalUserCommand` operation is executed the user commands shown in Table 8.3 SHALL be supported in case the existence column is set to REQUIRED and MAY be supported in case the existence co lumn is set to OPTIONAL. Conditional commands SHALL only be available if the manual operation mode is in use, except for the `CropManually` , `acceptImage` and `rejectImage` command. In case a user command is not al lowed at a certain point of time during the execution of the service the user SHALL be informed via the `ge tServiceFeedback` operation. The user commands of Table 8.3 SHALL also be present within the `serviceDe scriptionXML` that is returned with the `getServiceDescription` operation. 

|**Parameter ID**|**M/O/C1**|**Description**|**Name and type**|**Possible Values**|
|---|---|---|---|---|
|`Cancel`|M|Abort/Terminate a running<br>capture.|-|-|
|`Capture`|M/C|Force capturing the current<br>ly showing camera's field of<br>view. This overrules the re<br>sult of a live-QA. This com<br>mand SHALL only usable<br>when the live image is visible<br>during the capture process.|-|-|
|`SwitchMode`|M/C|Allows the switch between<br>the manual and automated<br>operation mode. This com<br>mand SHALL only usable<br>when the live image is visible<br>during the capture process.|-|-|
|`Trigger`<br>`AutoFocus`|C|Manual (anew) usage of the<br>auto focus of the camera in<br>order to focus a face positio<br>ned infront of the camera.<br>This command SHALL only<br>be available in manual mode.|-|-|
|`SetManual`<br>`FocusPoint`|C|Sets the focus of the camera's<br>field of view to the given ab<br>solute focus distance in cm.<br>This command SHALL only<br>be available in manual mode.|Focus<br>`xsd:float`|Range:`[40, ...,`<br>`100]`<br>Nearest focus:`40`cm<br>Farest focus:`100`cm|
|`TriggerAuto`<br>`Height`<br>`Adjustment`|C|Manual (anew) usage of the<br>auto height adjustment. The<br>camera's field of view will be<br>adjusted according to the bo<br>dy height of the traveler, so<br>that the traveler's face is well-<br>seen in the camera's field of<br>view. This command SHALL<br>only be available in manual<br>mode.|-|-|



> 1 Mandatory / Optional / Conditional 

Federal Office for Information Security 

64 

8 Service Definitions 

|**Parameter ID**|**M/O/C1**|**Description**|**Name and type**|**Possible Values**|
|---|---|---|---|---|
|`SetVertical`<br>`Position`|C|Sets the absolute vertical po<br>sition of the camera's field of<br>view. In case a multi came<br>ra solution is used, it SHALL<br>NOT be possible to set the ca<br>mera's field of view to a posi<br>tion where a merge image of<br>two or more cameras is crea<br>ted. This command SHALL<br>only be available in manual<br>mode.|Position<br>`xsd:float`|Range:`[0, ..., 1]`<br>Lowest position:`0`<br>Middle position:`0.5`<br>Highest position:`1`|
|`Increment`<br>`Vertical`<br>`Position`|C|Stepwise increment the ver<br>tical position of the came<br>ra's field of view by the defi<br>ned value in cm, maximum<br>to the highest position. In ca<br>se a multi camera solution is<br>used, it SHALL NOT be pos<br>sible to set the camera's field<br>of view to a position where a<br>merge image of two or more<br>cameras is created. This com<br>mand SHALL only be avail<br>able in manual mode.|Step<br>`xsd:int`|_Arbitrary Value_|
|`Decrement`<br>`Vertical`<br>`Position`|C|Stepwise decrement the ver<br>tical position of the came<br>ra's field of view by the defi<br>ned value in cm, maximum<br>to the lowest position. In ca<br>se a multi camera solution is<br>used, it SHALL NOT be pos<br>sible to set the camera's field<br>of view to a position where a<br>merge image of two or more<br>cameras is created. This com<br>mand SHALL only be avail<br>able in manual mode.|Step<br>`xsd:int`|_Arbitrary Value_|
|`SetAbsolute`<br>`Illumination`<br>`Level`|C|Set the absolute face illumi<br>nation-brightness. This com<br>mand SHALL only be avail<br>able in manual mode.|Level<br>`xsd:float`|Range:`[0, ..., 1]`<br>Minimum brightness:<br>`0`<br>Middle brightness:`0.5`<br>Maximum brightness:<br>`1`|
|`Increment`<br>`Illumination`<br>`Level`|C|Stepwise increment of the<br>face illumination-brightness<br>at the given proportion of the<br>maximum brightness. This<br>command SHALL only be<br>available in manual mode.|Step<br>`xsd:float`|Range:`[0, ..., 1]`|
|`Decrement`<br>`Illumination`<br>`Level`|C|Stepwise decrement of the<br>face illumination-brightness<br>at the given proportion of the<br>maximum brightness. This<br>command SHALL only be<br>available in manual mode.|Step<br>`xsd:float`|Range:`[0, ..., 1]`|



> 1 Mandatory / Optional / Conditional 

Federal Office for Information Security 

65 

8 Service Definitions 

|**Parameter ID**|**M/O/C1**|**Description**|**Name and type**|**Possible Values**|
|---|---|---|---|---|
|`CropManually`|M/C|After capturing a facial image<br>the operator SHALL have the<br>option to crop the image ma<br>nually. Thereby the automa<br>ted cropping will be overru<br>led. The command SHALL<br>NOT be useable anytime else.<br>The source of the image di<br>mensions is the`QAEntireI`<br>`mage`feedback.|Region<br>`hlbs:`<br>`Image`<br>`Region`|The area to be crop<br>ped in is defined by the<br>point of the upper left<br>corner (x1, y1) and the<br>point of the bottom<br>right corner (x2, y,2).<br>Range x1 and x2: [`0`, ...,<br>_Image width in pixel_]<br>Range y1 and y2: [`0`, ...,<br>_Image height in pixel_]|
|`RotateManually`|M/C|After capturing a facial image<br>the operator SHALL have the<br>option to rotate the image<br>manually. Thereby the au<br>tomated de-rotation will be<br>overruled. The command<br>SHALL NOT be useable any<br>time else. The rotation axis<br>SHALL be the center of the<br>`QACroppedFacialImage`.<br>Furthermore, the absolute<br>value SHALL always be used,<br>i.e. the rotation always starts<br>from the original image (wi<br>thout rotation) and not rela<br>tive to a possible previous ro<br>tation.|Angle<br>`xsd:float`|Amount of clockwise<br>rotation in degree wi<br>thin the range [`0.0`, …,<br>`360.0`[, where`0.0`me<br>ans no rotation.|
|`AcceptImage`|M/C|After capturing a facial image<br>the operator SHALL have the<br>option to accept the image<br>using this command. The<br>command SHALL NOT be<br>useable anytime else.|-|-|
|`RejectImage`|M/C|After capturing a facial image<br>the operator SHALL have the<br>option to reject the image<br>using this command. The<br>command SHALL NOT be<br>useable anytime else. No<br>te, that information about<br>the acquisition of a rejected<br>image SHALL still be part of<br>a log. Only the record itself<br>SHALL NOT be stored in the<br>log anymore.|-|-|



**Table 8.3** FIAS UserCommands 

## 8.1.4 Feedback 

When the `getServiceFeedback` operation is executed the `feedbackElements` shown in Table 8.4 SHALL be returned in case the existence column is set to REQUIRED and MAY be returned in case the existence column is set to OPTIONAL. Conditional feedback SHALL only be available if the manual operation mode is in use. Furthermore the `userCommands*` SHALL contain the `hlbs:UserCommandInfo` for each implemented `hlbs:U serCommand` that is currently allowed to be used. E.g. for the `hlbs:UserCommand IncrementIlluminationLevel` the value `not-allowed` is to be returned if the maximum illumination-brightness is already reached. The pos sible `feedbackElements*` of Table 8.4 SHALL also be part of the `serviceDescriptionXML` that is returned with the `getServiceDescription` . 

> 1 Mandatory / Optional / Conditional 

Federal Office for Information Security 

66 

8 Service Definitions 

|**Parameter ID**|**M/O/C2**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`LiveStatus`|M|Transmission of sta<br>tus information of the<br>FIAS during the run<br>ning capture process<br>for further processing<br>within the client soft<br>ware.|`xsd:`<br>`string`|`Initializing`<br>(service initializes)<br>`SearchingFace`<br>(searching for face),<br>`FaceRecognized`<br>(face detected),<br>`Capturing`<br>(capture is running),<br>`StepBack`<br>(face is too close),<br>`StepForward`<br>(face is too far in the back<br>ground),<br>`StepLeft`<br>(face is too far left),<br>`StepRight`<br>(face is too far right),<br>`MoveUp`<br>(face is too far down),<br>`MoveDown`<br>(face is too far up),<br>`StandStill`<br>(face is too much in move<br>ment),<br>`LookStraight`<br>(face is not facing frontal),<br>`OpenEyes`<br>(eyes are closed),<br>`CloseMouth`<br>(mouth is opened),<br>`MultipleFaces`<br>(multiple faces detected),<br>`PerformingQA`<br>(software-based QA is run<br>ning),<br>`AssessQuality`<br>(operator is asked to accept or<br>reject an acquired image)|
|`LiveImage`|M|Contains a live image<br>of the constantly ac<br>quired live stream<br>of the camera of the<br>FIAS.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|
|`LiveCropped`<br>`FacialImage`|M|As soon as a face is<br>within the acquisiti<br>on area of the FIAS,<br>with this parameter a<br>cropped facial image<br>is transmitted.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|
|`Current`<br>`Focus`<br>`Point`|C|Returns the current<br>absolute focus dis<br>tance of the camera's<br>field of view in cm.<br>This feedback SHALL<br>only be available in<br>manual mode.|`xsd:`<br>`float`|Range:`[40, ..., 100]`|



> 2 Mandatory / Optional / Conditional 

Federal Office for Information Security 

67 

8 Service Definitions 

|**Parameter ID**|**M/O/C2**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`Current`<br>`Vertical`<br>`Position`|C|Returns the current<br>absolute vertical po<br>sition of the came<br>ra's field of view. This<br>feedback SHALL only<br>be available in manu<br>al mode.|`xsd:`<br>`float`|Range:`[0, ..., 1]`|
|`Current`<br>`Illumination`<br>`Level`|C|Returns the current<br>absolute face illumi<br>nation-brightness.<br>This feedback SHALL<br>only be available in<br>manual mode.|`xsd:`<br>`float`|Range:`[0, ..., 1]`|
|`QAFeedback`|M/C|Returns the`Face`<br>`Feedback`node<br>of the TR-03121<br>XML Schema (see<br>`hlbs6v1.xsd`) contai<br>ning all relevant qua<br>lity information to as<br>sist the operator in his<br>or her quality assess<br>ment. This feedback<br>SHALL only be retur<br>ned for the manual<br>operator assessment<br>after the FIAS has ma<br>de a capture.|`xsd:`<br>`string`|See TR-03121 XML Schema|
|`QAEntire`<br>`FacialImage`|M/C|Returns the entire<br>image that MAY be<br>used for re-cropping<br>the captured facial<br>image. This feedback<br>SHALL only be re<br>turned for the ma<br>nual operator assess<br>ment after the FIAS<br>has made a capture.<br>The<br>`hlbs:ImageRe`<br>`gion`SHALL mark the<br>image section of the<br>`QACroppedFacialI`<br>`mage`.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|
|`QACropped`<br>`FacialImage`|M/C|Returns the cropped<br>image that shall be<br>assessed by the ope<br>rator. This feedback<br>SHALL only be retur<br>ned for the manual<br>operator assessment<br>after the FIAS has ma<br>de a capture.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|



> 2 Mandatory / Optional / Conditional 

Federal Office for Information Security 

68 

8 Service Definitions 

|**Parameter ID**|**M/O/C2**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`QACropped`<br>`FacialImageRota`<br>`tion`|M/C|Returns the current<br>rotation of the crop<br>ped image that shall<br>be assessed by the<br>operator. This feed<br>back SHALL only be<br>returned for the ma<br>nual operator assess<br>ment after the Basic<br>Facial Image Acquisi<br>tion System has ma<br>de a capture. It SHALL<br>be updated in case the<br>operator has changed<br>the rotation manual<br>ly.|`xsd:float`|Amount of clockwise rotati<br>on in degree within the range<br>[`0.0`, …,`360.0`[, where`0.0`me<br>ans no rotation.|



**Table 8.4** FIAS Feedback Elements 

## 8.1.5 Results 

The `getResults` operation returns the `resultElements*` as `hlbs:KeyValue` . The key-value pairs that SHALL be returned are shown in Table 8.5. The possible results of Table 8.4 SHALL also be part of the `serviceDe scriptionXML` that is returned with the `getServiceDescription` . 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Result`|Description of the result of the image<br>acquisition.|`xsd:`<br>`string`|`Success`<br>(acquisition successful),<br>`Canceled`<br>(acquisition canceled),<br>`TimeOutWithImage`<br>(time out and image with insuffici<br>ent quality captured),<br>`TimeOut`<br>`WithoutImage`<br>(time out and no image captured),<br>`CameraFailure`<br>(camera failure)|
|`FaceAcquisition`|Contains the full XML root element<br>`FaceAcquisition`(see TR-03121 XML<br>`biotypes6v1.xsd`) which logs the<br>entire acquisition process, including<br>quality information and the finally ac<br>cepted facial image as record. The da<br>ta format, compression and file size<br>of the record SHALL comply with the<br>configured`ApplicationProfile`.|`xsd:`<br>`string`|See TR-03121 XML Schema|



**Table 8.5** FIAS Result Elements 

## 8.2 Service Definition Basic Facial Image Acquisition System 

This Service Definition specifies requirements for a Facial Image Acquisition System with basic functionality (e.g. used for Supervised Facial Image Acquisition without Central Identity Register (CIR) Lookup) that imple ments HLBS as communication interface. 

## 8.2.1 ServiceInformation 

When the `getAllServices` operation is requested at least the `ServiceInformation` shown in Table 8.6 SHALL be returned. Further parameters are vendor specific and SHALL be set as well. 

> 2 Mandatory / Optional / Conditional 

Federal Office for Information Security 

69 

8 Service Definitions 

|**Parameter ID**|**Description**|**Type**|**Value**|
|---|---|---|---|
|`Id`|Unique UUID of the service.|`xsd:`<br>`string`|`ac9317c9-46d5-4925-`<br>`80cf-0cb45d73ef3d`|
|`Name`|Name of the service.|`xsd:`<br>`string`|`Basic Facial Image Acquisition`<br>`System`|
|`Version`|Version of BSI TR-03121 of<br>the implemented service.|`xsd:`<br>`string`|`7.0`|



**Table 8.6** Basic Facial Image Acquisition System ServiceInformation 

## 8.2.2 Configuration 

At least the configuration options listed in Table 8.7 SHALL be available for the `configureService` ope ration. These configuration options including their allowed and default values SHALL also be part of the `ser viceDescriptionXML` that is returned with the `getServiceDescription` operation. 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Purpose`|The purpose of the facial<br>image acquisition.|`hlbs:`<br>`ServiceType`|`enrolment`,<br>`identification`,<br>`verification`,<br>`other` _(e.g. purpose is ambi_<br>_guous)_|
|`ApplicationProfile`|Relevant Application Profile<br>to be used for the acquisition<br>process and its results.|`hlbs:`<br>`Application`<br>`Profile`|_Choice of the implemen_<br>_ted Application Profiles (e.g._<br>`IMA_`<br>`MultiModalProcessin`<br>`gImmigrationAuthori`<br>`tiesEES`_)_|
|`TimeOut`|Sets the timeout for acquisi<br>tions in milliseconds for the<br>automated operation mode.|`xsd:int`|_Arbitrary Value_<br>Default:`0`(no timeout)|



**Table 8.7** Basic Facial Image Acquisition System Configuration 

## 8.2.3 User Commands 

When the `signalUserCommand` operation is executed the user commands shown in Table 8.8 SHALL be supported in case the existence column is set to REQUIRED and MAY be supported in case the existence co lumn is set to OPTIONAL. Conditional commands SHALL only be available if the manual operation mode is in use, except for the `CropManually` , `acceptImage` and `rejectImage` command. In case a user command is not al lowed at a certain point of time during the execution of the service the user SHALL be informed via the `ge tServiceFeedback` operation. The user commands of Table 8.8 SHALL also be present within the `serviceDe scriptionXML` that is returned with the `getServiceDescription` operation. 

|**Parameter ID**|**M/O/C3**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`Cancel`|M|Abort/Terminate a running<br>capture.|-|-|
|`Capture`|M/C|Force capturing the current<br>ly showing camera's field of<br>view. This overrules the re<br>sult of a live-QA. This com<br>mand SHALL only usable<br>when the live image is visible<br>during the capture process.|-|-|



> 3 Mandatory / Optional / Conditional 

Federal Office for Information Security 

70 

8 Service Definitions 

|**Parameter ID**|**M/O/C3**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`CropManually`|M/C|After capturing a facial image<br>the operator SHALL have the<br>option to crop the image ma<br>nually. Thereby the automa<br>ted cropping will be overru<br>led. The command SHALL<br>NOT be useable anytime else.<br>The source of the image di<br>mensions is the`QAEntireI`<br>`mage`feedback.|Region<br>`hlbs:`<br>`Image`<br>`Region`|The area to be crop<br>ped in is defined by the<br>point of the upper left<br>corner (x1, y1) and the<br>point of the bottom<br>right corner (x2, y,2).<br>Range x1 and x2: [`0`, ...,<br>_Image width in pixel_]<br>Range y1 and y2: [`0`, ...,<br>_Image height in pixel_]|
|`RotateManually`|M/C|After capturing a facial image<br>the operator SHALL have the<br>option to rotate the image<br>manually. Thereby the au<br>tomated de-rotation will be<br>overruled. The command<br>SHALL NOT be useable any<br>time else. The rotation axis<br>SHALL be the center of the<br>`QACroppedFacialImage`.<br>Furthermore, the absolute<br>value SHALL always be used,<br>i.e. the rotation always starts<br>from the original image (wi<br>thout rotation) and not rela<br>tive to a possible previous ro<br>tation.|Angle<br>`xsd:float`|Amount of clockwise<br>rotation in degree wi<br>thin the range [`0.0`, …,<br>`360.0`[, where`0.0`me<br>ans no rotation.|
|`AcceptImage`|M/C|After capturing a facial image<br>the operator SHALL have the<br>option to accept the image<br>using this command. The<br>command SHALL NOT be<br>useable anytime else.|-|-|
|`RejectImage`|M/C|After capturing a facial image<br>the operator SHALL have the<br>option to reject the image<br>using this command. The<br>command SHALL NOT be<br>useable anytime else. No<br>te, that information about<br>the acquisition of a rejected<br>image SHALL still be part of<br>a log. Only the record itself<br>SHALL NOT be stored in the<br>log anymore.|-|-|



**Table 8.8** Basic Facial Image Acquisition System UserCommands 

## 8.2.4 Feedback 

When the `getServiceFeedback` operation is executed the `feedbackElements` shown in Table 8.9 SHALL be returned in case the existence column is set to REQUIRED and MAY be returned in case the existence column is set to OPTIONAL. Conditional feedback SHALL only be available if the manual operation mode is in use. Furthermore the `userCommands*` SHALL contain the `hlbs:UserCommandInfo` for each implemented `hlbs:U serCommand` that is currently allowed to be used. E.g. for the `hlbs:UserCommand IncrementIlluminationLevel` the value `not-allowed` is to be returned if the maximum illumination-brightness is already reached. The pos sible `feedbackElements*` of Table 8.9 SHALL also be part of the `serviceDescriptionXML` that is returned with the `getServiceDescription` . 

> 3 Mandatory / Optional / Conditional 

Federal Office for Information Security 

71 

8 Service Definitions 

|**Parameter ID**|**M/O/C4**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`LiveStatus`|M|Transmission of sta<br>tus information of<br>the Basic Facial Image<br>Acquisition System<br>during the running<br>capture process for<br>further processing wi<br>thin the client soft<br>ware.|`xsd:`<br>`string`|`Initializing`<br>(service initializes)<br>`SearchingFace`<br>(searching for face),<br>`FaceRecognized`<br>(face detected),<br>`Capturing`<br>(capture is running),<br>`StepBack`<br>(face is too close),<br>`StepForward`<br>(face is too far in the back<br>ground),<br>`StepLeft`<br>(face is too far left),<br>`StepRight`<br>(face is too far right),<br>`MoveUp`<br>(face is too far down),<br>`MoveDown`<br>(face is too far up),<br>`StandStill`<br>(face is too much in move<br>ment),<br>`LookStraight`<br>(face is not facing frontal),<br>`OpenEyes`<br>(eyes are closed),<br>`CloseMouth`<br>(mouth is opened),<br>`MultipleFaces`<br>(multiple faces detected),<br>`PerformingQA`<br>(software-based QA is run<br>ning),<br>`AssessQuality`<br>(operator is asked to accept or<br>reject an acquired image)|
|`LiveImage`|M|Contains a live image<br>of the constantly ac<br>quired live stream of<br>the camera of the Ba<br>sic Facial Image Ac<br>quisition System.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|
|`LiveCropped`<br>`FacialImage`|M|As soon as a face is<br>within the acquisition<br>area of the Basic Faci<br>al Image Acquisition<br>System, with this pa<br>rameter a cropped fa<br>cial image is transmit<br>ted.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|



> 4 Mandatory / Optional / Conditional 

Federal Office for Information Security 

72 

8 Service Definitions 

|**Parameter ID**|**M/O/C4**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`QAFeedback`|M/C|Returns the`Face`<br>`Feedback`node<br>of the TR-03121<br>XML Schema (see<br>`hlbs6v1.xsd`) contai<br>ning all relevant qua<br>lity information to as<br>sist the operator in<br>his or her quality as<br>sessment. This feed<br>back SHALL only be<br>returned for the ma<br>nual operator assess<br>ment after the Basic<br>Facial Image Acquisi<br>tion System has made<br>a capture.|`xsd:`<br>`string`|See TR-03121 XML Schema|
|`QAEntire`<br>`FacialImage`|M/C|Returns the entire<br>image that MAY be<br>used for re-cropping<br>the captured facial<br>image. This feedback<br>SHALL only be re<br>turned for the ma<br>nual operator assess<br>ment after the Ba<br>sic Facial Image Ac<br>quisition System has<br>made a capture.The<br>`hlbs:ImageRegi`<br>`on`SHALL mark the<br>image section of the<br>`QACroppedFacialI`<br>`mage`.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|
|`QACropped`<br>`FacialImage`|M/C|Returns the cropped<br>image that shall be<br>assessed by the ope<br>rator. This feedback<br>SHALL only be retur<br>ned for the manual<br>operator assessment<br>after the Basic Faci<br>al Image Acquisition<br>System has made a<br>capture. It SHALL be<br>updated in case the<br>operator has changed<br>the cropping or rota<br>tion manually.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|



> 4 Mandatory / Optional / Conditional 

Federal Office for Information Security 

73 

8 Service Definitions 

|**Parameter ID**|**M/O/C4**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`QACropped`<br>`FacialImage`<br>`Rotation`|M/C|Returns the current<br>rotation of the crop<br>ped image that shall<br>be assessed by the<br>operator. This feed<br>back SHALL only be<br>returned for the ma<br>nual operator assess<br>ment after the Basic<br>Facial Image Acquisi<br>tion System has ma<br>de a capture. It SHALL<br>be updated in case the<br>operator has changed<br>the rotation manual<br>ly.|`xsd:float`|Amount of clockwise rotati<br>on in degree within the range<br>[`0.0`, …,`360.0`[, where`0.0`me<br>ans no rotation.|



**Table 8.9** Basic Facial Image Acquisition System Feedback Elements 

## 8.2.5 Results 

The `getResults` operation returns the `resultElements*` as `hlbs:KeyValue` . The key-value pairs that SHALL be returned are shown in Table 8.10. The possible results of Table 8.9 SHALL also be part of the `serviceDe scriptionXML` that is returned with the `getServiceDescription` . 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Result`|Description of the result of the image<br>acquisition.|`xsd:`<br>`string`|`Success`<br>(acquisition successful),<br>`Canceled`<br>(acquisition canceled),<br>`TimeOutWithImage`<br>(time out and image with insuffici<br>ent quality captured),<br>`TimeOut`<br>`WithoutImage`<br>(time out and no image captured),<br>`CameraFailure`<br>(camera failure)|
|`FaceAcquisition`|Contains the full XML root element<br>`FaceAcquisition`(see TR-03121 XML<br>`biotypes6v1.xsd`) which logs the<br>entire acquisition process, including<br>quality information and the finally ac<br>cepted facial image as record. The da<br>ta format, compression and file size<br>of the record SHALL comply with the<br>configured`ApplicationProfile`.|`xsd:`<br>`string`|See TR-03121 XML Schema|



**Table 8.10** Basic Facial Image Acquisition System Result Elements 

## 8.3 Service Definition Facial Image Delivery System 

This Service Definition specifies requirements for a Facial Image Delivery System with basic functionality (e.g. used for cropping and rotating images and for assessing the image quality) that implements HLBS as communication interface. 

## 8.3.1 ServiceInformation 

When the `getAllServices` operation is requested at least the `ServiceInformation` shown in Table 8.11 SHALL be returned. Further parameters are vendor specific and SHALL be set as well. 

> 4 Mandatory / Optional / Conditional 

Federal Office for Information Security 

74 

8 Service Definitions 

|**Parameter ID**|**Description**|**Type**|**Value**|
|---|---|---|---|
|`Id`|Unique UUID of the service.|`xsd:`<br>`string`|`ac9317c9-46d5-4925-`<br>`80cf-0cb45d73ef3e`|
|`Name`|Name of the service.|`xsd:`<br>`string`|`Facial Image Delivery System`|
|`Version`|Version of BSI TR-03121 of<br>the implemented service.|`xsd:`<br>`string`|`7.0`|



**Table 8.11** Facial Image Delivery System ServiceInformation 

## 8.3.2 Configuration 

At least the configuration options listed in Table 8.12 SHALL be available for the `configureService` ope ration. These configuration options including their allowed and default values SHALL also be part of the `ser viceDescriptionXML` that is returned with the `getServiceDescription` operation. 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Purpose`|The purpose of the facial<br>image acquisition.|`hlbs:`<br>`ServiceType`|`enrolment`,<br>`identification`,<br>`verification`,<br>`other` _(e.g. purpose is ambi_<br>_guous)_|
|`ApplicationProfile`|Relevant Application Profile<br>to be used for the acquisition<br>process and its results.|`hlbs:`<br>`Application`<br>`Profile`|_Choice of the implemen_<br>_ted Application Profiles (e.g._<br>`ARE_`<br>`ArrivalAttestationDo`<br>`cument`_)_|
|`AdjustAutomatically`|Flag for enabling/disabling<br>automatic image adjustments<br>(cropping/rotating).|`xsd:boolean`|`true`,`false`<br>Default:`true`|
|`FacialImages`|The facial image(s) to be as<br>sessed and delivered.|`hlbs:`<br>`Image`<br>`List`|For each contained<br>`hlbs:Image`the`xmlPa`<br>`rameters`SHALL contain<br>the`bio:Origin`of`bioty`<br>`pes6v1.xsd`._Image(s) in an_<br>_expected data format for the_<br>_Application Profile._|



**Table 8.12** Facial Image Delivery System Configuration 

## 8.3.3 User Commands 

When the `signalUserCommand` operation is executed the user commands shown in Table 8.13 SHALL be supported in case the existence column is set to REQUIRED and MAY be supported in case the existence co lumn is set to OPTIONAL. In case a user command is not allowed at a certain point of time during the execu tion of the service the user SHALL be informed via the `getServiceFeedback` operation. The user commands of Table 8.13 SHALL also be present within the `serviceDescriptionXML` that is returned with the `getSer viceDescription` operation. 

|**Parameter ID**|**M/O/C5**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`Cancel`|M|Abort/Terminate a running<br>operation.|-|-|



> 5 Mandatory / Optional / Conditional 

Federal Office for Information Security 

75 

8 Service Definitions 

|**Parameter ID**|**M/O/C5**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`CropManually`|M/C|After the automatic cropping<br>has been performed the ope<br>rator SHALL have the opti<br>on to crop the image manu<br>ally. Thereby the automated<br>cropping will be overruled.<br>The command SHALL NOT<br>be useable anytime else. The<br>source of the image dimen<br>sions is the`QAEntireImage`<br>feedback.|ImageListItem<br>`xsd:int`<br>Region<br>`hlbs:`<br>`Image`<br>`Region`|The item number<br>of the`QAFeedback`<br>`List`[`0`, …, List Size - 1]<br>The area to be crop<br>ped in is defined by the<br>point of the upper left<br>corner (x1, y1) and the<br>point of the bottom<br>right corner (x2, y,2).<br>Range x1 and x2: [`0`, ...,<br>_Image width in pixel_]<br>Range y1 and y2: [`0`, ...,<br>_Image height in pixel_]|
|`RotateManually`|M/C|After the automatic rotation<br>has been performed the ope<br>rator SHALL have the opti<br>on to rotate the image ma<br>nually. Thereby the automa<br>ted de-rotation will be over<br>ruled. The command SHALL<br>NOT be useable anytime else.<br>The rotation axis SHALL be<br>the center of the`QACropped`<br>`FacialImage`. Furthermore,<br>the absolute value SHALL al<br>ways be used, i.e. the rotation<br>always starts from the origi<br>nal image (without rotation)<br>and not relative to a possible<br>previous rotation.|ImageListItem<br>`xsd:int`<br>Angle<br>`xsd:float`|The item number of<br>the`QAFeedbackList`<br>[`0`, …, List Size - 1]<br>Amount of clockwise<br>rotation in degree wi<br>thin the range [`0.0`, …,<br>`360.0`[, where`0.0`me<br>ans no rotation.|
|`AcceptImage`|M/C|After delivering a facial<br>image the operator SHALL<br>have the option to accept the<br>image using this command.<br>The command SHALL NOT<br>be useable anytime else.|ImageListItem<br>`xsd:int`|The item number<br>of the`QAFeedback`<br>`List`[`0`, …, List Size - 1]|
|`RejectAllImages`|M/C|After delivering a facial<br>image the operator SHALL<br>have the option to reject the<br>image using this command.<br>The command SHALL NOT<br>be useable anytime else. No<br>te, that information about<br>the acquisition of a rejected<br>image SHALL still be part of<br>a log. Only the record itself<br>SHALL NOT be stored in the<br>log anymore.|-|-|



**Table 8.13** Facial Image Delivery System UserCommands 

## 8.3.4 Feedback 

When the `getServiceFeedback` operation is executed the `feedbackElements` shown in Table 8.14 SHALL be returned in case the existence column is set to REQUIRED and MAY be returned in case the existence column is set to OPTIONAL. Conditional feedback SHALL only be available if the manual operation mode is in use. Furthermore the `userCommands*` SHALL contain the `hlbs:UserCommandInfo` for each implemented `hlbs:UserCommand` that is currently allowed to be used. The possible `feedbackElements*` of Table 8.14 SHALL also be part of the `serviceDescriptionXML` that is returned with the `getServiceDescription` . 

> 5 Mandatory / Optional / Conditional 

Federal Office for Information Security 

76 

8 Service Definitions 

|**Parameter ID**|**M/O/C6**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`LiveStatus`|M|Transmission of sta<br>tus information of the<br>Facial Image Delivery<br>System during the<br>running capture pro<br>cess for further pro<br>cessing within the cli<br>ent software.|`xsd:`<br>`string`|`Initializing`<br>(service initializes),<br>`PerformingQA`<br>(software-based QA is run<br>ning),<br>`AssessQuality`<br>(operator is asked to accept or<br>reject a delivered image)|
|`QAFeedbackList`|M/C|Returns the`Face`<br>`Feedback`node<br>of the TR-03121<br>XML Schema (see<br>`hlbs6v1.xsd`) for<br>each image contai<br>ning all relevant qua<br>lity information to as<br>sist the operator in his<br>or her quality assess<br>ment. The list SHALL<br>be ordered by descen<br>ding quality.|`hlbs:`<br>`StringList`|See TR-03121 XML Schema|
|`QAEntire`<br>`FacialImageList`|M/C|Returns each entire<br>image that MAY be<br>used for re-cropping<br>the captured facial<br>image. The<br>`hlbs:I`<br>`mageRegion`SHALL<br>mark the image sec<br>tion of the`QACrop`<br>`pedFacialImage`.<br>The list SHALL be or<br>dered according to<br>`QAFeedbackList`.|`hlbs:`<br>`ImageList`|_Image(s) in an expected data_<br>_format for the Application Pro_<br>_file._|
|`QACropped`<br>`FacialImageList`|M/C|Returns all cropped<br>images that shall be<br>assessed by the ope<br>rator. It SHALL be up<br>dated in case the ope<br>rator has changed the<br>cropping or rotati<br>on manually. The list<br>SHALL be ordered ac<br>cording to`QAFeed`<br>`backList`.|`hlbs:`<br>`ImageList`|_Image(s) in an expected data_<br>_format for the Application Pro_<br>_file._|
|`QACropped`<br>`FacialImage`<br>`RotationList`|M/C|Returns the current<br>rotation of the crop<br>ped image that shall<br>be assessed by the<br>operator. It SHALL be<br>updated in case the<br>operator has changed<br>the rotation manual<br>ly. The list SHALL be<br>ordered according to<br>`QAFeedbackList`.|`hlbs:String`<br>`List`|Amount of clockwise rotati<br>on in degree as float within the<br>range [`0.0`, …,`360.0`[, where<br>`0.0`means no rotation.|



**Table 8.14** Facial Image Delivery System Feedback Elements 

> 6 Mandatory / Optional / Conditional 

Federal Office for Information Security 

77 

8 Service Definitions 

## 8.3.5 Results 

The `getResults` operation returns the `resultElements*` as `hlbs:KeyValue` . The key-value pairs that SHALL be returned are shown in Table 8.15. The possible results of Table 8.14 SHALL also be part of the `service DescriptionXML` that is returned with the `getServiceDescription` . 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Result`|Description of the result of the image<br>delivery.|`xsd:`<br>`string`|`Success`<br>(delivery successful),<br>`Canceled`<br>(delivery canceled),<br>`Failure`<br>(failure during processing)|
|`FaceDelivery`|Contains the full XML root element<br>`FaceDelivery`(see TR-03121 XML<br>`biotypes6v1.xsd`) which logs the<br>entire acquisition process, including<br>quality information and the finally ac<br>cepted facial image as record. The da<br>ta format, compression and file size<br>of the record SHALL comply with the<br>configured`ApplicationProfile`.|`xsd:`<br>`string`|See TR-03121 XML Schema|



**Table 8.15** Facial Image Delivery System Result Elements 

## 8.4 Service Definition Fingerprint Acquisition 

This service definition specifies requirements for a system acquiring fingerprints. 

## 8.4.1 ServiceInformation 

When the `getAllServices` operation is requested at least the `hlbs:ServiceInformation` shown in Ta ble 8.16 SHALL be returned. Further parameters are vendor specific and SHALL be set as well. 

|**Parameter ID**|**Description**|**Type**|**Value**|
|---|---|---|---|
|`Id`|Unique UUID of the service.|`xsd:`<br>`string`|`186266e5-3760-4d0c-b7ec-`<br>`b866024e6b61`|
|`Name`|Name of the service.|`xsd:`<br>`string`|`Fingerprint Acquisition`|
|`Version`|Version of BSI TR-03121 of<br>the implemented service.|`xsd:`<br>`string`|`7.0`|



**Table 8.16** Fingerprint Acquisition ServiceInformation 

## 8.4.2 Configuration 

At least the configuration options listed in Table 8.17 SHALL be available for the `configureService` ope ration. These configuration options including their allowed and default values SHALL also be part of the `ser viceDescriptionXML` that is returned with the `getServiceDescription` operation. 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Purpose`|The purpose of the fingerprint image<br>acquisition.|`hlbs:`<br>`ServiceType`|`enrolment`,`identification`,<br>`verification`|
|`ApplicationProfile`|Relevant Application Profile to be<br>used for the acquisition process and<br>its results.|`hlbs:`<br>`Application`<br>`Profile`||
|`Fingerprints`<br>`ToAcquire`|Fingerprints/slaps that shall be ac<br>quired.|`hlbs:`<br>`Biometric`<br>`Code`<br>`List`|_Codes for fingerprints (see_<br>_hlbs:_<br>_Iso19794_<br>_FingerCode)._|



Federal Office for Information Security 

78 

8 Service Definitions 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Missing`<br>`Fingers`|**DEPRECATED**. Reports (temporary)<br>missing fingers that can not be ac<br>quired, but have been requested to<br>acquire.|`xsd:`<br>`string`|`FingerMissingList`(see<br>TR-03121 XML,`hlbs1v1.xsd`)<br>is used.|
|`SlapClassifier`|Configures whether the slap classi<br>fication shall be performed or not.<br>This SHALL only have effect when<br>a slap acquisition is performed (see<br>`FingerprintsToAcquire`).|`xsd:`<br>`string`|`activated`(default),<br>`deactivated`,<br>`evaluation`(classification is<br>only performed for internal<br>evaluation purposes)|



**Table 8.17** Fingerprint Acquisition Configuration 

## 8.4.3 User Commands 

When the `signalUserCommand` operation is executed the user commands shown in Table 8.18 SHALL be supported by the service. In case a user command is not allowed at a certain point of time during the execution of the service the user SHALL be informed via the `getServiceFeedback` operation. The user commands of Table 8.18 SHALL also be present within the `serviceDescriptionXML` that is returned with the `getService Description` operation. 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Cancel`|Abort/Terminate the running ser<br>vice. Command SHALL be execute<br>able at any time.|-|-|
|`Capture`|Force capturing the currently sho<br>wing capture area of the fingerprint<br>acquisition system. This overrules<br>the result of a live-QA (pre-qualifi<br>cation). This command SHALL only<br>usable when the live image is visible<br>during the capture process.|-|-|
|`Continue`|Continue with the next capture or fi<br>nalise the overall capture process af<br>ter the last fingerprint has been cap<br>tured. The command SHALL be exe<br>cuteable when the intermediate re<br>sult image is shown.|-|-|
|`Discard`|Reject the last capture (namely the<br>intermediate result image) and start<br>the capture process for it anew. The<br>command SHALL be executeable<br>when the intermediate result image<br>is shown.|-|-|
|`DiscardAll`|Reject all previous captures and start<br>the overall capture process anew.<br>The command SHALL be executeable<br>when the intermediate result image<br>is shown.|-|-|
|`UseSingleFinger`<br>`AcquisitionFallback`|In case a biometric subject is not ca<br>pable to place the fingers of a slap<br>on the fingerprint scanner this com<br>mand may be used to activate the<br>fallback acquisition of single fingers<br>for this slap.|-|-|



Federal Office for Information Security 

79 

8 Service Definitions 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`SelectMissingFingers`|In case one or more fingers are not<br>available for capture (e.g. amputa<br>ted, bandaged) missing fingers can be<br>reported using this command. This<br>command SHALL either be triggered<br>for the entire acquisition before the<br>actual acquisition or before each cap<br>ture of a new finger/slap (e.g. when<br>switching between left and right<br>hand slap). Note, that in the later ca<br>se the Feedback`ExpectedFingers`is<br>REQUIRED to be send by the service<br>beforehand. This command SHALL<br>only be exectuable in the beforehand<br>described scenarios.|`xsd:`<br>`string`|`FingerMissingList`(see<br>TR-03121 XML,`hlbs1v1.xsd`)<br>is used.|



**Table 8.18** Fingerprint Acquisition UserCommands 

## 8.4.4 Feedback 

Within the `hlbs:Feedback` the `feedbackElements*` of Table 8.19 as `hlbs:KeyValue` SHALL be returned. Furthermore the `userCommands*` SHALL contain the `hlbs:UserCommandInfo` for each implemented `hlbs:U serCommand` . The possible `feedbackElements*` of Table 8.19 SHALL also be part of the `serviceDescriptionXML` that is returned with the `getServiceDescription` . 

Federal Office for Information Security 

80 

8 Service Definitions 

|**Parameter ID**|**M/O/C7**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`LiveStatus`|O|Transmission of sta<br>tus information du<br>ring the continuous<br>capture process (live<br>view) for further pro<br>cessing within the cli<br>ent software.|`xsd:`<br>`string`|`Initializing`<br>(service initializes),<br>`SelectMissingFingers`(ope<br>rator is asked to select missing<br>fingers)<br>`SearchingFingers`<br>(searching for fingers),<br>`FingersRecognized`<br>(fingers detected),<br>`Capturing`<br>(capture is running),<br>`ReduceFinger`<br>`Pressure`<br>(fingers are placed with too<br>much pressure),<br>`RaiseFingerPressure`<br>(fingers are placed with too<br>less pressure or are placed<br>partly in the air),<br>`MoveFingersLeft`<br>(fingers are too far right),<br>`MoveFingersRight`<br>(fingers are too far left),<br>`MoveFingersForward`<br>(fingers are too far back),<br>`MoveFingersBackward`<br>(fingers are too far ahead),<br>`KeepFingersStill`<br>(fingers are too much in move<br>ment),<br>`PerformingQA`<br>(software-based QA is run<br>ning),<br>`AssessQuality`<br>(operator is asked to accept or<br>reject an acquired image)|
|`ExpectedFingers`|M|Indicates which fin<br>ger(s) are expected<br>to be captured for<br>the current capture<br>round.|`hlbs:`<br>`Biometric`<br>`CodeList`|_Codes for fingerprints (see_<br>_hlbs:_<br>_Iso19794_<br>_FingerCode)._|
|`LiveImage`|O|Contains a live image<br>of the constantly ac<br>quired live stream of<br>the fingerprint scan<br>ner.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|
|`Intermediate`<br>`FingerAmount`<br>`Mismatch`|O|There is a problem<br>with the amount of<br>fingers that have been<br>captured with the last<br>intermediate finger<br>print image.|`xsd:`<br>`string`|`TooLessFingers`<br>`Captured`<br>(less fingers than expected ha<br>ve been captured),<br>`TooManyFingers`<br>`Captured`<br>(more fingers than expected<br>have been captured)|
|`Intermediate`<br>`Fingerprint`<br>`Images`|M|Contains the finger<br>prints (segmented)<br>that have been acqui<br>red last.|`hlbs:`<br>`ImageList`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|



> 7 Mandatory / Optional / Conditional 

Federal Office for Information Security 

81 

8 Service Definitions 

|**Parameter ID**|**M/O/C7**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`Intermediate`<br>`FingerCodes`|M|Denotes the finger<br>code of each returned<br>intermediate finger<br>print image.|`hlbs:`<br>`Biometric`<br>`CodeList`|The order of the<br>`hlbs:`<br>`Iso19794FingerCode`ele<br>ments in this list has to be the<br>same as in the previous list of<br>`Intermediate`<br>`FingerprintImages`|
|`Intermediate`<br>`SlapImage`|O|In case the acquisition<br>is a slap acquisition,<br>the slap image of the<br>last capture SHALL be<br>contained here.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|
|`Intermediate`<br>`FingerFeedback`|M|Returns the`Fin`<br>`gerFeedback`node<br>of the TR-03121<br>XML Schema (see<br>`hlbs6v1.xsd`) con<br>taining all relevant<br>quality, PAD and uni<br>queness informati<br>on to assist the opera<br>tor in his or her qua<br>lity assessment. This<br>feedback SHALL on<br>ly be returned for the<br>manual operator as<br>sessment after a fin<br>ger capture has been<br>made.|`xsd:`<br>`string`|See TR-03121 XML Schema|



**Table 8.19** Fingerprint Acquisition Feedback Elements 

## 8.4.5 Results 

The `getResults` operation returns the `resultElements*` as `hlbs:KeyValue` . The key-value pairs that SHALL be returned are shown in Table 8.20. The possible results of Table 8.19 SHALL also be part of the `service DescriptionXML` that is returned with the `getServiceDescription` . 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Result`|Description of the result of the fingerprint<br>image acquisition.|`xsd:`<br>`string`|`Success`<br>(acquisition success<br>ful),<br>`Canceled`<br>(acquisition canceled)|
|`FingerAcquisition`|Contains the full XML root element`Finge`<br>`rAcquisition`(see TR-03121 XML`bioty`<br>`pes6v1.xsd`), which logs the entire acquisition<br>process, information about quality, PAD and<br>uniqueness as well as the finally accepted fin<br>gerprint(s) as record(s). The data format, com<br>pression and file size of the record SHALL com<br>ply with the configured`ApplicationProfile`.|`xsd:`<br>`string`|See TR-03121 XML<br>Schema|



**Table 8.20** Fingerprint Acquisition Result Elements 

## 8.5 Service Definition Rolled Fingerprint Acquisition 

This service definition specifies requirements for a system acquiring rolled fingerprints. 

> 7 Mandatory / Optional / Conditional 

Federal Office for Information Security 

82 

8 Service Definitions 

## 8.5.1 ServiceInformation 

When the `getAllServices` operation is requested at least the `hlbs:ServiceInformation` shown in Ta ble 8.21 SHALL be returned. Further parameters are vendor specific and SHALL be set as well. 

|**Parameter ID**|**Description**|**Type**|**Value**|
|---|---|---|---|
|`Id`|Unique UUID of the service.|`xsd:`<br>`string`|`293ccc7c-9603-4a2e-`<br>`9f79-2b255b6d1b2f`|
|`Name`|Name of the service.|`xsd:`<br>`string`|`Rolled Fingerprint Acquisiti`<br>`on`|
|`Version`|Version of BSI TR-03121 of<br>the implemented service.|`xsd:`<br>`string`|`7.0`|



**Table 8.21** Rolled Fingerprint Acquisition ServiceInformation 

## 8.5.2 Configuration 

At least the configuration options listed in Table 8.22 SHALL be available for the `configureService` ope ration. These configuration options including their allowed and default values SHALL also be part of the `ser viceDescriptionXML` that is returned with the `getServiceDescription` operation. 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Purpose`|The purpose of the fingerprint image<br>acquisition.|`hlbs:`<br>`ServiceType`|`enrolment`,`identification`,<br>`verification`|
|`ApplicationProfile`|Relevant Application Profile to be<br>used for the acquisition process and<br>its results.|`hlbs:`<br>`Application`<br>`Profile`|_Choice of the implemented App_<br>_lication Profiles (e.g._ `ARE_`<br>`ArrivalAttestation`<br>`Document`_)_|
|`Fingerprints`<br>`ToAcquire`|Fingerprints that shall be acquired.|`hlbs:`<br>`Biometric`<br>`Code`<br>`List`|_Codes for fingerprints (see_<br>_hlbs:_<br>_Iso19794_<br>_FingerCode)._|
|`ReferenceFingerprints`|GSAT 3.02 XML containing the refe<br>rence fingerprint images as type 14<br>records in order to perform a control<br>verification during the acquisition<br>process.|`hlbs:`<br>`binary`|_Flat fingerprints of previous ac_<br>_quisition_|



**Table 8.22** Rolled Fingerprint Acquisition Configuration 

## 8.5.3 User Commands 

When the `signalUserCommand` operation is executed the user commands shown in Table 8.23 SHALL be supported by the service. In case a user command is not allowed at a certain point of time during the execution of the service the user SHALL be informed via the `getServiceFeedback` operation. The user commands of Table 8.18 SHALL also be present within the `serviceDescriptionXML` that is returned with the `getService Description` operation. 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Cancel`|Abort/Terminate the running ser<br>vice. Command SHALL be executable<br>at any time.|-|-|
|`Capture`|Force capturing the currently sho<br>wing capture area of the fingerprint<br>acquisition system. This overrules<br>the result of a live-QA (pre-qualifi<br>cation). This command SHALL only<br>usable when the live image is visible<br>during the capture process.|-|-|



Federal Office for Information Security 

83 

8 Service Definitions 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Continue`|Continue with the next capture or fi<br>nalise the overall capture process af<br>ter the last fingerprint has been cap<br>tured. The command SHALL be exe<br>cutable when the intermediate result<br>image is shown.|-|-|
|`Discard`|Reject the last capture (namely the<br>intermediate result image) and start<br>the capture process for it anew. The<br>command SHALL be executable<br>when the intermediate result image<br>is shown.|-|-|
|`DiscardAll`|Reject all previous captures and start<br>the overall capture process anew.<br>The command SHALL be executable<br>when the intermediate result image<br>is shown.|-|-|
|`SelectMissingFingers`|In case one or more fingers are not<br>available for capture (e.g. amputa<br>ted, bandaged) missing fingers can be<br>reported using this command. This<br>command SHALL either be triggered<br>for the entire acquisition before the<br>actual acquisition or before each cap<br>ture of a new finger/slap (e.g. when<br>switching between left and right<br>hand slap). Note, that in the later ca<br>se the Feedback`ExpectedFingers`is<br>REQUIRED to be send by the service<br>beforehand. This command SHALL<br>only be exectuable in the beforehand<br>described scenarios.|`xsd:`<br>`string`|`FingerMissingList`(see<br>TR-03121 XML,`hlbs1v1.xsd`)<br>is used.|



**Table 8.23** Rolled Fingerprint Acquisition UserCommands 

## 8.5.4 Feedback 

Within the `hlbs:Feedback` the `feedbackElements*` of Table 8.19 as `hlbs:KeyValue` SHALL be returned. Furthermore the `userCommands*` SHALL contain the `hlbs:UserCommandInfo` for each implemented `hlbs:U serCommand` . The possible `feedbackElements*` of Table 8.24 SHALL also be part of the `serviceDescriptionXML` that is returned with the `getServiceDescription` . 

Federal Office for Information Security 

84 

8 Service Definitions 

|**Parameter ID**|**M/O/C8**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`LiveStatus`|O|Transmission of sta<br>tus information du<br>ring the continuous<br>capture process (live<br>view) for further pro<br>cessing within the cli<br>ent software.|`xsd:`<br>`string`|`Initializing`<br>(service initializes),<br>`SelectMissingFingers`(ope<br>rator is asked to select missing<br>fingers)<br>`SearchingFingers`<br>(searching for fingers),<br>`FingersRecognized`<br>(fingers detected),<br>`Capturing`<br>(capture is running),<br>`ReduceFinger`<br>`Pressure`<br>(fingers are placed with too<br>much pressure),<br>`RaiseFingerPressure`<br>(fingers are placed with too<br>less pressure or are placed<br>partly in the air),<br>`MoveFingersLeft`<br>(fingers are too far right),<br>`MoveFingersRight`<br>(fingers are too far left),<br>`MoveFingersForward`<br>(fingers are too far back),<br>`MoveFingersBackward`<br>(fingers are too far ahead),<br>`KeepFingersStill`<br>(fingers are too much in move<br>ment),<br>`PerformingQA`<br>(software-based QA is run<br>ning),<br>`AssessQuality`<br>(operator is asked to accept or<br>reject an acquired image)|
|`ExpectedFingers`|M|Indicates which fin<br>ger(s) are expected<br>to be captured for<br>the current capture<br>round.|`hlbs:`<br>`Biometric`<br>`CodeList`|_Codes for fingerprints (see_<br>_hlbs:_<br>_Iso19794_<br>_FingerCode)._|
|`LiveImage`|O|Contains a live image<br>of the constantly ac<br>quired live stream of<br>the fingerprint scan<br>ner.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|
|`Intermediate`<br>`Fingerprint`<br>`Images`|M|Contains the finger<br>prints (segmented)<br>that have been acqui<br>red last.|`hlbs:`<br>`ImageList`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is expec_<br>_ted._|



> 8 Mandatory / Optional / Conditional 

Federal Office for Information Security 

85 

8 Service Definitions 

|**Parameter ID**|**M/O/C8**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`Intermediate`<br>`FingerFeedback`|M|Returns the`Fin`<br>`gerFeedback`node<br>of the TR-03121<br>XML Schema (see<br>`hlbs6v1.xsd`) con<br>taining all relevant<br>quality, PAD and uni<br>queness informati<br>on to assist the opera<br>tor in his or her qua<br>lity assessment. This<br>feedback SHALL on<br>ly be returned for the<br>manual operator as<br>sessment after a fin<br>ger capture has been<br>made.|`xsd:`<br>`string`|See TR-03121 XML Schema|
|`Intermediate`<br>`ControlVerificati`<br>`on`<br>`Feedback`|O|Returns the result of<br>the control verifica<br>tion. This feedback<br>SHALL be returned<br>for the manual opera<br>tor assessment.|`xsd:`<br>`string`|`undetermined`<br>(Application was unable to re<br>ceive a verification result),<br>`successful`<br>(Application determined a<br>match between a reference<br>and the captured fingerprint),<br>`failed`<br>(Application determines a no<br>match between captured fin<br>gerprint and reference finger<br>print, but a match between<br>captured fingerprint and ano<br>ther finger of the set of refe<br>rence fingerprints)|



**Table 8.24** Rolled Fingerprint Acquisition Feedback Elements 

## 8.5.5 Results 

The `getResults` operation returns the `resultElements*` as `hlbs:KeyValue` . The key-value pairs that SHALL be returned are shown in Table 8.25. The possible results of Table 8.24 SHALL also be part of the `service DescriptionXML` that is returned with the `getServiceDescription` . 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`Result`|Description of the result of the fingerprint<br>image acquisition.|`xsd:`<br>`string`|`Success`<br>(acquisition success<br>ful),<br>`DiscardAll`<br>(discard all and re-<br>start total acquisition<br>process),<br>`Canceled`,<br>(acquisition canceled)|



> 8 Mandatory / Optional / Conditional 

Federal Office for Information Security 

86 

8 Service Definitions 

|**Parameter ID**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|
|`FingerAcquisition`|Contains the full XML root element`Finge`<br>`rAcquisition`(see TR-03121 XML`bioty`<br>`pes6v1.xsd`), which logs the entire acquisition<br>process, information about quality, PAD and<br>uniqueness as well as the finally accepted fin<br>gerprint(s) as record(s). The data format, com<br>pression and file size of the record SHALL com<br>ply with the configured`ApplicationProfile`.|`xsd:`<br>`string`|See TR-03121 XML<br>Schema|



**Table 8.25** Rolled Fingerprint Acquisition Result Elements 

## 8.6 Service Definition for Self-Service System 

In this section HLBS service definitions are given that are used for external evaluation of biometric acquisiti on components within self-service systems (SSSs) individually without executing the entire SSS process. The service definitions stated below mirrors feedback that is shown to the biometric subject infront of the SSS and returns a result that would also be returned in productive mode. Currently, this service definition is only intended for the BCL volume of this technical guideline. 

## 8.6.1 Automated Acquisition of Slap Fingerprints 

## 8.6.1.1 ServiceInformation 

When the `getAllServices` operation is requested at least the `hlbs:ServiceInformation` shown in Ta ble 8.26 SHALL be returned. Further parameters are vendor specific and SHALL be set as well. 

|**Parameter ID**|**Description**|**Type**|**Value**|
|---|---|---|---|
|`Id`|Unique UUID of the ser<br>vice.|`xsd:`<br>`string`|`eb299a2a-00e6-4e3d-a569-d1e4cf`<br>`d2e8fa`|
|`Name`|Name of the service.|`xsd:`<br>`string`|`Automated Acquisition Slap Fin`<br>`gerprints SSS`|
|`Version`|Version of BSI TR-03121 of<br>the implemented service.|`xsd:`<br>`string`|`7.0`|



**Table 8.26** Automated Acquisition of Slap Fingerprints ServiceInformation 

## 8.6.1.2 Configuration 

At least the configuration options listed in Table 8.27 SHALL be available for the `configureService` ope ration. These configuration options including their allowed and default values SHALL also be part of the `ser viceDescriptionXML` that is returned with the `getServiceDescription` operation. 

|**Parameter ID**|**M/O9**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`Purpose`|M|The purpose of the finger<br>print image acquisition.|`hlbs:`<br>`ServiceType`|`enrolment`,`verifica`<br>`tion`|
|`RequestSlaps`|M|Request the acquisition of<br>the right and/or left hand<br>slap.|`hlbs:`<br>`BiometricCodeList`|`hlbs:`<br>`Iso19794FingerCode`<br>`13`and/or`14`is expected<br>within the list.|
|`TimeoutMs`|M|Maximum time in ms after<br>which the acquisition pro<br>cess will abort, in case no<br>fingerprints have been ac<br>quired.|`xsd:int`|_Arbitrary value_<br>(default:`0`)|



> 9 Mandatory / Optional 

Federal Office for Information Security 

87 

8 Service Definitions 

|**Parameter ID**|**M/O9**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`SlapClassifier`|O|Configures whether the slap<br>classification shall be per<br>formed or not. This SHALL<br>only have effect when a slap<br>acquisition is performed<br>(see`FingerprintsToAc`<br>`quire`).|`xsd:`<br>`string`|`activated`(default),<br>`deactivated`,<br>`evaluation`(classifica<br>tion is only performed<br>for internal evaluation<br>purposes)|



**Table 8.27** Automated Acquisition of Slap Fingerprints Configuration 

## 8.6.1.3 User Commands 

When the `signalUserCommand` operation is executed the user commands shown in Table 8.28 SHALL be supported by the service. In case a user command is not allowed at a certain point of time during the execution of the service the user SHALL be informed via the `getServiceFeedback` operation. The user commands of Table 8.28 SHALL also be present within the `serviceDescriptionXML` that is returned with the `getService Description` operation. 

|**Parameter ID**|**Description**|
|---|---|
|`Cancel`|Abort/Terminate the running service. Command SHALL be executable at any time.|



**Table 8.28** Automated Acquisition of Slap Fingerprints UserCommands 

## 8.6.1.4 Feedback 

Within the `hlbs:Feedback` the `feedbackElements*` of Table 8.29 as `hlbs:KeyValue` SHALL be returned. Furthermore the `userCommands*` SHALL contain the `hlbs:UserCommandInfo` for each implemented `hlbs:U serCommand` . The possible `feedbackElements*` of Table 8.29 SHALL also be part of the `serviceDescriptionXML` that is returned with the `getServiceDescription` . 

|**Parameter ID**|**M/O10**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`ExpectedSlap`|M|Indicates which<br>slap is currently ex<br>pected to be captu<br>red.|`hlbs:`<br>`Iso19794`<br>`FingerCode`|`13`or`14`|



> 9 Mandatory / Optional 

> 10 Mandatory / Optional 

Federal Office for Information Security 

88 

8 Service Definitions 

|**Parameter ID**|**M/O10**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`LiveInformation`|M|Transmission of<br>status information<br>during the conti<br>nuous capture pro<br>cess (live view) for<br>further processing<br>within the client<br>software.|`xsd:`<br>`string`|`Initializing`<br>(service initializes),<br>`SearchingSlap`<br>(searching for slap),<br>`SlapRecognized`<br>(slap detected),<br>`Capturing`<br>(capture is running),<br>`ReduceSlapPressure`<br>(slap is placed with too<br>much pressure),<br>`RaiseSlapPressure`<br>(slap is placed with too less<br>pressure or is placed partly<br>in the air),<br>`MoveSlapLeft`<br>(slap is too far right),<br>`MoveSlapRight`<br>(slap is too far left),<br>`MoveSlapForward`<br>(slap is too far back),<br>`MoveSlapBackward`<br>(slap is too far ahead),<br>`KeepStill`<br>(fingers are too much in<br>movement)|
|`LiveFingerprint`<br>`Image`|O|Contains a live<br>image of the con<br>stantly acquired<br>live stream of the<br>fingerprint scan<br>ner.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is ex_<br>_pected._|
|`LiveEnvironment`<br>`SurveillanceImage`|O|Contains a live<br>image of the con<br>stantly acquired<br>live stream of the<br>enviroment sur<br>veillance camera.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is ex_<br>_pected._|
|`LiveFingerprint`<br>`Scanner`<br>`SurveillanceImage`|O|Contains a live<br>image of the con<br>stantly acquired<br>live stream of the<br>fingerprint scanner<br>surveillance came<br>ra.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is ex_<br>_pected._|



**Table 8.29** Automated Acquisition of Slap Fingerprints Feedback Elements 

## 8.6.1.5 Results 

The `getResults` operation returns the `resultElements*` as `hlbs:KeyValue` . The key-value pairs that SHALL be returned are shown in Table 8.30. The possible results of Table 8.29 SHALL also be part of the `service DescriptionXML` that is returned with the `getServiceDescription` . 

> 10 Mandatory / Optional 

Federal Office for Information Security 

89 

8 Service Definitions 

|**Parameter ID**|**M/O11**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`Result`|M|Description of the result<br>of the fingerprint image<br>acquisition.|`xsd:`<br>`string`|`Success`<br>(acquisition successful),<br>`Canceled`<br>(acquisition canceled),<br>`Timeout`<br>(acquisition aborted by<br>system due to timeout),<br>`BiometricSubject`<br>`Disappeared`<br>(acquisition aborted by<br>system due to disap<br>pearance of biometric<br>subject),<br>`FingerAmount`<br>`Mismatch`<br>(acquisition failed due to<br>finger amount mismatch<br>for final slap image)|
|`FingerAcquisition`|M|Contains the full XML<br>root element`FingerAc`<br>`quisition`(see TR-03121<br>XML`biotypes6v1.xsd`)<br>with all relevant informa<br>tion about the process in<br>cluding its results as re<br>cords. The requirements<br>of the SSS Application<br>Profile of the BCL Volu<br>me of this technical gui<br>deline apply.|`xsd:`<br>`string`|See TR-03121 XML Sche<br>ma|



**Table 8.30** Automated Acquisition of Slap Fingerprints Result Elements 

## 8.6.2 Automated Acquisition of Facial Images 

## 8.6.2.1 ServiceInformation 

When the `getAllServices` operation is requested at least the `hlbs:ServiceInformation` shown in Ta ble 8.31 SHALL be returned. Further parameters are vendor specific and SHALL be set as well. 

|**Parameter ID**|**Description**|**Type**|**Value**|
|---|---|---|---|
|`Id`|Unique UUID of the service.|`xsd:`<br>`string`|`457b3255-568b-43ab-b63c-`<br>`ccdd120da1fa`|
|`Name`|Name of the service.|`xsd:`<br>`string`|`Automated Acquisition Facial`<br>`Images SSS`|
|`Version`|Version of BSI TR-03121 of<br>the implemented service.|`xsd:`<br>`string`|`7.0`|



**Table 8.31** Automated Acquisition of Facial Images ServiceInformation 

## 8.6.2.2 Configuration 

At least the configuration options listed in Table 8.32 SHALL be available for the `configureService` ope ration. These configuration options including their allowed and default values SHALL also be part of the `ser viceDescriptionXML` that is returned with the `getServiceDescription` operation. 

> 11 Mandatory / Optional 

Federal Office for Information Security 

90 

8 Service Definitions 

|**Parameter ID**|**M/O12**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`Purpose`|M|The purpose of the facial<br>image acquisition.|`hlbs:`<br>`ServiceType`|`enrolment`,`verifica`<br>`tion`|
|`TimeoutMs`|M|Maximum time in ms after<br>which the acquisition pro<br>cess will abort, in case no fa<br>cial images have been acqui<br>red.|`xsd:int`|_Arbitrary value_<br>(default:`0`)|



**Table 8.32** Automated Acquisition of Facial Images Configuration 

## 8.6.2.3 User Commands 

When the `signalUserCommand` operation is executed the user commands shown in Table 8.33 SHALL be supported by the service. In case a user command is not allowed at a certain point of time during the execution of the service the user SHALL be informed via the `getServiceFeedback` operation. The user commands of Table 8.33 SHALL also be present within the `serviceDescriptionXML` that is returned with the `getService Description` operation. 

|**Parameter ID**|**Description**|
|---|---|
|`Cancel`|Abort/Terminate the running service. Command SHALL be executable at any time.|



**Table 8.33** Automated Acquisition of Facial Images UserCommands 

## 8.6.2.4 Feedback 

Within the `hlbs:Feedback` the `feedbackElements*` of Table 8.34 as `hlbs:KeyValue` SHALL be returned. Furthermore the `userCommands*` SHALL contain the `hlbs:UserCommandInfo` for each implemented `hlbs:U serCommand` . The possible `feedbackElements*` of Table 8.34 SHALL also be part of the `serviceDescriptionXML` that is returned with the `getServiceDescription` . 

> 12 Mandatory / Optional 

Federal Office for Information Security 

91 

8 Service Definitions 

|**Parameter ID**|**M/O13**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`LiveInformation`|M|Transmission of sta<br>tus information du<br>ring the continuous<br>capture process (live<br>view) for further<br>processing within<br>the client software.|`xsd:`<br>`string`|`Initializing`<br>(service initializes),<br>`SearchingFace`<br>(searching for face),<br>`FaceRecognized`<br>(face detected),<br>`Capturing`<br>(capture is running),<br>`StepBack`<br>(face is too close),<br>`StepForward`<br>(face is too far in the back<br>ground),<br>`MoveLeft`<br>(face is too far right),<br>`MoveRight`<br>(face is too far left),<br>`MoveUp`<br>(face is too far down),<br>`MoveDown`<br>(face is too far up),<br>`StandStill`<br>(face is too much in move<br>ment),<br>`LookStraight`<br>(face is not facing frontal),<br>`OpenEyes`<br>(eyes are closed),<br>`CloseMouth`<br>(mouth is opened),<br>`MultipleFaces`<br>(multiple faces detected)|
|`LiveFacial`<br>`Image`|O|Contains a live<br>image of the con<br>stantly acquired live<br>stream of the facial<br>image camera.|`hlbs:`<br>`Image`|_Image in a common data for_<br>_mat (e.g. jpeg or bmp) is ex_<br>_pected._|



**Table 8.34** Automated Acquisition of Facial Images Feedback Elements 

## 8.6.2.5 Results 

The `getResults` operation returns the `resultElements*` as `hlbs:KeyValue` . The key-value pairs that SHALL be returned are shown in Table 8.35. The possible results of Table 8.34 SHALL also be part of the `service DescriptionXML` that is returned with the `getServiceDescription` . 

> 13 Mandatory / Optional 

Federal Office for Information Security 

92 

8 Service Definitions 

|**Parameter ID**|**M/O14**|**Description**|**Type**|**Possible Values**|
|---|---|---|---|---|
|`Result`|M|Description of the result<br>of the facial image ac<br>quisition.|`xsd:`<br>`string`|`Success`<br>(acquisition successful),<br>`Canceled`<br>(acquisition canceled),<br>`Timeout`<br>(acquisition aborted by<br>system due to timeout),<br>`BiometricSubject`<br>`Disappeared`<br>(acquisition aborted by<br>system due to disap<br>pearance of biometric<br>subject)|
|`FaceAcquisition`|M|Contains the full XML<br>root element`Face`<br>`Acquisition`(see<br>TR-03121 XML`bioty`<br>`pes6v1.xsd`) with all<br>relevant information<br>about the process in<br>cluding its results as re<br>cords. The requirements<br>of the SSS Application<br>Profile of the BCL Volu<br>me of this technical gui<br>deline apply.|`xsd:`<br>`string`|See TR-03121 XML Sche<br>ma|



**Table 8.35** Automated Acquisition of Facial Images Result Elements 

> 14 Mandatory / Optional 

Federal Office for Information Security 

93 

List of Abbreviations 

## List of Abbreviations 

|**Abbreviation**|**Description**|
|---|---|
|API|Application Programming Interface|
|BioAPI|Biometric Application Programming Interface|
|BSP|Biometric Service Provider|
|CIR|Central Identity Register|
|DHCP|Dynamic Host Configuration Protocol|
|FIAS|Facial Image Acqisition System|
|GUI|graphical user interface|
|HLBS|High Level Biometric Services|
|IPv4|Internet Protocol Version 4|
|IPv6|Internet Protocol Version 6|
|SOAP|Simple Object Access Protocol|
|SSS|self-service system|
|TCP/IP|Transmission Control Protocol/Internet Protocol|
|TLS|Transport Layer Security|
|UI|User Interface|
|USB|Universal Serial Bus|



Federal Office for Information Security 

94 

Bibliography 

## Bibliography 

- [BIB_ISO_19794_FACE] _ISO/IEC 19794-5:2005 "Information technology – Biometric data interchange formats – Part 5: Face image data"._ 

- [BIB_ISO_19794_FINGER] _ISO/IEC 19794-4:2005 "Information technology – Biometric data interchange formats – Part 4: Finger image data"._ 

- [BIB_ISO_IRIS] _ISO/IEC 19794-6:2005 "Information technology – Biometric data interchange formats - Part 6: Iris image data"._ 

- [BIB_ISO_MINUTIAE] _ISO/IEC 19794-2:2005 "Information technology – Biometric data interchange formats – Part 2: Finger minutiae data"._ 

- [BIB_RFC2119] _RFC 2119: Key words for use in RFCs to Indicate Requirement Levels._ 

Federal Office for Information Security 

95 

Bibliography 

Federal Office for Information Security 

96 


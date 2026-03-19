## BSI Technical Guideline 03125 Preservation of Evidence of Cryptographically Signed Documents 

## Annex TR-ESOR-C.2: 

Conformity Test Specification (Level 2   Technical Conformity) Designation Technical Conformity Test Specification (Level 2) Abbreviation BSI TR-ESOR-C.2 Version 1.3 update 2 (on base of the eIDAS-Regulation and ETSI Preservation Standards with a new certification scheme including a new version of C.2-Testbed with support for ETSI TS 119 512)) 

Date 06.05.2025 

## Document history 

|Version|Date|Editor|Description|
|---|---|---|---|
|1.3|31.03.2022|BSI|TR-ESOR-C.2|
|1.3 (update 1)|22.03.2023|BSI|First<br>update<br>of<br>TR-<br>ESOR-C.2 v. 1.3|
|1.3 (update 2)|06.05.2025|BSI|Third update of TR-<br>ESOR-C.2<br>v.1.3<br>(TR-<br>S.512)|



Table 1: Document history 

Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn Tel.: +49 22899 9582- 0 E-Mail:  tresor@bsi.bund.de Internet: https://www.bsi.bund.de © Federal Office for Information Security 2025 

Table of Contents 

## Table of Contents 

|1|Introduction ............................................................................................................................................................................................ 5|Introduction ............................................................................................................................................................................................ 5|Introduction ............................................................................................................................................................................................ 5|Introduction ............................................................................................................................................................................................ 5|Introduction ............................................................................................................................................................................................ 5|Introduction ............................................................................................................................................................................................ 5|
|---|---|---|---|---|---|---|
|2|Overview ................................................................................................................................................................................................... 8||||||
|3|Web Service Interfaces||..................................................................................................................................................................... 11||||
||3.1<br>Test suite for TR-S.4-interface and additional TR-S.512-interface .................................................................. 11||||||
||3.1.1<br>Test environment ............................................................................................................................................................... 11||||||
||3.2<br>Standard Test Configurations ............................................................................................................................................ 12||||||
||3.2.1<br>CONFIG_Common ............................................................................................................................................................. 12||||||
||3.2.2<br>CONFIG_ArchiSafe_C.2 .................................................................................................................................................... 13||||||
||3.2.3<br>CONFIG_LXAIP|||(conditional) ....................................................................................................................................... 13|||
||3.2.4<br>CONFIG_S.4|(conditional)|||............................................................................................................................................... 13||
||3.2.5<br>CONFIG_S.512||(conditional)|||.......................................................................................................................................... 14|
||3.3<br>Standard Test Objects ............................................................................................................................................................ 14||||||
||3.4<br>Mandatory Tests ....................................................................................................................................................................... 26||||||
||3.4.1<br>Tests of the TR-S.4-interface ......................................................................................................................................... 26||||||
||3.4.1.1<br>Function RetrieveInfo of S.4-interface .......................................................................................................... 26||||||
||3.4.1.2<br>Function ArchiveSubmission of S.4-interface ............................................................................................ 30||||||
||3.4.1.3<br>Function ArchiveUpdate of S.4-interface ..................................................................................................... 49||||||
||3.4.1.4<br>Function ArchiveRetrieval of S.4-interface ................................................................................................. 60||||||
||3.4.1.5<br>Function ArchiveEvidence of S.4-interface ................................................................................................. 66||||||
||3.4.1.6<br>Function ArchiveDeletion of S.4-interface .................................................................................................. 75||||||
||3.4.1.7<br>Function Verify of S.4-interface ........................................................................................................................ 81||||||
||3.4.1.8<br>Additional tests of S.4-interface ..................................................................................................................... 108||||||
||3.4.2<br>Tests of the TR-S.512-interface ................................................................................................................................. 119||||||
||3.4.2.1<br>Function RetrieveInfo of S.512-interface .................................................................................................. 119||||||
||3.4.2.2<br>Function PreservePO of S.512-interface .................................................................................................... 122||||||
||3.4.2.3<br>Function UpdatePOC of S.512-interface .................................................................................................... 142||||||
||3.4.2.4<br>Function RetrievePO of S.512-interface ..................................................................................................... 155||||||
||3.4.2.5<br>Function DeletePO of S.512-interface ......................................................................................................... 172||||||
||3.4.2.6<br>Function ValidateEvidence of S.512-interface ........................................................................................ 178||||||
||3.4.2.7<br>Additional tests of S.512-interface ................................................................................................................ 203||||||
|4|TR-ESOR-C.2-Testbed how-to .................................................................................................................................................. 215||||||
||4.1<br>TR-ESOR-C.2-Testbed Prerequisites............................................................................................................................ 215||||||
||4.2<br>TR-ESOR-C.2-Testbed introduction ............................................................................................................................ 215||||||
||4.2.1<br>Subdirectory DOCKERS................................................................................................................................................ 216||||||
||4.2.2<br>Subdirectory ERVT-UPLOADs .................................................................................................................................. 216||||||
||4.2.3<br>Subdirectory LXAIP-UPLOADs ................................................................................................................................. 216||||||



Introduction 

|4.2.4|Subdirectory PROPERTIES ......................................................................................................................................... 216|
|---|---|
|4.2.5|Subdirectory RUN-DATA ............................................................................................................................................ 216|
|4.2.6|Subdirectory TESTDATA ............................................................................................................................................. 216|
|4.2.7|Subdirectory XSVT-UPLOADs .................................................................................................................................. 217|
|4.2.8|File TR-ESOR-1.3.0-C2-Testbed-soapui-project.xml ..................................................................................... 217|
|4.2.9|File BSI TR-03125_C.2_V1.3.pdf ................................................................................................................................ 217|
|4.3|TR-ESOR-C.2-Testbed configuration .......................................................................................................................... 217|
|4.4|TR-ESOR-C.2-Testbed: configuration and start of XSVT and ERVT ............................................................ 219|
|4.5|TR-ESOR-C.2-Testbed usage ........................................................................................................................................... 221|
|4.6|TR-ESOR-C.2-Testbed<br>final documentation ....................................................................................................... 222|
|4.7|TR-ESOR-C.2-Testbed results ......................................................................................................................................... 224|



## Table of Figures 

|Figure|1: Schematic Depiction of the IT Reference Architecture withTR-S.4.................................................................. 6|
|---|---|
|Figure|2: Schematic Depiction of the IT Reference Architecture withTR-S.512............................................................. 6|
|Figure|3: Overview of the BSI TR-ESOR-C.2-Testbed environment (version 1.3 update 3) ...................................... 12|
|Figure|4: TR-ESOR-C.2-Testbed<br>project directory structure. ............................................................................................ 215|
|Figure|5: Example output of dbuild.cmd/dbuild.sh. ................................................................................................................. 219|
|Figure|6: Final statement of initialization of XSVT. ................................................................................................................... 220|
|Figure|7: Final statement of initialization of ERVT. .................................................................................................................. 220|
|Figure|8: Sample output of dstatus.cmd/dstatus.sh .................................................................................................................. 221|
|Figure|9: Sample output of dstart.cmd/dstart.sh. ....................................................................................................................... 221|



Federal Office for Information Security 

4 

Introduction 

## 1 Introduction 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0005-02.png)


specify technical security requirements for the long-term preservation of evidence of cryptographically signed electronic documents and data along with associated electronic administrative data (meta data). 

A Middleware defined for this purpose (TR-ESOR-Middleware) in the sense of this Guideline includes all of the modules (M) and interfaces (S) [for the Germa authenticity and proving the integrity of the stored documents and data. 

The Reference Architecture introduced in the Main Document of this Technical Guideline consists of the interfaces, functions and logical units described in the following: 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0005-06.png)



![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0005-07.png)



![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0005-08.png)



![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0005-09.png)



![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0005-10.png)


- the TR-S.4 and the TS119512 input interface TR-S.512 according to profile [TR-ESORTRANS] of the TR-ESOR-Middleware, which serves to embed the TR-ESOR-Middleware in the existing IT and infrastructure landscape; 

- [TR-ESOR-M.1] ), which regulates the flow of information in the 

- Middleware, implements the security requirements for the interfaces with the IT applications and ensures that the application systems are decoupled from the ECM-/Long-term storage; -Module ( [TR-ESOR-M.2] ) and the associated interfaces TR-S.1 and TR- 

- S.3 that provide the required functions for creating hash values and verifying electronic signatures or seals or time-stamps, verifying electronic certificates, and for obtaining qualified electronic time stamps or (optional) electronic signatures or seals for the Middleware. Furthermore, it can provide the functions for the encryption and decryption of data and documents; 

- -Module ([ TR-ESOR-M.3] ) with the TR-S.6 interface that provides the required 

- functions for the preservation of evidence of the digitally signed documents; 

- an ECM-/Long-Term Storage with the TR-S.2 and TR-S.5 interfaces  that assumes the physical archiving/storage and also the storage of the meta data that preserve evidence. This ECM-/Long-Tterm Storage is no longer directly a part of the Technical Guideline, but requirements will be set for it through the two interfaces that are still part of the TR-ESORMiddleware. 

- The application layer that can include an XML-Adapter is not a direct part of this Technical Guideline, either, even though this XML-Adapter can be implemented as part of a Middleware. 

The IT Reference Architecture depicted in Figure 1 and Figure 2 is based on the ArchiSafe Reference Architecture and is supposed to enable and support the logical (functional) interoperability of future products with the objectives and requirements of the Technical Guideline. In principle, the upper interface of the TR-ESOR-Middleware is either the S.4-Interface (TR-S.4) pursuant to [TR-ESOR-E] , according to Figure 1, or the S.512-Interface (TR-S.512) pursuant to [ETSI TS 119 512] according to the profile [TR-ESOR-TRANS] , according to Figure 2. 

Introduction 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0006-01.png)


Figure 1: Schematic Depiction of the IT Reference Architecture with TR-S.4 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0006-03.png)


Figure 2: Schematic Depiction of the IT Reference Architecture with TR-S.512 

Federal Office for Information Security 

6 

Introduction 

The optional XML-Adapter and/or the optional TR-ESOR-512-Transformator[1] may be integrated under the following circumstances: 

- Both as separate components with two interfaces to the IT-application and the ArchiSafe-Module, 

- Both as separate components, but as parts of the IT-application with interfaces to the ArchiSafeModule 

- One common component, separate from the IT-application and including the XML-Adapter and TRESOR-512-Transformator as parts, with two interfaces to the IT-application and the ArchiSafeModule, 

- One common component including the XML-Adapter and TR-ESOR-512-Transformator as parts, which is part of the IT-application, with an interface to the ArchiSafe-Module. 

- [eIDAS-VO] to transform incoming ETSI TS119512 (V1.1.2) messages[2] into TR-S4 messages. These messages can be sent to an attached http://www.bsi.bund.de/EN/tr-esor system without any need for changing the system. 

The usage of the ETSI TS119512 TR-ESOR Transformator is recommended in case that a TR-ESOR-Product with a TR-S.4-Interface should be used in Europe supporting interoperability with other European (qualified) Preservation Services or Preservation Products. 

This Technical Guideline is modularly structured, and the individual annexes to the Main Document specify the functional and technological security requirements for the needed IT components and interfaces of the TR-ESOR-Middleware. The specifications are strictly platform, product and manufacturer independent. 

The document at hand bear -ESORconformity tests for the Conformity Level 2 (Technical Conformity) for TR-ESOR V1.3 supporting also the archive information package LXAIP, ASiC-AIP (not yet ready for certification), the Upload- and Downloadinterface and the upper ETSI TS 119 512-interface TR-S.512. 

Products that want to be certified pursuant to the Technical Guideline 03125 TR-ESOR shall prove their conformity pursuant to this document [TR-ESOR-C.2] and [TR-ESOR-C.1] . 

> 1 - See ETSI TS 119512 TR ESOR Transformator under an Open Source Licence 

> 2 In the profiling of [TR-ESOR-TRANS] 

Federal Office for Information Security 

7 

Overview 

## 2 Overview 

Products or systems, which want to become certified according to this Technical Guideline, have to demonstrate their conformance to the specifications. There are two defined conformance levels, which mainly differ in the technical detail specifications of interfaces and data formats used: 

- Conformity Level 1 Functional Conformity, 

- Conformity Level 2 Technical Conformity. 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0008-05.png)



![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0008-06.png)


in [TR-ESOR-C.1] . 

This document specifies the technical test criteria (tests) for reaching Conformity Level 1 (Technical Conformity), which are derived from the requirements and web service interfaces specified in Annex [TRESOR-E] , [TR-ESOR-F] , [TR-ESOR-ERS] and [TR-ESOR-VR] and complement the mandatory (red) tests for interface functions specified in section 5.5 of Annex [TR-ESOR-C.1] of the present Technical Guideline. 

The tests for Conformity Level 1 (Technical Conformity) aim at verifying technical interoperability between different components within the reference architecture as depicted in Figure 1 and Figure 2. For this purpose the present document specifies test cases for the different web service based interfaces (see section 3) and verification report structures for central data structures (see section [TR-ESOR-VR] ). 

Each test case is identified by a unique ID and specified in a semi-formal pseudo-code, which provides the basis for the technical implementation of the test cases in an appropriate test environment. 

In general, the optional elements of the request and response structures of the functional calls according Annex E are omitted. The usage or omission of these optional elements has no impact on the fulfilling on the conformance requirements of this specification. 

The tests of the web service based interfaces can be performed using the freely available SoapUI[3] test tool. 

All tests, which are required to be passed are marked with the color red. Tests, which are only applicable in certain situations are marked grey. All tests use the same basic configuration, which is denoted by CONFIG_ArchiSafe_C.2 in the following. In case, the TOT does support some additional features (e.g. LXAIP pursuant to [TR-ESOR-F] , chapter 3.2), corresponding additional configuration has to be taken into consideration (e.g. CONFIG_LXAIP). 

In order to become certified according to Conformity Level 1 Functional Conformity and Conformity Level 2 Technical Conformity, a product or system has to pass 

- all mandatory (red) conformity criteria (tests) for this Conformity Level 1 Functional Conformity pursuant to [TR-ESOR-C.1] and 

- all mandatory (red) conformity criteria (tests) for Conformity Level 2 technical Conformity pursuant to this document, [TR-ESOR-C.2] . 

If one or more tests, marked with the color red, are not successful, the conformity cannot be certified. 

Because [TR-ESOR-C.2] extends [TR-ESOR-C.1] , it is necessary for the testing body to assess the assessment criteria of [TR-ESOR-C.1] beforehand. 

NOTICE 1: 

In TR-ESOR-Version1.3 the three Archive Information Package (AIP) Archive Information Archive Data Object synonymously. 

> 3 See http://www.soapui.org . 

Federal Office for Information Security 

8 

Overview 

## NOTICE 2: 

The TR-ESOR input interface TR-S.4 or the TS119512 input interface TR-S.512 pursuant to the preservationAPI of [ETSI TS 119 512] in the profiling of [TR-ESOR-TRANS] shall be used which logicallycorresponds to the input-interface TR-S.4 of the TR-ESOR-Middleware [TR-ESOR-E] , as shown in the table 1 of [TR-ESORE], clause 4.1 . Another input interface instead of TR-S.4 or TR-S.512 is not allowed. To improve readability, the insertion of the TS119512-function calls, equivalent to TR-S.4, is renounced, at several places in this -S.4 or TR-S.512 shall - - . 

## NOTICE 3: 

In this TR-ESOR- Version, the word -ESOR-Annexes : 

- a) the XML[TR-ESOR-F], clause 3.1 as well as b) [TR-ESOR-F], clause 3.2 as well as - 

- c) the [TR-ESOR F], clause 3.3 on base of [ETSI EN 319162-1]. 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0009-06.png)


- 

- In general, this TR- 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0009-08.png)


- - renounced, and the footnote shall supported 

## NOTICE 4: 

In this TR-ESOR- Version, BIN is restricted to the following preservation object formats: 

- ASiC-ERS (in TR-ESOR v1.3 called ASiC-AIP) pursuant to [ETSI TS 119 512] , Annex A.3.1 and A.3.1.3 - 

- (http://uri.etsi.org/ades/ASiC/type/ASiC ERS) and pursuant to [TR-ESOR-F] , Clause 3.3); 

- CAdES pursuant to [ETSI TS 119 512] Annex A.1.1 (http://uri.etsi.org/ades/CAdES). If there is no MIME type filled, then the default application/cms is used; 

- XAdES pursuant to [ETSI TS 119 512] Annex A.1.2 (http://uri.etsi.org/ades/XAdES). If there is no MIME type filled, then the defaultapplication/xml is used; 

- PAdES pursuant to [ETSI TS 119 512] Annex A.1.3 (http://uri.etsi.org/ades/PAdES). If there is no MIME Type filled, then the default application/pdf is used; 

- - ASiC-E pursuant to [ETSI TS 119 512] Annex A.1.4 (http://uri.etsi.org/ades/ASiC/type/ASiC-E). If there is - 

- no MIME type filled, then the default application/vnd.etsi.asic e+zip is used; 

- ASiC-S pursuant to [ETSI EN 319 162] (http://uri.etsi.org/ades/ASiC/type/ASiC-S). If there is no MIME type filled, then the default application/vnd.etsi.asic-s+zip is used; 

- -DigestList pursuant to [ETSI TS 119 512] Annex A.1.6 (http://uri.etsi.org/19512/format/DigestList). If there is no MIME Type filled, then the default application/xml is used. 

In case of Upload- and Download-function the following format is allowed additionally: 

- - 

- Binary Data (BIN) as Octet Stream, which is stored in the ECM-/Longbut only, 

- if connected with a corresponding LXAIP and referenced there acc. to [TR-ESOR-F] , Sec. 3.2, 

- - - if appropriate, retrieved by a linked to a corresponding LXAIP or embedded in a XAIP and retrieved by an ArchiveRetrieval-Request and 

- - no Upload of XAIP, nor LXAIP, nor ASiC-AIP is possible. 

## ATTENTION 1: 

If implemented, an ASiC-AIP-Container pursuant to clause 3.3 in [TR-ESOR-F] shall be inserted in the TS119152-intefrace as a base64Binary-coded ASiC-AIP-Container with the - - Type=http://uri.etsi.org/ades/ASiC/type/ASiC ERS Attribute (see https://www.w3.org/TR/xmlschema 2/#base64Binary). 

In TR-ESOR V1.3, actually, ASiC-AIP is announced but it is still not released and does not lead to a certification. 

Federal Office for Information Security 

9 

Overview 

NOTICE 5: In the following text the term covers advanced electronic pursuant to [eIDAS-VO], Article 3(11), qualified electronic to [eIDAS-VO], Article 3(12) , advanced electronic to [eIDAS-VO], Article 3(26) and qualified electronic pursuant to [eIDAS-VO], Article 3(27) . Insofar, the documents signed by advanced electronic signatures or seals as documents signed by qualified electronic signatures or seals. 

In this TR the term cryptographic signed documents qualified signed documents pursuant to [eIDAS-VO], Article 3(12) or qualified sealed documents pursuant to [eIDAS-VO], Article 3(27) or qualified time-stamped documents pursuant to [eIDAS-VO], Article 3(34) (within the meaning of the eIDAS regulation) ) but also documents with advanced electronic signatures pursuant to [eIDAS-VO], Article 3(11) or with advanced electronic seals pursuant to [eIDAS-VO], Article 3(26) or with electronic time-stamps pursuant to [eIDAS-VO], Article 3(33) , as they are often used in the internal communication  of public authorities. The documents with simple signatures or seals based on other (e.g. non-cryptographic) technologies are not meant here. 

Federal Office for Information Security 

10 

Web Service Interfaces 

## 3 Web Service Interfaces 

As shown in Figure 1 and Figure 2 the reference architecture comprises different interfaces, which can be implemented by a TR-ESOR-compliant middleware product. The present specification defines test suites for the interface TR-S.4 (see section 3.4.1) and the interface TR-S.512 (see section 3.4.2), which comprise test cases for different functions (see section 3.1) using the different standard test objects as defined in section 3.3. 

## 3.1 Test suite for TR-S.4-interface and additional TR-S.512-interface 

The test suite for TR-S.4 contains the test cases for the following functions pursued to [TR-ESOR-E] , chapter 3: 

- RetrieveInfo (see section 3.4.1.1) 

- ArchiveSubmission (see section 3.4.1.2) 

- ArchiveUpdate (see section 3.4.1.3) 

- ArchiveRetrieval (see section 3.4.1.4) 

- ArchiveEvidence (see section 3.4.1.5) 

- ArchiveDeletion (see section 3.4.1.6) 

- Verify (see section 3.4.1.7) 

- Additional tests of S.4-interface (see section 3.4.1.8). 

The test suite for additional TR-S.512-interface contains the test cases for the following functions pursued to [TR-ESOR-E] , chapter 4: 

- RetrieveInfo (see section 3.4.2.1) 

- PreservePO (see section 3.4.2.2) 

- Update POC (see section 3.4.2.3) 

- RetrievePO (see section 3.4.2.4) 

- DeletePO (see section 3.4.2.5) 

- ValidateEvidence (see section 3.4.2.6) 

- Additional tests od S.512-interface (see section 3.4.2.7) 

## 3.1.1 Test environment 

Requirenment: 

(A3.1.1-1) Following figure describes the structure of the BSI-TR-ESOR-C.2-Testbed Environment (also called TR-C.2-Testbed Environment) in the version 1.3 (update 3), which shall be used in order to perform the test cases defined in this document, incl. TR-ESOR-Testclient (incl. implementing test cases and provided test data), tr-esor-AIP-eIDAS-SigValidator (XSV) and BSI-ErVerifyTool (ERVT). The results of the execution of all test cases shall be documented and provided to certification body (BSI). 

Federal Office for Information Security 

11 

Web Service Interfaces 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0012-01.png)


Figure 3: Overview of the BSI TR-ESOR-C.2-Testbed environment (version 1.3 update 3) 

The TR-ESOR-C.2-Testbed environment defines four separated domains: 

1. Target of Testing (ToT) it is the TR-ESOR version 1.3 (update 3) complied product to be tested against this test specification, 

2. BSI TR-ESOR-C.2-Testbed covers the implementation of the test cases as well as the integration of the BSI-Testtools, 

3. XSV-Verification-Service a verification service used by the tr-esor-AIP-eIDAS-SigValidator (AIPeIDAS-SigValidaor or simply XSV) in order to verify the supported signatures, seals and time-stamps (cf. https://github.com/de-bund-bsi-tr-esor/tr-esor-AIP-eIDAS-SigValidator), 

4. ERV-Verification-Service a verification service used by the BSI-ErVerifyTool (ERVerifyTool or simply ERV) in order to verify the archive time stamps obtained from provided evidence records (cf. - - - - 

https://github.com/de bund bsi tr esor/ERVerifyTool). 

The optional parts have The both verification tools XSVT and ERVT are able to work online, with activated optional verification service corresponding for the digital signatures/seals or timestamps, or offline. The verification services have to be integrated by the user itself, please refer to the corresponding documentation for more information, how to do that. 

## 3.2 Standard Test Configurations 

Here, a set of standard configurations of the test setup will be described. These setups are referenced in the test cases and should be used to actually perform the tests. 

## 3.2.1 CONFIG_Common 

This standard configuration shall apply for all tests. 

- The test setup shall contain the product to be tested (Target of Testing, TOT). 

- The user manual in the test setup shall refer at least to one preservation profile pursuant to [ETSI TS 119 512] , clause 5.4.7, to one actual preservation evidence policy pursuant to [ETSI TS 119 511] , clause 6.5 and to one actual signature validation policy pursuant to [ETSI TS 119 511] , clause 6.6. 

- The test setup shall contain all other modules of the reference architecture (including the storage) functionally not covered by the TOT. 

Federal Office for Information Security 

12 

Web Service Interfaces 

- The TOT and all other modules required shall be installed and configured according to the respective guidance including all security recommendations. 

- The TOT and all other modules shall be physically and logically interconnected. The connections shall be secured as described in the respective guidance documents (e.g. enabling encryption, explicit physical connection). 

- The BSI-ERVerifyTool shall be installed and running in a proper working mode (see chapter 3.1.1). 

- The BSI-AIP-eIDAS-SigValidator testing tool shall be installed and running in a proper working mode (see chapter 3.1.1). 

- The TOT shall provide at least one active Protection Profile and at least one inactive Protection Profile. 

- The TOT shall support Evidence Record pursued to [RFC4998] . 

The complete test setup shall be up and running and in an operational and working mode. 

## 3.2.2 CONFIG_ArchiSafe_C.2 

This configuration is based on CONFIG_Common and introduces following additional points: 

Additionally, the ArchiSafe-Module shall be configured as follows: 

- XAIP shall be mandatory. 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0013-12.png)


- -input of the POshall be 

- A XSD defining the XAIPs or LXAIPs pursuant to [TR-ESOR-F] shall be configured. 

- TOT shall support either TR-S.4-interface or TR-S.512-interface. 

- The validation of digital signatures/seals and electronic time stamps[4] during `ArchiveSubmission/PreservePO` and `ArchiveUpdate/UpdatePOC` shall be enabled. 

   - 3.2.3 CONFIG_LXAIP (conditional) 

This configuration is based on CONFIG_ArchiSafe_C.2. 

If LXAIP is implemented and CONFIG_LXAIP is configurable, then TOT does fullfill following requirenments in addition to level CONFIG_ArchiSafe_C.2: 

- TOT shall support LXAIP-format pursued to [TR-ESOR-F] , chapter 3.2. 

   - TOT shall support the Upload/Download-module. 

   - TOT shall support the retrieval of submitted LXAIP as transformed equivalent XAIP. 

      - 3.2.4 CONFIG_S.4 (conditional) 

This configuration is based on CONFIG_ArchiSafe_C.2. 

If TR-S.512 is implemented and CONFIG_S.4 is configurable, then TOT shall fullfill following requirenments in addition to level CONFIG_ArchiSafe_C.2: 

   - TOT shall support the TR-S.4-interface pursued to [TR-ESOR-E] , chapter 3. 

   - The TOT shall support the optional input parameter `pres:POFormat` while executing the function ArchiveRetrieval 

- 4 The validation of digital signatures/seals or electronic time stamps of documents included in the XAIP/LXAIP, DXAIP/DLXAIP or passed over as binary. 

Federal Office for Information Security 

13 

Web Service Interfaces 

- The XSD verification of XAIP/DXAIP containers during `ArchiveSubmission` and `ArchiveUpdate` shall be enabled. 

- The XSD verification of LXAIP/DLXAIP containers during `ArchiveSubmission` and `ArchiveUpdate` shall be enabled. (conditional, if CONFIG_LXAIP applies) 

- TOT shall support the following URI http://www.bsi.bund.de/tr-esor/lxaip/1.3 as value of `pres:POFormat` as optional input of `ArchiveRetrievalRequest` input parameter of `ArchiveRetrieval` function (c.f. [TR-ESOR-E], chapter 3.3.2). (conditional, if CONFIG_LXAIP applies) 

## 3.2.5 CONFIG_S.512 (conditional) 

This configuration is based on CONFIG_ArchiSafe_C.2. 

If TR-S.512 is implemented and CONFIG_S.512 is configurable, then TOT shall fullfill following requirenments in addition to level CONFIG_ArchiSafe_C.2: 

- TOT shall support the TR-S.512-interface pursued to [TR-ESOR-E] , chapter 4. 

- The XSD verification of XAIP/DXAIP containers during `PreservePO` and `UpdatePOC` shall be enabled. 

- The XSD verification of LXAIP/DLXAIP containers during `PreservePO` and `UpdatePOC` shall be enabled. (conditional, if CONFIG_LXAIP applies) 

- TOT shall support the following URI http://www.bsi.bund.de/tr-esor/lxaip/1.3 as value of `pres:POFormat` as optional input of `RetrievePO` input parameter of `RetrievePO` function (c.f. [TR-ESORE], chapter 3.3.2 and [ETSI TS 119 512], chapter 5.3.4.1.1). (conditional, if CONFIG_LXAIP applies) 

## 3.3 Standard Test Objects 

For most of the tests test data is required. In order to make the tests repeatable, this section defines some standard test objects. 

## **Notice** 

The used test data will be published by BSI as part of the open source application TR-ESOR-C.2-Testbed. It is strongly recommended to use the testbed and the corresponding test data while TR-ESOR product development for test purposes. 

|Container or Object Name|Description|
|---|---|
|ACTIVE_PROFILE|An active Preservation Profile supported by TOT.|
|ACTIVE_PROFILE_URI|The Profile Identifier as URI of ACTIVE_PROFILE.|
|INACTIVE_PROFILE|An inactive Preservation Profile supported by TOT.|
|INACTIVE_PROFILE_URI|The Profile Identifier as URI of INACTIVE_PROFILE.|
|UNKNOWN_PROFILE_URI|A Profile Identifier of an unknown profile.|
|UNKNOWN_OPT_INPUT|An unknown control as optional input.|
|XAIP_OK|The XAIP is syntactically correct and passes the defined consistency checks.<br>The XAIP contains following objects:<br>•<br>TXT_DATA.txt and<br>•<br>PDF_DATA.pdf as well as<br>•<br>one metadata object XML_MDO.xml embedded as binary metadata.|
|TXT_DATA.txt|A reference text-based test data (CRLF and CP1252).|
|PDF_DATA.pdf|A reference PDF test data.|
|XML_MDO.xml|A reference XML-based test data (LF and UTF-8).|
|XAIP_OK_V1_ER_OK|An evidence record provided by TOT for XAIP_OK.|



Federal Office for Information Security 

14 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|XAIP_OK_SIG_OK|The XAIP is syntactically correct and passes the defined consistency checks.<br>The XAIP containes following objects:<br>•<br>data object TXT_DATA.txt and<br>•<br>corresponding detached CAdES TXT_DATA.txt.p7s,<br>•<br>data object PDF_DATA.pdf and<br>•<br>corresponding detached CAdES PDF_DATA.pdf.p7s and<br>•<br>a metadata object XML_MDO.xml.|
|TXT_DATA.txt.p7s|A detached CAdES of TXT_DATA.txt.|
|PDF_DATA.pdf.p7s|A detached CAdES of PDF_DATA.pdf.|
|XAIP_OK_SIG_OK_V1_ER_OK|An evidence record provided by TOT for XAIP_OK_SIG_OK.|
|LXAIP_OK|The LXAIP is syntactically correct and passes the defined consistency checks.<br>The LXAIP references following data:<br>•<br>TXT_DATA.txt5as data object,<br>•<br>PDF_DATA.pdf as data object,<br>•<br>XML_MDO.xml as metadata object.|
|ASiC_AIP_OK|The ASiC-AIP is syntactically and passes the defined consistency checks. The<br>ASiC-AIP contains an LXAIP with two data objects and two corresponding<br>digital signatures and one metadata object.|
|REF_TXT_DATA_50|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_50.txt.|
|REF_PDF_DATA_50|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_50.pdf.|
|REF_XML_MDO_50|A reference to XML_MDO.xml, which has been uploaded in advance as<br>MDO_XML_50.xml.|
|LXAIP_OK_V1_ER_OK|An evidence record provided by TOT for LXAIP_OK.|
|LXAIP_OK_SIG_OK|The LXAIP is syntactically correct and passes the defined consistency checks.<br>The LXAIP references following data:<br>•<br>TXT_DATA.txt as data object,<br>•<br>TXT_DATA.txt.p7s as credential,<br>•<br>PDF_DATA.pdf as data object,<br>•<br>PDF_DATA.pdf.p7s as credential and<br>•<br>XML_MDO.xml as metadata object.|
|REF_TXT_DATA_51|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_51.txt.|
|REF_CADES_DET_TXT_DATA_51|A reference to TXT_DATA.txt.p7s, which has been uploaded in advance as<br>TXT_DATA_51.txt.p7s.|
|REF_PDF_DATA_51|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_51.pdf.|
|REF_CADES_DET_PDF_DATA_51|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_51.pdf.p7s.|
|REF_XML_MDO_51|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_51.xml.|
|LXAIP_OK_SIG_OK_V1_ER_OK|An evidence record provided by TOT for LXAIP_OK_SIG_OK.|
|XAIP_NOK|The<br>schema<br>validation<br>of<br>the<br>XAIP<br>fails.<br>(unexpected<br>element<br>`xaip:dataObject`in element`xaip:packageInfoUnit`)|
|XAIP_NOK_VERSION|The fix attribute`XAIPVersion`in the element`xaip:XAIP`has wrong value.|
|LXAIP_NOK|The<br>schema<br>validation<br>of<br>the<br>LXAIP<br>fails.<br>(missing<br>element<br>`ds:DigestValue`in element`asic:DataObjectReference`)|
|XAIP_NOK_EXPIRED|The<br>schema<br>validation<br>for<br>the<br>XAIP<br>succeeds,<br>but<br>the<br>`xaip:preservationInfo`-element indicates a preservation date, which is<br>already exceeded.|



> 5 Every instance of LXAIP or DLXAIP has to contain its own references. There is no possibility to share the references between two or more LXAIP or DLXAIP instances (c.f. M-ADD-03a in Chapter 3.4.1.8.5.). 

Federal Office for Information Security 

15 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|XAIP_NOK_SUBMTIME|The<br>schema<br>validation<br>for<br>the<br>XAIP<br>succeeds,<br>but<br>the<br>`xaip:submissionTime`-element deviates from the current time beyond a<br>reasonable tolerance range.<br>The documentation of the middleware or the module, which shall be tested,<br>shall contain some assertions and related conditions or constraints indicating<br>when the`xaip:submissionTime`contained in the provided XAIP deviates<br>too much from the current time.|
|XAIP_NOK_SIG|The XAIP is syntactically correct and passes the defined consistency checks,<br>but the XAIP contains an invalid digital signature.<br>Invalid digital signature means that the digital signature is syntactically not<br>correct or at least one of the evidence relevant data, for example a signature,<br>time-stamp, certificate, certificate revocation list or OCSP-response, etc., is<br>wrong.|
|XAIP_NOK_ER|The XAIP is syntactically correct and passes the defined consistency checks,<br>but the XAIP contains an invalid Evidence Record: ER_NOK_XAIP_OK.|
|ER_NOK_XAIP_OK|An invalid Evidence Record for XAIP_OK means, that the Evidence Record is<br>syntactically not correct or does not fulfil the requirements according to<br>Annex ERS.|
|XAIP_NOK_ER_VR|A verification report produced by the TOT for XAIP_NOK_ER.|
|LXAIP_OK_ER_NOK|The LXAIP is based on LXAIP_OK, syntactically correct and passes the defined<br>consistency checks, but the LXAIP contains an invalid Evidence Record:<br>ER_NOK_LXAIP_OK.|
|LXAIP_OK_ER_NOK_VR|A verification report produced by the TOT for LXAIP_OK_ER_NOK.|
|REF_TXT_DATA_52|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_52.txt.|
|REF_PDF_DATA_52|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_52.pdf.|
|REF_XML_MDO_52|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_52.xml.|
|ER_NOK_LXAIP_OK|An invalid Evidence Record for LXAIP_OK means, that the Evidence Record is<br>syntactically not correct or does not fulfil the requirements according to<br>Annex ERS.|
|CADES_ATT_OK|Alias for TXT_DATA.txt.p7m.|
|TXT_DATA.txt.p7m|A valid detached CAdES for TXT_DATA.txt.|
|XADES_ENVELOPED_OK|A valid attached enveloped XAdES.|
|XADES_ENVELOPING_OK|A valid attached enveloping XAdES.|
|PADES_OK|A valid visible PAdES.|
|ASiC_E_CADES_OK|A valid ASiC-E with a valid CAdES.|
|ASIC_E_XADES_OK|A valid ASiC-E with a valid XAdES.|
|ASIC_E_TST_OK|A valid ASiC-E with a valid timestamp.|
|ASIC_E_ER_OK|A valid ASiC-E with a valid evidence record.|
|DIGEST_LIST|A vlaid digest list.|
|ASiC_S_CADES_OK|A valid ASiC-S with a valid CAdES.|
|ASIC_S_XADES_OK|A valid ASiC-S with a valid XAdES.|
|ASIC_S_TST_OK|A valid ASiC-S with a valid timestamp.|
|ASIC_S_ER_OK|A valid ASiC-S with a valid evidence record.|
|CADES_ATT_NOK|An invalid attached CAdES.|
|CADES_ATT_NOK_VR|A verification report produced by TOT of CADES_ATT_NOK.|
|XADES_ENVELOPED_NOK|An invalid attached enveloped XAdES.|
|XADES_ENVELOPING_NOK|An invalid attached enveloping XAdES.|
|PADES_NOK|An invalid visible PAdES.ASIC_E_CADES_NOK|
|ASIC_E_CADES_NOK|A valid ASiC-E with invalid CAdES.|
|ASIC_E_XADES_NOK|A valid ASiC-E with invalid XAdES.|
|ASIC_E_TST_NOK|A valid ASiC-E with invalid timestamp.|
|ASIC_E_ER_NOK|A valid ASiC-E with invalid evidence record.|
|ASIC_S_CADES_NOK|A valid ASiC-S with invalid CAdES.|
|ASIC_S_XADES_NOK|A valid ASiC-S with invalid XAdES.|



Federal Office for Information Security 

16 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|ASIC_S_TST_NOK|A valid ASiC-S with invalid timestamp.|
|ASIC_S_ER_NOK|A valid ASiC-S with invalid evidence record.|
|DXAIP_OK|The DXAIP is syntactically correct and represents a valid update container<br>with version 2) for XAIP_OK (version 1), which contains the<br>corresponding AOID. Additional data: TXT_DATA.txt.p7m.|
|DXAIP_OK_2|The DXAIP is syntactically correct and represents a valid update container<br>with version 3) for XAIP_OK (in version 2), which contains the<br>corresponding AOID. Additional data:<br>•<br>XML_DATA.xml and<br>•<br>XML_DATA.xml.p7s.|
|XML_DATA.xml|A reference xml-based test data (CRLF and UTF-8).|
|XML_DATA.xml.p7s|A valid attached CAdES of XML_DATA.xml.|
|002-test-document.xml|Some other xml reference data for XAdES.|
|XADES_DET_OK|A valid detached XAdES of 002-test-document.xml.|
|XADES_DET_NOK_VR|A verification report of XADES_DET_OK, created by the TOT.|
|XADES_DET_NOK|An invalid detached XAdES of 002-test-document.xml.|
|XADES_DET_NOK_VR|A verification report of XADES_DET_NOK, created by TOT.|
|DXAIP_OK_SIG_ONLY|The DXAIP is syntactically correct and represents a valid update container<br>with version 2) for XAIP_OK (version 1), which contains the<br>corresponding AOID. Additional data:<br>•<br>TXT_DATA_QESI.txt.p7s.|
|TXT_DATA_QESI.txt.p7s|A valid detached CAdES of TXT_DATA.txt made with a test digital seal<br>certificate.|
|DLXAIP_OK|The DXAIP is syntactically correct and represents a valid update container<br>LXAIP_OK (with version 1), which contains the<br>corresponding AOID. DLXAIP references following data additionally:<br>•<br>TXT_DATA.txt.p7m.|
|REF_CADES_ATT_TXT_DATA_53|A reference to TXT_DATA.txt.p7m, which has been uploaded in advance as<br>TXT_DATA_53.txt.p7m.|
|DLXAIP_OK_2|The DXAIP is syntactically correct and represents a valid update container<br>LXAIP_OK (with version 2), which contains the<br>corresponding AOID. DLXAIP references following data additionaly:<br>•<br>XML_DATA.xml and<br>•<br>XML_DATA.xml.p7s .|
|REF_XML_DATA_54|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_54.xml.|
|REF_CADES_DET_XML_DATA_54|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_54.xml.p7s.|
|DXAIP_NOK_AOID|The schema validation for the Delta XAIP succeeds, but the update container|
|DXAIP_NOK|The Delta XAIP is syntactically not correct, the schema validation fails.|
|DLXAIP_NOK|The Delta LXAIP is syntactically not correct, the schema validation fails.|
|REF_TXT_DATA_55|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_55.txt.|
|REF_PDF_DATA_55|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_55.pdf.|
|REF_XML_MDO_55|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_55.xml.|
|REF_XML_DATA_56|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_56.xml.|
|REF_CADES_DET_XML_DATA_56|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_56.xml.p7s.|
|DXAIP_NOK_EXPIRED|The<br>schema<br>validation<br>for<br>the<br>Delta<br>XAIP<br>succeeds,<br>but<br>the<br>`xaip:preservationInfo`-element indicates a point in time in the past.|



Federal Office for Information Security 

17 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|DXAIP_NOK_SUBMTIME|The<br>schema<br>validation<br>for<br>the<br>Delta<br>XAIP<br>succeeds,<br>but<br>the<br>`xaip:submissionTime`-element deviates from the current time beyond a<br>reasonable tolerance range.<br>The documentation of the middleware or the module, whichshallbe tested,<br>shall contain some assertions and related conditions or constraints indicating<br>when the submission time contained in the provided XAIP deviates too much<br>from the current time|
|DXAIP_NOK_SIG|The schema validation for the Delta XAIP succeeds, but the XAIP contains an<br>invaliddigital signature.|
|DXAIP_NOK_SIG_VR|A verification report produced by TOT for DXAIP_NOK_SIG.|
|DXAIP_NOK_ER|The schema validation for the Delta LXAIP succeeds, but the Delta LXAIP<br>contains an invalid Evidence Record (invalid format).|
|DXAIP_NOK_ER_VR|A verification report produced by TOT for DXAIP_NOK_ER.|
|DLXAIP_NOK_ER|The schema validation for the Delta LXAIP succeeds, but the Delta LXAIP<br>contains an invalid Evidence Record (invalid format).|
|DLXAIP_NOK_ER_VR|A verification report produced by TOT of DLXAIP_NOK_ER.|
|ER_NOK_LXAIP_OK_V2|Incorrect evidence record (invalid format) of DLXAIP_NOK_ER.|
|REF_CADES_ATT_TXT_DATA_57|A reference to TXT_DATA.txt.p7m, which has been uploaded in advance as<br>TXT_DATA_57.txt.p7m.|
|DXAIP_NOK_VERSION|The schema validation for the XAIP succeeds, but there is a syntactical<br>collision with the original XAIP such that the schema validation for the<br>compound XAIP fails, for example, the element`xaip:prevVersion`in the<br>`xaip:updateSection`of the DXAIP is not the latest version of this XAIP.|
|REF_TXT_DATA_58|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_58.txt.|
|REF_PDF_DATA_58|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_58.pdf.|
|REF_XML_MDO_58|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_58.xml.|
|REF_CADES_ATT_TXT_DATA_59|A reference to TXT_DATA.txt.p7m, which has been uploaded in advance as<br>TXT_DATA_59.txt.p7m.|
|REF_CADES_ATT_TXT_DATA_60|A reference to TXT_DATA.txt.p7m, which has been uploaded in advance as<br>TXT_DATA_60.txt.p7m.|
|REF_XML_DATA_60-1|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_60-1.xml.|
|REF_CADES_DET_XML_DATA_60-1|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_60-1.xml.p7s.|
|XAIP_OK_V3_ER_OK|An evidence record for DXAIP_OK_2, created by TOT.|
|XAIP_OK_V2_ER_OK|An evidence record for DXAIP_OK, created by TOT.|
|LXAIP_OK_V3_ER_OK|An evidence record for DLXAIP_OK_2, created by TOT.|
|LXAIP_OK_V2_ER_OK|An evidence record for DLXAIP_OK, created by TOT.|
|XAIP_OK_SIG_OK_VR|A verification report for XAIP_OK_SIG_OK, created by TOT.|
|XAIP_OK_SIG_OK_ER|An evidence record for XAIP_OK_SIG_OK, created by TOT.|
|REF_TXT_DATA_61|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_61.txt.|
|REF_CADES_DET_TXT_DATA_61|A reference to TXT_DATA.txt.p7s, which has been uploaded in advance as<br>TXT_DATA_61.txt.p7s.|
|REF_PDF_DATA_61|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_61.pdf.|
|REF_CADES_DET_PDF_DATA_61|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_61.pdf.p7s.|
|REF_XML_MDO_61|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_61.xml.|
|LXAIP_OK_SIG_OK_ER|An evidence record of LXAIP_OK_SIG_OK, created by TOT.|
|DXAIP_OK_SIG_OK|A syntactically correct Delta-XAIP consisting of second version of<br>XAIP_OK_SIG_OK. DXAIP contains following additional data:<br>•<br>XML_DATA.xml and<br>•<br>XML_DATA.xml.p7s.|



Federal Office for Information Security 

18 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|DLXAIP_OK_SIG_OK|A syntactically correct Delta-XAIP consisting of second version of<br>LXAIP_OK_SIG_OK. DXAIP references following additionaly data:<br>•<br>XML_DATA.xml and<br>•<br>XML_DATA.xml.p7s.|
|REF_XML_DATA_62|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_62.xml.|
|REF_CADES_DET_XML_DATA_62|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_62.xml.p7s.|
|REF_XML_DATA_63|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_63.xml.|
|REF_CADES_DET_XML_DATA_63|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_63.xml.p7s.|
|REF_XML_DATA_64|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_64.xml.|
|REF_CADES_DET_XML_DATA_64|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_64.xml.p7s.|
|XAIP_OK_SIG_NOK|An<br>XAIP_OK_SIG_OK<br>containing<br>an<br>invalid<br>digital<br>signature<br>(TXT_DATA_NOK.txt.p7s).|
|TXT_DATA_NOK.txt.p7s|An invalid digital signatur of TXT_DATA.txt.|
|XAIP_OK_SIG_NOK_VR|A verification report of XAIP_OK_SIG_NOK created by the TOT.|
|XAIP_OK_SIG_OK_ER_NOK|An invalid evidence record of XAIP_OK_SIG_OK.|
|XAIP_OK_SIG_OK_ER_NOK_VR|A verification report of XAIP_OK_SIG_OK_ER_NOK created by the TOT|
|LXAIP_OK_SIG_NOK|An LXAIP_OK_SIG_OK referencing a single invalid digital signature<br>(TXT_DATA_NOK.txt.p7s).|
|REF_TXT_DATA_65|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_65.txt.|
|REF_CADES_DET_NOK_TXT_DATA_65|A reference to TXT_DATA_NOK.txt.p7s, which has been uploaded in advance<br>as TXT_DATA_65_NOK.p7s.|
|REF_PDF_DATA_65|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_65.pdf.|
|REF_CADES_DET_PDF_DATA_65|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_65.pdf.p7s.|
|REF_XML_MDO_65|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_65.xml.|
|LXAIP_OK_SIG_OK_VR|A verification report of LXAIP_OK_SIG_OK produced by TOT.|
|LXAIP_OK_SIG_NOK_VR|A verification report of LXAIP_OK_SIG_NOK created by TOT.|
|LXAIP_OK_SIG_OK_ER_NOK|A LXAIP_OK_SIG_OK containing additionally an invalid evidence record<br>(ER_NOK_XAIP_OK_SIG_OK_00).|
|LXAIP_OK_SIG_OK_ER_NOK_VR|A verification report of LXAIP_OK_SIG_OK_ER_NOK, created by the TOT.|
|REF_TXT_DATA_66|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_66.txt.|
|REF_CADES_DET_TXT_DATA_66|A reference to TXT_DATA_NOK.txt.p7s, which has been uploaded in advance<br>as TXT_DATA_66.txt.p7s.|
|REF_PDF_DATA_66|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_66.pdf.|
|REF_CADES_DET_PDF_DATA_66|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_66.pdf.p7s.|
|REF_XML_MDO_66|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_66.xml.|
|ER_NOK_XAIP_OK_SIG_OK_00|An invalid evidence record of LXAIP_OK_SIG_OK.|
|REF_TXT_DATA_67|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_67.txt.|
|REF_CADES_DET_NOK_TXT_DATA_67|A reference to TXT_DATA_NOK.txt.p7s, which has been uploaded in advance<br>as TXT_DATA_NOK_67.txt.p7s.|
|REF_PDF_DATA_67|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_67.pdf.|
|REF_CADES_DET_PDF_DATA_67|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_67.pdf.p7s.|



Federal Office for Information Security 

19 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|REF_XML_MDO_67|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_67.xml.|
|REF_TXT_DATA_68|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_68.txt.|
|REF_CADES_DET_TXT_DATA_68|A reference to TXT_DATA_NOK.txt.p7s, which has been uploaded in advance<br>as TXT_DATA_68.txt.p7s.|
|REF_PDF_DATA_68|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_68.pdf.|
|REF_CADES_DET_PDF_DATA_68|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance<br>asPDF_DATA_68.pdf.p7s.|
|REF_XML_MDO_68|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_68.xml.|
|DXAIP_OK_SIG_NOK|A<br>DXAIP_OK_SIG_OK<br>containing<br>an<br>invalid<br>digital<br>signature<br>(XML_DATA_NOK.xml.p7s).|
|XML_DATA_NOK.xml.p7s|An invalid detached electronic signature of XML_DATA.xml.|
|DXAIP_OK_SIG_NOK_VR|A verification report of DXAIP_OK_SIG_NOK created by the TOT.|
|DLXAIP_OK_SIG_NOK|A<br>DLXAIP_OK_SIG_OK<br>referencing<br>an<br>invalid<br>digital<br>signature<br>(XML_DATA_NOK.xml.p7s).|
|DXAIP_OK_SIG_NOK_VR|A verification report of DLXAIP_OK_SIG_NOK, created by the TOT.|
|REF_XML_DATA_69|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_69.xml.|
|REF_CADES_DET_NOK_XML_DATA_69|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_NOK_69.xml.p7s.|
|REF_XML_DATA_70|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_70.xml.|
|REF_CADES_DET_NOK_XML_DATA_70|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_NOK_70.xml.p7s.|
|CADES_DET_OK|A valid digital signature of TXT_DATA.txt.|
|CADES_DET_NOK|An invalid digital signature of TXT_DATA.txt.|
|CADES_DET_NOK_VR|A verification report of CADES_DET_NOK created by the TOT.|
|XADES_ENVELOPED_NOK_VR|A verification report of XADES_ENVELOPED_NOK created by the TOT.|
|XADES_ENVELOPING_NOK_VR|A verification report of XADES_ENVELOPING_NOK created by the TOT.|
|PADES_NOK_VR|A verification report of PADES_NOK created by the TOT.|
|ASIC_E_CADES_NOK_VR|A verification report of ASIC_E_CADES_NOK created by the TOT.|
|ASIC_E_XADES_NOK_VR|A verification report of ASIC_E_XADES_NOK created by the TOT.|
|ASIC_E_TST_NOK_VR|A verification report of ASIC_E_TST_NOK created by the TOT.|
|ASIC_E_ER_NOK_VR|A verification report of ASIC_E_ER_NOK created by the TOT.|
|ASIC_S_CADES_NOK_VR|A verification report of ASIC_S_CADES_NOK created by the TOT.|
|ASIC_S_XADES_NOK_VR|A verification report of ASIC_S_XADES_NOK created by the TOT.|
|ASIC_S_TST_NOK_VR|A verification report of ASIC_S_TST_NOK created by the TOT.|
|ASIC_S_ER_NOK_VR|A verification report of ASIC_S_ER_NOK created by the TOT.|
|ER_OK_SHA-1_XAIP_OK_SIG_OK|A valid evidence record of XAIP_OK_SIG_OK using a SHA-1 for building the<br>hash tree.|
|ER_OK_SHA-1_XAIP_OK_SIG_OK_VR|A verification report of ER_OK_SHA-1_XAIP_OK_SIG_OK created by the TOT.|
|ER_NOK_SHA-1_XAIP_OK_SIG_OK|A invalid evidence record of XAIP_OK_SIG_OK using a SHA-1 for building the<br>hash tree.|
|ER_NOK_SHA-1_XAIP_OK_SIG_OK_VR|A verification report of ER_NOK_SHA-1_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_OK_SHA-224_XAIP_OK_SIG_OK|A valid evidence record of XAIP_OK_SIG_OK using a SHA-224 for building the<br>hash tree.|
|ER_OK_SHA-224_XAIP_OK_SIG_OK_VR|A verification report of ER_OK_SHA-224_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_NOK_SHA-224_XAIP_OK_SIG_OK|A invalid evidence record of XAIP_OK_SIG_OK using a SHA-224 for building<br>the hash tree.|
|ER_NOK_SHA-224_XAIP_OK_SIG_OK_VR|A verification report of ER_NOK_SHA-224_XAIP_OK_SIG_OK created by the<br>TOT.|



Federal Office for Information Security 

20 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|ER_OK_SHA-256_XAIP_OK_SIG_OK|A valid evidence record of XAIP_OK_SIG_OK using a SHA-256 for building the<br>hash tree.|
|ER_OK_SHA-256_XAIP_OK_SIG_OK_VR|A verification report of ER_OK_SHA-256_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_NOK_SHA-256_XAIP_OK_SIG_OK|A invalid evidence record of XAIP_OK_SIG_OK using a SHA-256 for building<br>the hash tree.|
|ER_NOK_SHA-256_XAIP_OK_SIG_OK_VR|A verification report of ER_NOK_SHA-256_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_OK_SHA-384_XAIP_OK_SIG_OK|A valid evidence record of XAIP_OK_SIG_OK using a SHA-284 for building the<br>hash tree.|
|ER_OK_SHA-384_XAIP_OK_SIG_OK_VR|A verification report of ER_OK_SHA-384_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_NOK_SHA-384_XAIP_OK_SIG_OK|A invalid evidence record of XAIP_OK_SIG_OK using a SHA-384 for building<br>the hash tree.|
|ER_NOK_SHA-384_XAIP_OK_SIG_OK_VR|A verification report of ER_NOK_SHA-384_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_OK_SHA-512_XAIP_OK_SIG_OK|A valid evidence record of XAIP_OK_SIG_OK using a SHA-512 for building the<br>hash tree.|
|ER_OK_SHA-512_XAIP_OK_SIG_OK_VR|A verification report of ER_OK_SHA-512_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_NOK_SHA-512_XAIP_OK_SIG_OK|A invalid evidence record of XAIP_OK_SIG_OK using a SHA-512 for building<br>the hash tree.|
|ER_NOK_SHA-512_XAIP_OK_SIG_OK_VR|A verification report of ER_NOK_SHA-512_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_OK_SHA3-224_XAIP_OK_SIG_OK|A valid evidence record of XAIP_OK_SIG_OK using a SHA3-224 for building<br>the hash tree.|
|ER_OK_SHA3-224_XAIP_OK_SIG_OK_VR|A verification report of ER_OK_SHA3-224_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_NOK_SHA3-224_XAIP_OK_SIG_OK|A invalid evidence record of XAIP_OK_SIG_OK using a SHA3-224 for building<br>the hash tree.|
|ER_NOK_SHA3-224_XAIP_OK_SIG_OK_VR|A verification report of ER_NOK_SHA3-224_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_OK_SHA3-256_XAIP_OK_SIG_OK|A valid evidence record of XAIP_OK_SIG_OK using a SHA3-256 for building<br>the hash tree.|
|ER_OK_SHA3-256_XAIP_OK_SIG_OK_VR|A verification report of ER_OK_SHA3-256_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_NOK_SHA3-256_XAIP_OK_SIG_OK|A invalid evidence record of XAIP_OK_SIG_OK using a SHA3-256 for building<br>the hash tree.|
|ER_NOK_SHA3-256_XAIP_OK_SIG_OK_VR|A verification report of ER_NOK_SHA3-256_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_OK_SHA3-384_XAIP_OK_SIG_OK|A valid evidence record of XAIP_OK_SIG_OK using a SHA3-384 for building<br>the hash tree.|
|ER_OK_SHA3-384_XAIP_OK_SIG_OK_VR|A verification report of ER_OK_SHA3-384_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_NOK_SHA3-384_XAIP_OK_SIG_OK|A invalid evidence record of XAIP_OK_SIG_OK using a SHA3-384 for building<br>the hash tree.|
|ER_NOK_SHA3-384_XAIP_OK_SIG_OK_VR|A verification report of ER_NOK_SHA3-384_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_OK_SHA3-512_XAIP_OK_SIG_OK|A valid evidence record of XAIP_OK_SIG_OK using a SHA3-512 for building<br>the hash tree.|
|ER_OK_SHA3-512_XAIP_OK_SIG_OK_VR|A verification report of ER_OK_SHA3-512_XAIP_OK_SIG_OK created by the<br>TOT.|
|ER_NOK_SHA3-512_XAIP_OK_SIG_OK|A invalid evidence record of XAIP_OK_SIG_OK using a SHA3-512 for building<br>the hash tree.|
|ER_NOK_SHA3-512_XAIP_OK_SIG_OK_VR|A verification report of ER_NOK_SHA3-512_XAIP_OK_SIG_OK created by the<br>TOT.|
|XAIP_OK_V1_ER_OK_RESG|A valid evidence record of the first version of XAIP_OK, after successful<br>resigning operation on the hash tree has been finished.|
|XAIP_OK_V2_ER_OK_RESG|A valid evidence record of the second version of XAIP_OK and DXAIP_OK,<br>after successful resigning operation on the hash tree has been finished.|



Federal Office for Information Security 

21 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|XAIP_OK_V3_ER_OK_RESG|A valid evidence record of the third version of XAIP_OK and DXAIP_OK and<br>DXAIP_OK_2, after successful resigning operation on the hash tree has been<br>finished.|
|LXAIP_OK_V1_ER_OK_RESG|A valid evidence record of the first version of LXAIP_OK, after successful<br>resigning operation on the hash tree has been finished.|
|LXAIP_OK_V2_ER_OK_RESG|A valid evidence record of the second version of LXAIP_OK and DLXAIP_OK,<br>after successful resigning operation on the hash tree has been finished.|
|LXAIP_OK_V3_ER_OK_RESG|A valid evidence record of the third version of LXAIP_OK and DLXAIP_OK and<br>DLXAIP_OK_2, after successful resigning operation on the hash tree has been<br>finished.|
|XAIP_OK_V1_ER_OK_RESG_REH|The XAIP_OK_V1_ER_OK_RESG, after successful rehashing operation on the<br>hash tree has been finished.|
|XAIP_OK_V2_ER_OK_RESG_REH|The XAIP_OK_V2_ER_OK_RESG, after successful rehashing operation on the<br>hash tree has been finished.|
|XAIP_OK_V3_ER_OK_RESG_REH|The XAIP_OK_V3_ER_OK_RESG, after successful rehashing operation on the<br>hash tree has been finished.|
|LXAIP_OK_V1_ER_OK_RESG_REH|The LXAIP_OK_V1_ER_OK_RESG, after successful rehashing operation on the<br>hash tree has been finished.|
|LXAIP_OK_V2_ER_OK_RESG_REH|The LXAIP_OK_V2_ER_OK_RESG, after successful rehashing operation on the<br>hash tree has been finished.|
|LXAIP_OK_V3_ER_OK_RESG_REH|The LXAIP_OK_V3_ER_OK_RESG, after successful rehashing operation on the<br>hash tree has been finished.|
|REF_TXT_DATA_71|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_71.txt.|
|REF_PDF_DATA_71|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_71.pdf|
|REF_XML_MDO_71|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_71.xml.|
|REF_TXT_DATA_72|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_72.txt.|
|REF_PDF_DATA_72|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_72.pdf.|
|REF_XML_MDO_72|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_72.xml.|
|ER_NOK_LXAIP_OK_72|An invalid evidence record of LXAIP_OK.|
|REF_CADES_ATT_TXT_DATA_73|A reference to valid attached digital signature of TXT_DATA.txt, which has<br>been uploaded in advance as TXT_DATA_73.txt.p7m.|
|REF_TXT_DATA_74|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_74.txt.|
|REF_PDF_DATA_74|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_74.pdf.|
|REF_XML_MDO_74|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_74.xml.|
|XAIP_OK_SO|A valid XAIP containing only single data object:<br>•<br>TXT_DATA.txt.|
|ER_SO-1_OK_XAIP_OK_SO|A valid evidence record of XAIP_OK_SO, the hash value of the data object is<br>directly included in the message imprint of the timestamp:<br>•<br>ER(TSP(H(DO-01))).|
|ER_SO-2_OK_XAIP_OK_SO|A valid evidence record of XAIP_OK_SO, the hash value of the data object is<br>placed in the single reduced hash tree and the same hash value is included in<br>the message imprint of the timestamp:<br>•<br>ER(H(DO-01),TSP(H(DO-01))).|
|ER_SO-3_OK_XAIP_OK_SO|A valid evidence record of XAIP_OK_SO, the hash value of the data object is<br>placed in the single reduced hash tree and the hash value of those hash value<br>(computet hash tree root) is included in the message imprint of the timestamp:<br>•<br>ER(H(DO-01),TSP(H(H(DO-01))).|
|||
|REF_TXT_DATA_50b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_50.txt.|



Federal Office for Information Security 

22 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|REF_PDF_DATA_50b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_50.pdf.|
|REF_XML_MDO_50b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>MDO_XML_50.xml.|
|REF_TXT_DATA_51b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_51.txt.|
|REF_CADES_DET_TXT_DATA_51b|A reference to TXT_DATA.txt.p7s, which has been uploaded in advance as<br>TXT_DATA_51.txt.p7s.|
|REF_PDF_DATA_51b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_51.pdf.|
|REF_CADES_DET_PDF_DATA_51b|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_51.pdf.p7s.|
|REF_XML_MDO_51b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_51.xml.|
|REF_TXT_DATA_52b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_52.txt.|
|REF_PDF_DATA_52b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_52.pdf.|
|REF_XML_MDO_52b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_52.xml.|
|REF_CADES_ATT_TXT_DATA_53b|A reference to TXT_DATA.txt.p7m, which has been uploaded in advance as<br>TXT_DATA_53.txt.p7m.|
|REF_XML_DATA_54b|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_54.xml.|
|REF_CADES_DET_XML_DATA_54b|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_54.xml.p7s.|
|REF_TXT_DATA_55b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_55.txt.|
|REF_PDF_DATA_55b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_55.pdf.|
|REF_XML_MDO_55b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_55.xml.|
|REF_XML_DATA_56b|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_56.xml.|
|REF_CADES_DET_XML_DATA_56b|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_56.xml.p7s.|
|REF_CADES_ATT_TXT_DATA_57b|A reference to TXT_DATA.txt.p7m, which has been uploaded in advance as<br>TXT_DATA_57.txt.p7m.|
|REF_TXT_DATA_58b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_58.txt.|
|REF_PDF_DATA_58b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_58.pdf.|
|REF_XML_MDO_58b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_58.xml.|
|REF_CADES_ATT_TXT_DATA_59b|A reference to TXT_DATA.txt.p7m, which has been uploaded in advance as<br>TXT_DATA_59.txt.p7m.|
|REF_CADES_ATT_TXT_DATA_60b|A reference to TXT_DATA.txt.p7m, which has been uploaded in advance as<br>TXT_DATA_60.txt.p7m.|
|REF_XML_DATA_60-1b|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_60-1.xml.|
|REF_CADES_DET_XML_DATA_60-1b|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_60-1.xml.p7s.|
|REF_TXT_DATA_61b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_61.txt.|
|REF_CADES_DET_TXT_DATA_61b|A reference to TXT_DATA.txt.p7s, which has been uploaded in advance as<br>TXT_DATA_61.txt.p7s.|
|REF_PDF_DATA_61b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_61.pdf.|
|REF_CADES_DET_PDF_DATA_61b|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_61.pdf.p7s.|



Federal Office for Information Security 

23 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|REF_XML_MDO_61b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_61.xml.|
|REF_XML_DATA_62b|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_62.xml.|
|REF_CADES_DET_XML_DATA_62b|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_62.xml.p7s.|
|REF_XML_DATA_63b|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_63.xml.|
|REF_CADES_DET_XML_DATA_63b|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_63.xml.p7s.|
|REF_TXT_DATA_65b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_65.txt.|
|REF_CADES_DET_NOK_TXT_DATA_65b|A reference to TXT_DATA_NOK.txt.p7s, which has been uploaded in advance<br>as TXT_DATA_65_NOK.p7s.|
|REF_PDF_DATA_65b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_65.pdf.|
|REF_CADES_DET_PDF_DATA_65b|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_65.pdf.p7s.|
|REF_XML_MDO_65b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_65.xml.|
|REF_TXT_DATA_66b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_66.txt.|
|REF_CADES_DET_TXT_DATA_66b|A reference to TXT_DATA_NOK.txt.p7s, which has been uploaded in advance<br>as TXT_DATA_66.txt.p7s.|
|REF_PDF_DATA_66b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_66.pdf.|
|REF_CADES_DET_PDF_DATA_66b|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_66.pdf.p7s.|
|REF_XML_MDO_66b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_66.xml.|
|REF_TXT_DATA_67b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_67.txt.|
|REF_CADES_DET_NOK_TXT_DATA_67b|A reference to TXT_DATA_NOK.txt.p7s, which has been uploaded in advance<br>as TXT_DATA_NOK_67.txt.p7s.|
|REF_PDF_DATA_67b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_67.pdf.|
|REF_CADES_DET_PDF_DATA_67b|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance as<br>PDF_DATA_67.pdf.p7s.|
|REF_XML_MDO_67b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_67.xml.|
|REF_TXT_DATA_68b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_68.txt.|
|REF_CADES_DET_TXT_DATA_68b|A reference to TXT_DATA_NOK.txt.p7s, which has been uploaded in advance<br>as TXT_DATA_68.txt.p7s.|
|REF_PDF_DATA_68b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_68.pdf.|
|REF_CADES_DET_PDF_DATA_68b|A reference to PDF_DATA.pdf.p7s, which has been uploaded in advance<br>asPDF_DATA_68.pdf.p7s.|
|REF_XML_MDO_68b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_68.xml.|
|REF_XML_DATA_69b|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_69.xml.|
|REF_CADES_DET_NOK_XML_DATA_69b|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_NOK_69.xml.p7s.|
|REF_XML_DATA_70b|A reference to XML_DATA.xml, which has been uploaded in advance as<br>XML_DATA_70.xml.|
|REF_CADES_DET_NOK_XML_DATA_70b|A reference to XML_DATA.xml.p7s, which has been uploaded in advance as<br>XML_DATA_NOK_70.xml.p7s.|
|REF_TXT_DATA_71b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_71.txt.|



Federal Office for Information Security 

24 

Web Service Interfaces 

|Container or Object Name|Description|
|---|---|
|REF_PDF_DATA_71b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_71.pdf|
|REF_XML_MDO_71b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_71.xml.|
|REF_TXT_DATA_72b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_72.txt.|
|REF_PDF_DATA_72b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_72.pdf.|
|REF_XML_MDO_72b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_72.xml.|
|REF_CADES_ATT_TXT_DATA_73b|A reference to valid attached digital signature of TXT_DATA.txt, which has<br>been uploaded in advance as TXT_DATA_73.txt.p7m.|
|REF_TXT_DATA_74b|A reference to TXT_DATA.txt, which has been uploaded in advance as<br>TXT_DATA_74.txt.|
|REF_PDF_DATA_74b|A reference to PDF_DATA.pdf, which has been uploaded in advance as<br>PDF_DATA_74.pdf.|
|REF_XML_MDO_74b|A reference to XML_MDO.xml, which has been uploaded in advance as<br>XML_MDO_74.xml.|



Table 2: Definition of test objects[6] 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0025-03.png)


- - "urn:oasis:names:tc:dss:1.0:core:schema" which can be found at http://ws.openecard.org/schema/oasis dss core-schema-v1.0-os.xsd. 

6 The test objects are listed in order of appearance in the particular test cases. 

Federal Office for Information Security 

25 

Web Service Interfaces 

## 3.4 Mandatory Tests 

## 3.4.1 Tests of the TR-S.4-interface 

## 3.4.1.1 Function RetrieveInfo of S.4-interface 

All test cases defined in this section are derived from the general requirement A2.0-2 together with the interface specification of the RetrieveInfo function in section 3.8 of [TR-ESOR-E] . 

At least one active Preservation Profile is available: 

http://www.bsi.bund.de/tr-esor/V1.3.0/profile/S.4/v1.0. 

with URI= `http://www.bsi.bund.de/tr-esor/V1.3.0/profile/S.4/V1.0` 

At least one inactive Preservation Profile is available: 

- http://www.bsi.bund.de/tr esor/V1.3.0/profile/S.4/v0.05 

with URI = **http://www.bsi.bund.de/tr-esor/V1.3.0/profile/S.4/V0.5** 

## 3.4.1.1.1 M-RI-01 Retrieve Preservation Profile 

|**Identifier**|**M-RI-01**|
|---|---|
|Test Purpose|The test shall retrieve the actual Preservation Profile with<br>http://www.bsi.bund.de/tr-esor/V1.3.0/profile/S.4/V1.0|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>At least one active Preservation Profile is available (ACTIVE_PROFILE) and one not-active<br>(INACTIVE_PROFILE).|



Federal Office for Information Security 

26 

Web Service Interfaces 

|Step|Test sequence of M-RI-01|Expected Results|
|---|---|---|
|1|RetrieveInfoRequest<br>(<br>ProfileIdentifier( ACTIVE_PROFILE_URI )<br>)|RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok),<br>ACTIVE_PROFILE<br>)|
|2|RetrieveInfoRequest<br>(<br>Status( inactive )<br>)|RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok),<br>INACTIVE_PROFILE<br>)|
|3|RetrieveInfoRequest<br>(<br>Status( all )<br>)|RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok),<br>ACTIVE_PROFILE,<br>INACTIVE_PROFILE<br>)|
|4|RetrieveInfoRequest<br>(<br>Status( active )<br>)|RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok),<br>ACTIVE_PROFILE<br>)|
|5|RetrieveInfoRequest<br>(<br>ProfileIdentifier( ACTIVE_PROFILE_URI ),<br>Status( active )<br>)|RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok),<br>ACTIVE_PROFILE<br>)|
|6|RetrieveInfoRequest<br>(<br>ProfileIdentifier(ACTIVE_PROFILE_URI ),<br>Status( inactive )<br>)|RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|7|RetrieveInfoRequest<br>(<br>ProfileIdentifier(ACTIVE_PROFILE_URI ),<br>Status( all )<br>)|RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok),<br>ACTIVE_PROFILE<br>)|
|8|RetrieveInfoRequest<br>(<br>)|RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok),<br>ACTIVE_PROFILE<br>)|



## Verdict of M-RI-01 

Observations: 

## Verdict: 

## 3.4.1.1.2 M-RI-02 RetrieveInfo with unknown URI 

## Identifier M-RI-02 

Test Purpose The test shall verify that it will yield an error, if `RetrieveInfo` is called without providing a known URI. As the present call also contains the UNKNOWN_PROFILE_URI, the `dss:Result` 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0027-08.png)


Federal Office for Information Security 

27 

Web Service Interfaces 

|Identifier|Identifier|M-RI-02|M-RI-02|
|---|---|---|---|
|Configuration||•<br>CONFIG_S.4||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.||
|||||
|Step|Test sequence of M-RI-02||Expected Results|
|1|RetrieveInfoRequest<br>(<br>UNKNOWN_PROFILE_URI<br>)||RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownURI)<br>)|
|2|RetrieveInfoRequest<br>(<br>ACTIVE_PROFILE_URI<br>)||RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok),<br>ACTIVE_PROFILE<br>)|
|||||
||Verdict||of M-RI-02|
|Observations:||||
|Verdict:||||



## 3.4.1.1.3 M-RI-03 RetrieveInfo with unknown control in OptionalInputs 

|Identifier|Identifier|M-RI-03|M-RI-03|M-RI-03|M-RI-03|
|---|---|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element and the`RetrieveInfoRequest`will not be successful.||||
|Configuration||•|CONFIG_S.4|||
|Pre-test<br>conditions||•<br>•<br>•|Authenticated connection to middleware exists.<br>At least one active Preservation Profile is available with<br>http://www.bsi.bund.de/tr-<br>esor/V1.3.0/profile/S.4/V1.0<br>The`OptionalInputs`-element and the`RetrieveInfoRequest`contains an unknown item.|||
|||||||
|Step|Test sequence of M-RI-03|||Expected Results||
|1|RetrieveInfoReqest<br>(<br>dss:OptionalInputs(SomethingUnknown),<br>ACTIVE_PROFILE_URI<br>)|||RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/notSupported)<br>)||
|2|RetrieveInfoRequest<br>(<br>ACTIVE_PROFILE_URI<br>)|||RetrieveInfoResponse<br>(<br>dss:Result(resultmajor#ok),<br>ACTIVE_PROFILE<br>)||



Federal Office for Information Security 

28 

Web Service Interfaces 

Verdict of M-RI-03 

Observations: 

## Verdict: 

Federal Office for Information Security 

29 

Web Service Interfaces 

## 3.4.1.2 Function ArchiveSubmission of S.4-interface 

All test cases defined in this section are derived from the requirement [TR ESOR M.1] , (A4.1 1) and the general requirement [TR-ESOR-E] , (A2.0-2) together with the interface specification of the ArchiveSubmission function in section 3.1 of [TR-ESOR-E] . 

## 3.4.1.2.1 M-SU-01 XAIP_OK without AOID 

|Identifier|M-SU-01|
|---|---|
|Test Purpose|The test shall verify that it is possible to submit XAIP_OK without AOID.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence of M-SU-01|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>XAIP_OK<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-01<br>)|
|2|ArchiveRetrievalRequest<br>(<br>AOID-01<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-01, VID-01)<br>)|
|3|ArchiveEvidenceRequest7<br>(<br>AOID-01<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01,VID-01,<br>XAIP_OK_V1_ER_OK)<br>)|
|4|Test<br>of<br>correctness<br>of<br>the<br>obtained<br>XAIP_OK(AOID-01, VID-01) by using AIP-<br>eIDAS-SigValidator<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK(AOID-01, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid )<br>dssvr:Details(<br>vr:XAIPReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|



- 7 Make sure the tested TR-ESOR-system has already obtained the archive time stamp. 

Federal Office for Information Security 

30 

Web Service Interfaces 

|Step|Test sequence of M-SU-01|Expected Results|
|---|---|---|
|5|Test<br>of<br>correcteness<br>of<br>the<br>obtained<br>XAIP_OK_V1_ER_OK by using ERVerifyTool.<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK(AOID-01, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(<br>AOID-01,VID-01,<br>XAIP_OK_V1_ER_OK)<br>)<br>)<br>)|VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid )<br>dssvr:Details(<br>vr:EvidenceRecordReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|
|6|ArchiveSubmissionRequest<br>(<br>XAIP_OK_SIG_OK<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-02<br>)|
|7|ArchiveRetrievalRequest<br>(<br>AOID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK_SIG_OK(AOID-02, VID-01)<br>)|
|8|ArchiveEvidenceRequest7<br>(<br>AOID-02<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-02,VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK)<br>)|



Verdict of M-SU-01 Observations: Verdict: 

Federal Office for Information Security 

31 

Web Service Interfaces 

## 3.4.1.2.2 M-SU-01a LXAIP_OK without AOID 

|Identifier|M-SU-01a|
|---|---|
|Test Purpose|The test shall verify that it is possible to submit XAIP_OK without AOID.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



Step Test sequence of M-SU-01a Expected Results 1 To be done manually! As a result following data structures (proper instances of Following files have to be uploaded into middleware asic:DataObjectReferences) will be delivered: via upload/download-module (cf. chapters 4.2 and 4.3): 1) TXT_DATA_50.txt 1) REF_TXT_DATA_50 2) XML_MDO_50.xml 2) REF_XML_MDO_50 3) PDF_DATA_50.pdf 3) REF_PDF_DATA_50 4) TXT_DATA_51.txt 4) REF_TXT_DATA_51 5) TXT_DATA_51.txt.p7s 5) REF_CADES_DET_TXT_DATA_51 6) PDF_DATA_51.pdf 6) REF_PDF_DATA_51 7) PDF_DATA_51.pdf.p7s 7) REF_CADES_DET_PDF_DATA_51 8) XML_MDO_51.xml 8) REF_XML_MDO_51 9) TXT_DATA_52.txt 9) REF_TXT_DATA_52 10) PDF_DATA_52.pdf 10) REF_PDF_DATA_52 11) XML_MDO_52.xml 11) REF_XML_MDO_52 12) TXT_DATA_53.txt.p7m 12) REF_CADES_ATT_TXT_DATA_53 13) XML_DATA_54.xml 13) REF_XML_DATA_54 14) XML_DATA_54.xml.p7s 14) REF_CADES_DET_XML_DATA_54 15) TXT_DATA_55.txt 15) REF_TXT_DATA_55 16) PDF_DATA_55.pdf 16) REF_PDF_DATA_55 17) XML_MDO_55.xml 17) REF_XML_MDO_55 18) XML_DATA_56.xml 18) REF_XML_DATA_56 19) XML_DATA_56.xml.p7s 19) REF_CADES_DET_XML_DATA_56 20) TXT_DATA_57.txt.p7m 20) REF_CADES_ATT_TXT_DATA_57 21) TXT_DATA_58.txt 21) REF_TXT_DATA_58 22) PDF_DATA_58.pdf 22) REF_PDF_DATA_58 23) XML_MDO_58.xml 23) REF_XML_MDO_58 24) TXT_DATA_59.txt.p7m 24) REF_CADES_ATT_TXT_DATA_59 

Web Service Interfaces 

## Step 

## Test sequence of M-SU-01a 

## Expected Results 

1 To be done manually! As a result following data structures (proper instances of Following files have to be uploaded into middleware asic:DataObjectReferences) will be delivered: via upload/download-module (cf. chapters 4.2 and 4.3): 25) TXT_DATA_60.txt.p7m 25) REF_CADES_ATT_TXT_DATA_60 26) XML_DATA_60-1.xml 26) REF_XML_DATA_60-1 27) XML_DATA_60-1.xml.p7s 27) REF_CADES_DET_XML_DATA_60-1 28) TXT_DATA_61.txt 28) REF_TXT_DATA_61 29) TXT_DATA_61.txt.p7s 29) REF_CADES_DET_TXT_DATA_61 30) PDF_DATA_61.pdf 30) REF_PDF_DATA_61 31) PDF_DATA_61.pdf.p7s 31) REF_CADES_DET_PDF_DATA_61 32) XML_MDO_61.xml 32) REF_XML_MDO_61 33) XML_DATA_62.xml 33) REF_XML_DATA_62 34) XML_DATA_62.xml.p7s 34) REF_CADES_DET_XML_DATA_62 35) XML_DATA_63.xml 35) REF_XML_DATA_63 36) XML_DATA_63.xml.p7s 36) REF_CADES_DET_XML_DATA_63 37) XML_DATA_64.xml 37) REF_XML_DATA_64 38) XML_DATA_64.xml.p7s 38) REF_CADES_DET_XML_DATA_64 39) TXT_DATA_65.txt 39) REF_TXT_DATA_65 40) TXT_DATA_65_NOK.p7s 40) REF_CADES_DET_NOK_TXT_DATA_65 41) PDF_DATA_65.pdf 41) REF_PDF_DATA_65 42) PDF_DATA_65.pdf.p7s 42) REF_CADES_DET_PDF_DATA_65 43) XML_MDO_65.xml 43) REF_XML_MDO_65 44) TXT_DATA_66.txt 44) REF_TXT_DATA_66 45) TXT_DATA_66.txt.p7s 45) REF_CADES_DET_TXT_DATA_66 46) PDF_DATA_66.pdf 46) REF_PDF_DATA_66 47) PDF_DATA_66.pdf.p7s 47) REF_CADES_DET_PDF_DATA_66 48) XML_MDO_66.xml 48) REF_XML_MDO_66 49) TXT_DATA_67.txt 49) REF_TXT_DATA_67 50) TXT_DATA_NOK_67.txt.p7s 50) REF_CADES_DET_NOK_TXT_DATA_67 51) PDF_DATA_67.pdf 51) REF_PDF_DATA_67 52) PDF_DATA_67.pdf.p7s 52) REF_CADES_DET_PDF_DATA_67 53) XML_MDO_67.xml 53) REF_XML_MDO_67 54) TXT_DATA_68.txt 54) REF_TXT_DATA_68 55) TXT_DATA_68.txt.p7s 55) REF_CADES_DET_TXT_DATA_68 56) PDF_DATA_68.pdf 56) REF_PDF_DATA_68 57) PDF_DATA_68.pdf.p7s 57) REF_CADES_DET_PDF_DATA_68 58) XML_MDO_68.xml 58) REF_XML_MDO_68 59) XML_DATA_69.xml 59) REF_XML_DATA_69 60) XML_DATA_NOK_69.xml.p7s 60) REF_CADES_DET_NOK_XML_DATA_69 1 To be done manually! As a result following data structures (proper instances of Following files have to be uploaded into middleware asic:DataObjectReferences) will be delivered: via upload/download-module (cf. chapters 4.2 and 4.3): 61) XML_DATA_70.xml 61) REF_XML_DATA_70 62) XML_DATA_NOK_70.xml.p7s 62) REF_CADES_DET_NOK_XML_DATA_70 63) TXT_DATA_71.txt 63) REF_TXT_DATA_71 64) PDF_DATA_71.pdf 64) REF_PDF_DATA_71 65) XML_MDO_71.xml 65) REF_XML_MDO_71 66) TXT_DATA_72.txt 66) REF_TXT_DATA_72 67) PDF_DATA_72.pdf 67) REF_PDF_DATA_72 68) XML_MDO_72.xml 68) REF_XML_MDO_72 69) TXT_DATA_73.txt.p7m 69) REF_CADES_ATT_TXT_DATA_73 70) TXT_DATA_74.txt 70) REF_TXT_DATA_74 71) PDF_DATA_74.pdf 71) REF_PDF_DATA_74 72) XML_MDO_74.xml 72) REF_XML_MDO_74 The references in the particular LXAIP* and DLXAIP* test objects will be adjusted according to the results in step a) automatically, the references have to be inserted into the configuration file of the testbed. 

Federal Office for Information Security 

33 

Web Service Interfaces 

|Step|Test sequence of M-SU-01a|Expected Results|
|---|---|---|
||||
|2|To be done manually!<br>Try<br>to<br>upload<br>the<br>XAIP_OK<br>by<br>using<br>the<br>upload/download interface of the middleware.|The upload-operation failed. Some kind of the machine-<br>readable error code is delivered back. No data has been<br>stored in the Storage.|
|3|To be done manually!<br>Try<br>to<br>upload<br>the<br>LXAIP_OK<br>by<br>using<br>the<br>upload/download interface of the middleware.|The upload-operation failed. Some kind of the machine-<br>readable error code is delivered back. No data has been<br>stored in the Storage.|
|4|To be done manually!<br>Try to upload the ASiC_AIP_OK by using the<br>upload/download interface of the middleware.|The upload-operation failed. Some kind of the machine-<br>readable error code is delivered back. No data has been<br>stored in the Storage.|
|5|ArchiveSubmissionRequest<br>(<br>LXAIP_OK(<br>REF_TXT_DATA_50,<br>REF_PDF_DATA_50,<br>REF_XML_MDO_50)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-01a<br>)|
|6|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-01a<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-01a, VID-01)<br>)|
|7|ArchiveEvidenceRequest8<br>(<br>AOID-01a<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01a, VID-01,<br>LXAIP_OK_V1_ER_OK)<br>)|
|8|Make sure all in LXAIP_OK(AOID-01a, VID-01)<br>referenced files have been copied into corresponding<br>LXAIP-directory of the AIP-eIDAS-SigValidator adjust<br>the given references in in LXAIP_OK(AOID-01a, VID-01)<br>in order to get them resolveable by the AIP-eIDAS-<br>SigValidator.|<br>LXAIP_OK_XSV(AOID-01a, VID-01)|



8 Make sure the tested TR-ESOR-system has already obtained the archive time stamp. 

Federal Office for Information Security 

34 

Web Service Interfaces 

|Step|Test sequence of M-SU-01a|Expected Results|
|---|---|---|
||||
|9|Test of correctness of the obtained LXAIP_OK(AOID-01,<br>VID-01) by using AIP-eIDAS-SigValidator<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_XSV(AOID-01a, VID-01)<br>)<br>)<br>)<br>)|<br>VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>dssvr:Details(<br>vr:XAIPReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|
|10|Test<br>of<br>correcteness<br>of<br>the<br>obtained<br>LXAIP_OK_V1_ER_OK by using ERVerifyTool.<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_XSV(AOID-01a, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(<br>AOID-01a, VID-01,<br>LXAIP_OK_V1_ER_OK)<br>)<br>)<br>)|<br>VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>dssvr:Details(<br>vr:EvidenceRecordReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|
|11|ArchiveSubmissionRequest<br>(<br>LXAIP_OK_SIG_OK(<br>REF_TXT_DATA_51,<br>REF_CADES_DET_TXT_DATA_51,<br>REF_PDF_DATA_51,<br>REF_CADES_DET_PDF_DATA_51,<br>REF_XML_MDO_51<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-02a<br>)|
|12|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-02a<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK_SIG_OK(AOID-02a, VID-01)<br>)|



Federal Office for Information Security 

35 

Web Service Interfaces 

|Step|Test sequence of M-SU-01a|Expected Results|
|---|---|---|
||||
|13|ArchiveEvidenceRequest8<br>(<br>AOID-02a<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-02a, VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK)<br>)|
||||
||Verdict of M-SU-01a||
|Observations:|||
|Verdict:|||



## 3.4.1.2.3 M-SU-02 XAIP_NOK 

|Identifier|M-SU-02|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a (syntactically incorrect) XAIP_NOK is<br>submitted.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence M-SU-02|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>XAIP_NOK<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK)<br>)<br>Alternatively response to the one above could be<br>following or similar:<br><soap:Envelope<br>xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"<br>><br><soap:Body><br><soap:Fault><br><faultcode>soap:Client</faultcode><br><faultstring>Problems<br>creating<br>SAAJ<br>object<br>model</faultstring><br></soap:Fault><br></soap:Body><br></soap:Envelope>|



Federal Office for Information Security 

36 

Web Service Interfaces 

|Step|Test sequence M-SU-02|Expected Results|
|---|---|---|
|2|ArchiveSubmissionRequest<br>(<br>XAIP_NOK_VERSION<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK)<br>)<br>Alternatively response to the one above could be<br>following or similar:<br><soap:Envelope<br>xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"<br>><br><soap:Body><br><soap:Fault><br><faultcode>soap:Client</faultcode><br><faultstring>Problems<br>creating<br>SAAJ<br>object<br>model</faultstring><br></soap:Fault><br></soap:Body><br></soap:Envelope>|
||||
||Verdict of M-SU-02||
|Observations:|||
|Verdict:|||



## 3.4.1.2.4 M-SU-02a LXAIP_NOK 

|Identifier|M-SU-02a|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a (syntactically incorrect, missing element<br>`ds:DigestValue`in element`asic:DataObjectReference`) LXAIP_NOK is submitted.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence M-SU-02a|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>LXAIP_NOK<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK)<br>)<br>Alternatively response to the one above could be<br>following or similar:<br><soap:Envelope<br>xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"<br>><br><soap:Body><br><soap:Fault><br><faultcode>soap:Client</faultcode><br><faultstring>Problems<br>creating<br>SAAJ<br>object<br>model</faultstring><br></soap:Fault><br></soap:Body><br></soap:Envelope>|



Federal Office for Information Security 

37 

Web Service Interfaces 

Verdict of M-SU-02a 

Observations: 

Verdict: 

## 3.4.1.2.5 M-SU-03 XAIP_NOK_EXPIRED 

|Identifier|Identifier|M-SU-03|M-SU-03|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, if the semantically incorrect XAIP_NOK_EXPIRED<br>is submitted.||
|Configuration||•<br>CONFIG_S.4||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.||
|||||
|Step||Test sequence|Expected Results|
|1|ArchiveSubmissionRequest<br>(<br>XAIP_NOK_EXPIRED<br>)||ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_EXPIRED)<br>)|
|||||
||Verdict of M-SU-03|||
|Observations:||||
|Verdict:||||



3.4.1.2.6 M-SU-04 XAIP_NOK_SUBMTIME 

|Identifier|M-SU-04|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the semantically incorrect<br>XAIP_NOK_SUBMTIME is submitted.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



Federal Office for Information Security 

38 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Prepare XAIP_NOK_SUBMTIME, set the value of<br>the<br>element<br>`xaip:submissionTime`<br>in<br>`xaip:submissionInfo`to the time in the past|XAIP_NOK_SUBMTIME(past)|
|2|ArchiveSubmissionRequest<br>(<br>XAIP_NOK_SUBMTIME(past)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SUBMTIME)<br>)|
|3|Prepare XAIP_NOK_SUBMTIME, set the value of<br>the<br>element<br>`xaip:submissionTime`<br>in<br>`xaip:submissionInfo`to the time in the future|XAIP_NOK_SUBMTIME(future)|
|4|ArchiveSubmissionRequest<br>(<br>XAIP_NOK_SUBMTIME(future)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SUBMTIME)<br>)|



## Verdict of M-SU-04 

Observations: Verdict: 

## 3.4.1.2.7 M-SU-05 XAIP_NOK_SIG 

|Identifier|Identifier|M-SU-05|M-SU-05|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, if the submitted XAIP_NOK_SIG contains digital<br>signatures, which do not verify correctly9.||
|Configuration||•<br>CONFIG_S.4||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>The TOT is configured only to accept valid signatures.||
|||||
|Step||Test sequence|Expected Results|
|1|ArchiveSubmissionRequest<br>(<br>XAIP_NOK_SIG<br>)||ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(XAIP_NOK_SIG_VR)<br>)|



## Verdict of M-SU-05 

Observations: 

## Verdict: 

> 9 See also Annex E (Version 1.3, Chapter 3.7.1 ( `VerifyUnderSignaturePolicy` )). 

Federal Office for Information Security 

39 

Web Service Interfaces 

## 3.4.1.2.8 M-SU-06 XAIP_NOK_ER 

|Identifier|Identifier|M-SU-06|M-SU-06|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, because the submitted XAIP_NOK_ER contains an<br>incorrect Evidence Record.||
|Configuration||•<br>CONFIG_S.4||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.||
|||||
|Step||Test sequence|Expected Results|
|1|ArchiveSubmissionRequest<br>(<br>XAIP_NOK_ER<br>)||ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER)<br>dss:OptionalOutputs(XAIP_NOK_ER_VR)<br>)|
|||||
||Verdict of M-SU-06|||
|Observations:||||
|Verdict:||||



## 3.4.1.2.9 M-SU-06a LXAIP_OK_ER_NOK 

|Identifier|Identifier|M-SU-06a|M-SU-06a|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, because the submitted LXAIP_OK_ER_NOK<br>contains an incorrect Evidence Record.||
|Configuration||•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Test case M-SU-01a has been performed successfully.||
|||||
|Step||Test sequence|Expected Results|
|1|ArchiveSubmissionRequest<br>(<br>LXAIP_OK_ER_NOK(<br>REF_TXT_DATA_52,<br>REF_PDF_DATA_52,<br>REF_XML_MDO_52,<br>ER_NOK_LXAIP_OK)<br>)||ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER)<br>dss:OptionalOutputs(LXAIP_NOK_ER_VR)<br>)|
|||||
||Verdict of M-SU-06a|||
|Observations:||||



Federal Office for Information Security 

40 

Web Service Interfaces 

Verdict of M-SU-06a 

Verdict: 

## 3.4.1.2.10 M-SU-07 XAIP_OK and unknown control in OptionalInputs 

|Identifier|Identifier|M-SU-07|M-SU-07|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element and the archive data object will not be imported.||
|Configuration||•<br>CONFIG_S.4||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.||
|||||
|Step||Test sequence|Expected Results|
|1|ArchiveSubmissionRequest<br>(<br>dss:OptionalInputs(SomethingUnknown),<br>XAIP_OK<br>)||ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/notSupported),<br>)|



Verdict of M-SU-07 Observations: Verdict: 

## 3.4.1.2.11 M-SU-08 BIN_OK 

|Identifier|M-SU-08|
|---|---|
|Test Purpose|The test shall validate that it is possible to submit as BIN defined data. BIN means here:<br>•<br>CADES_ATT_OK,<br>•<br>XADES_ENVELOPED_OK, XADES_ENVELOPING_OK,<br>•<br>PADES_OK,<br>•<br>ASiC_S_CADES_OK, ASIC_S_XADES_OK, ASIC_S_TST_OK, ASIC_S_ER_OK,<br>•<br>ASiC_E_CADES_OK, ASIC_E_XADES_OK, ASIC_E_TST_OK, ASIC_E_ER_OK,<br>•<br>DIGEST_LIST.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



Federal Office for Information Security 

41 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/CAdES,<br>AD-01,<br>CADES_ATT_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-200<br>)|
|2|ArchiveRetrievalRequest<br>(<br>AOID-200<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-200, VID-01,<br>credential(AD-01, CADES_ATT_OK))<br>)|
|3|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/XAdES,<br>AD-01,<br>XADES_ENVELOPED_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-201<br>)|
|4|ArchiveRetrievalRequest<br>(<br>AOID-201<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-201, VID-01,<br>dataObject(AD-01,<br>xmlData(XADES_ENVELOPED_OK)<br>)<br>)<br>)<br>OR10<br>ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-201, VID-01,<br>dataObject(AD-01,<br>binaryData(XADES_ENVELOPED_OK)<br>)<br>)<br>)|
|5|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/XAdES,<br>AD-01,<br>XADES_ENVELOPING_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-202<br>)|



> 10 An enveloped XAdES could be placed in XAIP as binary data stream in an element `<xaip:binaryData>` (as recommended in [TR-ESOR-F] , section 6.2), or as xml data stream in an element `<xaip:xmlData>` in the `<xaip:dataObjectsSection>` -element. 

Federal Office for Information Security 

42 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|6|ArchiveRetrievalRequest<br>(<br>AOID-202<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-202, VID-01,<br>credential(AD-01,<br>SignatureObject(<br>XADES_ENVELOPING_OK)<br>)<br>)<br>)<br>)<br>OR11<br>ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-202, VID-01,<br>credential(AD-01,<br>Base64Signature(<br>XADES_ENVELOPING_OK)<br>)<br>)<br>)<br>)|
|7|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/PAdES,<br>AD-01,<br>PADES_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-203<br>)|
|8|ArchiveRetrievalRequest<br>(<br>AOID-203<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-203, VID-01,<br>dataObject(AD-01, PADES_OK))<br>)|
|'9|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-E,<br>AD-01,<br>ASiC_E_CADES_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-204<br>)|
|10|ArchiveRetrievalRequest<br>(<br>AOID-204<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-204, VID-01,<br>credential(AD-01,<br>Base64Signature(ASiC_E_CADES_OK)))<br>)|



11 An enveloping XAdES could be placed in XAIP as binary credential data stream in an element `<dss:base64Signature>` (as recommended in [TR-ESOR-F] , section 6.2), or as xml credential data stream directly aa element `<dss:Signature>` in the `<dss:SignatureObject>` -element of the `<xaip:credential>` parent element. 

Federal Office for Information Security 

43 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|11|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-E,<br>AD-01,<br>ASIC_E_XADES_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-205<br>)|
|12|ArchiveRetrievalRequest<br>(<br>AOID-205<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-205, VID-01,<br>credential(AD-01,<br>Base64Signature(ASIC_E_XADES_OK)))<br>)|
|13|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-E,<br>AD-01,<br>ASIC_E_TST_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-206<br>)|
|14|ArchiveRetrievalRequest<br>(<br>AOID-206<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-206, VID-01,<br>credential(AD-01,<br>Base64Signature(ASIC_E_TST_OK)))<br>)|
|15|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-E,<br>AD-01,<br>ASIC_E_ER_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-207<br>)|
|16|ArchiveRetrievalRequest<br>(<br>AOID-207<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-207, VID-01,<br>credential(AD-01,<br>Base64Signature(ASIC_E_ER_OK)))<br>)|
|17|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/19512/format/DigestList,<br>AD-01,<br>DIGEST_LIST<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-208<br>)|



Federal Office for Information Security 

44 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|18|ArchiveRetrievalRequest<br>(<br>AOID-208<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-208, VID-01,<br>dataObject(AD-01,<br>xmlData(DIGEST_LIST)<br>)<br>)<br>)<br>OR12<br>ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-208, VID-01,<br>dataObject(AD-01,<br>binaryData(DIGEST_LIST)<br>)<br>)<br>)|
|19|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-S,<br>AD-01,<br>ASiC_S_CADES_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-209<br>)|
|20|ArchiveRetrievalRequest<br>(<br>AOID-209<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-209, VID-01,<br>credential(AD-01,<br>Base64Signature(ASiC_S_CADES_OK)))<br>)|
|21|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-S,<br>AD-01,<br>ASIC_S_XADES_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-210<br>)|
|22|ArchiveRetrievalRequest<br>(<br>AOID-210<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-210, VID-01,<br>credential(AD-01,<br>Base64Signature(ASIC_S_XADES_OK)))<br>)|



> 12 A digest list as XML based data object could be placed in XAIP as binary data stream in an element `<xaip:binaryData>` or as xml data stream in an element `<xaip:xmlData>` in the `<xaip:dataObjectsSection>` -element. 

Federal Office for Information Security 

45 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|23|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-S,<br>AD-01,<br>ASIC_S_TST_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-211<br>)|
|24|ArchiveRetrievalRequest<br>(<br>AOID-211<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-211, VID-01,<br>credential(AD-01,<br>Base64Signature(ASIC_S_TST_OK)))<br>)|
|25|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-S,<br>AD-01,<br>ASIC_S_ER_OK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-212<br>)|
|26|ArchiveRetrievalRequest<br>(<br>AOID-212<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP(<br>AOID-212, VID-01,<br>credential(AD-01,<br>Base64Signature(ASIC_S_ER_OK)))<br>)|



Verdict of M-SU-08 Observations: Verdict: 

## 3.4.1.2.12 M-SU-09 BIN_NOK 

|Identifier|M-SU-09|
|---|---|
|Test Purpose|The test shall validate that there will be an error in case an as BIN defined data containing an<br>invalid signature will be submitted. BIN means here:<br>•<br>CADES_ATT_NOK<br>•<br>XADES_ENVELOPED_NOK, XADES_ENVELOPING_NOK,<br>•<br>PADES_NOK,<br>•<br>ASIC_E_CADES_NOK, ASIC_E_XADES_NOK, ASIC_E_TST_NOK, ASIC_E_ER_NOK,<br>•<br>ASIC_S_CADES_NOK, ASIC_S_XADES_NOK, ASIC_S_TST_NOK, ASIC_S_ER_NOK.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The TOT is configured only to accept valid signatures.|



Federal Office for Information Security 

46 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/CAdES,<br>AD-01,<br>CADES_ATT_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(CADES_ATT_NOK_VR)<br>)|
|2|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/XAdES,<br>AD-01,<br>XADES_ENVELOPED_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(XADES_ENVELOPED_NOK_VR)<br>)|
|3|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/XAdES,<br>AD-01,<br>XADES_ENVELOPING_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(XADES_ENVELOPING_NOK_VR)<br>)|
|4|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/PAdES,<br>AD-01,<br>PADES_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(PADES_NOK_VR)<br>)|
|'5|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-E,<br>AD-01,<br>ASIC_E_CADES_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(ASIC_E_CADES_NOK_VR)<br>)|
|6|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-E,<br>AD-01,<br>ASIC_E_XADES_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(ASIC_E_XADES_NOK_VR)<br>)|
|7|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-E,<br>AD-01,<br>ASIC_E_TST_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(ASIC_E_TST_NOK_VR)<br>)|



Federal Office for Information Security 

47 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|8|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-E,<br>AD-01,<br>ASIC_E_ER_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(ASIC_E_ER_NOK_VR)<br>)|
|9|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-S,<br>AD-01,<br>ASIC_S_CADES_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(ASIC_S_CADES_NOK_VR)<br>)|
|10|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-S,<br>AD-01,<br>ASIC_S_XADES_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(ASIC_S_XADES_NOK_VR)<br>)|
|11|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-S,<br>AD-01,<br>ASIC_S_TST_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(ASIC_S_TST_NOK_VR)<br>)|
|12|ArchiveSubmissionRequest<br>(<br>ArchiveData(<br>  http://uri.etsi.org/ades/ASiC/type/ASiC-S,<br>AD-01,<br>ASIC_S_ER_NOK<br>)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature)<br>dss:OptionalOutputs(ASIC_S_ER_NOK_VR)<br>)|



Verdict of M-SU-09 Observations: Verdict: 

Federal Office for Information Security 

48 

Web Service Interfaces 

## 3.4.1.3 Function ArchiveUpdate of S.4-interface 

All test cases defined in this section are derived from the requirement A4.2-3 and the general requirement A2.0-2 together with the interface specification of the `ArchiveUpdate` function in section 3.2 of [TR-ESORE] . According to section 2 of [TR-ESOR-E] , `ArchiveUpdateRequest` and `ArchiveUpdateResponse` shall be supported. 

## 3.4.1.3.1 M-UP-01 DXAIP_OK 

|Identifier|M-UP-01|
|---|---|
|Test Purpose|The test shall verify that it is possible to submit a correct DXAIP_OK with<br>`ArchiveUpdateRequest`.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test case M-SU-01 was successfully performed with AOID-01.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-01<br>into<br>the<br>prepared<br>DXAIP_OK-template.|DXAIP_OK(AOID-01, VID-01, VID-02)|
|2|ArchiveUpdateRequest<br>(<br>DXAIP_OK(AOID-01, VID-01, VID-02)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#OK),<br>VersionID(VID-02)<br>)|
|3|Insert<br>AOID-01<br>into<br>the<br>prepared<br>DXAIP_OK_2-template.|DXAIP_OK_2(AOID-01, VID-02, VID-03)|
|4|ArchiveUpdateRequest<br>(<br>DXAIP_OK_2(AOID-01, VID-02, VID-03)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#OK),<br>VersionID(VID-03)<br>)|
|5|ArchiveSubmissionRequest<br>(<br>XAIP_OK<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-01z<br>)|
|6|Insert<br>AOID-01z<br>into<br>the<br>prepared<br>DXAIP_OK_SIG_ONLY-template.|DXAIP_OK_SIG_ONLY(AOID-01z, VID-01, VID-02)|
|7|ArchiveUpdateRequest<br>(<br>DXAIP_OK_SIG_ONLY(<br>AOID-01z, VID-01, VID-02)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#OK),<br>VersionID(VID-02)<br>)|



Verdict of M-UP-01 

Observations: 

Verdict: 

Federal Office for Information Security 

49 

Web Service Interfaces 

## 3.4.1.3.2 M-UP-01a DLXAIP_OK 

|Identifier|M-UP-01a|
|---|---|
|Test Purpose|The test shall verify that it is possible to submit a correct DLXAIP_OK with<br>`ArchiveUpdateRequest`.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test case M-UP-01a was successfully performed with AOID-01a.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-01a<br>into<br>the<br>prepared<br>DLXAIP_OK-template.|DLXAIP_OK(AOID-01a, VID-01, VID-02)|
|2|ArchiveUpdateRequest<br>(<br>DLXAIP_OK(AOID-01a, VID-01, VID-02,<br>REF_CADES_ATT_TXT_DATA_53)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#OK),<br>VersionID(VID-02)<br>)|
|3|Insert<br>AOID-01a<br>into<br>the<br>prepared<br>DLXAIP_OK_2-template.|DLXAIP_OK_2(AOID-01a, VID-02, VID-03)|
|4|ArchiveUpdateRequest<br>(<br>DLXAIP_OK_2(<br>AOID-01a, VID-02, VID-03,<br>REF_XML_DATA_54,<br>REF_CADES_DET_XML_DATA_54)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#OK),<br>VersionID(VID-03)<br>)|
||||
||Verdict of M-UP-01a||
|Observations:|||
|Verdict:|||



## 3.4.1.3.3 M-UP-02 DXAIP_NOK_AOID 

|Identifier|M-UP-02|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a DXAIP_NOK_AOID with a not yet assigned<br>AOID is submitted.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



Federal Office for Information Security 

50 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Choice an AOID-03 within the possible range<br>and make sure, that it has not been assigned yet.<br>This is realised by the following call:<br>ArchiveRetrievalRequest<br>(<br>AOID-03<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|
|2|Insert AOID-03 into DXAIP_NOK_AOID.|DXAIP_NOK_AOID(AOID-03)|
|3|ArchiveUpdateRequest<br>(<br>DXAIP_NOK_AOID(AOID-03)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_AOID)<br>)|
||||
||Verdict of M-UP-02||
|Observations:|||
|Verdict:|||



## 3.4.1.3.4 M-UP-03 DXAIP_NOK 

|Identifier|M-UP-03|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a (syntactically incorrect) DXAIP_NOK is<br>submitted.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>XAIP_OK<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-04<br>)|
|2|Insert AOID-04 into the prepared DXAIP_NOK-<br>template.|DXAIP_NOK(AOID-04, VID-01, VID-02)|



Federal Office for Information Security 

51 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|3|ArchiveUpdateRequest<br>(<br>DXAIP_NOK(AOID-04, VID-01, VID-02)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK)<br>)<br>Alternatively response to the one above could be<br>following or similar:<br><soapenv:Envelope<br>xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelo<br>pe/"><br><soapenv:Body><br><soapenv:Fault><br><faultcode>Server</faultcode><br><faultstring>Failed<br>to<br>dispatch<br>using<br>script;<br>java.lang.Exception: VALIDATION ERRORS: [<br>line<br>1:<br>Expected<br>element<br>'protectedObjectPointer@http://www.bsi.bund.de/tr-<br>esor/xaip' instead of 'AOID@http://www.bsi.bund.de/tr-<br>esor/xaip'<br>here<br>in<br>element<br>packageInfoUnit@http://www.bsi.bund.de/tr-<br>esor/xaip]</faultstring><br></soapenv:Fault><br></soapenv:Body><br></soapenv:Envelope>>|
||||
||Verdict of M-UP-03||
|Observations:|||
|Verdict:|||



## 3.4.1.3.5 M-UP-03a DLXAIP_NOK 

|Identifier|M-UP-03a|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a (syntactically incorrect) DLXAIP_NOK is<br>submitted.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>LXAIP_OK(<br>REF_TXT_DATA_55,<br>REF_PDF_DATA_55,<br>REF_XML_MDO_55)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-04a<br>)|
|2|Insert<br>AOID-04a<br>into<br>the<br>prepared<br>DLXAIP_NOK-template.|DLXAIP_NOK(AOID-04a, VID-01, VID-02)|



Federal Office for Information Security 

52 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|3|ArchiveUpdateRequest<br>(<br>DLXAIP_NOK(AOID-04a, VID-01, VID-02<br>REF_XML_DATA_56,<br>REF_CADES_DET_XML_DATA_56)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK)<br>)<br>Alternatively response to the one above could be<br>following or similar:<br><soapenv:Envelope<br>xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelo<br>pe/"><br><soapenv:Body><br><soapenv:Fault><br><faultcode>Server</faultcode><br><faultstring>Failed<br>to<br>dispatch<br>using<br>script;<br>java.lang.Exception: VALIDATION ERRORS: [<br>line<br>1:<br>Expected<br>element<br>'protectedObjectPointer@http://www.bsi.bund.de/tr-<br>esor/xaip' instead of 'AOID@http://www.bsi.bund.de/tr-<br>esor/xaip'<br>here<br>in<br>element<br>packageInfoUnit@http://www.bsi.bund.de/tr-<br>esor/xaip]</faultstring><br></soapenv:Fault><br></soapenv:Body><br></soapenv:Envelope>|
||||
||Verdict of M-UP-03a||
|Observations:|||
|Verdict:|||



## 3.4.1.3.6 M-UP-04 DXAIP_NOK_EXPIRED 

|Identifier|M-UP-04|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the invalid DXAIP_NOK_EXPIRED is submitted.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test case M-UP-03 was successfully performed with AOID-04.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-04<br>into<br>the<br>prepared<br>DXAIP_NOK_EXPIRED-template.|DXAIP_NOK_EXPIRED(AOID-04, VID-01, VID-02)|
|2|ArchiveUpdateRequest<br>(<br>DXAIP_NOK_EXPIRED(<br>AOID-04, VID-01, VID-02)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_EXPIRED)<br>)|



Verdict of M-UP-04 Observations: 

Federal Office for Information Security 

53 

Web Service Interfaces 

Verdict of M-UP-04 

## Verdict: 

## 3.4.1.3.7 M-UP-05 DXAIP_NOK_SUBMTIME 

|Identifier|M-UP-05|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the invalid DXAIP_NOK_SUBMTIME is<br>submitted.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test case M-UP-03 was successfully performed with AOID-04|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-04<br>into<br>the<br>prepared<br>DXAIP_NOK_SUBMTIME-template<br>Prepare DXAIP_NOK_SUBMTIME, set the value<br>of the element`xaip:submissionTime`in<br>`xaip:submissionInfo`to the time in the past.|DXAIP_NOK_SUBMTIME(<br>AOID-04,<br>VID-01, VID-02,<br>SubmissionTime(in the past))|
|2|ArchiveUpdateRequest<br>(<br>DXAIP_NOK_SUBMTIME(<br>AOID-04,<br>VID-01, VID-02,<br>SubmissionTime(in the past))<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SUBMTIME)<br>)|
|3|Insert<br>AOID-04<br>into<br>the<br>prepared<br>DXAIP_NOK_SUBMTIME-template<br>Prepare DXAIP_NOK_SUBMTIME, set the value<br>of the element`xaip:submissionTime`in<br>`xaip:submissionInfo`to the time in the future|DXAIP_NOK_SUBMTIME(<br>AOID-04,<br>VID-01, VID-02,<br>SubmissionTime(in the future))|
|4|ArchiveUpdateRequest<br>(<br>DXAIP_NOK_SUBMTIME(<br>AOID-04,<br>VID-01, VID-02,<br>SubmissionTime(in the future))<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SUBMTIME)<br>)|



## Verdict of M-UP-05 

## Observations: 

## Verdict: 

Federal Office for Information Security 

54 

Web Service Interfaces 

3.4.1.3.8 M-UP-06 DXAIP_NOK_SIG 

Identifier M-UP-06 

|Identifier|M-UP-06|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the submitted DXAIP_NOK_SIG contains digital<br>signatures, which do not verify correctly13.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test case M-UP-03 was successfully performed with AOID-04<br>•<br>The TOT is configured only to accept valid signatures.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-04<br>into<br>the<br>prepared<br>DXAIP_NOK_SIG-template.|DXAIP_NOK_SIG(AOID-04, VID-01, VID-02)|
|2|ArchiveUpdateRequest<br>(<br>DXAIP_NOK_SIG(<br>AOID-04, VID-01, VID-02)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG),<br>dss:OptionalOutputs(<br>DXAIP_NOK_SIG_VR(AOID-04, VID-01, VID-02))<br>)|



Verdict of M-UP-06 Observations: Verdict: 

## 3.4.1.3.9 M-UP-07 DXAIP_NOK_ER 

Identifier M-UP-07 Test Purpose The test shall verify that there will be an error, because the submitted DXAIP_NOK_ER contains an invalid Evidence Record. Configuration • CONFIG_S.4 Pre-test • Authenticated connection to middleware exists. conditions • Make sure that test case M-UP-03 was successfully performed with AOID-04. 

Step Test sequence Expected Results 1 Insert AOID-04 into the prepared DXAIP_NOK_ER(AOID-04, VID-01, VID-02) DXAIP_NOK_ER-template. 2 ArchiveUpdateRequest ArchiveUpdateResponse ( ( DXAIP_NOK_ER( dss:Result(resultmajor#error, AOID-04, VID-01, VID-02) resultminor/arl/DXAIP_NOK_ER), ) dss:OptionalOutputs( DXAIP_NOK_ER_VR(AOID-04, VID-01, VID-02)) ) 

> 13 See Annex E (Version 1.2, Chapter 3.7.1, `(VerifyUnderSignaturePolicy)` 

Federal Office for Information Security 

55 

Web Service Interfaces 

Verdict of M-UP-07 

Observations: 

Verdict: 

## 3.4.1.3.10 M-UP-07a DLXAIP_NOK_ER 

## Identifier 

Identifier M-UP-07a Test Purpose The test shall verify that there will be an error, because the submitted DLXAIP_NOK_ER contains an invalid Evidence Record. Configuration • CONFIG_S.4 • CONFIG_LXAIP Pre-test • Authenticated connection to middleware exists. conditions • Make sure that test case M-UP-03a was successfully performed with AOID-04a. 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-04a<br>into<br>the<br>prepared<br>DLXAIP_NOK_ER-template.|DLXAIP_NOK_ER(AOID-04a, VID-01, VID-02)|
|2|ArchiveUpdateRequest<br>(<br>DLXAIP_NOK_ER(<br>AOID-04a, VID-01, VID-02,,<br>REF_CADES_ATT_TXT_DATA_57,<br>ER_NOK_LXAIP_OK_V2)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_ER),<br>dss:OptionalOutputs(<br>DLXAIP_NOK_ER_VR(AOID-04a, VID-01, VID-02))<br>)|



## Verdict of M-UP-07a 

Observations: 

## Verdict: 

3.4.1.3.11 M-UP-08 DXAIP_NOK_VERSION 

|Identifier|M-UP-08|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a DXAIP_NOK_VERSION is submitted with<br>`ArchiveUpdateRequest`, which produces a collision14with the already existing XAIP.|
|Configuration|•<br>CONFIG_S.4|



> 14 DXAIP_NOK_Version) may be caused by inserting a DXAIP where the value in the element `prevVersion` in the `updateSection` of the DXAIP is not the latest version of this XAIP. 

Federal Office for Information Security 

56 

Web Service Interfaces 

Identifier M-UP-08 Pre-test • Authenticated connection to middleware exists. conditions • Make sure that test case M-UP-03 was successfully performed with AOID-04. 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-04<br>into<br>the<br>prepared<br>DXAIP_NOK_VERSION-template.<br>Set<br>the<br>previous version to VID-10.|DXAIP_NOK_VERSION(AOID-04, VID-10, VID-02)|
|2|ArchiveUpdateRequest<br>(<br>DXAIP_NOK_VERSION(<br>AOID-04, VID-10, VID-02)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_Version)<br>)|
|3|Insert AOID-04 into the prepared DXAIP_OK-<br>template.|DXAIP_OK(AOID-04, VID-01, VID-02)|
|4|ArchiveUpdateRequest<br>(<br>DXAIP_OK(AOID-04, VID-01, VID-02)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#OK),<br>VersionID(VID-02)<br>)|
|5|Insert<br>AOID-04<br>into<br>the<br>prepared<br>DXAIP_NOK_VERSION-template.<br>Set<br>the<br>previous version to VID-01.|DXAIP_NOK_VERSION(AOID-04, VID-01, VID-03)|
|6|ArchiveUpdateRequest<br>(<br>DXAIP_NOK_VERSION(<br>AOID-04, VID-01, VID-03)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_Version)<br>)|
||||
||Verdict of M-UP-08||
|Observations:|||
|Verdict:|||



- 3.4.1.3.12 M-UP-09 DXAIP_OK with unknown control in OptionalInputs 

|Identifier|Identifier|M-UP-09|M-UP-09|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element.||
|Configuration||•<br>CONFIG_S.4||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.||
|||||
|Step||Test sequence|Expected Results|
|1|ArchiveSubmissionRequest<br>(<br>XAIP_OK<br>)||ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-05<br>)|



Federal Office for Information Security 

57 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|2|Insert AOID-05 into the prepared DXAIP_OK-<br>template.|DXAIP_OK(AOID-05, VID-01, VID-02)|
|3|ArchiveUpdateRequest<br>(<br>dss:OptionalInputs(SomethingUnknown),<br>DXAIP_OK(AOID-05, VID-01, VID-02)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/notSupported)<br>)|
|4|ArchiveUpdateRequest<br>(<br>DXAIP_OK(AOID-05, VID-01, VID-02)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#ok),<br>VersionID(VID-02)<br>)|
|5|Insert AOID-05 and VID-02 as previous and<br>VID-03 as new versions into the prepared<br>DXAIP_OK_2-template.|DXAIP_OK_2(AOID-05, VID-02, VID-03)|
|6|ArchiveUpdateRequest<br>(<br>DXAIP_OK_2(AOID-05, VID-02, VID-03)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#ok),<br>VersionID(VID-03)<br>)|



Verdict of M-UP-09 Observations: Verdict: 

## 3.4.1.3.13 M-UP-09a DLXAIP_OK with unknown control in OptionalInputs 

|Identifier|M-UP-09a|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>LXAIP_OK(<br>REF_TXT_DATA_58,<br>REF_PDF_DATA_58,<br>REF_XML_MDO_58<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-05a<br>)|
|2|Insert AOID-05a into the prepared DLXAIP_OK-<br>template.|DLXAIP_OK(AOID-05a, VID-01, VID-02)|



Federal Office for Information Security 

58 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|3|ArchiveUpdateRequest<br>(<br>dss:OptionalInputs(SomethingUnknown),<br>DLXAIP_OK(AOID-05a, VID-01, VID-02,<br>REF_CADES_ATT_TXT_DATA_59)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/notSupported)<br>)|
|4|ArchiveUpdateRequest<br>(<br>DLXAIP_OK(AOID-05a, VID-01, VID-02,<br>REF_CADES_ATT_TXT_DATA_60)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#ok),<br>VersionID(VID-02)<br>)|
|5|Insert<br>AOID-05a<br>into<br>the<br>prepared<br>DLXAIP_OK_2-template.|DLXAIP_OK_2(AOID-05a, VID-02, VID-03)|
|6|ArchiveUpdateRequest<br>(<br>DLXAIP_OK_2(<br>AOID-05a, VID-02, VID-03,<br>REF_XML_DATA_60-1,<br>REF_CADES_DET_XML_DATA_60-1)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#OK),<br>VersionID(VID-03)<br>)|
||||
||Verdict of M-UP-09a||
|Observations:|||
|Verdict:|||



Federal Office for Information Security 

59 

Web Service Interfaces 

## 3.4.1.4 Function ArchiveRetrieval of S.4-interface 

All test cases defined in this section are derived from the general requirement A2.0-2 together with the interface specification of the ArchiveRetrieval function in section 3.3 of [TR-ESOR-E] . 

## 3.4.1.4.1 M-RE-01 Retrieval of previously archived XAIPs 

|Identifier|M-RE-01|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve previously archived XAIPs.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test cases M-SU-01, M-UP-01 and M-UP-09 were successfully performed.<br>•<br>Requirements (A3.3.1-1) and (A3.3.1-2) of[TR-ESOR-E];|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveRetrievalRequest<br>(<br>AOID-01<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-01, VID-03)<br>)|
|2|ArchiveRetrievalRequest<br>(<br>AOID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK_SIG_OK(AOID-02, VID-01)<br>)|
|3|The fulfilment of the requirement A3.3.1-215is<br>checked.||
|4|ArchiveRetrievalRequest<br>(<br>AOID-05, VID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-05, VID-02)<br>)|
|5|ArchiveRetrievalRequest<br>(<br>AOID-05, VID-01<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-05, VID-01)<br>)|
|6|ArchiveRetrievalRequest<br>(<br>AOID-05, VID-01, VID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-05, VID-01, VID-02)<br>)|
|7|ArchiveRetrievalRequest<br>(<br>AOID-05, ALL<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-05, VID-01, VID-02, VID-03)<br>)|



15 See Annex E (Section 3.3.1). 

Federal Office for Information Security 

60 

Web Service Interfaces 

Step Test sequence Expected Results 8 Test of correctness of the obtained XAIP_OK(AOID-05, VID-01, VID-02, VID-03) by using AIP-eIDAS-SigValidator VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( XAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-05, VID-01, VID-02, VID-03) dssvr:Details( ) vr:XAIPReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) ) Verdict of M-RE-01 Observations: Verdict: 

## 3.4.1.4.2 M-RE-01a Retrieval of previously archived LXAIPs 

|Identifier|Identifier|M-RE-01a|M-RE-01a|
|---|---|---|---|
|Test Purpose||The test shall verify that it is possible to retrieve previously archived LXAIPs.||
|Configuration||•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test cases M-SU-01a, M-UP-01a and M-UP-09a were successfully<br>performed.<br>•<br>Requirements (A3.3.1-1) and (A3.3.1-2) of[TR-ESOR-E];;||
|||||
|Step||Test sequence|Expected Results|
|1|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-01a<br>)||ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-01a, VID-03)<br>)|



Federal Office for Information Security 

61 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|2|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-02a<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK_SIG_OK(AOID-02a, VID-01)<br>)|
|3|The fulfilment of the requirement A3.3.1-216is<br>checked.||
|4|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-05a, VID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-05a, VID-02)<br>)|
|5|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-05a, VID-01<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-05a, VID-01)<br>)|
|6|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-05a, VID-01, VID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-05a, VID-01, VID-02)<br>)|
|7|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-05a, ALL<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-05a, VID-01, VID-02, VID-03)<br>)|
|8|The all in LXAIP_OK(AOID-05a, VID-01, VID-02,<br>VID-03) referenced files has been copied into<br>corresponding LXAIP-directory of the AIP-<br>eIDAS-SigValidator during test preparation (cf.<br>chapter 4.3) and the given references in<br>LXAIP_OK(AOID-05a, VID-01, VID-02, VID-03)<br>will be adjusted automatically in order to get<br>them<br>resolveable<br>by<br>the<br>AIP-eIDAS-<br>SigValidator.|LXAIP_OK_XSV(AOID-05a, VID-01, VID-02, VID-03)|



16 See Annex E (Section 3.3.1). 

Federal Office for Information Security 

62 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|9|Test of correctness of the obtained and prepared<br>LXAIP_OK_XSV(AOID-05a,<br>VID-01,<br>VID-02,<br>VID-03) by using AIP-eIDAS-SigValidator<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_XSV(<br>AOID-05a, VID-01, VID-02, VID-03)<br>)<br>)<br>)<br>)|VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid )<br>dssvr:Details(<br>vr:XAIPReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|
|10|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/xaip/1.3 <br>)<br>),<br>AOID-01a<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-01a, VID-03)<br>)|
|11|ArchiveRetrievalRequest<br>(<br>AOID-01a<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-01a, VID-03)<br>)|



Verdict of M-RE-01a 

Observations: 

## Verdict: 

## 3.4.1.4.3 M-RE-02 Retrieval of XAIPs for known and unknown AOIDs 

|Identifier|M-RE-02|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve XAIPs for known AOIDs and there will be an error<br>in case of unknown AOIDs.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test cases M-SU-01 was successfully performed.|



Federal Office for Information Security 

63 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Choice an AOID-06 within the possible range<br>and make sure, that it has not been assigned yet.<br>This is realised by the following call:<br>ArchiveRetrievalRequest<br>(<br>AOID-06<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|
|'2|ArchiveRetrievalRequest<br>(<br>AOID-01<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-01, VID-03)<br>)|
|3|ArchiveRetrievalRequest<br>(<br>AOID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK_SIG_OK(AOID-02, VID-01)<br>)|
|4|ArchiveRetrievalRequest<br>(<br>AOID-06<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|



## Verdict M-RE-02 

Observations: Verdict: 

## 3.4.1.4.4 M-RE-03 Retrieval of XAIPs for known and unknown VersionIDs 

|Identifier|M-RE-03|
|---|---|
|Test Purpose|The test shall verify that there will be a requestOnlyPartlySuccessfulWarning, if it is not possible<br>to retrieve XAIPs for all indicated`VersionID`-attributes.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test case M-SU-01 was successful performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Choice a VID-10 within the possible range and<br>make sure, that it has not been assigned yet. This<br>is realised by the following call:<br>ArchiveRetrievalRequest<br>(<br>AOID-01, VID-10<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownVersionID)<br>)|



Federal Office for Information Security 

64 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|'2|ArchiveRetrievalRequest<br>(<br>AOID-01, VID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-01, VID-02)<br>)|
|3|ArchiveRetrievalRequest<br>(<br>AOID-01, VID-10<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownVersionID)<br>)|
|4|ArchiveRetrievalRequest<br>(<br>AOID-01, VID-02, VID-10<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#warning<br>resultminor/arl/requestOnlyPartlySuccessfulWarning),<br>XAIP_OK(AOID-01, VID-02)<br>)|
||||
||Verdict of M-RE-03||
|Observations:|||
|Verdict:|||



## 3.4.1.4.5 M-RE-04 Unknown control in OptionalInputs 

|Identifier|Identifier|M-RE-04|M-RE-04|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element.||
|Configuration||•<br>CONFIG_S.4||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test case M-SU-01 was successfully performed.||
|||||
|Step||Test sequence|Expected Results|
|1|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(SomethingUnknown),<br>AOID-01<br>)||ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/notSupported)<br>)|
|||||
||Verdict of M-RE-04|||
|Observations:||||
|Verdict:||||



Federal Office for Information Security 

65 

Web Service Interfaces 

## 3.4.1.5 Function ArchiveEvidence of S.4-interface 

All test cases defined in this section are derived from the general requirement A2.0-2 together with the interface specification of the ArchiveEvidence function in section 3.4 of [TR ESOR E] . 

- 3.4.1.5.1 M-EV-01 Retrieval of Evidence Records of previously archived XAIPs without specifying the desired ERS Format 

|Identifier|M-EV-01|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve Evidence Records for previously archived XAIPs.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test cases M-SU-01 M-UP-01, M-UP-09 and M-RE-01 were successfully<br>performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveEvidenceRequest<br>(<br>AOID-01<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS17(<br>AOID-01, VID-03,<br>XAIP_OK_V3_ER_OK)<br>)|
|2|ArchiveEvidenceRequest<br>(<br>AOID-02<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-02, VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK)<br>)|
|3|ArchiveEvidenceRequest<br>(<br>AOID-01, VID-02<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01, VID-02,<br>XAIP_OK_V2_ER_OK)<br>)|
|4|ArchiveEvidenceRequest<br>(<br>AOID-01, VID-01<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01, VID-01,<br>XAIP_OK_V1_ER_OK)<br>)|



> 17 XAIP-ERS does mean a RFC4998-ER embedded in the element `xaip:asn1EvidenceRecord` , which in turn is embedded in the element `xaip:evidenceRecord` and can contain the both attributes `AOID` and `VersionID` . 

Federal Office for Information Security 

66 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|5|ArchiveEvidenceRequest<br>(<br>AOID-01, VID-01, VID-03<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01, VID-01,<br>XAIP_OK_V1_ER_OK),<br>XAIP_ERS(<br>AOID-01, VID-03,<br>XAIP_OK_V3_ER_OK)<br>)|
|6|ArchiveEvidenceRequest<br>(<br>AOID-01, ALL<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01, VID-01,<br>XAIP_OK_V1_ER_OK),<br>XAIP_ERS(<br>AOID-01, VID-02,<br>XAIP_OK_V2_ER_OK),<br>XAIP_ERS(<br>AOID-01, VID-03,<br>XAIP_OK_V3_ER_OK)<br>)|
|7|ArchiveRetrievalRequest<br>(<br>AOID-01, ALL<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-01, VID-01, VID-02, VID-03)<br>)|



Federal Office for Information Security 

67 

Web Service Interfaces 

Step Test sequence Expected Results 8 Test of correcteness of the obtained XAIP_OK_V1_ER_OK, XAIP_OK_V2_ER_OK and XAIP_OK_V3_ER_OK by using ERVerifyTool. VerifyRequest ( VerifyResponse( dss:InputDocuments( dss:Result(resultmajor#ok), dss:Document( dss:OptionalOutputs( dss:InlineXML( dssvr:VerificationReport( XAIP_OK( dssvr:IndividualReport( AOID-01, VID-01, VID-02, VID-03) dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) ) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( dss:SignatureObject( urn:oasis:names:tc:dss:1.0:detail:valid dss:Other( ) XAIP_ERS( AOID-01,VID-01, ) XAIP_OK_V1_ER_OK), ) XAIP_ERS( ), AOID-01,VID-02, dssvr:IndividualReport( XAIP_OK_V2_ER_OK), dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) XAIP_ERS( dssvr:Details( AOID-01,VID-03, vr:EvidenceRecordReport( XAIP_OK_V3_ER_OK) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

Verdict of M-EV-01 

Observations: 

## Verdict: 

- 3.4.1.5.2 M-EV-01a Retrieval of Evidence Records of previously archived LXAIPs without specifying the desired ERS Format 

Identifier M-EV-01a 

Test Purpose The test shall verify that it is possible to retrieve Evidence Records for previously archived LXAIPs. 

Federal Office for Information Security 

68 

Web Service Interfaces 

|Identifier|M-EV-01a|
|---|---|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test cases M-SU-01a, M-UP-01a and M-UP-09a were successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveEvidenceRequest<br>(<br>AOID-01a<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS18(<br>AOID-01a, VID-03,<br>LXAIP_OK_V3_ER_OK)<br>)|
|2|ArchiveEvidenceRequest<br>(<br>AOID-02a<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-02a, VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK)<br>)|
|3|ArchiveEvidenceRequest<br>(<br>AOID-01a, VID-02<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01a, VID-02,<br>LXAIP_OK_V2_ER_OK)<br>)|
|4|ArchiveEvidenceRequest<br>(<br>AOID-01a, VID-01<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01a, VID-01,<br>LXAIP_OK_V1_ER_OK)<br>)|
|5|ArchiveEvidenceRequest<br>(<br>AOID-01a, VID-01, VID-03<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01a, VID-01,<br>LXAIP_OK_V1_ER_OK),<br>XAIP_ERS(<br>AOID-01a, VID-03,<br>LXAIP_OK_V3_ER_OK)<br>)|



> 18 XAIP-ERS does mean a RFC4998-ER embedded in the element `xaip:asn1EvidenceRecord` , which in turn is embedded in the element `xaip:evidenceRecord` and can contain the both attributes `AOID` and `VersionID` . 

Federal Office for Information Security 

69 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|6|ArchiveEvidenceRequest<br>(<br>AOID-01a, ALL<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01a, VID-01,<br>LXAIP_OK_V1_ER_OK),<br>XAIP_ERS(<br>AOID-01a, VID-02,<br>LXAIP_OK_V2_ER_OK),<br>XAIP_ERS(<br>AOID-01a, VID-03,<br>LXAIP_OK_V3_ER_OK)<br>)|
|7|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-01a, ALL<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-01a, VID-01, VID-02, VID-03)<br>)|



Federal Office for Information Security 

70 

Web Service Interfaces 

Step Test sequence Expected Results 8 Test of correcteness of the obtained LXAIP_OK_V1_ER_OK, LXAIP_OK_V2_ER_OK and LXAIP_OK_V3_ER_OK by using ERVerifyTool. The particular object references in the obtained LXAIP_OK will be replaced by the references compatible with the ERVerifyTool in advance. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( LXAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01a, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01a, VID-01, ) LXAIP_OK_V1_ER_OK), ), XAIP_ERS( dssvr:IndividualReport( AOID-01a, VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) LXAIP_OK_V2_ER_OK), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01a, VID-03, vr:FormatOK( LXAIP_OK_V3_ER_OK) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

Verdict of M-EV-01a 

Observations: 

## Verdict: 

Federal Office for Information Security 

71 

Web Service Interfaces 

## 3.4.1.5.3 M-EV-02 Retrieval of Evidence Records for known and unknown AOIDs 

|Identifier|Identifier|M-EV-02|M-EV-02|
|---|---|---|---|
|Test Purpose||The test case verifies that that it is possible to retrieve an EvidenceRecord for known AOIDs and<br>there will be an error in case of unknown AOIDs.||
|Configuration||•<br>CONFIG_S.4||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test cases M-SU-01 and M-RE-02 were successfully performed.||
|||||
|Step||Test sequence|Expected Results|
|1|Make sure, that the previous chosen AOID-06 is<br>within the possible range and it is still not<br>assigned yet. This is realised by the following<br>call:<br>ArchiveRetrievalRequest<br>(<br>AOID-06<br>)||ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|
|2|ArchiveEvidenceRequest<br>(<br>AOID-01<br>)||ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01, VID-03,<br>XAIP_OK_V3_ER_OK)<br>)|
|3|ArchiveEvidenceRequest<br>(<br>AOID-02<br>)||ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-02, VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK)<br>)|
|4|ArchiveEvidenceRequest<br>(<br>AOID-06<br>)||ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|



## **Verdict of M-EV-02** 

Observations: 

Verdict: 

## 3.4.1.5.4 M-EV-03 Retrieval of Evidence Records for partly known VersionIDs 

Identifier M-EV-03 Test Purpose The test case verifies that there is a requestOnlyPartlySuccessfulWarning, if an Evidence Record for an unknown `VersionID` is requested. 

Federal Office for Information Security 

72 

Web Service Interfaces 

M-EV-03 

## Identifier 

|Identifier|M-EV-03|
|---|---|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test cases M-SU-01 and M-RE-03 were successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Make sure, that concerning AOID-01, the chosen<br>version VID-10 is within the possible range but<br>is an unknown VersionID. This is realised by the<br>following call:<br>ArchiveRetrievalRequest<br>(<br>AOID-01, VID-10<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownVersionID)<br>)|
|2|ArchiveEvidenceRequest<br>(<br>AOID-01<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-01, VID-03,<br>XAIP_OK_V3_ER_OK)<br>)|
|3|ArchiveEvidenceRequest<br>(<br>AOID-01, VID-10<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownVersionID)<br>)|
|4|ArchiveEvidenceRequest<br>(<br>AOID-01, VID-02, VID-10<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#warning,<br>resultminor/arl/requestOnlyPartlySucessfulWarning),<br>XAIP_ERS(<br>AOID-01, VID-02,<br>XAIP_OK_V2_ER_OK)<br>)|



Verdict of M-EV-03 

Observations: Verdict: 

## 3.4.1.5.5 M-EV-04 Unknown control in OptionalInputs 

|Identifier|M-EV-04|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test case M-SU-01 was successfully performed.|



Federal Office for Information Security 

73 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveEvidenceRequest<br>(<br>dss:OptionalInputs(SomethingUnknown),<br>AOID-01<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/notSupported)<br>)|



Verdict of M-EV-04 Observations: Verdict: 

Federal Office for Information Security 

74 

Web Service Interfaces 

## 3.4.1.6 Function ArchiveDeletion of S.4-interface 

All test cases defined in this section are derived from the general requirement A2.0-2 together with the interface specification of the ArchiveDeletion function in section 3.5 of [TR ESOR E] . 

## 3.4.1.6.1 M-DE-01 Deletion of XAIP without `ReasonOfDeletion` 

|Identifier|M-DE-01|
|---|---|
|Test Purpose|The test shall verify that it will yield an error, if`ArchiveDeletionRequest`is called without<br>providing a`ReasonOfDeletion,`if the element`retentionPeriod`in the XAIP contains a<br>predetermined future date.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>In one test case the element`retentionPeriod`in the XAIP to be deleted contains a<br>predetermined future date. In the other test case the element`retentionPeriod`contains a<br>date in the past.<br>•<br>Authenticated connection to middleware exists.<br>•<br>Requirement (A3.5.1-1)of [TR-ESOR-E]:<br>•<br>The<br>`ArchiveDeletionRequest`of XAIP with AOID-02 with the end of the<br>`retentionPeriod`in the future must not be successful without a reason for the deletion.<br>•<br>Make sure that the test case M-SU-01 was successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveDeletionRequest<br>(<br>AOID-02<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/missingReasonOfDeletion)<br>)|
|'2|ArchiveRetrievalRequest<br>(<br>AOID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK_SIG_OK(AOID-02, VID-01)<br>)|
|3|ArchiveRetrievalRequest<br>(<br>AOID-0019<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-00, VID-01)<br>)|
|4|ArchiveDeletionRequest<br>(<br>AOID-00<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|5|ArchiveRetrievalRequest<br>(<br>AOID-00<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|



> 19 The XAIP with AOID-00 and LXAIP with AOID-00a were imported some days ago. The retention period is expired. 

Federal Office for Information Security 

75 

Web Service Interfaces 

Verdict of M-DE-01 

Observations: 

## Verdict: 

## 3.4.1.6.2 M-DE-01a Deletion of LXAIP without `ReasonOfDeletion` 

|Identifier|M-DE-01a|
|---|---|
|Test Purpose|The test shall verify that it will yield an error, if`ArchiveDeletionRequest`is called without<br>providing a`ReasonOfDeletion`if the element`retentionPeriod`in the LXAIP contains a<br>predetermined future date.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>In one test case the element`retentionPeriod`in the LXAIP to be deleted contains a<br>predetermined future date. In the other test case the element`retentionPeriod`contains a<br>date in the past.<br>•<br>Authenticated connection to middleware exists.<br>•<br>Requirement (A3.5.1-1) of[TR-ESOR-E];:<br>•<br>The`ArchiveDeletionRequest`of LXAIP with AOID-02a with the end of the<br>`retentionPeriod`in the future must not be successful without a reason for the deletion.<br>•<br>Make sure that the test case M-SU-01a was successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveDeletionRequest<br>(<br>AOID-02a<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/missingReasonOfDeletion)<br>)|
|'2|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-02a<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK_SIG_OK(AOID-02a, VID-01)<br>)|
|3|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-00a19<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-00a, VID-01)<br>)|
|4|ArchiveDeletionRequest<br>(<br>AOID-00a<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

76 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|5|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-00a<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|
||||
||Verdict of M-DE-01a||
|Observations:|||
|Verdict:|||



## 3.4.1.6.3 M-DE-02 Deletion of XAIP with `ReasonOfDeletion` 

|Identifier|M-DE-02|
|---|---|
|Test Purpose|The test shall verify that it is possible to delete an XAIP by calling`ArchiveDeletionRequest`<br>with`ReasonOfDeletion`among the`dss:OptionalInputs`.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>The element`retentionPeriod`in the XAIP to be deleted contains a predetermined future<br>date.<br>•<br>Make sure that the test case M-SU-01 was successfully performed.<br>•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveDeletionRequest<br>(<br>dss:OptionalInputs(ReasonOfDeletion(<br>RequestorName(SomeName),<br>RequestInfo(SomeInfo)<br>),<br>AOID-02<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|'2|ArchiveRetrievalRequest<br>(<br>AOID-02<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|
|3|Check requirement A3.5.1-220.||



20 See Annex E (Section 3.5.1). 

Federal Office for Information Security 

77 

Web Service Interfaces 

Verdict of M-DE-02 

Observations: 

Verdict: 

## 3.4.1.6.4 M-DE-02a Deletion of LXAIP with `ReasonOfDeletion` 

|Identifier|M-DE-02a|
|---|---|
|Test Purpose|The test shall verify that it is possible to delete an LXAIP by calling`ArchiveDeletionRequest`<br>with`ReasonOfDeletion`among the`dss:OptionalInputs`.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>The element`retentionPeriod`in the LXAIP to be deleted contains a predetermined future<br>date.<br>•<br>Make sure that the test case M-SU-01a was successfully performed.<br>•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveDeletionRequest<br>(<br>dss:OptionalInputs(ReasonOfDeletion(<br>RequestorName(SomeName),<br>RequestInfo(SomeInfo)<br>),<br>AOID-02a<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|'2|ArchiveRetrievalRequest<br>(<br>dss:OptionalInputs(<br>pres:POFormat(<br>  http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>)<br>),<br>AOID-02a<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|
|3|Check requirement A3.5.1-221.||
||||
||Verdict of M-DE-02a||
|Observations:|||
|Verdict:|||



21 See Annex E (Section 3.5.1). 

Federal Office for Information Security 

78 

Web Service Interfaces 

## 3.4.1.6.5 M-DE-03 Deletion of unknown XAIPs without `ReasonOfDeletion` 

|Identifier|M-DE-03|
|---|---|
|Test Purpose|The test shall verify that it will yield an error, if`ArchiveDeletionRequest`is called without<br>providing a`ReasonOfDeletion`. As the present call also contains the unknown AOID-06, the<br>AOID-specific`dss:Result`needs to indicate that the AOID is unknown.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>The element`retentionPeriod`in the XAIP to be deleted contains a predetermined future<br>date.<br>•<br>Make sure that the test cases M-UP-09 and M-RE-02 were successfully performed.<br>•<br>Make sure, that the randomly generated AOID-06 is within the possible range but has not<br>been assigned yet.<br>•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveDeletionRequest<br>(<br>AOID-05<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/missingReasonOfDeletion)<br>)|
|2|ArchiveDeletionRequest<br>(<br>AOID-06<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|
|3|ArchiveRetrievalRequest<br>(<br>AOID-05<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-05, VID-03)<br>)|



Verdict of M-DE-03 Observations: Verdict: 

## 3.4.1.6.6 M-DE-04 Deletion of unknown XAIPs with `ReasonOfDeletion` 

|Identifier|M-DE-04|
|---|---|
|Test Purpose|The test shall verify that it will yield an error, if`ArchiveDeletionRequest`is called with<br>unknown AOIDs with providing a`ReasonOfDeletion`.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>The element`retentionPeriod`în the XAIP to be deleted contains a predetermined future<br>date.<br>•<br>Make sure that the test case M-RE-02 was successfully performed<br>•<br>Make sure, that the randomly generated AOID-06 is within the possible range but has not<br>been assigned yet.<br>•<br>Authenticated connection to middleware exists.|



Federal Office for Information Security 

79 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveDeletionRequest<br>(<br>dss:OptionalInputs(ReasonOfDeletion(<br>RequestorName(SomeName),<br>RequestInfo(SomeInfo)<br>)),<br>AOID-06<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/unknownAOID)<br>)|
||||
||Verdict of M-DE-04||
|Observations:|||
|Verdict:|||



## 3.4.1.6.7 M-DE-05 Unknown control in `OptionalInputs` 

|Identifier|M-DE-05|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element and the`ArchiveDeletionRequest`will not be successful.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The element`retentionPeriod`in the XAIP to be deleted contains a predetermined future<br>date.<br>•<br>Make sure that the test case M-UP-09 was successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveDeletionRequest<br>(<br>dss:OptionalInputs(SomethingUnknown),<br>AOID-05<br>)|ArchiveDeletionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/notSupported)<br>)|
|'2|ArchiveRetrievalRequest<br>(<br>AOID-05<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-05, VID-03)<br>)|



Verdict of M-DE-05 Observations: Verdict: 

Federal Office for Information Security 

80 

Web Service Interfaces 

## 3.4.1.7 Function Verify of S.4-interface 

All test cases defined in this section are derived from the general requirement A2.0-2 together with the interface specification of the Verify function in section 3.7 of [TR ESOR E] . 

3.4.1.7.1 M-VE-01 XAIP_OK_SIG_OK and XAIP_OK_SIG_OK_ER 

|Identifier|M-VE-01|
|---|---|
|Test Purpose|The<br>test<br>shall<br>verify<br>that<br>it<br>is<br>possible<br>to<br>verify<br>XAIP_OK_SIG_OK<br>and<br>XAIP_OK_SIG_OK_V1_ER_OK<br>with<br>the<br>TR-ESOR-specific<br>signature<br>policy<br>http://www.bsi.bund.de/tr-esor/sigpolicy/verify-xaip.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>XAIP_OK_SIG_OK<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-100<br>)|
|2|ArchiveRetrievalRequest<br>(<br>AOID-100<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK_SIG_OK(AOID-100, VID-01)<br>)|
|3|ArchiveEvidenceRequest7<br>(<br>AOID-100<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-100,VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK)<br>)|
|4|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK_SIG_OK(AOID-100, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|5|VerifyRequest<br>(<br>dss:OptionalInputs(<br>vr:ReturnVerificationReport),<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK_SIG_OK(AOID-100, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR)<br>)<br>)|



Federal Office for Information Security 

81 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|'6|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-100, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|7|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>XAIP_OK_SIG_OK(AOID-100, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|8|Prepare XAIP_OK_SIG_OK_ER(AOID-100, VID-<br>01) by inserting the XAIP_ERS(AOID-100,VID-<br>01, XAIP_OK_SIG_OK_V1_ER_OK) obtained in<br>step 3 into`credentialsSection`element of<br>XAIP_OK_SIG_OK(AOID-100, VID-01) from step<br>2.|XAIP_OK_SIG_OK_ER(AOID-100, VID-01)|
|9|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK_SIG_OK_ER(AOID-100,VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|10|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK_ER(AOID-100,VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|11|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>XAIP_OK_SIG_OK_ER(AOID-100,VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

82 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|12|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK_SIG_OK(AOID-100, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-100,VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|13|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-100, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-100,VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|14|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>XAIP_OK_SIG_OK(AOID-100, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-100,VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|




![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0083-02.png)


**----- Start of picture text -----**<br>
Verdict of M-VE-01<br>Observations:<br>Verdict:<br>**----- End of picture text -----**<br>


Federal Office for Information Security 

83 

Web Service Interfaces 

## 3.4.1.7.2 M-VE-01a - LXAIP_OK_SIG_OK and LXAIP_OK_SIG_OK_ER 

|Identifier|M-VE-01a|
|---|---|
|Test Purpose|The test shall verify that it is possible to verify LXAIP_OK_SIG_OK and LXAIP_OK_SIG_OK_ER<br>with the TR-ESOR-specific signature policy http://www.bsi.bund.de/tr-esor/sigpolicy/verify-<br>xaip.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Test M-SU-01a has been performed successfully and the references has been set properly in<br>LXAIP_OK_SIG_OK|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>LXAIP_OK_SIG_OK(<br>REF_TXT_DATA_61,<br>REF_CADES_DET_TXT_DATA_61,<br>REF_PDF_DATA_61,<br>REF_CADES_DET_PDF_DATA_61,<br>REF_XML_MDO_61<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-101<br>)|
|2|ArchiveRetrievalRequest<br>(<br>AOID-101<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK_SIG_OK(AOID-101, VID-01)<br>)|
|3|ArchiveEvidenceRequest7<br>(<br>AOID-101<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS(<br>AOID-101,VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK)<br>)|
|4|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_SIG_OK(AOID-101, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|5|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:OptionalInputs(<br>vr:ReturnVerificationReport),<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_SIG_OK(AOID-101, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(LXAIP_OK_SIG_OK_VR)<br>)|



Federal Office for Information Security 

84 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|'6|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>LXAIP_OK_SIG_OK(AOID-101, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|7|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>LXAIP_OK_SIG_OK(AOID-101, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|8|Prepare<br>LXAIP_OK_SIG_OK_ER(AOID-101,<br>VID-01) by inserting the XAIP_ERS(AOID-<br>101,VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK)<br>obtained in step 3 into credentialsSection<br>element of LXAIP_OK_SIG_OK(AOID-101, VID-<br>01) from step 2.|LXAIP_OK_SIG_OK_ER(AOID-101, VID-01)|
|9|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_SIG_OK_ER(AOID-101,VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|10|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>LXAIP_OK_SIG_OK_ER(AOID-101,VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|11|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>LXAIP_OK_SIG_OK_ER(AOID-101,VID-01)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

85 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|12|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_SIG_OK(AOID-101, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-101,VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|13|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>LXAIP_OK_SIG_OK(AOID-101, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-101,VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|14|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>LXAIP_OK_SIG_OK(AOID-101, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-101,VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
||||
||Verdict of M-VE-01a||
|Observations:|||
|Verdict:|||



Federal Office for Information Security 

86 

Web Service Interfaces 

## 3.4.1.7.3 M-VE-02 - DXAIP_OK_SIG_OK 

|Identifier|M-VE-02|
|---|---|
|Test Purpose|The test shall verify that it is possible to verify DXAIP_OK_SIG_OK with the TR-ESOR-specific<br>signature policy http://www.bsi.bund.de/tr-esor/sigpolicy/verify-xaip.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The test M-VE-01 has been performed successfully|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Prepare DXAIP_OK_SIG_OK by inserting the<br>AOID-100|DXAIP_OK_SIG_OK(AOID-100, VID-01, VID-02)|
|2|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>DXAIP_OK_SIG_OK(<br>AOID-100, VID-01,VID-02)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|'3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>DXAIP_OK_SIG_OK(<br>AOID-100, VID-01, VID-02)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|4|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>DXAIP_OK_SIG_OK(<br>AOID-100, VID-01, VID-02)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Verdict of M-VE-02 

Observations: 

## Verdict: 

Federal Office for Information Security 

87 

Web Service Interfaces 

## 3.4.1.7.4 M-VE-02a - DLXAIP_OK_SIG_OK 

|Identifier|M-VE-02a|
|---|---|
|Test Purpose|The test shall verify that it is possible to verify DLXAIP_OK_SIG_OK with the TR-ESOR-specific<br>signature policy http://www.bsi.bund.de/tr-esor/sigpolicy/verify-xaip.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The test M-VE-01a has been performed successfully.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Prepare DLXAIP_OK_SIG_OK by inserting the<br>AOID-101.|DLXAIP_OK_SIG_OK(AOID-101, VID-01, VID-02)|
|2|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>DLXAIP_OK_SIG_OK(<br>AOID-101, VID-01, VID-02,<br>REF_XML_DATA_62,<br>REF_CADES_DET_XML_DATA_62)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|'3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>DLXAIP_OK_SIG_OK(<br>AOID-101, VID-01, VID-02,<br>REF_XML_DATA_63,<br>REF_CADES_DET_XML_DATA_63)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|4|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>DLXAIP_OK_SIG_OK(<br>AOID-101, VID-01, VID-02,<br>REF_XML_DATA_64,<br>REF_CADES_DET_XML_DATA_64)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

88 

Web Service Interfaces 

Verdict of M-VE-02a 

Observations: 

## Verdict: 

## 3.4.1.7.5 M-VE-03 BIN_OK 

|Identifier|M-VE-03|
|---|---|
|Test Purpose|The test shall validate that it is possible to verify as BIN defined data. BIN means here:<br>•<br>CADES_DET_OK, CADES_ATT_OK,<br>•<br>XADES_DET_OK, XADES_ENVELOPED_OK, XADES_ENVELOPING_OK,<br>•<br>PADES_OK,<br>•<br>ASiC_S_CADES_OK, ASIC_S_XADES_OK, ASIC_S_TST_OK, ASIC_S_ER_OK,<br>•<br>ASiC_E_CADES_OK, ASIC_E_XADES_OK, ASIC_E_TST_OK, ASIC_E_ER_OK.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The as CONDITIONAL marked test steps shall be executed, in case the TOT does support<br>passing by the XML data as native XML, e.g.`dss:InlineXML`-element, or`ds:Signature`-<br>element etc.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(TXT_DATA.txt)<br>)<br>)<br>dss:SignatureObject(<br>dss:Base64Signature(CADES_DET_OK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|2|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(CADES_ATT_OK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(PADES_OK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

89 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|4|[CONDITIONAL]<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(002-test-document.xml)<br>)<br>)<br>dss:SignatureObject(<br>ds:Signature(XADES_DET_OK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|'5|[CONDITIONAL]<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(002-test-document.xml)<br>)<br>)<br>dss:SignatureObject(<br>ds:Signature(XADES_DET_OK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|6|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(002-test-document.xml)<br>)<br>)<br>dss:SignatureObject(<br>dss:Base64Signature(XADES_DET_OK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|7|[CONDITIONAL]<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(XADES_ENVELOPED_OK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|8|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(XADES_ENVELOPED_OK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|9|[CONDITIONAL]<br>VerifyRequest<br>(<br>dss:SignatureObject(<br>ds:Signature(XADES_ENVELOPING_OK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

90 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|10|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>XADES_ENVELOPING_OK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|11|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASiC_S_CADES_OK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|12|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_S_XADES_OK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|13|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_S_TST_OK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|14|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_S_ER_OK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|15|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASiC_E_CADES_OK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|16|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_E_XADES_OK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

91 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|17|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_E_TST_OK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|18|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_E_ER_OK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
||||
||Verdict of M-VE-03||
|Observations:|||
|Verdict:|||



## 3.4.1.7.6 M-VE-04 - XAIP_OK_SIG_NOK & XAIP_OK_SIG_OK_ER_NOK 

|Identifier|M-VE-04|
|---|---|
|Test Purpose|The test shall verify that there will be a verification error, in case XAIP_OK_SIG_NOK or<br>XAIP_OK_SIG_OK_ER_NOK is submitted.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK_SIG_NOK<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(XAIP_OK_SIG_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_NOK(XAIP_OK_SIG_NOK_VR)<br>)<br>)|



Federal Office for Information Security 

92 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|2|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK_SIG_OK_ER_NOK<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER)<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_ER_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK_ER_NOK(<br>XAIP_OK_SIG_OK_ER_NOK_VR)<br>)<br>)|
|3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_NOK<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(XAIP_OK_SIG_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_NOK(XAIP_OK_SIG_NOK_VR)<br>)<br>)|
|4|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK_ER_NOK<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER)<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_ER_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER)<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK_ER_NOK(<br>XAIP_OK_SIG_OK_ER_NOK_VR)<br>)<br>)|



Verdict of M-VE-04 Observations: 

Verdict: 

Federal Office for Information Security 

93 

Web Service Interfaces 

3.4.1.7.7 M-VE-04a - LXAIP_OK_SIG_NOK & LXAIP_OK_SIG_OK_ER_NOK 

Identifier M-VE-04a Test Purpose The test shall verify that there will be a verification error, in case of LXAIP_OK_SIG_NOK or LXAIP_OK_SIG_OK_ER_NOK is submitted. The response will include either the `VerificationReport` -element only or the LXAIP including the `VerificationReport` -element. Configuration • CONFIG_S.4 • CONFIG_LXAIP Pre-test • Authenticated connection to middleware exists. conditions • Test M-SU-01a has been performed successfully and the references has been set properly in LXAIP_OK_SIG_OK. 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_SIG_NOK(<br>TXT_DATA_65.txt,<br>REF_CADES_DET_NOK_TXT_DATA_65,<br>REF_PDF_DATA_65,<br>REF_CADES_DET_PDF_DATA_65,<br>REF_XML_MDO_65<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(LXAIP_OK_SIG_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>LXAIP_OK_SIG_NOK(LXAIP_OK_SIG_NOK_VR)<br>)<br>)|
|2|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_SIG_OK_ER_NOK(<br>TXT_DATA_66.txt,<br>REF_CADES_DET_TXT_DATA_66,<br>REF_PDF_DATA_66,<br>REF_CADES_DET_PDF_DATA_66,<br>REF_XML_MDO_66,<br>ER_NOK_XAIP_OK_SIG_OK_00<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER)<br>dss:OptionalOutputs(LXAIP_OK_SIG_OK_ER_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>LXAIP_OK_SIG_OK_ER_NOK(<br>LXAIP_OK_SIG_OK_ER_NOK_VR)<br>)<br>)|



Federal Office for Information Security 

94 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>LXAIP_OK_SIG_NOK(<br>TXT_DATA_67.txt,<br>REF_CADES_DET_NOK_TXT_DATA_67,<br>REF_PDF_DATA_67,<br>REF_CADES_DET_PDF_DATA_67,<br>REF_XML_MDO_67<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(LXAIP_OK_SIG_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>LXAIP_OK_SIG_NOK(LXAIP_OK_SIG_NOK_VR)<br>)<br>)|
|4|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>LXAIP_OK_SIG_OK_ER_NOK(<br>TXT_DATA_68.txt,<br>REF_CADES_DET_TXT_DATA_68,<br>REF_PDF_DATA_68,<br>REF_CADES_DET_PDF_DATA_68,<br>REF_XML_MDO_68,<br>ER_NOK_XAIP_OK_SIG_OK_00<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER)<br>dss:OptionalOutputs(LXAIP_OK_SIG_OK_ER_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>LXAIP_OK_SIG_OK_ER_NOK(<br>LXAIP_OK_SIG_OK_ER_NOK_VR)<br>)<br>)|



Verdict of M-VE-04a Observations: Verdict: 

||Observations:|Observations:||
|---|---|---|---|
||Verdict:|||
|3.4.1.7.8||M-VE-05|-DXAIP_OK_SIG_NOK|



|Identifier|Identifier|M-VE-05|M-VE-05|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be a verification error, in case DXAIP_OK_SIG_NOK is<br>submitted.||
|Configuration||•<br>CONFIG_S.4||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Test M-VE-01 has been performed successfully.||
|||||
|Step||Test sequence|Expected Results|
|1|Prepare DXAIP_OK_SIG_NOK by inserting<br>AOID-100.||DXAIP_OK_SIG_NOK (AOID-100, VID-01, VID-02)|



Federal Office for Information Security 

95 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|2|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>DXAIP_OK_SIG_NOK (<br>AOID-100, VID-01, VID-02)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG)<br>dss:OptionalOutputs(DXAIP_OK_SIG_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>DXAIP_OK_SIG_NOK(DXAIP_OK_SIG_NOK_VR)<br>)<br>)|
|3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>DXAIP_OK_SIG_NOK(<br>AOID-100, VID-01, VID-02)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG)<br>dss:OptionalOutputs(DXAIP_OK_SIG_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>DXAIP_OK_SIG_NOK(DXAIP_OK_SIG_NOK_VR)<br>)<br>)|



Verdict of M-VE-05 Observations: Verdict: 

## 3.4.1.7.9 M-VE-05a - DLXAIP_OK_SIG_NOK 

|Identifier|Identifier|M-VE-05a|M-VE-05a|
|---|---|---|---|
|Test Purpose||The test case shall verify that there will be a verification error, in case DLXAIP_OK_SIG_NOK is<br>submitted.||
|Configuration||•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Test M-VE-01a has been performed successfully.||
|||||
|Step||Test sequence|Expected Results|
|1|Prepare DLXAIP_OK_SIG_NOK by inserting<br>AOID-101.||DLXAIP_OK_SIG_NOK(AOID-100, VID-01, VID-02)|



Federal Office for Information Security 

96 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|2|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>DLXAIP_OK_SIG_NOK(<br>AOID-101, VID-01, VID-02,<br>REF_XML_DATA_69,<br>REF_CADES_DET_NOK_XML_DATA_69)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG)<br>dss:OptionalOutputs(DXAIP_OK_SIG_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>DLXAIP_OK_SIG_NOK(<br>AOID-101, VID-01, VID-02, DXAIP_OK_SIG_NOK_VR)<br>)<br>)|
|3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>DLXAIP_OK_SIG_NOK(<br>AOID-101, VID-01, VID-02,<br>REF_XML_DATA_70,<br>REF_CADES_DET_NOK_XML_DATA_70)<br>)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG)<br>dss:OptionalOutputs(DXAIP_OK_SIG_NOK_VR)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG)<br>dss:OptionalOutputs(<br>DLXAIP_OK_SIG_NOK(<br>AOID-101, VID-01, VID-02, DXAIP_OK_SIG_NOK_VR)<br>)<br>)|



Verdict of M-VE-05a Observations: Verdict: 

## 3.4.1.7.10 M-VE-06 BIN_NOK 

|Identifier|M-VE-06|
|---|---|
|Test Purpose|The test case shall validate that there will be an error in case an as BIN defined data object<br>containing an invalid signature will be submitted to verification. BIN means here:<br>•<br>CADES_DET_NOK, CADES_ATT_NOK<br>•<br>XADES_DET_NOK, XADES_ENVELOPED_NOK, XADES_ENVELOPING_NOK,<br>•<br>PADES_NOK,<br>•<br>ASIC_E_CADES_NOK, ASIC_E_XADES_NOK, ASIC_E_TST_NOK, ASIC_E_ER_NOK,<br>•<br>ASIC_S_CADES_NOK, ASIC_S_XADES_NOK, ASIC_S_TST_NOK, ASIC_S_ER_NOK.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The as CONDITIONAL marked test steps shall be executed, in case the TOT does support<br>passing by the XML data as native XML, e.g.`dss:InlineXML`-element, or`ds:Signature`-<br>element etc.|



Federal Office for Information Security 

97 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(TXT_DATA.txt)<br>)<br>),<br>dss:SignatureObject(<br>dss:Base64Signature(CADES_DET_NOK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(CADES_DET_NOK_VR)<br>)|
|2|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(CADES_ATT_NOK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(CADES_ATT_NOK_VR)<br>)|
|3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(PADES_NOK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(PADES_NOK_VR)<br>)|
|4|[CONDITIONAL]<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(002-test-document.xml)<br>)<br>),<br>dss:SignatureObject(<br>ds:Signature(XADES_DET_NOK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(XADES_DET_NOK_VR)<br>)|
|'5|[CONDITIONAL]<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(002-test-document.xml)<br>)<br>),<br>dss:SignatureObject(<br>ds:Signature(XADES_DET_NOK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(XADES_DET_NOK_VR)<br>)|
|6|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(002-test-document.xml)<br>)<br>),<br>dss:SignatureObject(<br>dss:Base64Signature(XADES_DET_NOK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(XADES_DET_NOK_VR)<br>)|



Federal Office for Information Security 

98 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|7|[CONDITIONAL]<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(XADES_ENVELOPED_NOK)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(XADES_ENVELOPED_NOK_VR)<br>)|
|8|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XADES_ENVELOPED_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(XADES_ENVELOPED_NOK_VR)<br>)|
|9|[CONDITIONAL]<br>VerifyRequest<br>(<br>dss:SignatureObject(<br>ds:Signature(XADES_ENVELOPING_NOK)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(XADES_ENVELOPING_NOK_VR)<br>)|
|10|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>XADES_ENVELOPING_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(XADES_ENVELOPING_NOK_VR)<br>)|
|11|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_S_CADES_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(ASIC_S_CADES_NOK_VR)<br>)|
|12|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_S_XADES_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(ASIC_S_XADES_NOK_VR)<br>)|
|13|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_S_TST_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(ASIC_S_TST_NOK_VR)<br>)|



Federal Office for Information Security 

99 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|14|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_S_ER_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(ASIC_S_ER_NOK_VR)<br>)|
|15|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_E_CADES_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(ASIC_E_CADES_NOK_VR)<br>)|
|16|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_E_XADES_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(ASIC_E_XADES_NOK_VR)<br>)|
|17|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_E_TST_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(ASIC_E_TST_NOK_VR)<br>)|
|18|VerifyRequest<br>(<br>dss:SignatureObject(<br>dss:Base64Signature(<br>ASIC_E_ER_NOK<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/sal#invalidSignature),<br>dss:OptionalOutputs(ASIC_E_ER_NOK_VR)<br>)|
||||
||Verdict of M-VE-06||
|Observations:|||
|Verdict:|||



Federal Office for Information Security 

100 

Web Service Interfaces 

## 3.4.1.7.11 M-VE-07 Hash algorithms 

|Identifier|M-VE-07|
|---|---|
|Test Purpose|The test shall verify that it is possible to verify XAIP_OK and corresponding evidence record with<br>the TR-ESOR-specific signature policyhttp://www.bsi.bund.de/tr-esor/sigpolicy/verify-xaip by<br>using different hash algorithms for underlaying hash tree. The hash algorithms to be tested are<br>following SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA3-224, SHA3-256, SHA3-384,<br>SHA3-512.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Prepare XAIP_OK_SIG_OK by inserting of<br>AOID-999|XAIP_OK_SIG_OK(AOID-999, VID-01)|
|2|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_OK_SHA-1_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/il/algorithm#hashAlgorithmNotSuitable),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_OK_SHA-1_XAIP_OK_SIG_OK_VR))<br>)|
|3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_NOK_SHA-1_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_NOK_SHA-1_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK(<br>AOID-999, VID-01,<br>XAIP_OK_SIG_OK_VR(AOID-999, VID-01,<br>ER_NOK_SHA-1_XAIP_OK_SIG_OK_VR))<br>)<br>)|



Federal Office for Information Security 

101 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|4|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_OK_SHA-224_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/il/algorithm#hashAlgorithmNotSuitable),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_OK_SHA-224_XAIP_OK_SIG_OK_VR))<br>)|
|5|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_NOK_SHA-224_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_NOK_SHA-224_XAIP_OK_SIG_OK_VR<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK (<br>AOID-999, VID-01,<br>XAIP_OK_SIG_OK_VR (AOID-999, VID-01,<br>ER_NOK_SHA-224_XAIP_OK_SIG_OK_VR))<br>)<br>)|
|6|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_OK_SHA-256_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

102 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|7|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_NOK_SHA-256_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_NOK_SHA-256_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK(<br>AOID-999, VID-01,<br>XAIP_OK_SIG_OK_VR(AOID-999, VID-01,<br>ER_NOK_SHA-256_XAIP_OK_SIG_OK_VR))<br>)<br>)|
|8|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_OK_SHA-384_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|9|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_NOK_SHA-384_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_NOK_SHA-384_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK(<br>AOID-999, VID-01,<br>XAIP_OK_SIG_OK_VR(AOID-999, VID-01,<br>ER_NOK_SHA-384_XAIP_OK_SIG_OK_VR))<br>)<br>)|



Federal Office for Information Security 

103 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|10|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_OK_SHA-512_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|11|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_NOK_SHA-512_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_NOK_SHA-512_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK(<br>AOID-999, VID-01,<br>XAIP_OK_SIG_OK_VR(AOID-999, VID-01,<br>ER_NOK_SHA-512_XAIP_OK_SIG_OK_VR))<br>)<br>)|
|12|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_OK_SHA3-224_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/il/algorithm#hashAlgorithmNotSuitable),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_OK_SHA3-224_XAIP_OK_SIG_OK_VR))<br>)|



Federal Office for Information Security 

104 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|13|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_NOK_SHA3-224_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_NOK_SHA3-224_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK(<br>AOID-999, VID-01,<br>XAIP_OK_SIG_OK_VR(AOID-999, VID-01,<br>ER_NOK_SHA3-224_XAIP_OK_SIG_OK_VR))<br>)<br>)|
|14|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_OK_SHA3-256_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|15|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_NOK_SHA3-256_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_NOK_SHA3-256_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK(<br>AOID-999, VID-01,<br>XAIP_OK_SIG_OK_VR(AOID-999, VID-01,<br>ER_NOK_SHA3-256_XAIP_OK_SIG_OK_VR))<br>)<br>)|



Federal Office for Information Security 

105 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|16|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_OK_SHA3-384_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|17|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_NOK_SHA3-384_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(XAIP_OK_SIG_OK_VR(<br>AOID-999, VID-01,<br>ER_NOK_SHA3-384_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER),<br>dss:OptionalOutputs(<br>XAIP_OK_SIG_OK(<br>AOID-999, VID-01,<br>XAIP_OK_SIG_OK_VR(AOID-999, VID-01,<br>ER_NOK_SHA3-384_XAIP_OK_SIG_OK_VR))<br>)<br>)|
|18|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64XML(<br>XAIP_OK_SIG_OK(AOID-999, VID-01)<br>))),<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-999,VID-01,<br>ER_NOK_SHA-512_XAIP_OK_SIG_OK)<br>))<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

106 

Web Service Interfaces 

Step Test sequence Expected Results 19 VerifyRequest VerifyResponse ( ( dss:InputDocuments( dss:Result(resultmajor#error, dss:Document( resultminor/arl/XAIP_NOK_ER), dss:Base64XML( dss:OptionalOutputs(XAIP_OK_SIG_OK_VR( XAIP_OK_SIG_OK(AOID-999, VID-01) AOID-999, VID-01, ))), ER_OK_SHA3-512_XAIP_OK_SIG_OK_VR)) dss:SignatureObject( ) dss:Other( OR XAIP_ERS(AOID-999,VID-01, VerifyResponse ER_OK_SHA3-512_XAIP_OK_SIG_OK) ( )) dss:Result(resultmajor#error, ) resultminor/arl/XAIP_NOK_ER), dss:OptionalOutputs( XAIP_OK_SIG_OK( AOID-999, VID-01, XAIP_OK_SIG_OK_VR(AOID-999, VID-01, ER_OK_SHA3-512_XAIP_OK_SIG_OK_VR)) ) ) Verdict of M-VE-07 Observations: Verdict: 

Federal Office for Information Security 

107 

Web Service Interfaces 

## 3.4.1.8 Additional tests of S.4-interface 

## 3.4.1.8.1 M-ADD-01 XAIP_OK and Resigning 

|Identifier|M-ADD-01|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve previously submitted and updated XAIP_OK after<br>the time-stamp resigning procedure has been successfully applied.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The time-stamp resigning procedure has been successfully performed<br>•<br>Make sure that the test case M-UP-01 was successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveRetrievalRequest<br>(<br>AOID-01, ALL<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-01, VID-01, VID-02, VID-03)<br>)|
|'2|ArchiveEvidenceRequest<br>(<br>AOID-01, ALL<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS22(<br>AOID-01, VID-01,<br>XAIP_OK_V1_ER_OK_RESG),<br>XAIP_ERS(<br>AOID-01, VID-02,<br>XAIP_OK_V2_ER_OK_RESG),<br>XAIP_ERS(<br>AOID-01, VID-03,<br>XAIP_OK_V3_ER_OK_RESG)<br>)|



> 22 XAIP-ERS does mean a RFC4998-ER embedded in the element `xaip:asn1EvidenceRecord` , which in turn is embedded in the element `xaip:evidenceRecord` and can contain the both attributes `AOID` and `VersionID` . 

Federal Office for Information Security 

108 

Web Service Interfaces 

Step Test sequence Expected Results 3 Test of correcteness of the obtained: • XAIP_OK_V1_ER_OK_RESG, • XAIP_OK_V2_ER_OK_RESG and • XAIP_OK_V3_ER_OK_RESG by using ERVerifyTool. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( XAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01, VID-01, ) XAIP_OK_V1_ER_OK_RESG), ), XAIP_ERS( dssvr:IndividualReport( AOID-01, VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) XAIP_OK_V2_ER_OK_RESG), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01, VID-03, vr:FormatOK( XAIP_OK_V3_ER_OK_RESG) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

## Verdict of M-ADD-01 

Observations: 

## Verdict: 

## 3.4.1.8.2 M-ADD-01a LXAIP_OK and Resigning 

## Identifier 

Identifier M-ADD-01a Test Purpose The test shall verify that it is possible to retrieve previously submitted and updated LXAIP_OK after the time-stamp resigning procedure has been successfully applied. 

Federal Office for Information Security 

109 

Web Service Interfaces 

|Identifier|M-ADD-01a|
|---|---|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The time-stamp resigning procedure has been successfully performed<br>•<br>Make sure that the test case M-UP-01a was successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveRetrievalRequest<br>(<br>AOID-01a, ALL<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-01a, VID-01, VID-02, VID-03)<br>)|
|'2|ArchiveEvidenceRequest<br>(<br>AOID-01a , ALL<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS23(<br>AOID-01a, VID-01,<br>LXAIP_OK_V1_ER_OK_RESG),<br>XAIP_ERS(<br>AOID-01a, VID-02,<br>LXAIP_OK_V2_ER_OK_RESG),<br>XAIP_ERS(<br>AOID-01a, VID-03,<br>LXAIP_OK_V3_ER_OK_RESG)<br>)|



> 23 XAIP-ERS does mean a RFC4998-ER embedded in the element `xaip:asn1EvidenceRecord` , which in turn is embedded in the element `xaip:evidenceRecord` and can contain the both attributes `AOID` and `VersionID` . 

Federal Office for Information Security 

110 

Web Service Interfaces 

Step Test sequence Expected Results 3 Test of correcteness of the obtained: • LXAIP_OK_V1_ER_OK_RESG, • LXAIP_OK_V2_ER_OK_RESG and • LXAIP_OK_V3_ER_OK_RESG by using ERVerifyTool. The particular object references in the obtained LXAIP_OK will be replaced by the references compatible with the ERVerifyTool in advance. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( LXAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01a, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01a, VID-01, ) LXAIP_OK_V1_ER_OK_RESG), ), XAIP_ERS( dssvr:IndividualReport( AOID-01a, VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) LXAIP_OK_V2_ER_OK_RESG), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01a, VID-03, vr:FormatOK( LXAIP_OK_V3_ER_OK_RESG) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

Verdict of M-ADD-01a Observations: 

## Verdict: 

Federal Office for Information Security 

111 

Web Service Interfaces 

## 3.4.1.8.3 M-ADD-02 XAIP_OK and Rehashing 

|Identifier|M-ADD-02|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve previously submitted and updated XAIP_OK after<br>the hash tree renewal procedure (rehashing) has been successfully applied.|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The rehashing procedure has been successfully performed<br>•<br>Make sure that the test case M-ADD-01 was successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveRetrievalRequest<br>(<br>AOID-01, ALL<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_OK(AOID-01, VID-01, VID-02, VID-03)<br>)|
|'2|ArchiveEvidenceRequest<br>(<br>AOID-01, ALL<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS24(<br>AOID-01, VID-01,<br>XAIP_OK_V1_ER_OK_RESG_REH),<br>XAIP_ERS(<br>AOID-01, VID-02,<br>XAIP_OK_V2_ER_OK_RESG_REH),<br>XAIP_ERS(<br>AOID-01, VID-03,<br>XAIP_OK_V3_ER_OK_RESG_REH)<br>)|



> 24 XAIP-ERS does mean a RFC4998-ER embedded in the element `xaip:asn1EvidenceRecord` , which in turn is embedded in the element `xaip:evidenceRecord` and can contain the both attributes `AOID` and `VersionID` . 

Federal Office for Information Security 

112 

Web Service Interfaces 

Step Test sequence Expected Results 3 Test of correcteness of the obtained: • XAIP_OK_V1_ER_OK_RESG_REH, • XAIP_OK_V2_ER_OK_RESG_REH and • XAIP_OK_V3_ER_OK_RESG_REH by using ERVerifyTool. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( XAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01, VID-01, ) XAIP_OK_V1_ER_OK_RESG_REH), ), XAIP_ERS( dssvr:IndividualReport( AOID-01, VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) XAIP_OK_V2_ER_OK_RESG_REH), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01, VID-03, vr:FormatOK( XAIP_OK_V3_ER_OK_RESG_REH) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

## Verdict of M-ADD-02 

Observations: 

## Verdict: 

## 3.4.1.8.4 M-ADD-02a LXAIP_OK and Resigning 

## Identifier 

Identifier M-ADD-02a Test Purpose The test shall verify that it is possible to retrieve previously submitted and updated LXAIP_OK after the hash tree renewal procedure (rehashing) has been successfully applied. 

Federal Office for Information Security 

113 

Web Service Interfaces 

|Identifier|M-ADD-02a|
|---|---|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The rehashing procedure has been successfully performed<br>•<br>Make sure that the test case M-ADD-01a was successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveRetrievalRequest<br>(<br>AOID-01a, ALL<br>)|ArchiveRetrievalResponse<br>(<br>dss:Result(resultmajor#ok),<br>LXAIP_OK(AOID-01a, VID-01, VID-02, VID-03)<br>)|
|'2|ArchiveEvidenceRequest<br>(<br>AOID-01a, ALL<br>)|ArchiveEvidenceResponse<br>(<br>dss:Result(resultmajor#ok),<br>XAIP_ERS25(<br>AOID-01a, VID-01,<br>LXAIP_OK_V1_ER_OK_RESG_REH),<br>XAIP_ERS(<br>AOID-01a, VID-02,<br>LXAIP_OK_V2_ER_OK_RESG_REH),<br>XAIP_ERS(<br>AOID-01a, VID-03,<br>LXAIP_OK_V3_ER_OK_RESG_REH)<br>)|



> 25 XAIP-ERS does mean a RFC4998-ER embedded in the element `xaip:asn1EvidenceRecord` , which in turn is embedded in the element `xaip:evidenceRecord` and can contain the both attributes `AOID` and `VersionID` . 

Federal Office for Information Security 

114 

Web Service Interfaces 

Step Test sequence Expected Results 3 Test of correcteness of the obtained: • LXAIP_OK_V1_ER_OK_RESG_REH, • LXAIP_OK_V2_ER_OK_RESG_REH and • LXAIP_OK_V3_ER_OK_RESG_REH by using ERVerifyTool. The particular object references in the obtained LXAIP_OK will be replaced by the references compatible with the ERVerifyTool in advance. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( LXAIP_OK ( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01a, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01a, VID-01, ) LXAIP_OK_V1_ER_OK_RESG_REH), ), XAIP_ERS( dssvr:IndividualReport( AOID-01a, VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) LXAIP_OK_V2_ER_OK_RESG_REH), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01a, VID-03, vr:FormatOK( LXAIP_OK_V3_ER_OK_RESG_REH) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

Verdict of M-ADD-02a Observations: 

## Verdict: 

Federal Office for Information Security 

115 

Web Service Interfaces 

## 3.4.1.8.5 M-ADD-03a Relation between upload data and LXAIP/DLXAIP 

|Identifier|M-ADD-03a|
|---|---|
|Test Purpose|The test shall verify that 1:1-relation between the uploaded data and corresponding<br>LXAIP/DLXAIP is adhered to. It is not possible to use a single reference in two different<br>LXAIP/DLXAIP instances and in such case, an error will be returned.|
|Configuration|•<br>CONFIG_S.4<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Test case M-SU-01a has been performed successfully.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ArchiveSubmissionRequest<br>(<br>LXAIP_OK(<br>REF_TXT_DATA_71,<br>REF_PDF_DATA_71,<br>REF_XML_MDO_71)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-300a<br>)|
|2|ArchiveSubmissionRequest<br>(<br>LXAIP_OK(<br>REF_TXT_DATA_71,<br>REF_PDF_DATA_71,<br>REF_XML_MDO_71)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/al/common#parameterError)<br>)|
|3|ArchiveSubmissionRequest<br>(<br>LXAIP_OK_ER_NOK(<br>REF_TXT_DATA_72,<br>REF_PDF_DATA_72,<br>REF_XML_MDO_72,<br>ER_NOK_LXAIP_OK_72)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/XAIP_NOK_ER)<br>dss:OptionalOutputs(LXAIP_OK_ER_NOK_VR)<br>)|
|4|ArchiveSubmissionRequest<br>(<br>LXAIP_OK(<br>REF_TXT_DATA_72,<br>REF_PDF_DATA_72,<br>REF_XML_MDO_72)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/al/common#parameterError)<br>)|
|5|ArchiveUpdateRequest<br>(<br>DLXAIP_OK( AOID-300a, VID-01, VID-02,<br>REF_CADES_ATT_TXT_DATA_73)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#OK),<br>VersionID(VID-02)<br>)|
|6|ArchiveSubmissionRequest<br>(<br>LXAIP_OK(<br>REF_TXT_DATA_74,<br>REF_PDF_DATA_74,<br>REF_XML_MDO_74)<br>)|ArchiveSubmissionResponse<br>(<br>dss:Result(resultmajor#ok),<br>AOID-301a<br>)|



Federal Office for Information Security 

116 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|7|ArchiveUpdateRequest<br>(<br>DLXAIP_OK(AOID-301a, VID-01, VID-02,<br>REF_CADES_ATT_TXT_DATA_73)<br>)|ArchiveUpdateResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/al/common#parameterError)<br>)|



Verdict of M-ADD-03a Observations: Verdict: 

## 3.4.1.8.6 M-ADD-04 Evidence Record with single hash value 

|Identifier|M-ADD-04|
|---|---|
|Test Purpose|The test shall verify that it is possible to verify every variant of the evidence record computed on<br>a single data object:<br>•<br>ER(TSP(H(DO-01)))<br>hash value of the data object is directly included in the message imprint<br>of the timestamp (ER_SO-1_OK_XAIP_OK_SO),<br>•<br>ER(H(DO-01),TSP(H(DO-01)))<br>the hash value of the data object is placed in the single<br>reduced hash tree and the same hash value is included in the message imprint of the<br>timestamp (ER_SO-2_OK_XAIP_OK_SO),<br>•<br>ER(H(DO-01),TSP(H(H(DO-01))) - the hash value of the data object is placed in the single<br>reduced hash tree and the hash value of those hash value (computet hash tree root) is<br>included in the message imprint of the timestamp (ER_SO-3_OK_XAIP_OK_SO).|
|Configuration|•<br>CONFIG_S.4|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>XAIP_OK_SO(AOID-100, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-100,VID-01,<br>ER_SO-1_OK_XAIP_OK_SO)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|



Federal Office for Information Security 

117 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|2|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>XAIP_OK_SO(AOID-100, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-100,VID-01,<br>ER_SO-2_OK_XAIP_OK_SO)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
|3|VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:Base64Data(<br>XAIP_OK_SO(AOID-100, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(AOID-100,VID-01,<br>ER_SO-3_OK_XAIP_OK_SO)<br>)<br>)<br>)|VerifyResponse<br>(<br>dss:Result(resultmajor#ok)<br>)|
||||
||Verdict of M-ADD-04||
|Observations:|||
|Verdict:|||



Federal Office for Information Security 

118 

Web Service Interfaces 

## 3.4.2 Tests of the TR-S.512-interface 

The following section introduces the mandatory tests to be passed through in case the TOT does support additionally the TR-S.512-interface (or simply S.512) as well. The test-IDs of the S.512-RI-02 b 

## 3.4.2.1 Function RetrieveInfo of S.512-interface 

## 3.4.2.1.1 M-RI-01b Retrieve Preservation Profile 

|**Identifier**|**Identifier**|**M-RI-01b**|**M-RI-01b**|**M-RI-01b**|
|---|---|---|---|---|
|Test Purpose||The test shall retrieve the actual preservation profile with the corresponding<br>`ProfileIdentifier`:<br>**http://www.bsi.bund.de/tr-esor/V1.3.0/profile/preservation-api/V1.1.2**|||
|Configuration||•<br>CONFIG_S.512|||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>At least one active Preservation Profile is available (ACTIVE_PROFILE) and one not-active<br>(INACTIVE_PROFILE).|||
||||||
|Step||Test sequence||Expected Results|
|1|RetrieveInfo<br>(<br>pres26:Profile( ACTIVE_PROFILE_URI )<br>)|||RetrieveInfoResponse<br>(<br>dsb27:Result(resultmajor:Success),<br>pres:Profile(ACTIVE_PROFILE)<br>)|
|2|RetrieveInfo<br>(<br>pres:Status( inactive )<br>)|||RetrieveInfoResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:Profile(INACTIVE_PROFILE)<br>)|
|3|RetrieveInfo<br>(<br>pres:Status( all )<br>)|||RetrieveInfoResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:Profile(ACTIVE_PROFILE),<br>pres:Profile(INACTIVE_PROFILE)<br>)|
|4|RetrieveInfo<br>(<br>pres:Status( active )<br>)|||RetrieveInfoResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:Profile(ACTIVE_PROFILE)<br>)|
|5|RetrieveInfo<br>(<br>pres:Profile( ACTIVE_PROFILE_URI ),<br>pres:Status( active )<br>)|||RetrieveInfoResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:Profile(ACTIVE_PROFILE)<br>)|
|6|RetrieveInfo<br>(<br>pres:Profile(ACTIVE_PROFILE_URI ),<br>pres:Status( inactive )<br>)|||RetrieveInfoResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



> 26 pres http://uri.etsi.org/19512/v1.1.2# 

> 27 http://docs.oasis-open.org/dss- 

Federal Office for Information Security 

119 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|7|RetrieveInfo<br>(<br>pres:Profile(ACTIVE_PROFILE_URI ),<br>pres:Status( all )<br>)|RetrieveInfoResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:Profile(ACTIVE_PROFILE)<br>)|
|8|RetrieveInfoRequest<br>(<br>)|RetrieveInfoResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:Profile(ACTIVE_PROFILE)<br>)|
||||
||Verdict of M-RE-01b||
|Observations:|||
|Verdict:|||



## 3.4.2.1.2 M-RI-02b RetrieveInfo with unknown URI 

|Identifier|M-RI-02b|
|---|---|
|Test Purpose|The test shall verify that it will yield an error, if`RetrieveInfo`is called without providing a<br>known URI. As the present call also contains the UNKNOWN_PROFILE_URI, the`dsb:Result`<br>needs to contain<br>http://uri.etsi.org/19512/error/notSupported<br>as content of`dsb:ResultMinor`<br>element.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|RetrieveInfo<br>(<br>pres:Profile(UNKNOWN_PROFILE_URI)<br>)|RetrieveInfoResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/notSupported))<br>)|
|2|RetrieveInfo<br>(<br>pres:Profile(ACTIVE_PROFILE_URI)<br>)|RetrieveInfoResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:Profile(ACTIVE_PROFILE)<br>)|



Verdict of M-RI-02b 

Observations: 

## Verdict: 

Federal Office for Information Security 

120 

Web Service Interfaces 

## 3.4.2.1.3 M-RI-03b RetrieveInfo with unknown control in OptionalInputs 

|Identifier|Identifier|M-RI-03b|M-RI-03b|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element and the`RetrieveInfo`request will not be successful.||
|Configuration||•<br>CONFIG_S.512||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>http://www.bsi.bund.de/tr-<br>esor/V1.3/profile/preservation-api/V1.1.2<br>•<br>The`OptionalInputs`-element and the`RetrieveInfo`request contains an unknown item.||
|||||
|Step||Test sequence|Expected Results|
|1|RetrieveInfo<br>(<br>pres:OptionalInputs(<br>dsb:Other(<br>dsb:Value(SomethingUnknown))),<br>pres:Profile(ACTIVE_PROFILE_URI)<br>)||RetrieveInfoResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/notSupported))<br>)|
|2|RetrieveInfo<br>(<br>Pres:Profile(ACTIVE_PROFILE_URI)<br>)||RetrieveInfoResponse<br>(<br>dsb:Result(resultmajor#ok),<br>pres:Profile(ACTIVE_PROFILE)<br>)|



Verdict of M-RI-03b Observations: 

Verdict: 

Federal Office for Information Security 

121 

Web Service Interfaces 

## 3.4.2.2 Function PreservePO of S.512-interface 

3.4.2.2.1 M-SU-01b XAIP_OK without AOID 

|Identifier|M-SU-01b|
|---|---|
|Test Purpose|The test shall verify that it is possible to submit XAIP_OK without AOID.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_OK))<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-01b)<br>)|
|2|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-01b, VID-01)))<br>)|
|3|RetrievePO28<br>(<br>pres:POID(AOID-01b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b,VID-01,<br>XAIP_OK_V1_ER_OK)))<br>)|
|4|Test<br>of<br>correctness<br>of<br>the<br>obtained<br>XAIP_OK(AOID-01, VID-01) by using AIP-<br>eIDAS-SigValidator<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK(AOID-01b, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid )<br>dssvr:Details(<br>vr:XAIPReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|



28 Make sure the tested TR-ESOR-system has already obtained the archive time stamp. 

Federal Office for Information Security 

122 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|5|Test<br>of<br>correcteness<br>of<br>the<br>obtained<br>XAIP_OK_V1_ER_OK by using ERVerifyTool.<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>XAIP_OK(AOID-01b, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(<br>AOID-01b,VID-01,<br>XAIP_OK_V1_ER_OK)<br>)<br>)<br>)|VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid )<br>dssvr:Details(<br>vr:EvidenceRecordReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|
|6|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_OK_SIG_OK))<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID( AOID-02b)<br>)|
|7|RetrievePO<br>(<br>pres:POID(AOID-02b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK_SIG_OK(AOID-02b, VID-01)))<br>)|
|8|RetrievePO<br>(<br>pres:POID(AOID-02b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-02b,VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK)))<br>)|



## Verdict of M-SU-01b 

Observations: 

Verdict: 

## 3.4.2.2.2 M-SU-01ab LXAIP_OK without AOID 

Identifier M-SU-01ab Test Purpose The test shall verify that it is possible to submit XAIP_OK without AOID. 

Federal Office for Information Security 

123 

Web Service Interfaces 

M-SU-01ab 

## Identifier 

|Identifier|M-SU-01ab|
|---|---|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|To be done manually!<br>a)<br>Following files have to be uploaded into<br>middleware via upload/download-module<br>(cf. chapters 4.2 and 4.3):<br>1)<br>TXT_DATA_50.txt<br>2)<br>XML_MDO_50.xml<br>3)<br>PDF_DATA_50.pdf<br>4)<br>TXT_DATA_51.txt<br>5)<br>TXT_DATA_51.txt.p7s<br>6)<br>PDF_DATA_51.pdf<br>7)<br>PDF_DATA_51.pdf.p7s<br>8)<br>XML_MDO_51.xml<br>9)<br>TXT_DATA_52.txt<br>10) PDF_DATA_52.pdf<br>11) XML_MDO_52.xml<br>12) TXT_DATA_53.txt.p7m<br>13) XML_DATA_54.xml<br>14) XML_DATA_54.xml.p7s<br>15) TXT_DATA_55.txt<br>16) PDF_DATA_55.pdf<br>17) XML_MDO_55.xml<br>18) XML_DATA_56.xml<br>19) XML_DATA_56.xml.p7s<br>20) TXT_DATA_57.txt.p7m<br>21) TXT_DATA_58.txt<br>22) PDF_DATA_58.pdf<br>23) XML_MDO_58.xml<br>24) TXT_DATA_59.txt.p7m<br>25) TXT_DATA_60.txt.p7m<br>26) XML_DATA_60-1.xml<br>27) XML_DATA_60-1.xml.p7s<br>28) TXT_DATA_61.txt<br>29) TXT_DATA_61.txt.p7s<br>30) PDF_DATA_61.pdf<br>31) PDF_DATA_61.pdf.p7s<br>32) XML_MDO_61.xml<br>33) XML_DATA_62.xml<br>34) XML_DATA_62.xml.p7s<br>35) XML_DATA_63.xml<br>36) XML_DATA_63.xml.p7s<br>37) TXT_DATA_65.txt<br>38) TXT_DATA_65_NOK.p7s<br>39) PDF_DATA_65.pdf<br>40) PDF_DATA_65.pdf.p7s<br>41) XML_MDO_65.xml<br>42) TXT_DATA_66.txt<br>43) TXT_DATA_66.txt.p7s<br>44) PDF_DATA_66.pdf<br>45) PDF_DATA_66.pdf.p7s<br>46) XML_MDO_66.xml<br>47) TXT_DATA_67.txt<br>48) TXT_DATA_NOK_67.txt.p7s<br>49) PDF_DATA_67.pdf<br>50) PDF_DATA_67.pdf.p7s<br>51) XML_MDO_67.xml|a)<br>As a result following data structures (proper instances<br>of`asic:DataObjectReferences`) will be delivered:<br>1)<br>REF_TXT_DATA_50b<br>2)<br>REF_XML_MDO_50b<br>3)<br>REF_PDF_DATA_50b<br>4)<br>REF_TXT_DATA_51b<br>5)<br>REF_CADES_DET_TXT_DATA_51b<br>6)<br>REF_PDF_DATA_51b<br>7)<br>REF_CADES_DET_PDF_DATA_51b<br>8)<br>REF_XML_MDO_51b<br>9)<br>REF_TXT_DATA_52b<br>10) REF_PDF_DATA_52b<br>11) REF_XML_MDO_52b<br>12) REF_CADES_ATT_TXT_DATA_53b<br>13) REF_XML_DATA_54b<br>14) REF_CADES_DET_XML_DATA_54b<br>15) REF_TXT_DATA_55b<br>16) REF_PDF_DATA_55b<br>17) REF_XML_MDO_55b<br>18) REF_XML_DATA_56b<br>19) REF_CADES_DET_XML_DATA_56b<br>20) REF_CADES_ATT_TXT_DATA_57b<br>21) REF_TXT_DATA_58b<br>22) REF_PDF_DATA_58b<br>23) REF_XML_MDO_58b<br>24) REF_CADES_ATT_TXT_DATA_59b<br>25) REF_CADES_ATT_TXT_DATA_60b<br>26) REF_XML_DATA_60-1b<br>27) REF_CADES_DET_XML_DATA_60-1b<br>28) REF_TXT_DATA_61b<br>29) REF_CADES_DET_TXT_DATA_61b<br>30) REF_PDF_DATA_61b<br>31) REF_CADES_DET_PDF_DATA_61b<br>32) REF_XML_MDO_61b<br>33) REF_XML_DATA_62b<br>34) REF_CADES_DET_XML_DATA_62b<br>35) REF_XML_DATA_63b<br>36) REF_CADES_DET_XML_DATA_63b<br>37) REF_TXT_DATA_65b<br>38) REF_CADES_DET_NOK_TXT_DATA_65b<br>39) REF_PDF_DATA_65b<br>40) REF_CADES_DET_PDF_DATA_65b<br>41) REF_XML_MDO_65b<br>42) REF_TXT_DATA_66b<br>43) REF_CADES_DET_TXT_DATA_66b<br>44) REF_PDF_DATA_66b<br>45) REF_CADES_DET_PDF_DATA_66b<br>46) REF_XML_MDO_66b<br>47) REF_TXT_DATA_67b<br>48) REF_CADES_DET_NOK_TXT_DATA_67b<br>49) REF_PDF_DATA_67b<br>50) REF_CADES_DET_PDF_DATA_67b<br>51) REF_XML_MDO_67b|



Federal Office for Information Security 

124 

Web Service Interfaces 

Test sequence Expected Results 

## Step 

|Step|Test sequence|Expected Results|
|---|---|---|
||52) TXT_DATA_68.txt<br>53) TXT_DATA_68.txt.p7s<br>54) PDF_DATA_68.pdf<br>55) PDF_DATA_68.pdf.p7s<br>56) XML_MDO_68.xml<br>57) XML_DATA_69.xml<br>58) XML_DATA_NOK_69.xml.p7s<br>59) XML_DATA_70.xml<br>60) XML_DATA_NOK_70.xml.p7s<br>61) TXT_DATA_71.txt<br>62) PDF_DATA_71.pdf<br>63) XML_MDO_71.xml<br>64) TXT_DATA_72.txt<br>65) PDF_DATA_72.pdf<br>66) XML_MDO_72.xml<br>67) TXT_DATA_73.txt.p7m<br>68) TXT_DATA_74.txt<br>69) PDF_DATA_74.pdf<br>70) XML_MDO_74.xml<br>b)<br>The references in the particular LXAIP*<br>and DLXAIP* test objects will be adjusted<br>according to the results in step a)<br>automatically, the references have to be<br>inserted into the configuration file of the<br>testbed.|52) REF_TXT_DATA_68b<br>53) REF_CADES_DET_TXT_DATA_68b<br>54) REF_PDF_DATA_68b<br>55) REF_CADES_DET_PDF_DATA_68b<br>56) REF_XML_MDO_68b<br>57) REF_XML_DATA_69b<br>58) REF_CADES_DET_NOK_XML_DATA_69b<br>59) REF_XML_DATA_70b<br>60) REF_CADES_DET_NOK_XML_DATA_70b<br>61) REF_XML_MDO_71b<br>62) REF_PDF_DATA_71b<br>63) REF_XML_MDO_71b<br>64) REF_TXT_DATA_72b<br>65) REF_PDF_DATA_72b<br>66) REF_XML_MDO_72b<br>67) REF_CADES_ATT_TXT_DATA_73b<br>68) REF_TXT_DATA_74b<br>69) REF_PDF_DATA_74b<br>70) REF_XML_MDO_74b|
|2|To be done manually!<br>Try to upload the XAIP_OK by using the<br>upload/download interface of the middleware.|The upload-operation failed. Some kind of the machine-<br>readable error code is delivered back. No data has been<br>stored in the Storage.|
|3|To be done manually!<br>Try to upload the LXAIP_OK by using the<br>upload/download interface of the middleware.|The upload-operation failed. Some kind of the machine-<br>readable error code is delivered back. No data has been<br>stored in the Storage.|
|4|To be done manually!<br>Try to upload the ASiC_AIP_OK by using the<br>upload/download interface of the middleware.|The upload-operation failed. Some kind of the machine-<br>readable error code is delivered back. No data has been<br>stored in the Storage.|
|5|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(<br>REF_TXT_DATA_50b,<br>REF_PDF_DATA_50b,<br>REF_XML_MDO_50b)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-01ab)<br>)|
|6|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>pres:POFormat(http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3)<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(AOID-01ab, VID-01)))<br>)|
|7|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>vidence<br>)|RetrievePOResponse<br>(<br>dss:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01ab, VID-01,<br>LXAIP_OK_V1_ER_OK)))|



Federal Office for Information Security 

125 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|||)|
|8|Make sure all in LXAIP_OK(AOID-01ab, VID-01)<br>referenced<br>files<br>have<br>been<br>copied<br>into<br>corresponding LXAIP-directory of the AIP-<br>eIDAS-SigValidator adjust the given references<br>in in LXAIP_OK(AOID-01ab, VID-01) in order to<br>get them resolveable by the AIP-eIDAS-<br>SigValidator.|LXAIP_OK_XSV(AOID-01ab, VID-01)|
|9|Test<br>of<br>correctness<br>of<br>the<br>obtained<br>LXAIP_OK(AOID-01ab, VID-01) by using AIP-<br>eIDAS-SigValidator<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_XSV(AOID-01ab, VID-01)<br>)<br>)<br>)<br>)|VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid )<br>dssvr:Details(<br>vr:XAIPReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|
|10|Test<br>of<br>correcteness<br>of<br>the<br>obtained<br>LXAIP_OK_V1_ER_OK by using ERVerifyTool.<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_XSV(AOID-01ab, VID-01)<br>)<br>)<br>)<br>dss:SignatureObject(<br>dss:Other(<br>XAIP_ERS(<br>AOID-01ab, VID-01,<br>LXAIP_OK_V1_ER_OK)<br>)<br>)<br>)|VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid )<br>dssvr:Details(<br>vr:EvidenceRecordReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|
|11|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK_SIG_OK(<br>REF_TXT_DATA_51b,|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>AOID-02ab<br>)|



Federal Office for Information Security 

126 

Web Service Interfaces 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0127-01.png)


**----- Start of picture text -----**<br>
Step  Test sequence  Expected Results<br>            REF_CADES_DET_TXT_DATA_51b,<br>            REF_PDF_DATA_51b,<br>            REF_CADES_DET_PDF_DATA_51b,<br>            REF_XML_MDO_51b)))<br>)<br>12  RetrievePO  RetrievePOResponse<br>(  (<br>    pres:POID(AOID-02ab),      dsb:Result(resultmajor:Success),<br>    pres:PO(<br>- -<br>    pres:POFormat(http://www.bsi.bund.de/tr http://www.bsi.bund.de/tr esor/lxaip/1.3<br>esor/lxaip/1.3)         pres:xmlData(LXAIP_OK_SIG_OK(AOID-02ab, VID-01)))<br>)  )<br>13  RetrievePO  RetrievePOResponse<br>(   (<br>    pres:POID(AOID-02ab),      dsb:Result(resultmajor:Success),<br>vidence     pres:PO(<br>)<br>        pres:xmlData(XAIP_ERS(AOID-02ab, VID-01,<br>                                      LXAIP_OK_SIG_OK_V1_ER_OK)))<br>)<br>M-SU-01ab<br>Observations:<br>Verdict:<br>**----- End of picture text -----**<br>


## 3.4.2.2.3 M-SU-02b XAIP_NOK 

|Identifier|M-SU-02b|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a (syntactically incorrect) XAIP_NOK is<br>submitted.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



Federal Office for Information Security 

127 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_NOK))<br>)|PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)<br>Alternatively response to the one above could be<br>following or similar:<br><soap:Envelope<br>xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"<br>><br><soap:Body><br><soap:Fault><br><faultcode>soap:Client</faultcode><br><faultstring>Problems<br>creating<br>SAAJ<br>object<br>model</faultstring><br></soap:Fault><br></soap:Body><br></soap:Envelope>|
|2|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>pres:xmlData(XAIP_NOK_VERSION))<br>)|PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)<br>Alternatively response to the one above could be<br>following or similar:<br><soap:Envelope<br>xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"<br>><br><soap:Body><br><soap:Fault><br><faultcode>soap:Client</faultcode><br><faultstring>Problems<br>creating<br>SAAJ<br>object<br>model</faultstring><br></soap:Fault><br></soap:Body><br></soap:Envelope>|
||||
||Verdict of M-SU-02b||
|Observations:|||
|Verdict:|||



## 3.4.2.2.4 M-SU-02ab LXAIP_NOK 

|Identifier|M-SU-02ab|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a (syntactically incorrect, missing element<br>`ds:DigestValue`in element`asic:DataObjectReference`) LXAIP_NOK is submitted.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



Federal Office for Information Security 

128 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_NOK))<br>)|PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)<br>Alternatively response to the one above could be<br>following or similar:<br><soap:Envelope<br>xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"<br>><br><soap:Body><br><soap:Fault><br><faultcode>soap:Client</faultcode><br><faultstring>Problems<br>creating<br>SAAJ<br>object<br>model</faultstring><br></soap:Fault><br></soap:Body><br></soap:Envelope>|
||||
||Verdict of M-SU-02ab||
|Observations:|||
|Verdict:|||



## 3.4.2.2.5 M-SU-03b XAIP_NOK_EXPIRED 

|Identifier|M-SU-03b|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the semantically incorrect XAIP_NOK_EXPIRED<br>is submitted.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_NOK_EXPIRED)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Verdict of M-SU-03b Observations: 

Federal Office for Information Security 

129 

Web Service Interfaces 

Verdict of M-SU-03b 

## Verdict: 

## 3.4.2.2.6 M-SU-04b XAIP_NOK_SUBMTIME 

|Identifier|M-SU-04b|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the semantically incorrect<br>XAIP_NOK_SUBMTIME is submitted.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Prepare XAIP_NOK_SUBMTIME, set the value of<br>the<br>element<br>`xaip:submissionTime`<br>in<br>`xaip:submissionInfo`to the time in the past|XAIP_NOK_SUBMTIME(past)|
|2|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>pres:xmlData(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>XAIP_NOK_SUBMTIME(past)))<br>)|PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|3|Prepare XAIP_NOK_SUBMTIME, set the value of<br>the<br>element<br>`xaip:submissionTime`<br>in<br>`xaip:submissionInfo`to the time in the future|XAIP_NOK_SUBMTIME(future)|
|4|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(<br>XAIP_NOK_SUBMTIME(future)))<br>)|PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Verdict of M-SU-04b 

Observations: 

## Verdict: 

Federal Office for Information Security 

130 

Web Service Interfaces 

## 3.4.2.2.7 M-SU-05b XAIP_NOK_SIG 

Identifier M-SU-05b Test Purpose The test shall verify that there will be an error, if the submitted XAIP_NOK_SIG contains digital signatures, which do not verify correctly[29] . Configuration • CONFIG_S.512 Pre-test • Authenticated connection to middleware exists. conditions • The TOT is configured only to accept valid signatures. Step Test sequence Expected Results 1 PreservePO PreservePOResponse ( ( pres:Profile(ACTIVE_PROFILE_URI), dsb:OptionalOutputs( pres:PO( dsb:Other( - http://www.bsi.bund.de/tr dsb:Value(XAIP_NOK_SIG_VR))), esor/xaip/1.3 dsb:Result( pres:xmlData(XAIP_NOK_SIG)) dsb:ResultMajor(resultmajor:RequesterError), ) dsb:ResultMinor(error/POFormatError)) ) Verdict of M-SU-05b Observations: Verdict: 

## 3.4.2.2.8 M-SU-06b XAIP_NOK_ER 

Identifier M-SU-06b Test Purpose The test shall verify that there will be an error, because the submitted XAIP_NOK_ER contains an incorrect Evidence Record. Configuration • CONFIG_S.512 Pre-test • Authenticated connection to middleware exists. conditions Step Test sequence Expected Results 1 PreservePO PreservePOResponse ( ( pres:Profile(ACTIVE_PROFILE_URI), dsb:OptionalOutputs( pres:PO( dsb:Other( - http://www.bsi.bund.de/tr dsb:Value(XAIP_NOK_ER_VR))), esor/xaip/1.3 dsb:Result( pres:xmlData(XAIP_NOK_ER)) dsb:ResultMajor(resultmajor:RequesterError), ) dsb:ResultMinor(error/POFormatError)) ) 

> 29 See also Annex E (Version 1.3, Chapter 3.7.1 ( `VerifyUnderSignaturePolicy` )). 

Federal Office for Information Security 

131 

Web Service Interfaces 

Verdict of M-SU-06b 

Observations: 

Verdict: 

## 3.4.2.2.9 M-SU-06ab LXAIP_NOK_ER 

|Identifier|M-SU-06ab|
|---|---|
|Test Purpose|The test shall verify that there will be an error, because the submitted LXAIP_OK_ER_NOK<br>contains an incorrect Evidence Record.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Test case M-SU-01ab has been performed successfully.|



Step Test sequence Expected Results 1 PreservePO PreservePOResponse ( ( pres:Profile(ACTIVE_PROFILE_URI), dsb:OptionalOutputs( pres:PO( dsb:Other( - http://www.bsi.bund.de/tr dsb:Value(LXAIP_NOK_ER_VR))), esor/lxaip/1.3 dsb:Result( pres:xmlData(LXAIP_OK_ER_NOK( dsb:ResultMajor(resultmajor:RequesterError), REF_TXT_DATA_52b, dsb:ResultMinor(error/POFormatError)) REF_PDF_DATA_52b, ) REF_XML_MDO_52b, ER_NOK_LXAIP_OK)) ) 

## Verdict of M-SU-06ab Observations: 

## Verdict: 

Federal Office for Information Security 

132 

Web Service Interfaces 

## 3.4.2.2.10 M-SU-07b XAIP_OK and unknown control in OptionalInputs 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0133-02.png)


**----- Start of picture text -----**<br>
Identifier  M-SU-07b<br>Test Purpose The test shall verify that there will be an error, if the request contains unknown controls in the<br>OptionalInputs -element and the archive data object will not be imported.<br>Configuration • CONFIG_S.512<br>Pre-test  • Authenticated connection to middleware exists.<br>conditions<br>Step  Test sequence  Expected Results<br>1 PreservePO  PreservePOResponse<br>(  (<br>    pres:OptionalInputs(      dsb:Result(<br>      dsb:Other(         dsb:ResultMajor(resultmajor:RequesterError),<br>          dsb:Value(SomethingUnknown))),         dsb:ResultMinor(error/notSupported))<br>    pres:Profile(ACTIVE_PROFILE_URI),  )<br>    pres:PO(<br>-<br>http://www.bsi.bund.de/tr<br>esor/xaip/1.3<br>        pres:xmlData(XAIP_OK))<br>)<br>Verdict of M-SU-07b<br>Observations:<br>Verdict:<br>**----- End of picture text -----**<br>


## 3.4.2.2.11 M-SU-08b BIN_OK 

|Identifier|M-SU-08b|
|---|---|
|Test Purpose|The test shall validate that it is possible to submit as BIN defined data. BIN means here:<br>•<br>CADES_ATT_OK,<br>•<br>XADES_ENVELOPED_OK, XADES_ENVELOPING_OK,<br>•<br>PADES_OK,<br>•<br>ASiC_S_CADES_OK, ASIC_S_XADES_OK, ASIC_S_TST_OK, ASIC_S_ER_OK,<br>•<br>ASiC_E_CADES_OK, ASIC_E_XADES_OK, ASIC_E_TST_OK, ASIC_E_ER_OK,<br>•<br>DIGEST_LIST.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/CAdES<br>pres:binaryData(CADES_ATT_OK)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-200b)<br>)|



Federal Office for Information Security 

133 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
||)<br>)||
|2|RetrievePO<br>(<br>pres:POID(AOID-200b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-200b, VID-01,<br>credential(CADES_ATT_OK))<br>)|
|3|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/XAdES<br>pres:binaryData(XADES_ENVELOPED_OK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-201b)<br>)|
|4|RetrievePO<br>(<br>pres:POID(AOID-201b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-201b, VID-01,<br>dataObject(xmlData(XADES_ENVELOPED_OK)))<br>)<br>)<br>)<br>OR30<br>RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-201b, VID-01,<br>dataObject(binaryData(XADES_ENVELOPED_OK)))<br>)<br>)<br>)|
|5|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/XAdES<br>pres:binaryData(XADES_ENVELOPING_OK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-202b)<br>)|
|6|RetrievePO<br>(<br>pres:POID(AOID-202b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-202b, VID-01,<br>credential(<br>SignatureObject(XADES_ENVELOPING_OK)))<br>)|



> 30 An enveloped XAdES could be placed in XAIP as binary data stream in an element `<xaip:binaryData>` (as recommended in [TR-ESOR-F] , section 6.2), or as xml data stream in an element `<xaip:xmlData>` in the `<xaip:dataObjectsSection>` -element. 

Federal Office for Information Security 

134 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|||)<br>)<br>)<br>OR31<br>RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-202b, VID-01,<br>credential(<br>Base64Signature(XADES_ENVELOPING_OK)))<br>)<br>)<br>)<br>)|
|7|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/PAdES<br>pres:binaryData(PADES_OK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-203b)<br>)|
|8|RetrievePO<br>(<br>pres:POID(AOID-203b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-203b, VID-01,<br>dataObject(PADES_OK)))<br>)<br>)|
|'9|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-E<br>pres:binaryData(ASiC_E_CADES_OK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-204b)<br>)|
|10|RetrievePO<br>(<br>pres:POID(AOID-204b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-204b, VID-01,<br>credential(ASiC_E_CADES_OK)))<br>)<br>)|
|11|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-205b)<br>)|



31 An enveloping XAdES could be placed in XAIP as binary credential data stream in an element `<dss:base64Signature>` (as recommended in [TR-ESOR-F] , section 6.2), or as xml credential data stream directly aa element `<dss:Signature>` in the `<dss:SignatureObject>` -element of the `<xaip:credential>` parent element. 

Federal Office for Information Security 

135 

Web Service Interfaces 

|Step||Test sequence|Expected Results|
|---|---|---|---|
||http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-E<br>pres:binaryData(ASIC_E_XADES_OK)<br>)<br>)|||
|12|RetrievePO<br>(<br>pres:POID(AOID-205b),<br>)||RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-205b, VID-01,<br>credential(ASIC_E_XADES_OK)))<br>)<br>)|
|13|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-E<br>pres:binaryData(ASIC_E_TST_OK)<br>)<br>)||PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-206b)<br>)|
|14|RetrievePO<br>(<br>pres:POID(AOID-206b),<br>)||RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-206b, VID-01,<br>credential(ASIC_E_TST_OK)))<br>)<br>)|
|15|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-E<br>pres:binaryData(ASIC_E_ER_OK)<br>)<br>)||PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-207b)<br>)|
|16|RetrievePO<br>(<br>pres:POID(AOID-207b),<br>)||RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-207b, VID-01,<br>credential(ASIC_E_ER_OK)))<br>)<br>)|
|17|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/19512/format/<br>DigestList<br>pres:binaryData(DIGEST_LIST)<br>)<br>)||PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-208b)<br>)|



Federal Office for Information Security 

136 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|18|RetrievePO<br>(<br>pres:POID(AOID-208b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-208b, VID-01,<br>dataObject (xmlData(DIGEST_LIST))))<br>)<br>)<br>OR32<br>RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-208b, VID-01,<br>dataObject(binaryData(DIGEST_LIST))))<br>)<br>)|
|19|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-S<br>pres:binaryData(ASiC_S_CADES_OK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-209b)<br>)|
|20|RetrievePO<br>(<br>pres:POID(AOID-209b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-209b, VID-01,<br>credential(ASiC_S_CADES_OK)))<br>)<br>)|
|21|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-S<br>pres:binaryData(ASIC_S_XADES_OK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-210b)<br>)|
|22|RetrievePO<br>(<br>pres:POID(AOID-210b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-210b, VID-01,<br>credential(ASIC_S_XADES_OK)))<br>)<br>)|



32 A digest list as XML based data object could be placed in XAIP as binary data stream in an element `<xaip:binaryData>` or as xml data stream in an element `<xaip:xmlData>` in the `<xaip:dataObjectsSection>` -element. 

Federal Office for Information Security 

137 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|23|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>@F<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-S<br>pres:binaryData(ASIC_S_TST_OK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-211b)<br>)|
|24|RetrievePO<br>(<br>pres:POID(AOID-211b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-211b, VID-01,<br>credential(ASIC_S_TST_OK)))<br>)<br>)|
|25|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-S<br>pres:binaryData(ASIC_S_ER_OK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-212b)<br>)|
|26|RetrievePO<br>(<br>pres:POID(AOID-212b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP(AOID-212b, VID-01,<br>credential(ASIC_S_ER_OK)))<br>)<br>)|



## Verdict of M-SU-08b 

## Observations: 

## Verdict: 

## 3.4.2.2.12 M-SU-09b BIN_NOK 

|Identifier|M-SU-09b|
|---|---|
|Test Purpose|The test shall validate that there will be an error in case an as BIN defined data containing an<br>invalid signature will be submitted. BIN means here:<br>•<br>CADES_ATT_NOK<br>•<br>XADES_ENVELOPED_NOK, XADES_ENVELOPING_NOK,<br>•<br>PADES_NOK,<br>•<br>ASIC_E_CADES_NOK, ASIC_E_XADES_NOK, ASIC_E_TST_NOK, ASIC_E_ER_NOK,<br>•<br>ASIC_S_CADES_NOK, ASIC_S_XADES_NOK, ASIC_S_TST_NOK, ASIC_S_ER_NOK.|
|Configuration|•<br>CONFIG_S.512|



Federal Office for Information Security 

138 

Web Service Interfaces 

## Identifier 

## M-SU-09b 

Pre-test • Authenticated connection to middleware exists. conditions • The TOT is configured only to accept valid signatures. 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/CAdES<br>pres:binaryData(CADES_ATT_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(CADES_ATT_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|2|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/XAdES<br>pres:binaryData(XADES_ENVELOPED_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XADES_ENVELOPED_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|3|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/XAdES<br>pres:binaryData(XADES_ENVELOPING_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XADES_ENVELOPING_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|4|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/PAdES<br>pres:binaryData(PADES_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(PADES_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|'5|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-E<br>,<br>pres:binaryData(ASIC_E_CADES_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(ASIC_E_CADES_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|6|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-E<br>,<br>pres:binaryData(ASIC_E_XADES_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(ASIC_E_XADES_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Federal Office for Information Security 

139 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|7|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-E<br>,<br>pres:binaryData(ASIC_E_TST_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(ASIC_E_TST_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|8|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-E<br>,<br>pres:binaryData(ASIC_E_ER_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(ASIC_E_ER_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|9|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>@FormatID=<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-S<br>,<br>pres:binaryData(ASIC_S_CADES_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(ASIC_S_CADES_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|10|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-S<br>pres:binaryData(ASIC_S_XADES_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(ASIC_S_XADES_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|11|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-S<br>pres:binaryData(ASIC_S_TST_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(ASIC_S_TST_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|12|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://uri.etsi.org/ades/ASiC/typ<br>e/ASiC-S<br>pres:binaryData(ASIC_S_ER_NOK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(ASIC_S_ER_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Verdict of M-SU-09b 

Observations: 

Federal Office for Information Security 

140 

Web Service Interfaces 

Verdict of M-SU-09b 

## Verdict: 

Federal Office for Information Security 

141 

Web Service Interfaces 

## 3.4.2.3 Function UpdatePOC of S.512-interface 

3.4.2.3.1 M-UP-01b DXAIP_OK 

|Identifier|M-UP-01b|
|---|---|
|Test Purpose|The test shall verify that it is possible to submit a correct DXAIP_OK with`UpdatePO`request.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test case M-SU-01b was successfully performed withAOID-01b.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-01b<br>into<br>the<br>prepared<br>DXAIP_OK-template.|DXAIP_OK(AOID-01b, VID-01, VID-02)|
|2|UpdatePOC<br>(<br>pres:POID(AOID-01b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_OK(AOID-01b, VID-01, VID-02))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(resultmajor:Success),<br>VersionID(VID-02)<br>)|
|3|Insert<br>AOID-01b<br>into<br>the<br>prepared<br>DXAIP_OK_2-template.|DXAIP_OK_2(AOID-01b, VID-02, VID-03)|
|4|UpdatePOC<br>(<br>pres:POID(AOID-01b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_OK_2(AOID-01b,VID-02,VID-03))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(resultmajor:Success),<br>VersionID(VID-03)<br>)|
|5|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_OK))<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-01zb)<br>)|
|6|Insert<br>AOID-01zb<br>into<br>the<br>prepared<br>DXAIP_OK_SIG_ONLY-template.|DXAIP_OK_SIG_ONLY(AOID-01zb, VID-01, VID-02)|



Federal Office for Information Security 

142 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|7|UpdatePOC<br>(<br>pres:POID(AOID-01zb),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_OK_SIG_ONLY(<br>AOID-01zb, VID-01, VID-02))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(resultmajor:Success),<br>VersionID(VID-02)<br>)|
||||
||Verdict of M-UP-01b||
|Observations:|||
|Verdict:|||



## 3.4.2.3.2 M-UP-01ab DLXAIP_OK 

|Identifier|M-UP-01ab|
|---|---|
|Test Purpose|The test shall verify that it is possible to submit a correct DLXAIP_OK with`UpdatePO`request.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test case M-SU-01ab and M-UP-01ab was successfully performed withAOID-<br>01ab.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-01ab<br>into<br>the<br>prepared<br>DLXAIP_OK-template.|DLXAIP_OK(AOID-01ab, VID-01, VID-02)|
|2|UpdatePOC<br>(<br>pres:POID(AOID-01ab),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:xmlData(<br>DLXAIP_OK(AOID-01ab,VID-01,VID-02,<br>REF_CADES_ATT_TXT_DATA_53b))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(resultmajor:Success),<br>VersionID(VID-02)<br>)|
|3|Insert<br>AOID-01abinto<br>the<br>prepared<br>DLXAIP_OK_2-template.|DLXAIP_OK_2(AOID-01ab, VID-02, VID-03)|



Federal Office for Information Security 

143 

Web Service Interfaces 

Step Test sequence Expected Results 4 UpdatePOC UpdatePOCResponse ( ( pres:POID(AOID-01ab), dsb:Result(resultmajor:Success), pres:DeltaPOC( VersionID(VID-03) - http://www.bsi.bund.de/tr ) esor/dlxaip/1.3 pres:xmlData( DLXAIP_OK_2( AOID-01ab, VID-02, VID-03, REF_XML_DATA_54b, REF_CADES_DET_XML_DATA_54b)) ) ) Verdict of A-UP-01ab Observations: Verdict: 

## 3.4.2.3.3 M-UP-02b DXAIP_NOK_AOID 

|Identifier|Identifier|M-UP-02b|M-UP-02b|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, if a DXAIP_NOK_AOID with a not yet assigned<br>AOID is submitted.||
|Configuration||•<br>CONFIG_S.512||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.||
|||||
|Step||Test sequence|Expected Results|
|1|Choice an AOID-03b within the possible range<br>and make sure, that it has not been assigned yet.<br>This is realised by the following call:<br>RetrievePO<br>(<br>pres:POID(AOID-03b),<br>pres:SubjectOfRe<br>)||PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownPOID))<br>)|
|2|Insert AOID-03b into DXAIP_NOK_AOID.||DXAIP_NOK_AOID(AOID-03b)|
|3|UpdatePOC<br>(<br>pres:POID(AOID-01ab),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_NOK_AOID(AOID-03b))<br>)<br>)||UpdatePOCResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownPOID))<br>)|



Federal Office for Information Security 

144 

Web Service Interfaces 

Verdict of M-UP-02b 

Observations: 

Verdict: 

## 3.4.2.3.4 M-UP-03b DXAIP_NOK 

|Identifier|M-UP-03b|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a (syntactically incorrect) DXAIP_NOK is<br>submitted.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_OK))<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-04b)<br>)|
|2|Insert<br>AOID-04b<br>into<br>the<br>prepared<br>DXAIP_NOK-template.|DXAIP_NOK(AOID-04b, VID-01, VID-02)|
|3|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_NOK(AOID-04b, VID-01, VID-02))<br>)<br>)|UpdatePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/DeltaPOCInternalProblem))<br>)<br>Alternatively, response to the one above could be<br>following or similar:<br><soapenv:Envelope<br>xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelo<br>pe/"><br><soapenv:Body><br><soapenv:Fault><br><faultcode>Server</faultcode><br><faultstring>Failed<br>to<br>dispatch<br>using<br>script;<br>java.lang.Exception: VALIDATION ERRORS: [<br>line<br>1:<br>Expected<br>element<br>'protectedObjectPointer@http://www.bsi.bund.de/tr-<br>esor/xaip' instead of 'AOID@http://www.bsi.bund.de/tr-<br>esor/xaip'<br>here<br>in<br>element<br>packageInfoUnit@http://www.bsi.bund.de/tr-<br>esor/xaip]</faultstring><br></soapenv:Fault><br></soapenv:Body><br></soapenv:Envelope>>|



Verdict of M-UP-03b 

Observations: 

Federal Office for Information Security 

145 

Web Service Interfaces 

Verdict of M-UP-03b 

## Verdict: 

## 3.4.2.3.5 M-UP-03ab DLXAIP_NOK 

|Identifier|M-UP-03ab|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if a (syntactically incorrect) DLXAIP_NOK is<br>submitted.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(<br>REF_TXT_DATA_55b,<br>REF_PDF_DATA_55b,<br>REF_XML_MDO_55b))<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-04ab)<br>)|
|2|Insert<br>AOID-04ab<br>into<br>the<br>prepared<br>DLXAIP_NOK-template.|DLXAIP_NOK(AOID-04ab, VID-01, VID-02)|
|3|UpdatePOC<br>(<br>pres:POID(AOID-04ab,<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:xmlData(<br>DLXAIP_NOK(AOID-04ab, VID-01, VID-02<br>REF_XML_DATA_56b,<br>REF_CADES_DET_XML_DATA_56b))<br>)<br>)|UpdatePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/DeltaPOCInternalProblem))<br>)<br>Alternatively, response to the one above could be<br>following or similar:<br><soapenv:Envelope<br>xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelo<br>pe/"><br><soapenv:Body><br><soapenv:Fault><br><faultcode>Server</faultcode><br><faultstring>Failed<br>to<br>dispatch<br>using<br>script;<br>java.lang.Exception: VALIDATION ERRORS: [<br>line<br>1:<br>Expected<br>element<br>'protectedObjectPointer@http://www.bsi.bund.de/tr-<br>esor/xaip' instead of 'AOID@http://www.bsi.bund.de/tr-<br>esor/xaip'<br>here<br>in<br>element<br>packageInfoUnit@http://www.bsi.bund.de/tr-<br>esor/xaip]</faultstring><br></soapenv:Fault><br></soapenv:Body><br></soapenv:Envelope>|



Federal Office for Information Security 

146 

Web Service Interfaces 

Verdict of M-UP-03ab Observations: 

## Verdict: 

## 3.4.2.3.6 M-UP-04b DXAIP_NOK_EXPIRED 

Identifier M-UP-04b Test Purpose The test shall verify that there will be an error, if the invalid DXAIP_NOK_EXPIRED is submitted. Configuration • CONFIG_S.512 Pre-test • Authenticated connection to middleware exists. conditions • Make sure that test case M-UP-03b was successfully performed with AOID-04b. 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-04b<br>into<br>the<br>prepared<br>DXAIP_NOK_EXPIRED-template.|DXAIP_NOK_EXPIRED(AOID-04b, VID-01, VID-02)|
|2|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_NOK_EXPIRED(<br>AOID-04b, VID-01, VID-02))<br>)<br>)|UpdatePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/DeltaPOCInternalProblem))<br>)|
||||
||Verdict of M-UP-04b||
|Observations:|||
|Verdict:|||



## 3.4.2.3.7 M-UP-05b DXAIP_NOK_SUBMTIME 

|Identifier|M-UP-05b|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the invalid DXAIP_NOK_SUBMTIME is<br>submitted.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test caseM-UP-03bwas successfully performed withAOID-04b.|



Federal Office for Information Security 

147 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-04b<br>into<br>the<br>prepared<br>DXAIP_NOK_SUBMTIME-template<br>Prepare DXAIP_NOK_SUBMTIME, set the value<br>of the element`xaip:submissionTime`in<br>`xaip:submissionInfo`to the time in the past.|DXAIP_NOK_SUBMTIME(<br>AOID-04b,<br>VID-01, VID-02,<br>SubmissionTime(in the past))|
|2|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_NOK_SUBMTIME(<br>AOID-04b,<br>VID-01, VID-02,<br>SubmissionTime(in the past)))<br>)<br>)|UpdatePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/DeltaPOCInternalProblem))<br>)|
|3|Insert<br>AOID-04b<br>into<br>the<br>prepared<br>DXAIP_NOK_SUBMTIME-template<br>Prepare DXAIP_NOK_SUBMTIME, set the value<br>of the element`xaip:submissionTime`in<br>`xaip:submissionInfo`to the time in the future|DXAIP_NOK_SUBMTIME(<br>AOID-04b,<br>VID-01, VID-02,<br>SubmissionTime(in the future))|
|4|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_NOK_SUBMTIME(<br>AOID-04b,<br>VID-01, VID-02,<br>SubmissionTime(in the future)))<br>)<br>)|UpdatePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/DeltaPOCInternalProblem))<br>)|



## Verdict of M-UP-05b 

Observations: 

Verdict: 

## 3.4.2.3.8 M-UP-06b DXAIP_NOK_SIG 

|Identifier|M-UP-06b|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the submitted DXAIP_NOK_SIG contains digital<br>signatures, which do not verify correctly.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test caseM-UP-03bwas successfully performed withAOID-04b.<br>•<br>The TOT is configured only to accept valid signatures.|



Federal Office for Information Security 

148 

Web Service Interfaces 

|Step|Test sequence|Test sequence|Expected Results|
|---|---|---|---|
|1|Insert<br>AOID-04b<br>into<br>the<br>prepared<br>DXAIP_NOK_SIG-template.||DXAIP_NOK_SIG(AOID-04b, VID-01, VID-02)|
|2|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_NOK_SIG(<br>AOID-04b, VID-01, VID-02))<br>)<br>)||PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(DXAIP_NOK_SIG_VR(<br>AOID-04b, VID-01, VID-02)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/DeltaPOCInternalProblem))<br>)|
|||||
||Verdict of M-UP-06b|||
|Observations:||||
|Verdict:||||
|3.4.2.3.9<br>M-UP-07b<br>DXAIP_NOK_ER||||
|Identifier||M-UP-07b||
|Test Purpose||The test shall verify that there will be an error, because the submitted DXAIP_NOK_ER contains<br>an invalid Evidence Record.||
|Configuration||•<br>CONFIG_S.512||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test caseM-UP-03bwas successfully performed withAOID-04b.||
|||||
|Step||Test sequence|Expected Results|
|1|Insert<br>AOID-04b<br>into<br>the<br>prepared<br>DXAIP_NOK_ER-template.||DXAIP_NOK_ER(AOID-04b, VID-01, VID-02)|
|2|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_NOK_ER(<br>AOID-04b, VID-01, VID-02))<br>)<br>)||PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(DXAIP_NOK_ER_VR(<br>AOID-04b, VID-01, VID-02)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/DeltaPOCInternalProblem))<br>)|



## 3.4.2.3.9 M-UP-07b DXAIP_NOK_ER 

## Verdict of M-UP-07b Observations: Verdict: 

Federal Office for Information Security 

149 

Web Service Interfaces 

## 3.4.2.3.10 M-UP-07ab DLXAIP_NOK_ER 

|Identifier|M-UP-07ab|
|---|---|
|Test Purpose|The test shall verify that there will be an error, because the submitted DLXAIP_NOK_ER contains<br>an invalid Evidence Record.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test caseM-UP-03abwas successfully performed withAOID-04ab.|



|Step|Test sequence|Test sequence|Expected Results|
|---|---|---|---|
|1|Insert<br>AOID-04ab<br>into<br>the<br>prepared<br>DLXAIP_NOK_ER-template.||DLXAIP_NOK_ER(AOID-04ab, VID-01, VID-02)|
|2|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:xmlData(<br>DLXAIP_NOK_ER(<br>AOID-04ab, VID-01, VID-02,<br>REF_CADES_ATT_TXT_DATA_57b,<br>ER_NOK_LXAIP_OK_V2))<br>)<br>)||PreservePOResponse<br>(<br>dsb:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(DLXAIP_NOK_ER_VR(<br>AOID-04ab, VID-01, VID-02)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|||||
||Verdict of M-UP-07ab|||
|Observations:||||
|Verdict:||||
|3.4.2.3.11<br>M-UP-08b<br> DXAIP_NOK_VERSION||||
|Identifier||M-UP-08b||
|Test Purpose||The test shall verify that there will be an error, if a DXAIP_NOK_VERSION is submitted with<br>`UpdatePO`request, which produces a collision33with the already existing XAIP.||
|Configuration||•<br>CONFIG_S.512||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test caseM-UP-03bwas successfully performed withAOID-04b.||



## 3.4.2.3.11 M-UP-08b DXAIP_NOK_VERSION 

> 33 DXAIP_NOK_VERSION) may be caused by inserting a DXAIP where the value in the element `prevVersion` in the `updateSection` of the DXAIP is not the latest version of this XAIP. 

Federal Office for Information Security 

150 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Insert<br>AOID-04b<br>into<br>the<br>prepared<br>DXAIP_NOK_VERSION-template.<br>Set<br>the<br>previous version to VID-10.|DXAIP_NOK_VERSION(AOID-04b, VID-10, VID-02)|
|2|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_NOK_VERSION(<br>AOID-04b, VID-10, VID-02))<br>)<br>)|UpdatePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/DeltaPOCInternalProblem))<br>)|
|3|Insert AOID-04b into the prepared DXAIP_OK-<br>template.|DXAIP_OK(AOID-04b, VID-01, VID-02)|
|4|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_OK(AOID-04b, VID-01, VID-02))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(resultmajor:Success),<br>VersionID(VID-02)<br>)|
|5|Insert<br>AOID-04b<br>into<br>the<br>prepared<br>DXAIP_NOK_VERSION-template.<br>Set<br>the<br>previous version to VID-01.|DXAIP_NOK_VERSION(AOID-04b, VID-01, VID-03)|
|6|UpdatePOC<br>(<br>pres:POID(AOID-04b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_NOK_VERSION(<br>AOID-04b, VID-01, VID-03))<br>)<br>)|UpdatePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/DeltaPOCInternalProblem))<br>)|
||||
||Verdict of M-UP-08b||
|Observations:|||
|Verdict:|||



## 3.4.2.3.12 M-UP-09b DXAIP_OK with unknown control in `OptionalInputs` 

|Identifier|M-UP-09b|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element.|
|Configuration|•<br>CONFIG_S.512|



Federal Office for Information Security 

151 

Web Service Interfaces 

Identifier M-UP-09b Pre-test • Authenticated connection to middleware exists. conditions 

## M-UP-09b 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_OK))<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-05b)<br>)|
|2|Insert AOID-05b into the prepared DXAIP_OK-<br>template.|DXAIP_OK(AOID-05b, VID-01, VID-02)|
|3|UpdatePOC<br>(<br>pres:OptionalInputs(<br>dsb:Other(<br>dsb:Value(SomethingUnknown))),<br>pres:POID(AOID-05b,<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_OK(AOID-05b, VID-01, VID-02))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/notSupported))<br>)|
|4|UpdatePOC<br>(<br>pres:POID(AOID-05b),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_OK(AOID-05b, VID-01, VID-02))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(resultmajor:Success),<br>VersionID(VID-02)<br>)|
|5|Insert AOID-05b and VID-02 as previous and<br>VID-03 as new versions into the prepared<br>DXAIP_OK_2-template.|DXAIP_OK_2(AOID-05b, VID-02, VID-03)|
|6|UpdatePOC<br>(<br>pres:POID(AOID-05b,<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(<br>DXAIP_OK_2(AOID-05b, VID-02, VID-03))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(resultmajor:Success),<br>VersionID(VID-03)<br>)|



Verdict of M-UP-09b Observations: 

## Verdict: 

Federal Office for Information Security 

152 

Web Service Interfaces 

## 3.4.2.3.13 M-UP-09ab DLXAIP_OK with unknown control in `OptionalInputs` 

|Identifier|M-UP-09ab|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(<br>REF_TXT_DATA_58b,<br>REF_PDF_DATA_58b,<br>REF_XML_MDO_58b))<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-05ab)<br>)|
|2|Insert<br>AOID-05ab<br>into<br>the<br>prepared<br>DLXAIP_OK-template.|DLXAIP_OK(AOID-05ab, VID-01, VID-02)|
|3|UpdatePOC<br>(<br>pres:OptionalInputs(<br>dsb:Other(<br>dsb:Value(SomethingUnknown))),<br>pres:POID(AOID-05ab,<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:xmlData(<br>DLXAIP_OK(AOID-05ab, VID-01, VID-02,<br>REF_CADES_ATT_TXT_DATA_60b))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/notSupported))<br>)|
|4|UpdatePOC<br>(<br>pres:POID(AOID-05ab,<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:xmlData(<br>DLXAIP_OK(AOID-05ab, VID-01, VID-02,<br>REF_CADES_ATT_TXT_DATA_59b))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(resultmajor:Success),<br>VersionID(VID-02)<br>)|
|5|Insert<br>AOID-05ab<br>into<br>the<br>prepared<br>DLXAIP_OK_2-template.|DLXAIP_OK_2(AOID-05ab, VID-02, VID-03)|



Federal Office for Information Security 

153 

Web Service Interfaces 

Step Test sequence Expected Results 6 UpdatePOC UpdatePOCResponse ( ( pres:POID(AOID-05ab, dsb:Result(resultmajor:Success), pres:DeltaPOC( VersionID(VID-03) - http://www.bsi.bund.de/tr ) esor/dlxaip/1.3 pres:xmlData( DLXAIP_OK_2( AOID-05ab, VID-02, VID-03, REF_XML_DATA_60-1b, REF_CADES_DET_XML_DATA_60-1b)) ) ) Verdict of M-UP-09ab Observations: Verdict: 

Federal Office for Information Security 

154 

Web Service Interfaces 

## 3.4.2.4 Function RetrievePO of S.512-interface 

- 3.4.2.4.1 M-RE-01b - Retrieval of previously archived XAIPs 

|Identifier|M-RE-01b|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve previously archived XAIPs.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test cases M-SU-01b, M-UP-01b and M-UP-09b were successfully<br>performed.<br>•<br>Requirements (A3.3.1-1) and (A3.3.1-2) of[TR-ESOR-E];|



Federal Office for Information Security 

155 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>,<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-01b, VID-03)))<br>)|
|2|RetrievePO<br>(<br>pres:POID(AOID-02b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK_SIG_OK(AOID-02b, VID-01)))<br>)|
|3|The fulfilment of the requirement A3.3.1-234is<br>checked.||
|4|RetrievePO<br>(<br>pres:POID(AOID-05b),<br>pres:VersionID(VID-02),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-05b, VID-02)))<br>)|
|5|RetrievePO<br>(<br>pres:POID(AOID-05b),<br>pres:VersionID(VID-01),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-05b, VID-01)))<br>)|
|6|RetrievePO<br>(<br>pres:POID(AOID-05b),<br>pres:VersionID(VID-01),<br>pres:VersionID(VID-02),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-05b, VID-01, VID-02)))<br>)|
|7|RetrievePO<br>(<br>pres:POID(AOID-05b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(<br>XAIP_OK(AOID-05b, VID-01, VID-02, VID-03)))<br>)|



34 See Annex E (Section 3.3.1). 

Federal Office for Information Security 

156 

Web Service Interfaces 

8 Test of correctness of the obtained XAIP_OK(AOID-05b, VID-01, VID-02, VID-03) by using AIP-eIDAS-SigValidator VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( XAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-05b, VID-01, VID-02, VID-03) dssvr:Details( ) vr:XAIPReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) ) 

## Verdict of M-RE-01b 

Observations: 

## Verdict: 

## 3.4.2.4.2 M-RE-01ab Retrieval of previously archived LXAIPs 

|Identifier|M-RE-01ab|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve previously archived LXAIPs.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test cases M-SU-01ab, M-UP-01ab and M-UP-09ab were successfully<br>performed.<br>•<br>Requirements (A3.3.1-1) and (A3.3.1-2) of[TR-ESOR-E];;|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(AOID-01ab, VID-03)))<br>)|
|2|RetrievePO<br>(<br>pres:POID(AOID-02ab),<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK_SIG_OK(<br>AOID-02ab, VID-01)))<br>)|



Federal Office for Information Security 

157 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|3|The fulfilment of the requirement A3.3.1-235is<br>checked.||
|4|RetrievePO<br>(<br>pres:POID(AOID-05ab),<br>pres:VersionID(VID-02),<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(AOID-05ab, VID-02)))<br>)|
|5|RetrievePO<br>(<br>pres:POID(AOID-05ab),<br>pres:VersionID(VID-01),<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(AOID-05ab, VID-01)))<br>)|
|6|RetrievePO<br>(<br>pres:POID(AOID-05ab),<br>pres:VersionID(VID-01),<br>pres:VersionID(VID-02),<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(AOID-05ab, VID-01, VID-02)))<br>)|
|7|RetrievePO<br>(<br>pres:POID(AOID-05ab),<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(<br>LXAIP_OK(AOID-05ab, VID-01, VID-02, VID-03)))<br>)|
|8|The all in LXAIP_OK(AOID-05ab, VID-01, VID-<br>02, VID-03) referenced files has been copied into<br>corresponding LXAIP-directory of the AIP-<br>eIDAS-SigValidator during test preparation (cf.<br>chapter 4.3) and the given references in<br>LXAIP_OK(AOID-05ab, VID-01, VID-02, VID-03)<br>will be adjusted automatically in order to get<br>them<br>resolveable<br>by<br>the<br>AIP-eIDAS-<br>SigValidator.|LXAIP_OK_XSV(AOID-05ab, VID-01, VID-02, VID-03)|



35 See Annex E (Section 3.3.1). 

Federal Office for Information Security 

158 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|9|Test of correctness of the obtained and prepared<br>LXAIP_OK_XSV(AOID-05a,<br>VID-01,<br>VID-02,<br>VID-03) by using AIP-eIDAS-SigValidator<br>VerifyRequest<br>(<br>dss:InputDocuments(<br>dss:Document(<br>dss:InlineXML(<br>LXAIP_OK_XSV(<br>AOID-05ab, VID-01, VID-02, VID-03)<br>)<br>)<br>)<br>)|VerifyResponse(<br>dss:Result(resultmajor#ok),<br>dss:OptionalOutputs(<br>dssvr:VerificationReport(<br>dssvr:IndividualReport(<br>dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid )<br>dssvr:Details(<br>vr:XAIPReport(<br>vr:FormatOK(<br>urn:oasis:names:tc:dss:1.0:detail:valid<br>)<br>)<br>)<br>)<br>)<br>)<br>)|
|10|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-05ab, VID-03)))<br>)|
|11|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-05ab, VID-03)))<br>)|



Verdict of M-RE-01ab 

Observations: 

## Verdict: 

## 3.4.2.4.3 M-RE-02b Retrieval of XAIPs for known and unknown AOIDs 

|Identifier|M-RE-02b|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve XAIPs for known AOIDs and there will be an error<br>in case of unknown AOIDs.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test casesM-SU-01bwas successfully performed.|



Federal Office for Information Security 

159 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Choice an AOID-06b within the possible range<br>and make sure, that it has not been assigned yet.<br>This is realised by the following call:<br>RetrievePO<br>(<br>pres:POID(AOID-06b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownPOID))<br>)|
|'2|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-01b, VID-03)))<br>)|
|3|RetrievePO<br>(<br>pres:POID(AOID-02b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK_SIG_OK(AOID-02b, VID-01)))<br>)|
|4|RetrievePO<br>(<br>pres:POID(AOID-06b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownPOID))<br>)|



Verdict of M-RE-02b Observations: Verdict: 

## 3.4.2.4.4 M-RE-03b Retrieval of XAIPs for known and unknown VersionIDs 

|Identifier|M-RE-03b|
|---|---|
|Test Purpose|The test shall verify that there will be a`requestOnlyPartlySuccessful`warning, if it is not<br>possible to retrieve XAIPs for all indicated VersionIDs.|
|Configuration|•<br>CONFIG_ArchiSafe_C.2|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test case M-SU-01 was successful performed.|



Federal Office for Information Security 

160 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Choice a VID-10 within the possible range and<br>make sure, that it has not been assigned yet. This<br>is realised by the following call:<br>RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-10),<br>)|RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownVersionID))<br>)|
|'2|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-02),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-01b, VID-02)))<br>)|
|3|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-10),<br>)|RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownVersionID))<br>)|
|4|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-02),<br>pres:VersionID(VID-10),<br>)|RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:Success),<br>dsb:ResultMinor(warning/requestOnlyPartlySuccessful)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-01b, VID-02))<br>)<br>)|



Verdict of M-RE-03b Observations: Verdict: 

## 3.4.2.4.5 M-RE-04b Unknown control in `OptionalInputs` 

|Identifier|M-RE-04b|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test case M-SU-01b was successfully performed.|



Federal Office for Information Security 

161 

Web Service Interfaces 

Step Test sequence Expected Results 1 RetrievePO RetrievePOResponse ( ( pres:OptionalInputs( dsb:Result( dsb:Other( dsb:ResultMajor(resultmajor:RequesterError), dsb:Value(SomethingUnknown))), dsb:ResultMinor(error/notSupported) pres:POID(AOID-01b), ) ) ) 

## Verdict of M-RE-04b 

Observations: Verdict: 

- 3.4.2.4.6 M-EV-01b Retrieval of Evidence Records of previously archived XAIPs without specifying the desired ERS Format 

|Identifier|M-EV-01b|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve Evidence Records for previously archived XAIPs.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that test cases M-SU-01b, M-UP-01b, M-UP-09b and M-RE-01b were successfully<br>performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b,VID-03,<br>XAIP_OK_V3_ER_OK)))<br>)|
|2|RetrievePO<br>(<br>pres:POID(AOID-02b),<br>Evidence<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-02b,VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK)))<br>)|
|3|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-02),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b,VID-02,<br>XAIP_OK_V2_ER_OK))<br>)<br>)|



Federal Office for Information Security 

162 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|4|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-01),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-01,<br>XAIP_OK_V1_ER_OK))<br>)<br>)|
|5|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-01),<br>pres:VersionID(VID-03),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-01,<br>XAIP_OK_V1_ER_OK))),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-03,<br>XAIP_OK_V3_ER_OK)))<br>)|
|6|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-01,<br>XAIP_OK_V1_ER_OK))),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-02,<br>XAIP_OK_V2_ER_OK))),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-03,<br>XAIP_OK_V3_ER_OK)))<br>)|
|7|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(<br>XAIP_OK(AOID-01b, VID-01, VID-02, VID-03)))<br>)|



Federal Office for Information Security 

163 

Web Service Interfaces 

Step Test sequence Expected Results 8 Test of correcteness of the obtained XAIP_OK_V1_ER_OK, XAIP_OK_V2_ER_OK and XAIP_OK_V3_ER_OK by using ERVerifyTool. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( XAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01b, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01b,VID-01, ) XAIP_OK_V1_ER_OK), ), XAIP_ERS( dssvr:IndividualReport( AOID-01b,VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) XAIP_OK_V2_ER_OK), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01b,VID-03, vr:FormatOK( XAIP_OK_V3_ER_OK) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 9 RetrievePO RetrievePOResponse ( ( pres:POID(AOID-01b), dsb:Result(resultmajor:Success), pres:PO( - pres:SubjectOfRetrieval( http://www.bsi.bund.de/tr esor/xaip/1.3 pres:xmlData( ) XAIP_OK(AOID-01b, VID-01, VID-02, VID-03, XAIP_OK_V1_ER_OK, XAIP_OK_V2_ER_OK, XAIP_OK_V3_ER_OK))) ) 

Federal Office for Information Security 

164 

Web Service Interfaces 

Step Test sequence Expected Results 10 Test of correcteness of the obtained XAIP_OK with embedded evidence records XAIP_OK_V1_ER_OK, XAIP_OK_V2_ER_OK and XAIP_OK_V3_ER_OK by using ERVerifyTool. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( XAIP_OK(AOID-01b, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) VID-01, VID-02, VID-03, dssvr:Details( XAIP_OK_V1_ER_OK, vr:EvidenceRecordReport( XAIP_OK_V2_ER_OK, vr:FormatOK( XAIP_OK_V3_ER_OK) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

Verdict of M-EV-01b Observations: 

## Verdict: 

- 3.4.2.4.7 M-EV-01ab Retrieval of Evidence Records of previously archived LXAIPs without specifying the desired ERS Format 

Identifier M-EV-01ab Test Purpose The test shall verify that it is possible to retrieve Evidence Records for previously archived LXAIPs. 

Federal Office for Information Security 

165 

Web Service Interfaces 

## Identifier 

## M-EV-01ab 

Configuration • CONFIG_S.512 • CONFIG_LXAIP Pre-test • Authenticated connection to middleware exists. conditions • Make sure that test cases M-SU-01ab, M-UP-01ab and M-UP-09ab were successfully performed. 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>vidence<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS36(AOID-01ab, VID-03,<br>LXAIP_OK_V3_ER_OK))<br>)<br>)|
|2|RetrievePO<br>(<br>pres:POID(AOID-02ab),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-02ab, VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK))<br>)<br>)|
|3|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>pres:VersionID(VID-02),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01ab, VID-02,<br>LXAIP_OK_V2_ER_OK))<br>)<br>)|
|4|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>pres:VersionID(VID-01),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01ab, VID-01,<br>LXAIP_OK_V1_ER_OK))<br>)<br>)|



> 36 XAIP-ERS does mean a RFC4998-ER embedded in the element `xaip:asn1EvidenceRecord` , which in turn is embedded in the element `xaip:evidenceRecord` and can contain the both attributes `AOID` and `VersionID` . 

Federal Office for Information Security 

166 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|5|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>pres:VersionID(VID-01),<br>pres:VersionID(VID-03),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01ab, VID-01,<br>LXAIP_OK_V1_ER_OK))<br>),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01ab, VID-03,<br>LXAIP_OK_V3_ER_OK))<br>)<br>)|
|6|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01ab, VID-01,<br>LXAIP_OK_V1_ER_OK))<br>),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01ab, VID-02,<br>LXAIP_OK_V2_ER_OK))<br>),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01ab, VID-03,<br>LXAIP_OK_V3_ER_OK))<br>)<br>)|
|7|RetrievePO<br>(<br>pres:POID(AOID-01ab),<br>pres:POFormat(http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3)<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(<br>AOID-01ab,VID-01,VID-02,VID-03))<br>)<br>)|



Federal Office for Information Security 

167 

Web Service Interfaces 

Step Test sequence Expected Results 8 Test of correcteness of the obtained LXAIP_OK_V1_ER_OK, LXAIP_OK_V2_ER_OK and LXAIP_OK_V3_ER_OK by using ERVerifyTool. The particular object references in the obtained LXAIP_OK will be replaced by the references compatible with the ERVerifyTool in advance. VerifyResponse( VerifyRequest dss:Result(resultmajor#ok), ( dss:OptionalOutputs( dss:InputDocuments( dssvr:VerificationReport( dss:Document( dssvr:IndividualReport( dss:InlineXML( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) LXAIP_OK( dssvr:Details( AOID-01ab, VID-01, VID-02, VID-03) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid ) ) dss:SignatureObject( dss:Other( ) XAIP_ERS( ) AOID-01ab, VID-01, ), LXAIP_OK_V1_ER_OK), dssvr:IndividualReport( XAIP_ERS( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01ab, VID-02, dssvr:Details( LXAIP_OK_V2_ER_OK), vr:EvidenceRecordReport( XAIP_ERS( vr:FormatOK( AOID-01ab, VID-03, urn:oasis:names:tc:dss:1.0:detail:valid LXAIP_OK_V3_ER_OK) ) ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

Verdict of M-EV-01ab 

Observations: 

Verdict: 

Federal Office for Information Security 

168 

Web Service Interfaces 

## 3.4.2.4.8 M-EV-02b Retrieval of Evidence Records for known and unknown AOIDs 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0169-02.png)


**----- Start of picture text -----**<br>
Identifier  M-EV-02b<br>Test Purpose The test case verifies that that it is possible to retrieve an Evidence Record for known AOIDs and<br>there will be an error in case of unknown AOIDs.<br>Configuration • CONFIG_S.512<br>Pre-test  • Authenticated connection to middleware exists.<br>conditions • Make sure that the test cases M-SU-01b and M-RE-02b were successfully performed.<br>Step  Test sequence  Expected Results<br>1  Make sure, that the previous chosen AOID-06b<br>is within the possible range and it is still not<br>assigned yet. This is realised by the following<br>call:<br>RetrievePO  RetrievePOResponse<br>(  (<br>    pres:POID(AOID-06b),      dsb:Result(<br>       dsb:ResultMajor(resultmajor:RequesterError),<br>)         dsb:ResultMinor(error/unknownPOID))<br>)<br>2  RetrievePO  RetrievePOResponse<br>(  (<br>    pres:POID(AOID-01b),      dsb:Result(resultmajor:Success),<br>    pres:PO(<br>)<br>        pres:xmlData(XAIP_ERS(AOID-01b,VID-03,<br>                                                         XAIP_OK_V3_ER_OK)))<br>)<br>3  RetrievePO RetrievePOResponse<br>(  (<br>    pres:POID(AOID-02b),      dsb:Result(resultmajor:Success),<br>    pres:PO(<br>)<br>        pres:xmlData(XAIP_ERS(AOID-02b,VID-01,<br>                                                      XAIP_OK_SIG_OK_V1_ER_OK)))<br>)<br>4  RetrievePO  RetrievePOResponse<br>(  (<br>    pres:POID(AOID-06b),      dsb:Result(<br>       dsb:ResultMajor(resultmajor:RequesterError),<br>)        dsb:ResultMinor(error/unknownPOID))<br>)<br>**----- End of picture text -----**<br>


Verdict of M-EV-02b Observations: Verdict: 

Federal Office for Information Security 

169 

Web Service Interfaces 

## 3.4.2.4.9 M-EV-03b Retrieval of Evidence Records for partly known `VersionID` s 

|Identifier|Identifier|M-EV-03b|M-EV-03b|
|---|---|---|---|
|Test Purpose||The test case verifies that there is a`requestOnlyPartlySuccessful`warning, if an Evidence<br>Record for an unknown`VersionID`is requested.||
|Configuration||•<br>CONFIG_S.512||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test cases M-SU-01b and M-RE-03b were successfully performed.||
|||||
|Step||Test sequence|Expected Results|
|1|Make sure, that concerning AOID-01b, the<br>chosen version VID-10 is within the possible<br>range but is an unknown`VersionID`. This is<br>realised by the following call:<br>RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-10),<br>)||RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownVersionID))<br>)|
|2|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)||RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b,VID-03,<br>XAIP_OK_V3_ER_OK)))<br>)|
|3|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-10),<br>)||RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownVersionID))<br>)|
|4|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>pres:VersionID(VID-02),<br>pres:VersionID(VID-10),<br>)||RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:Success),<br>dsb:ResultMinor(warning/requestOnlyPartlySuccessful)<br>),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-02,<br>XAIP_OK_V2_ER_OK))<br>)<br>)|
|||||
||Verdict of M-EV-03b|||
|Observations:||||
|Verdict:||||



Federal Office for Information Security 

170 

Web Service Interfaces 

## 3.4.2.4.10 M-EV-04b Unknown control in `OptionalInputs` 

|Identifier|Identifier|M-EV-04|M-EV-04|
|---|---|---|---|
|Test Purpose||The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element.||
|Configuration||•<br>CONFIG_S.512||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Make sure that the test case M-SU-01b was successfully performed.||
|||||
|Step||Test sequence|Expected Results|
|1|RetrievePO<br>(<br>pres:OptionalInputs(<br>dsb:Other(<br>dsb:Value(SomethingUnknown))),<br>pres:POID(AOID-01b),<br>)||RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/notSupported)<br>)<br>)|
|||||
||Verdict of M-EV-04b|||
|Observations:||||
|Verdict:||||



Federal Office for Information Security 

171 

Web Service Interfaces 

## 3.4.2.5 Function DeletePO of S.512-interface 

## 3.4.2.5.1 M-DE-01b Deletion of XAIP without `ReasonOfDeletion` 

|Identifier|M-DE-01b|
|---|---|
|Test Purpose|The test shall verify that it will yield an error, if`DeletePO`is called without providing a`Reason`of<br>deletion, if the element`retentionPeriod`in the XAIP contains a predetermined future date.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>In one test case the element`retentionPeriod`in the XAIP to be deleted contains a<br>predetermined future date. In the other test case the element`retentionPeriod`contains a<br>date in the past.<br>•<br>Authenticated connection to middleware exists.<br>•<br>Requirement (A3.5.1-1)of [TR-ESOR-E]:<br>•<br>The<br>`ArchiveDeletionRequest`of XAIP with<br>AOID-02bwith the end of the<br>`retentionPeriod`in the future must not be successful without a reason for the deletion.<br>•<br>Make sure that the test caseM-SU-01bwas successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|DeletePO<br>(<br>pres:POID(AOID-02b)<br>)|DeletePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/parameterError)<br>)<br>)|
|'2|RetrievePO<br>(<br>pres:POID(AOID-02b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK_SIG_OK(AOID-02b, VID-01))<br>)<br>)|
|3|RetrievePO<br>(<br>pres:POID(AOID-00b)37,<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-00b, VID-01))<br>)<br>)|
|4|DeletePO<br>(<br>pres:POID(AOID-00b)<br>)|DeletePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:Success)<br>)<br>)|
|5|RetrievePO<br>(<br>pres:POID(AOID-00b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownPOID))<br>)|



37 The XAIP with AOID-00b and LXAIP with AOID-00ab were imported some days ago. The retention period is expired. 

Federal Office for Information Security 

172 

Web Service Interfaces 

Verdict of M-DE-01b 

Observations: 

Verdict: 

## 3.4.2.5.2 M-DE-01ab Deletion of LXAIP without `ReasonOfDeletion` 

|Identifier|M-DE-01ab|
|---|---|
|Test Purpose|The test shall verify that it will yield an error, if`DeletePO`is called without providing a`Reason`of<br>deletion, if the element`retentionPeriod`in the LXAIP contains a predetermined future date.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>In one test case the element`retentionPeriod`in the LXAIP to be deleted contains a<br>predetermined future date. In the other test case the element`retentionPeriod`contains a<br>date in the past.<br>•<br>Authenticated connection to middleware exists.<br>•<br>Requirement (A3.5.1-1) of[TR-ESOR-E].<br>•<br>The`ArchiveDeletionRequest`of LXAIP withAOID-02abwith the end of the<br>`retentionPeriod`in the future must not be successful without a reason for the deletion.<br>•<br>Make sure that the test caseM-SU-01abwas successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|DeletePO<br>(<br>pres:POID(M-SU-02ab)<br>)|DeletePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/parameterError)<br>)<br>)|
|'2|RetrievePO<br>(<br>pres:POID(AOID-02ab),<br>pres:POFormat(http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3)<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK_SIG_OK(AOID-02ab, VID-01)))<br>)|
|3|RetrievePO<br>(<br>pres:POID(AOID-00ab37),<br>pres:POFormat(http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3)<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(AOID-00ab, VID-01))<br>)<br>)|
|4|DeletePO<br>(<br>pres:POID(AOID-00ab<br>)|DeletePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:Success)<br>)<br>)|



Federal Office for Information Security 

173 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|5|RetrievePO<br>(<br>pres:POID(AOID-00ab),<br>pres:POFormat(http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3)<br>)|RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownPOID))<br>)|



Verdict of M-DE-01ab Observations: Verdict: 

## 3.4.2.5.3 M-DE-02b Deletion of XAIP with `ReasonOfDeletion` 

|Identifier|M-DE-02b|
|---|---|
|Test Purpose|The test shall verify that it is possible to delete an XAIP by calling`DeletePO`with`Reason`of<br>deletion provided.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>The element`retentionPeriod`in the XAIP to be deleted contains a predetermined future<br>date.<br>•<br>Make sure that the test case M-SU-01b was successfully performed.<br>•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|DeletePO<br>(<br>pres:POID(AOID-02b),<br>pres:ClaimedRequestorName(SomeName),<br>pres:Reason(ReasonOfDeletion),<br>)|DeletePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:Success)<br>)<br>)|
|'2|RetrievePO<br>(<br>pres:POID(AOID-02b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/unknownPOID))<br>)|
|3|Check requirement A3.5.1-238.||



Verdict of M-DE-02b Observations: 

38 See Annex E (Section 3.5.1). 

Federal Office for Information Security 

174 

Web Service Interfaces 

Verdict of M-DE-02b 

Verdict: 

## 3.4.2.5.4 M-DE-02ab Deletion of LXAIP with `ReasonOfDeletion` 

## Identifier 

## M-DE-02ab 

Test Purpose The test shall verify that it is possible to delete an LXAIP by calling `DeletePO` with `Reason` of deletion provided. 

- Configuration • CONFIG_S.512 • CONFIG_LXAIP 

- Pre-test • The element `retentionPeriod` in the LXAIP to be deleted contains a predetermined future conditions date. • Make sure that the test case M-SU-01ab was successfully performed. • Authenticated connection to middleware exists. 

Step Test sequence Expected Results 1 DeletePO DeletePOResponse ( ( pres:POID(AOID-02ab), dsb:Result( pres:ClaimedRequestorName(SomeName), dsb:ResultMajor(resultmajor:Success) pres:Reason(ReasonOfDeletion), ) ) ) '2 RetrievePO RetrievePOResponse ( ( pres:POID(AOID-02ab), dsb:Result( dsb:ResultMajor(resultmajor:RequesterError), pres:POFormat(http://www.bsi.bund.de/trdsb:ResultMinor(error/unknownPOID)) esor/lxaip/1.3) ) ) 3 Check requirement A3.5.1-2[38] . 

Verdict of M-DE-02ab 

Observations: 

## Verdict: 

## 3.4.2.5.5 M-DE-03b Deletion of unknown XAIPs without `ReasonOfDeletion` 

|Identifier|M-DE-03b|
|---|---|
|Test Purpose|The test shall verify that it will yield an error, if`DeletePO`is called without providing a`Reason`of<br>deletion. As the present call also contains the unknownAOID-06b, the AOID-specific`dsb:Result`<br>needs to indicate that the AOID is unknown.|
|Configuration|•<br>CONFIG_ArchiSafe_C.2|



Federal Office for Information Security 

175 

Web Service Interfaces 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0176-01.png)


**----- Start of picture text -----**<br>
Identifier  M-DE-03b<br>Pre-test  • The element  retentionPeriod  in the XAIP to be deleted contains a predetermined future<br>conditions date.<br>• Make sure that the test cases M-UP-09b and M-RE-02b were successfully performed.<br>• Make sure, that the randomly generated AOID-06b is within the possible range but has not<br>been assigned yet.<br>• Authenticated connection to middleware exists.<br>Step  Test sequence  Expected Results<br>1  DeletePO  DeletePOResponse<br>(  (<br>    pres:POID(AOID-05b)      dsb:Result(<br>)         dsb:ResultMajor(resultmajor:RequesterError),<br>       dsb:ResultMinor(error/parameterError)<br>    )<br>)<br>2  DeletePO  DeletePOResponse<br>(  (<br>    pres:POID(AOID-06b)      dsb:Result(<br>)         dsb:ResultMajor(resultmajor:RequesterError),<br>       dsb:ResultMinor(error/unknownPOID))<br>)<br>3  RetrievePO  RetrievePOResponse<br>(  (<br>    pres:POID(AOID-05b),      dsb:Result(resultmajor:Success),<br>    pres:PO(<br>-<br>)  http://www.bsi.bund.de/tr esor/xaip/1.3<br>        pres:xmlData(XAIP_OK(AOID-05bVID-03))<br>    )<br>)<br>Verdict of M-DE-03b<br>Observations:<br>Verdict:<br>**----- End of picture text -----**<br>


## 3.4.2.5.6 M-DE-04b Deletion of unknown XAIPs with `ReasonOfDeletion` 

|Identifier|M-DE-04b|
|---|---|
|Test Purpose|The test shall verify that it will yield an error, if`DeletePO`is called with unknown AOIDs with<br>providing a`Reason`of deletion.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>The element`retentionPeriod`în the XAIP to be deleted contains a predetermined future<br>date.<br>•<br>Make sure that the test caseM-RE-02bwas successfully performed<br>•<br>Make sure, that the randomly generatedAOID-06bis within the possible range but has not<br>been assigned yet.<br>•<br>Authenticated connection to middleware exists.|



Federal Office for Information Security 

176 

Web Service Interfaces 

Step Test sequence Expected Results 1 DeletePO DeletePOResponse ( ( pres:POID(AOID-06b), dsb:Result( pres:ClaimedRequestorName(SomeName), dsb:ResultMajor(resultmajor:RequesterError), pres:Reason(ReasonOfDeletion), dsb:ResultMinor(error/unknownPOID)) ) ) 

Verdict of M-DE-04b 

Observations: 

Verdict: 

## 3.4.2.5.7 M-DE-05b Unknown control in `OptionalInputs` 

|Identifier|M-DE-05b|
|---|---|
|Test Purpose|The test shall verify that there will be an error, if the request contains unknown controls in the<br>`OptionalInputs`-element and the`DeletePO`request will not be successful.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The element`retentionPeriod`in the XAIP to be deleted contains a predetermined future<br>date.<br>•<br>Make sure that the test caseM-UP-09bwas successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|DeletePO<br>(<br>pres:OptionalInputs(<br>dsb:Other(<br>dsb:Value(SomethingUnknown))),<br>pres:POID(AOID-05b),<br>)|DeletePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/notSupported))<br>)|
|'2|RetrievePO<br>(<br>pres:POID(AOID-05b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK(AOID-05b, VID-03))<br>)<br>)|



Verdict of M-DE-05b Observations: Verdict: 

Federal Office for Information Security 

177 

Web Service Interfaces 

## 3.4.2.6 Function ValidateEvidence of S.512-interface 

3.4.2.6.1 M-VE-01b XAIP_OK_SIG_OK and XAIP_OK_SIG_OK_ER 

|Identifier|M-VE-01b|
|---|---|
|Test Purpose|The<br>test<br>shall<br>verify<br>that<br>it<br>is<br>possible<br>to<br>verify<br>XAIP_OK_SIG_OK<br>and<br>XAIP_OK_SIG_OK_V1_ER_OK<br>with<br>the<br>TR-ESOR-specific<br>signature<br>policy<br>http://www.bsi.bund.de/tr-esor/sigpolicy/verify-xaip.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_OK_SIG_OK)<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID( AOID-100b)<br>)|
|2|RetrievePO<br>(<br>pres:POID(AOID-100b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>)<br>)|
|3|RetrievePO7<br>(<br>pres:POID(AOID-100b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-100b,VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK))<br>)<br>)|
|4|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

178 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|5|ValidateEvidence<br>(<br>pres:OptionalInputs(<br>dsb:Other(<br>dsb:Value(vr:ReturnVerificationReport))),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>pres:ValidationReport(<br>pres:xmlData(XAIP_OK_SIG_OK_VR))<br>)|
|'6|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:binaryData(<br>XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|7|Prepare<br>XAIP_OK_SIG_OK_ER(AOID-100b,<br>VID-01) by inserting the XAIP_ERS(AOID-100b,<br>VID-01, XAIP_OK_SIG_OK_V1_ER_OK) obtained<br>in step 3 into credentialsSection element of<br>XAIP_OK_SIG_OK(AOID-100b, VID-01) from<br>step 2.|XAIP_OK_SIG_OK_ER(AOID-100b, VID-01)|
|8|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(<br>XAIP_OK_SIG_OK_ER(<br>AOID-100b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|9|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:binaryData(<br>XAIP_OK_SIG_OK_ER(<br>AOID-100b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

179 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|10|ValidateEvidence<br>(<br>pres:Evidence(<br>AOID-100b<br>-<br>pres:xmlData(<br>XAIP_ERS(AOID-100b, VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK))<br>)<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|11|ValidateEvidence<br>(<br>pres:Evidence(<br>AOID-100b<br>-<br>pres:binaryData(<br>XAIP_ERS(AOID-100b, VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK))<br>)<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|12|ValidateEvidence<br>(<br>pres:Evidence(<br>AOID-100b<br>-<br>pres:binaryData(<br>XAIP_ERS(AOID-100b, VID-01,<br>XAIP_OK_SIG_OK_V1_ER_OK))<br>)<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:binaryData(<br>XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
||||
||Verdict of M-VE-01b||
|Observations:|||
|Verdict:|||



Federal Office for Information Security 

180 

Web Service Interfaces 

## 3.4.2.6.2 M-VE-01ab - LXAIP_OK_SIG_OK and LXAIP_OK_SIG_OK_ER 

|Identifier|M-VE-01ab|
|---|---|
|Test Purpose|The test shall verify that it is possible to verify LXAIP_OK_SIG_OK and LXAIP_OK_SIG_OK_ER<br>with the TR-ESOR-specific signature policy http://www.bsi.bund.de/tr-esor/sigpolicy/verify-<br>xaip.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Test M-SU-01ab has been performed successfully and the references has been set properly in<br>LXAIP_OK_SIG_OK|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK_SIG_OK(<br>REF_TXT_DATA_61b,<br>REF_CADES_DET_TXT_DATA_61b,<br>REF_PDF_DATA_61b,<br>REF_CADES_DET_PDF_DATA_61b,<br>REF_XML_MDO_61b))<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-101ab)<br>)|
|2|RetrievePO<br>(<br>pres:POID(AOID-101ab),<br>pres:POFormat(http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3)<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/lxaip/1.3<br>pres:xmlData(<br>LXAIP_OK_SIG_OK(AOID-101ab, VID-01))<br>)<br>)|
|3|RetrievePO7<br>(<br>pres:POID(AOID-101ab),<br>)|RetrievePOResponse<br>(<br>dss:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(<br>AOID-101ab, VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK))<br>)<br>)|
|4|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(<br>LXAIP_OK_SIG_OK(AOID-101ab, VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|5|ValidateEvidence<br>(<br>pres:PO(|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)|



Federal Office for Information Security 

181 

Web Service Interfaces 

|Step||Test sequence|Expected Results|
|---|---|---|---|
||esor/lxaip/1.3||)|
|6|Prepare<br>LXAIP_OK_SIG_OK_ER(AOID-101ab,<br>VID-01) by inserting the XAIP_ERS(AOID-101ab,<br>VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK)<br>obtained in step 3 into credentialsSection<br>element of LXAIP_OK_SIG_OK(AOID-101ab,<br>VID-01) from step 2.||LXAIP_OK_SIG_OK_ER(AOID-101ab, VID-01)|
|7|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(<br>LXAIP_OK_SIG_OK_ER(<br>AOID-101ab,VID-01))<br>)<br>)||ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|8|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:binaryData(<br>LXAIP_OK_SIG_OK_ER(<br>AOID-101ab,VID-01))<br>)<br>)||ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|09|ValidateEvidence (<br>pres:Evidence(<br>AOID-101ab<br>-<br>pres:xmlData(<br>XAIP_ERS(AOID-101ab,VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK))<br>)<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(<br>LXAIP_OK_SIG_OK(AOID-101ab, VID-01))<br>)<br>)||ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|10|ValidateEvidence (<br>pres:Evidence(<br>AOID-101ab<br>-<br>pres:binaryData(<br>XAIP_ERS(AOID-101ab,VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK))<br>)<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(<br>LXAIP_OK_SIG_OK(AOID-101ab, VID-01))<br>)<br>)||ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

182 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|11|ValidateEvidence (<br>pres:Evidence(<br>AOID-101ab<br>-<br>pres:binaryData(<br>XAIP_ERS(AOID-101ab,VID-01,<br>LXAIP_OK_SIG_OK_V1_ER_OK))<br>)<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:binaryData(<br>LXAIP_OK_SIG_OK(AOID-101ab, VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Verdict of M-VE-01ab Observations: Verdict: 

## 3.4.2.6.3 M-VE-02b - DXAIP_OK_SIG_OK 

|Identifier|M-VE-02b|
|---|---|
|Test Purpose|The test shall verify that it is possible to verify DXAIP_OK_SIG_OK with the TR-ESOR-specific<br>signature policy http://www.bsi.bund.de/tr-esor/sigpolicy/verify-xaip.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The test M-VE-01b has been performed successfully|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Prepare DXAIP_OK_SIG_OK by inserting the<br>AOID-100b|DXAIP_OK_SIG_OK(AOID-100b, VID-01, VID-02)|
|2|ValidateEvidence (<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(DXAIP_OK_SIG_OK(<br>AOID-100b, VID-01,VID-02))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|'3|ValidateEvidence (<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:binaryData(DXAIP_OK_SIG_OK(<br>AOID-100b, VID-01,VID-02))|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

183 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
||)<br>)||
||||
||Verdict of M-VE-02b||
|Observations:|||
|Verdict:|||



## 3.4.2.6.4 M-VE-02ab - DLXAIP_OK_SIG_OK 

## Identifier M-VE-02ab 

Test Purpose The test shall verify that it is possible to verify DLXAIP_OK_SIG_OK with the TR-ESOR-specific signature policy http://www.bsi.bund.de/tr-esor/sigpolicy/verify-xaip. Configuration • CONFIG_S.512 • CONFIG_LXAIP Pre-test • Authenticated connection to middleware exists. conditions • The test M-VE-01ab has been performed successfully. 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Prepare DLXAIP_OK_SIG_OK by inserting the<br>AOID-101ab.|DLXAIP_OK_SIG_OK(AOID-101ab, VID-01, VID-02)|
|2|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:xmlData(<br>DLXAIP_OK_SIG_OK(<br>AOID-101ab, VID-01, VID-02,<br>REF_XML_DATA_62,<br>REF_CADES_DET_XML_DATA_62))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|'3|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:binaryData(<br>DLXAIP_OK_SIG_OK(<br>AOID-101ab, VID-01, VID-02,<br>REF_XML_DATA_63,<br>REF_CADES_DET_XML_DATA_63))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

184 

Web Service Interfaces 

Verdict of M-VE-02ab 

Observations: 

## Verdict: 

## 3.4.2.6.5 M-VE-04b - XAIP_OK_SIG_NOK & XAIP_OK_SIG_OK_ER_NOK 

|Identifier|M-VE-04b|
|---|---|
|Test Purpose|The test shall verify that there will be a verification error, in case XAIP_OK_SIG_NOK or<br>XAIP_OK_SIG_OK_ER_NOK is submitted.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_OK_SIG_NOK)<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(XAIP_OK_SIG_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_NOK(<br>XAIP_OK_SIG_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|2|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:xmlData(XAIP_OK_SIG_OK_ER_NOK)<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(XAIP_OK_SIG_OK_ER_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK_ER_NOK(<br>XAIP_OK_SIG_OK_ER_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Federal Office for Information Security 

185 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|3|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:binaryData(XAIP_OK_SIG_NOK)<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(XAIP_OK_SIG_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_NOK(<br>XAIP_OK_SIG_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|4|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>pres:binaryData(<br>XAIP_OK_SIG_OK_ER_NOK)<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(XAIP_OK_SIG_OK_ER_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK_ER_NOK(<br>XAIP_OK_SIG_OK_ER_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
||||
||Verdict of M-EV-04b||
|Observations:|||
|Verdict:|||



## 3.4.2.6.6 M-VE-04ab - LXAIP_OK_SIG_NOK & LXAIP_OK_SIG_OK_ER_NOK 

Identifier M-VE-04ab Test Purpose The test shall verify that there will be a verification error, in case of LXAIP_OK_SIG_NOK or LXAIP_OK_SIG_OK_ER_NOK is submitted. The response will include either the `VerificationReport` -Element only or the LXAIP including the `VerificationReport` - Element. Configuration • CONFIG_S.512 • CONFIG_LXAIP 

Federal Office for Information Security 

186 

Web Service Interfaces 

## Identifier 

Identifier M-VE-04ab Pre-test • Authenticated connection to middleware exists. conditions • Test M-SU-01ab has been performed successfully and the references has been set properly in LXAIP_OK_SIG_OK. 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK_SIG_NOK(<br>REF_TXT_DATA_65b,<br>REF_CADES_DET_NOK_TXT_DATA_65b,<br>REF_CADES_DET_PDF_DATA_65b,<br>REF_CADES_DET_PDF_DATA_65b,<br>REF_XML_MDO_65b))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(LXAIP_OK_SIG_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(LXAIP_OK_SIG_NOK(<br>LXAIP_OK_SIG_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|2|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(<br>LXAIP_OK_SIG_OK_ER_NOK(<br>REF_TXT_DATA_66b,<br>REF_CADES_DET_TXT_DATA_66b,<br>REF_CADES_DET_PDF_DATA_66b,<br>REF_CADES_DET_PDF_DATA_66b,<br>REF_XML_MDO_66b,<br>ER_NOK_XAIP_OK_SIG_OK_00))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(LXAIP_OK_SIG_OK_ER_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(LXAIP_OK_SIG_OK_ER_NOK(<br>LXAIP_OK_SIG_OK_ER_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Federal Office for Information Security 

187 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|3|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:binaryData(LXAIP_OK_SIG_NOK(<br>REF_TXT_DATA_67b,<br>REF_CADES_DET_NOK_TXT_DATA_67b,<br>REF_CADES_DET_PDF_DATA_67b,<br>REF_CADES_DET_PDF_DATA_67b,<br>REF_XML_MDO_67b))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(LXAIP_OK_SIG_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(LXAIP_OK_SIG_NOK(<br>LXAIP_OK_SIG_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|4|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:binaryData(<br>LXAIP_OK_SIG_OK_ER_NOK(<br>REF_TXT_DATA_68b,<br>REF_CADES_DET_TXT_DATA_68b,<br>REF_CADES_DET_PDF_DATA_68b,<br>REF_CADES_DET_PDF_DATA_68b,<br>REF_XML_MDO_68b,<br>ER_NOK_XAIP_OK_SIG_OK_00))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(LXAIP_OK_SIG_OK_ER_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(LXAIP_OK_SIG_OK_ER_NOK(<br>LXAIP_OK_SIG_OK_ER_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
||||
||Verdict of M-VE-04ab||
|Observations:|||
|Verdict:|||



## 3.4.2.6.7 M-VE-05b - DXAIP_OK_SIG_NOK 

|Identifier|M-VE-05b|
|---|---|
|Test Purpose|The test shall verify that there will be a verification error, in case DXAIP_OK_SIG_NOK is<br>submitted.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>TestM-VE-01bhas been performed successfully.|



Federal Office for Information Security 

188 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|1|Prepare DXAIP_OK_SIG_NOK by inserting<br>AOID-100b.|DXAIP_OK_SIG_NOK (AOID-100b, VID-01, VID-02)|
|2|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:xmlData(DXAIP_OK_SIG_NOK (<br>AOID-100b, VID-01, VID-02))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(DXAIP_OK_SIG_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(DXAIP_OK_SIG_NOK(<br>DXAIP_OK_SIG_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|3|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/dxaip/1.3<br>pres:binaryData(DXAIP_OK_SIG_NOK (<br>AOID-100b, VID-01, VID-02))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(DXAIP_OK_SIG_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(DXAIP_OK_SIG_NOK(<br>DXAIP_OK_SIG_NOK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
||||
||Verdict of M-VE-05b||
|Observations:|||
|Verdict:|||



## 3.4.2.6.8 M-VE-05ab - DLXAIP_OK_SIG_NOK 

|Identifier|M-VE-05ab|
|---|---|
|Test Purpose|The test case shall verify that there will be a verification error, in case DLXAIP_OK_SIG_NOK is<br>submitted.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|



Federal Office for Information Security 

189 

Web Service Interfaces 

|Identifier|Identifier|M-VE-05ab|M-VE-05ab|
|---|---|---|---|
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>Test M-VE-01ab has been performed successfully.||
|||||
|Step||Test sequence|Expected Results|
|1|Prepare DLXAIP_OK_SIG_NOK by inserting<br>AOID-101ab.||DLXAIP_OK_SIG_NOK(AOID-101ab, VID-01, VID-02)|
|2|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:xmlData(DLXAIP_OK_SIG_NOK(<br>AOID-101ab, VID-01, VID-02,<br>REF_XML_DATA_69b,<br>REF_CADES_DET_NOK_XML_DATA_69b))<br>)<br>)||ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(DXAIP_OK_SIG_NOK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(DLXAIP_OK_SIG_NOK(<br>AOID-101, VID-01, VID-02,<br>DXAIP_OK_SIG_NOK_VR)<br>),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>)|
|3|ValidateEvidence<br>(<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:binaryData(DLXAIP_OK_SIG_NOK(<br>AOID-101ab, VID-01, VID-02,<br>REF_XML_DATA_70b,<br>REF_CADES_DET_NOK_XML_DATA_70b))<br>)<br>)||VerifyResponse<br>(<br>dss:Result(resultmajor#error,<br>resultminor/arl/DXAIP_NOK_SIG)<br>dss:OptionalOutputs(DXAIP_OK_SIG_NOK_VR)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(DLXAIP_OK_SIG_NOK(<br>AOID-101ab, VID-01, VID-02,<br>DXAIP_OK_SIG_NOK_VR)<br>),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>)|



Verdict of M-VE-05ab Observations: Verdict: 

Federal Office for Information Security 

190 

Web Service Interfaces 

## 3.4.2.6.9 M-VE-07b Hash algorithms 

|Identifier|M-VE-07b|
|---|---|
|Test Purpose|The test shall verify that it is possible to verify XAIP_OK and corresponding evidence record with<br>the TR-ESOR-specific signature policyhttp://www.bsi.bund.de/tr-esor/sigpolicy/verify-xaip by<br>using different hash algorithms for underlaying hash tree. The hash algorithms to be tested are<br>following SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA3-224, SHA3-256, SHA3-384,<br>SHA3-512.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|Prepare XAIP_OK_SIG_OK by inserting of<br>AOID-999b|XAIP_OK_SIG_OK(AOID-999b, VID-01)|
|2|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>urn:ietf:rfc:4998:EvidenceRecord<br>XAIP-<br>@POID=<br>AOID-999b<br>,<br>@VersionID=<br>VID-01<br>pres:binaryData(<br>ER_OK_SHA-1_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>,<br>XAIP-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:RequesterError) ),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(XAIP_OK_SIG_OK_VR(<br>AOID-999b, VID-01,<br>ER_OK_SHA-1_XAIP_OK_SIG_OK_VR)<br>)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:RequesterError) ),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(XAIP_OK_SIG_OK_VR(<br>AOID-999b, VID-01,<br>ER_OK_SHA-1_XAIP_OK_SIG_OK_VR)<br>)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_OK_SHA-1_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Federal Office for Information Security 

191 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|3|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_NOK_SHA-1_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(ER_NOK_SHA-1_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(<br>ER_NOK_SHA-1_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_NOK_SHA-1_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Federal Office for Information Security 

192 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|4|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_OK_SHA-224_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:RequesterError) ),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(XAIP_OK_SIG_OK_VR(<br>AOID-999b, VID-01,<br>ER_OK_SHA-224_XAIP_OK_SIG_OK_VR)<br>)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:RequesterError) ),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(XAIP_OK_SIG_OK_VR(<br>AOID-999b, VID-01,<br>ER_OK_SHA-224_XAIP_OK_SIG_OK_VR)<br>)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_OK_SHA-224_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Federal Office for Information Security 

193 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|5|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_NOK_SHA-224_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(<br>ER_NOK_SHA-224_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(<br>ER_NOK_SHA-224_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_NOK_SHA-224_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|6|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>XAIP_ERS(AOID-999b,VID-01,<br>ER_OK_SHA-256_XAIP_OK_SIG_OK)<br>)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

194 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|7|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_NOK_SHA-256_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(<br>ER_NOK_SHA-256_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(<br>ER_NOK_SHA-256_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_NOK_SHA-256_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|8|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_OK_SHA-384_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

195 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|9|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_NOK_SHA-384_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(<br>ER_NOK_SHA-384_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(<br>ER_NOK_SHA-384_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_NOK_SHA-384_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|10|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_OK_SHA-512_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

196 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|11|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_NOK_SHA-512_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(<br>ER_NOK_SHA-512_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(<br>ER_NOK_SHA-512_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_NOK_SHA-512_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Federal Office for Information Security 

197 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|12|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_OK_SHA3-224_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:RequesterError) ),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(XAIP_OK_SIG_OK_VR(<br>AOID-999b, VID-01,<br>ER_OK_SHA3-224_XAIP_OK_SIG_OK_VR)<br>)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:RequesterError) ),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(XAIP_OK_SIG_OK_VR(<br>AOID-999b, VID-01,<br>ER_OK_SHA3-224_XAIP_OK_SIG_OK_VR)<br>)<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_OK_SHA3-<br>224_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Federal Office for Information Security 

198 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|13|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_NOK_SHA3-224_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(<br>ER_NOK_SHA3-224_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(<br>ER_NOK_SHA3-224_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_NOK_SHA3-224_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|14|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_OK_SHA3-256_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

199 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|15|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_NOK_SHA3-256_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(<br>ER_NOK_SHA3-256_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(<br>ER_NOK_SHA3-256_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_NOK_SHA3-256_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|16|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_OK_SHA3-384_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

200 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|17|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_NOK_SHA3-384_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(<br>ER_NOK_SHA3-384_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(<br>ER_NOK_SHA3-384_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_NOK_SHA3-384_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
|18|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_OK_SHA3-512_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

201 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|19|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=AOID-999b,<br>@VersionID=VID-01<br>pres:xmlData(<br>ER_NOK_SHA3-512_XAIP_OK_SIG_OK)<br>),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-999b,VID-01))<br>)<br>)|ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:xmlData(<br>ER_NOK_SHA3-512_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError)),<br>pres:ValidationReport(<br>pres:binaryData(<br>ER_NOK_SHA3-512_XAIP_OK_SIG_OK_VR))<br>)<br>OR<br>ValidateEvidenceResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(XAIP_OK_SIG_OK(AOID-999b, VID-01,<br>ER_NOK_SHA3-512_XAIP_OK_SIG_OK_VR)))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|
||||
||Verdict of M-VE-07b||
|Observations:|||
|Verdict:|||



Federal Office for Information Security 

202 

Web Service Interfaces 

## 3.4.2.7 Additional tests of S.512-interface 

3.4.2.7.1 M-ADD-01b XAIP_OK and Resigning 

|Identifier|Identifier|M-ADD-01b|M-ADD-01b|
|---|---|---|---|
|Test Purpose||The test shall verify that it is possible to retrieve previously submitted and updated XAIP_OK after<br>the time-stampresigningprocedure has been successfully applied.||
|Configuration||•<br>CONFIG_S.512||
|Pre-test<br>conditions||•<br>Authenticated connection to middleware exists.<br>•<br>The time-stamp resigning procedure has been successfully performed<br>•<br>Make sure that the test caseM-UP-01b was successfully performed.||
|||||
|Step||Test sequence|Expected Results|
|1|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)||RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(<br>XAIP_OK(AOID-01b, VID-01, VID-02, VID-03)))<br>)|
|'2|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)||RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-01,<br>XAIP_OK_V1_ER_OK_RESG))),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-02,<br>XAIP_OK_V2_ER_OK_RESG))),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-03,<br>XAIP_OK_V3_ER_OK_RESG)))<br>)|



Federal Office for Information Security 

203 

Web Service Interfaces 

Step Test sequence Expected Results 3 Test of correcteness of the obtained: • XAIP_OK_V1_ER_OK_RESG, • XAIP_OK_V2_ER_OK_RESG and • XAIP_OK_V3_ER_OK_RESG by using ERVerifyTool . VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( XAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01b, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01b, VID-01, ) XAIP_OK_V1_ER_OK_RESG), ), XAIP_ERS( dssvr:IndividualReport( AOID-01b, VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) XAIP_OK_V2_ER_OK_RESG), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01b, VID-03, vr:FormatOK( XAIP_OK_V3_ER_OK_RESG) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) [ ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

## Verdict of M-ADD-01b 

Observations: 

## Verdict: 

## 3.4.2.7.2 M-ADD-01ab LXAIP_OK and Resigning 

|Identifier|M-ADD-01ab|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve previously submitted and updated LXAIP_OK<br>after the time-stampresigningprocedure has been successfully applied.|



Federal Office for Information Security 

204 

Web Service Interfaces 

## Identifier 

## M-ADD-01ab 

- Configuration • CONFIG_S.512 • CONFIG_LXAIP 

- Pre-test • Authenticated connection to middleware exists. conditions • The time-stamp resigning procedure has been successfully performed • Make sure that the test case M-UP-01ab was successfully performed. 

Step Test sequence Expected Results 1 RetrievePO RetrievePOResponse ( ( pres:POID(AOID-01ab), dsb:Result(resultmajor:Success), pres:PO( - http://www.bsi.bund.de/tr esor/lxaip/1.3 - http://www.bsi.bund.de/tr pres:xmlData( esor/lxaip/1.3 LXAIP_OK(AOID-01ab, VID-01, VID-02, VID-03))) ) ) '2 RetrievePO RetrievePOResponse ( ( pres:POID(AOID-01ab), dsb:Result(resultmajor:Success), pres:PO( ) pres:xmlData(XAIP_ERS(AOID-01ab, VID-01, LXAIP_OK_V1_ER_OK_RESG)) ), pres:PO( pres:xmlData(XAIP_ERS(AOID-01ab, VID-02, LXAIP_OK_V2_ER_OK_RESG)) ), pres:PO( pres:xmlData(XAIP_ERS(AOID-01ab, VID-03, LXAIP_OK_V3_ER_OK_RESG)) ) ) 

Federal Office for Information Security 

205 

Web Service Interfaces 

Step Test sequence Expected Results 3 Test of correcteness of the obtained: • LXAIP_OK_V1_ER_OK_RESG, • LXAIP_OK_V2_ER_OK_RESG and • LXAIP_OK_V3_ER_OK_RESG by using ERVerifyTool. The particular object references in the obtained LXAIP_OK will be replaced by the references compatible with the ERVerifyTool in advance. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( LXAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01ab, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01ab, VID-01, ) LXAIP_OK_V1_ER_OK_RESG), ), XAIP_ERS( dssvr:IndividualReport( AOID-01ab, VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) LXAIP_OK_V2_ER_OK_RESG), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01ab, VID-03, vr:FormatOK( LXAIP_OK_V3_ER_OK_RESG) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) [ ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

Verdict of M-ADD-01ab 

## Observations: 

## Verdict: 

Federal Office for Information Security 

206 

Web Service Interfaces 

## 3.4.2.7.3 M-ADD-02b XAIP_OK and Rehashing 

|Identifier|M-ADD-02b|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve previously submitted and updated XAIP_OK after<br>the hash tree renewal procedure (rehashing) has been successfully applied.|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>The rehashing procedure has been successfully performed<br>•<br>Make sure that the test caseM-ADD-01bwas successfully performed.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>http://www.bsi.bund.de/tr-esor/xaip/1.3<br>pres:xmlData(<br>XAIP_OK(AOID-01b, VID-01, VID-02, VID-03)))<br>)|
|'2|RetrievePO<br>(<br>pres:POID(AOID-01b),<br>)|RetrievePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-01,<br>XAIP_OK_V1_ER_OK_RESG_REH))),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-02,<br>XAIP_OK_V2_ER_OK_RESG_REH))),<br>pres:PO(<br>pres:xmlData(XAIP_ERS(AOID-01b, VID-03,<br>XAIP_OK_V3_ER_OK_RESG_REH)))<br>)|



Federal Office for Information Security 

207 

Web Service Interfaces 

Step Test sequence Expected Results 3 Test of correcteness of the obtained: • XAIP_OK_V1_ER_OK_RESG_REH, • XAIP_OK_V2_ER_OK_RESG_REH and • XAIP_OK_V3_ER_OK_RESG_REH by using ERVerifyTool. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( XAIP_OK( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01b, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01b, VID-01, ) XAIP_OK_V1_ER_OK_RESG_REH), ), XAIP_ERS( dssvr:IndividualReport( AOID-01b, VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) XAIP_OK_V2_ER_OK_RESG_REH), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01b, VID-03, vr:FormatOK( XAIP_OK_V3_ER_OK_RESG_REH) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

## Verdict of M-ADD-02b 

Observations: 

## Verdict: 

## 3.4.2.7.4 M-ADD-02ab LXAIP_OK and Resigning 

|Identifier|M-ADD-02ab|
|---|---|
|Test Purpose|The test shall verify that it is possible to retrieve previously submitted and updated LXAIP_OK<br>after the hash tree renewal procedure (rehashing) has been successfully applied.|



Federal Office for Information Security 

208 

Web Service Interfaces 

## Identifier 

## M-ADD-02ab 

- Configuration • CONFIG_S.512 • CONFIG_LXAIP 

- Pre-test • Authenticated connection to middleware exists. conditions • The rehashing procedure has been successfully performed • Make sure that the test case M-ADD-01ab was successfully performed. 

Step Test sequence Expected Results 1 RetrievePO RetrievePOResponse ( ( pres:POID(AOID-01ab), dsb:Result(resultmajor:Success), pres:PO( - http://www.bsi.bund.de/tr esor/lxaip/1.3 - http://www.bsi.bund.de/tr pres:xmlData( esor/lxaip/1.3 LXAIP_OK(AOID-01ab, VID-01, VID-02, VID-03)))) ) '2 RetrievePO RetrievePOResponse ( ( pres:POID(AOID-01ab), dsb:Result(resultmajor:Success), pres:PO( ) pres:xmlData(XAIP_ERS(AOID-01ab, VID-01, LXAIP_OK_V1_ER_OK_RESG_REH)) ), pres:PO( pres:xmlData(XAIP_ERS(AOID-01ab, VID-02, LXAIP_OK_V2_ER_OK_RESG_REH)) ), pres:PO( pres:xmlData(XAIP_ERS(AOID-01ab, VID-03, LXAIP_OK_V3_ER_OK_RESG_REH)) ) ) 

Federal Office for Information Security 

209 

Web Service Interfaces 

Step Test sequence Expected Results 3 Test of correcteness of the obtained: • LXAIP_OK_V1_ER_OK_RESG_REH, • LXAIP_OK_V2_ER_OK_RESG_REH and • LXAIP_OK_V3_ER_OK_RESG_REH by using ERVerifyTool. The particular object references in the obtained LXAIP_OK will be replaced by the references compatible with the ERVerifyTool in advance. VerifyRequest VerifyResponse( ( dss:Result(resultmajor#ok), dss:InputDocuments( dss:OptionalOutputs( dss:Document( dssvr:VerificationReport( dss:InlineXML( dssvr:IndividualReport( LXAIP_OK ( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) AOID-01ab, VID-01, VID-02, VID-03) dssvr:Details( ) vr:EvidenceRecordReport( ) vr:FormatOK( ) urn:oasis:names:tc:dss:1.0:detail:valid dss:SignatureObject( ) dss:Other( XAIP_ERS( ) AOID-01ab, VID-01, ) LXAIP_OK_V1_ER_OK_RESG_REH), ), XAIP_ERS( dssvr:IndividualReport( AOID-01ab, VID-02, dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) LXAIP_OK_V2_ER_OK_RESG_REH), dssvr:Details( XAIP_ERS( vr:EvidenceRecordReport( AOID-01ab, VID-03, vr:FormatOK( LXAIP_OK_V3_ER_OK_RESG_REH) urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) [ ) ) ) ), dssvr:IndividualReport( dss:Result( urn:oasis:names:tc:dss:1.0:detail:valid ) dssvr:Details( vr:EvidenceRecordReport( vr:FormatOK( urn:oasis:names:tc:dss:1.0:detail:valid ) ) ) ) ) ) ) 

Verdict of M-ADD-02ab Observations: 

## Verdict: 

Federal Office for Information Security 

210 

Web Service Interfaces 

## 3.4.2.7.5 M-ADD-03ab Relation between upload data and LXAIP/DLXAIP 

|Identifier|M-ADD-03ab|
|---|---|
|Test Purpose|The test shall verify that 1:1-relation between the uploaded data and corresponding<br>LXAIP/DLXAIP is adhered to. It is not possible to use a single reference in two different<br>LXAIP/DLXAIP instances and in such case, an error will be returned.|
|Configuration|•<br>CONFIG_S.512<br>•<br>CONFIG_LXAIP|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.<br>•<br>Test case M-SU-01a has been performed successfully.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(<br>REF_TXT_DATA_71b,<br>REF_PDF_DATA_71b,<br>REF_XML_MDO_71b)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-300ab)<br>)|
|2|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(<br>REF_TXT_DATA_71b,<br>REF_PDF_DATA_71b,<br>REF_XML_MDO_71b)<br>)|PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/parameterError))<br>)|
|3|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK_ER_NOK(<br>REF_TXT_DATA_72b,<br>REF_PDF_DATA_72b,<br>REF_XML_MDO_72b,<br>ER_NOK_LXAIP_OK_72))<br>)<br>)|PreservePOResponse<br>(<br>pres:OptionalOutputs(<br>dsb:Other(<br>dsb:Value(LXAIP_OK_ER_NOK_VR))),<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/POFormatError))<br>)|



Federal Office for Information Security 

211 

Web Service Interfaces 

|Step|Test sequence|Expected Results|
|---|---|---|
|4|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK_ER_NOK(<br>REF_TXT_DATA_72b,<br>REF_PDF_DATA_72b,<br>REF_XML_MDO_72b,<br>ER_NOK_LXAIP_OK_72))<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/parameterError))<br>)|
|5|UpdatePOC<br>(<br>pres:POID(AOID-01ab),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:xmlData(<br>DLXAIP_OK(AOID-300ab,VID-01,VID-02,<br>REF_CADES_ATT_TXT_DATA_73b))<br>)<br>)|UpdatePOCResponse<br>(<br>dsb:Result(resultmajor:Success),<br>VersionID(VID-02)<br>)|
|6|PreservePO<br>(<br>pres:Profile(ACTIVE_PROFILE_URI),<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/lxaip/1.3<br>pres:xmlData(LXAIP_OK(<br>REF_TXT_DATA_74b,<br>REF_PDF_DATA_74b,<br>REF_XML_MDO_74b)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success),<br>pres:POID(AOID-301ab)<br>)|
|7|UpdatePOC<br>(<br>pres:POID(AOID-01ab),<br>pres:DeltaPOC(<br>http://www.bsi.bund.de/tr-<br>esor/dlxaip/1.3<br>pres:xmlData(<br>DLXAIP_OK(AOID-301ab,VID-01,VID-02,<br>REF_CADES_ATT_TXT_DATA_73b))<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(<br>dsb:ResultMajor(resultmajor:RequesterError),<br>dsb:ResultMinor(error/parameterError))<br>)|



Verdict of M-ADD-03ab Observations: Verdict: 

Federal Office for Information Security 

212 

Web Service Interfaces 

## 3.4.2.7.6 M-ADD-04b Evidence Record with single hash value 

|Identifier|M-ADD-04b|
|---|---|
|Test Purpose|The test shall verify that it is possible to verify every variant of the evidence record computed on<br>a single data object:<br>•<br>`ER(TSP(H(DO-01)))`<br>hash value of the data object is directly included in the message<br>imprint of the timestamp (`ER_SO-1_OK_XAIP_OK_SO`),<br>•<br>`ER(H(DO-01),TSP(H(DO-01)))`<br>the hash value of the data object is placed in the single<br>reduced hash tree and the same hash value is included in the message imprint of the<br>timestamp (`ER_SO-2_OK_XAIP_OK_SO`),<br>•<br>`ER(H(DO-01),TSP(H(H(DO-01))))`- the hash value of the data object is placed in the single<br>reduced hash tree and the hash value of those hash value (computet hash tree root) is<br>included in the message imprint of the timestamp (`ER_SO-3_OK_XAIP_OK_SO`).|
|Configuration|•<br>CONFIG_S.512|
|Pre-test<br>conditions|•<br>Authenticated connection to middleware exists.|



|Step|Test sequence|Expected Results|
|---|---|---|
|1|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>@POID=<br>AOID-999b<br>,<br>@VersionID=<br>VID-01<br>pres: binaryData(<br>ER_SO-1_OK_XAIP_OK_SO)<br>)<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|
|2|ValidateEvidence<br>(<br>pres:Evidence(<br>@FormatID=<br>-<br>AOID-999b<br>-<br>pres: binaryData(<br>ER_SO-2_OK_XAIP_OK_SO)<br>)<br>pres:PO(<br>http://www.bsi.bund.de/tr-<br>esor/xaip/1.3<br>-<br>pres:xmlData(<br>XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>)<br>)|PreservePOResponse<br>(<br>dsb:Result(resultmajor:Success)<br>)|



Federal Office for Information Security 

213 

Web Service Interfaces 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0214-01.png)


**----- Start of picture text -----**<br>
Step  Test sequence  Expected Results<br>3  ValidateEvidence  PreservePOResponse<br>(  (<br>    pres:Evidence(      dsb:Result(resultmajor:Success)<br>        @FormatID=  )<br>-<br>AOID-999b<br>-<br>      pres: binaryData(<br>          ER_SO-3_OK_XAIP_OK_SO)<br>    )<br>    pres:PO(<br>-<br>http://www.bsi.bund.de/tr<br>esor/xaip/1.3<br>-<br>      pres:xmlData(<br>          XAIP_OK_SIG_OK(AOID-100b, VID-01))<br>    )<br>)<br>Verdict of M-ADD-04b<br>Observations:<br>Verdict:<br>**----- End of picture text -----**<br>


Federal Office for Information Security 

214 

TR-ESOR-C.2-Testbed how-to 

## 4 TR-ESOR-C.2-Testbed how-to 

The following chapter will give a short description, how the TR-ESOR-C.2-Testbed (C.2-Testbed) can be set up and used. 

## 4.1 TR-ESOR-C.2-Testbed Prerequisites 

In order to use the C.2-Testbed following tools have to be provided: 

- Soap-UI - https://www.soapui.org/downloads/soapui/ 

The setup and generation of Soap-UI-configuration can be done either by using directly Microsoft Excel Product (optional requirement), or by editing the provided initial configuration file (cf. chapter 4.2.4). 

In order to run the XSVT and ERVT a docker environment is required, e.g.: 

- Desktop Docker - https://www.docker.com/products/docker-desktop/ (please check de license conditions), or 

- Rancher Desktop - https://rancherdesktop.io/, or 

- any other compatible docker installation. 

## 4.2 TR-ESOR-C.2-Testbed introduction 

The last version of C.2-Testbed can be obtained from the corresponding GIT repository: 

- https://github.com/de-bund-bsi-tr-esor/TR-ESOR-C.2-Testbed. 

The C.2-Testbed can be cloned by using the GIT functionality: 

- `git clone https://github.com/de-bund-bsi-tr-esor/TR-ESOR-C.2-Testbed.git` , or 

can be downloaded as a ZIP-archive and unzip locally. 

Notice: The used test material is dealing with cryptographic functions such electronic signatures timestamps etc. Therefore, this is important, that the checked out/cloned sources must not be altered in any way. This refer also to the CR and CRLF issue. Before clone the repository, please make sure the original alignment of the end lines, especially of xml- and txt-based files will not be altered. You can do that e.g. by switching off this transformation global in your git environment: `git config --global core.autocrlf false` . 

The obtained project directory will have the structured depicted in the Figure 4 below. 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0215-19.png)


Figure 4: TR-ESOR-C.2-Testbed project directory structure. 

Federal Office for Information Security 

215 

TR-ESOR-C.2-Testbed how-to 

Following chapters describe the content of the directories and the important files as well as their role in the - - - - - - - C.2-Testbed. For short version please refer to https://github.com/de bund bsi tr esor/TR ESOR C.2 Testbed/blob/main/README.md. 

## 4.2.1 Subdirectory DOCKERS 

This directory does contain the Docker definitions in order to setup and start the both BSI test tools: 

- xsv-srv BSI AIP signature validator (cf. chapter 3.1.1 

- erv-srv BSI Evidence Record validator (cf. chapter 3.1.1). 

## 4.2.2 Subdirectory ERVT-UPLOADs 

Notice : Only relevant in case the TOT is supporting LXAIP. 

This directory does contain all the files, which are necessary to execute the corresponding test cases linked to Evidence Record Verify Tool (ERVT). The references to those files are placed in the corresponding section of a given LXAIP and will be adjusted automatically by the C.2-Testbed during the execution of the test cases. All the files from this directory have to be copied to the dedicated LXAIP-directory of the ERVT. 

## 4.2.3 Subdirectory LXAIP-UPLOADs 

Notice : Only relevant in case the TOT is supporting LXAIP. 

This directory does contain all files required to perform the LXAIP test cases, which have to be uploaded to the TOT by using the Upload/Download module. The returned references have to be noted in the configuration file in order to instrument the C.2-Testbed for test execution (cf. chapter 4.2.4). The C.2-Testbed will automatically adjust the configured references in the test data during the test execution. 

Please refer to step 1 in M-SU-01a or in M-SU-01ab test case in the chapter 1.1.1.1.1 or chapter 3.4.2.2.2 for further information 

## 4.2.4 Subdirectory PROPERTIES 

This Subdirectory does contain only two files: 

- TR-C2-Soap-UI-List-of-Project-Properties.xlsm which defines all the configuration properties have to be set in advance of the test execution. After the necessary properties has been set, a configuration file can be exported an after that imported into the C.2-Testbed test suite; please refer to the -file for further information on that. 

- Initial-Soap-UI-configuration.props which does contain the initial version of SoapUI-Project configuration; the file can be directly edited an after that imported into the SoapUI-Project as an alternative solution. 

## 4.2.5 Subdirectory RUN-DATA 

This subdirectory does contain the environment to be used in order to run the final tests and collect the which can be used to execute either a chosen test cases, or whole tests, to clean up the documented results etc. The details how to use the environment and the particular scripts please find in the section 4.6. 

## 4.2.6 Subdirectory TESTDATA 

This Subdirectory does contain the test data which is directly used by the C.2-Testbed in order to execute the test cases, e.g. XAIP-, LXAIP- ER-objects etc. (cf. chapter 3.3). 

Federal Office for Information Security 

216 

TR-ESOR-C.2-Testbed how-to 

## 4.2.7 Subdirectory XSVT-UPLOADs 

Notice : Only relevant in case the TOT is supporting LXAIP. 

This directory does contain all the files, which are necessary to execute the corresponding test cases linked to XAIP Signature Validation Tool (XSVT). The references to those files are placed in the corresponding section of a given LXAIP and will be adjusted automatically by the C.2-Testbed during the execution of the test cases. All the files from this directory have to be copied to the dedicated LXAIP-directory of the XSVT. 

## 4.2.8 File TR-ESOR-1.3.0-C2-Testbed-soapui-project.xml 

This file does contain all the test cases implemented by C.2.Testbed SoapUI-Project file. 

## 4.2.9 File BSI TR-03125_C.2_V1.3.pdf 

This file does contain the current version of the [TR-ESOR-C.2] . 

## 4.3 TR-ESOR-C.2-Testbed configuration 

Notice : XAIP shall be supported, LXAIP may be supported (c.f. [TR-ESOR-F] , A3-1). 

Notice : At least one of the both interfaces TR-S.4 or TR-S.512 shall be supported (c.f. [TR-ESOR-E] , A2.0-1). 

Notice : The terms target of test (TOT) and target of evaluation/examination (TOE) are used as synonyms. 

Following Table 3 gives overview of steps have to be done in order to configure the C.2-Testbed. The column ed 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0217-13.png)


|#|Container|<br>Action|
|---|---|---|
|1|All|Do create a test tenant in the TOT with<br>chosen client-id e.g. "Bsi" (cf.<br>`<xaip:submissionInfoType>`in[TR-ESOR-F], page 17) and set the value of the<br>corresponding property CLIENT_ID_TO_BE_SET.|
|2|All|If TR-S.4 is supported by TOT, do<br>do<br>insert the TOT endpoint address of the TR-S.4 interface into the corresponding property<br>TOE_S4_ENDPOINT in the props-file.<br>If TR-S.512 is supported by TOT, do<br>and do insert the TOT endpoint address of the TR-S.512 interface into the corresponding<br>property TOE_S512_ENDPOINT in the props-file.<br>Please notice the C.2-Testbed does support the http communication as default one. Anything<br>supplementary has to be configured according to the SoapUI documentation.|
|3|All|Do check and adjust the value of the ERVT_ENDPOINT property in the props-file, as needed<br>(cf. chapter 4.4).|
|4|All|Do check and adjust the value of the XSVT_ENDPOINT property in the props-file, as needed<br>(cf. chapter 4.4).|
|5|All|Do configure the behaviour of TOT in case of signature verification errors by enabling one<br>(the other one has to be disabled - set to NO) of the following properties:<br>•<br>set value of OPT_VERIFY_VR_STANDALONE property to YES, if only verification report<br>used to be returned,<br>•<br>set value of OPT_VERIFY_VR_EMB_IN_CONTAINER property to YES, if the verification<br>report embedded into agiven XAIP or LXAIP used to be returned.|



Federal Office for Information Security 

217 

TR-ESOR-C.2-Testbed how-to 

|#|Container|<br>Action|
|---|---|---|
|6|All|Do configure the behaviour of the TOT in case an invalid XML structure is used at S.4 by<br>enabling one of the following properties (the other one has to be set to NO):<br>•<br>set value of OPT_INVALID_XML_AS_SOAP_FAULT to YES in case a soap fault used to be<br>returned,<br>•<br>set value of OPT_INVALID_XML_AS_S4_ERROR to YES in case an application level status<br>code used to be returned.<br>If TR-S.4 is supported by TOT, do configure, if the TOT is supporting passing by of the XML-<br>data as native XML (e.g. XAdES):<br>•<br>set value of OPT_SUPPORT_VERIFY_XML_DATA_PARAMETER to YES if passing by XML<br>data as native XML is supported by the TOT while calling Verify function od TR.S.4→the<br>CONDITIONAL test steps in test cases M-VE-03 and M-VE-06 will be executed in a such<br>case.|
|7|All|Do check and adjust as needed the value of SUBMISSION_TIME_RANGE_IN_DAYS property<br>(in days), which does describe the maximal deviation of the given`<xaip:submissionTime>`<br>and the current time.|
|8|All|Do configure the supported hash algorithms by checking and adjusting (as needed) the<br>properties {SHA1, SHA224, SHA256, SHA384, SHA512, SHA3-224, SHA3-256, SHA3-384,<br>SHA3-512}_SUPPORTED (enabled = YES, disabled - NO).|
|9|All|Do configure the acceptable hash algorithms for hash tree verification in the evidence records<br>by checking and adjusting (as needed) the properties {SHA1, SHA224, SHA256, SHA384,<br>SHA512, SHA3-224, SHA3-256, SHA3-384, SHA3-512}_TREE_ACCEPTABLE (enabled = YES,<br>disabled = NO).|
|10|All|Do<br>configure<br>an<br>inactive<br>profile<br>in<br>the<br>TOT<br>and<br>set<br>the<br>value<br>of<br>the<br>URI_PROFILE_V1.3_S.4_V1.0-inactive property as the corresponding profile id.|
|11|All|Do define the support of LXAIP by proper setting the value of property CONFIG_LXAIP<br>(possible values are ENABLED or DISABLED).|
|12|All|Do define the not existed AOIDs for the XAIP test cases by setting a value of AOID-03 and<br>AOID-06 (if TR-s.4 is supported) or AOID-03b and AOID-06b (if TR-S.512 is supported)<br>properties.|
|13|All|Do submit XAIP in order to have the belonging retention period expired at the time of test<br>execution and document the corresponding AOID and VersionID in properties:<br>•<br>if TR-S.4 is supported: in the properties AOID-00 and AOID-00.V01<br>•<br>if TR-S.512 is supported: in theproperties AOID-00b and AOID-00b.V1|
|14|LXAIP|Do check and adjust (as needed) the location for the referenced data objects for XSVT,<br>property XSV_LXAIP_DIR_URI (a valid directory path).|
|15|LXAIP|Do check and adjust (as needed) the location for the referenced data objects for ERVT,<br>property ERVT_LXAIP_DIR_URI (a valid directory path).|
|16|LXAIP|Do copy all the files from directory XSVT-UPLOADs into the location specified in step 14.|
|17|LXAIP|Do copy all the files from directory ERVT-UPLOADs into the location specified in step 15.|
|18|LXAIP|Do submit an LXAIP in order to have the belonging retention period expired at the time of<br>test execution and document the corresponding AOID and Version ID in properties:<br>•<br>if TR-S.4 is supported: in the properties AOID-00a and AOID-00a.V01<br>•<br>if TR-S.512 is supported: in theproperties AOID-00ab and AOID-00ab.V1|



Federal Office for Information Security 

218 

TR-ESOR-C.2-Testbed how-to 

|#|Container|<br>Action|
|---|---|---|
|19|LXAIP|Do upload all the files from LXAIP-UPLOADs directory into TOE by using the<br>Upload/Download-Interface and document the given references in the corresponding<br>property in the props-file.<br>•<br>Example: Uploading of PDF_DATA_50.pdf file did produce uuid:1122-2343-5634-4545 as<br>reference. Set the test value of REF_PDF_DATA_50 property to uuid:1122-2343-5634-<br>4545.|
|20|All|Do generate the property file used by the SoapUI-<br>rate SoapUI<br>TR-C2-Soap-UI-List-of-Project-<br>Properties.xlsm (cf. chapter 4.2.4).<br>•<br>Do provide the path and name of the SoapUI-Project property file and confirm the<br>export.|



Table 3: TR-ESOR-C.2-Testbed list of steps to be done during configuration. 

## 4.4 TR-ESOR-C.2-Testbed: configuration and start of XSVT and ERVT 

Following steps have to be performed in order to create the necessary docker images and containers: 

S.1 Change into DOCKERS directory 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0219-06.png)


Notice : The following usage of scripts means the script 

S.2 Call the script `dbuild.cmd` / `dbuild.sh` the necessary docker images will be built: 

`o` alpine-j11:1.0.0 foundation for further images, `o` xsv-srv:1.0.0 the image for XSVT `o` erv-srv:1.0.0 the image for ERVT 

and following or similar output will be displayed: 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0219-11.png)


Figure 5: Example output of dbuild.cmd/dbuild.sh. 

- S.3 Call the script `drun.cmd` / `drun.sh` the both necessary containers will be created and started: 

   - xsv-srv container built on base of xsv-srv:1.0.0 docker image, will host the running XSVT, 

   - `o` erv-srv container built on base of erv-srv:1.0.0 docker image, will host the running ERVT. 

Please notice, that this task will take some time, because the both tools will be built from the sources obtained from the official BSI repository on the GitHub (cf. https://github.com/de-bund-bsi-tr-esor). 

Only Windows : In order to monitor the progress, two extra shell windows will start up automatically, which have assigned following titles: 

- xsv-srv log progress of XSVT in xsv-srv container, 

- erv-srv log progress of ERVT in erv-srv container. 

The creation and initialization of the xsv-srv is finished as soon as following statement will be displayed in xsv-srv log window: 

Federal Office for Information Security 

219 

TR-ESOR-C.2-Testbed how-to 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0220-01.png)


Figure 6: Final statement of initialization of XSVT. 

The creation and initialization of the erv-srv is finished as soon as following statement will be displayed in erv-srv log window: 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0220-04.png)


Figure 7: Final statement of initialization of ERVT. 

The both Tools are up and running. 

Notice : The both log windows can be closed at any time. 

Linux/Apple : A log output of the erv-srv docker container will be displayed in the terminal. As soon as the statement depicted in the Figure 7 will appear, the erv-srv ist up and running. In order to check the - status of the xsv- 

statement depicted in the Figure 6 does appear, the xsv-srv docker container is up and running. 

- S.4 In order to access the both test tools by using the hostnames xsv-srv and erv-srv the following files have to be adjusted: 

`o` Windows: c:\Windows\System32\drivers\etc\hosts `o` Linux/Apple: /etc/hosts. 

Please edit the above-named file as administrator/root and insert following line: 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0220-13.png)


`o` xsv-srv erv- 

The availability of the both test tools could be tested by inserting following URLs in your browser: 

- xsv-srv: 

   - http://xsv-srv:19090/xaip-validate?wsdl or 

   - http://localhost:19090/xaip-validate?wsdl, 

- erv-srv: 

   - http://erv-srv:9090/ErVerifyTool/esor13/exec?wsdl, or 

   - http://localhost:9090/ErVerifyTool/esor13/exec?wsdl. 

the output should be the underlying WSDL. 

There are some more scripts, which could be used to control the both test tools: 

- `dstop.cmd` / `dstop.sh` by using this script the both running containers of test tools XSVT and ERVT can be stopped, 

- `dstatus.cmd` / `dstatus.sh` execution of this script will display current status of known docker containers and images, below a sample output of the script, 

Federal Office for Information Security 

220 

TR-ESOR-C.2-Testbed how-to 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0221-01.png)


Figure 8: Sample output of dstatus.cmd/dstatus.sh 

- `dstart.cmd` / `dstart.sh` (re)starts the both docker containers. 

Notice : This script can only be used after the containers have been successfully created with the script `drun.cmd` / `drun.sh` . 

Below a sample of output of the script: 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0221-06.png)


Figure 9: Sample output of dstart.cmd/dstart.sh. 

- `dclean-container.cmd` / `dclean-container.sh` removes the both docker containers (the containers have to stopped in advance). The containers can be recreated by using the script `drun.cmd` / `drun.sh` . 

- `dclean-all.cmd` / `dclean-all.sh` removes the both docker containers (the containers have to be stopped in advance) and the three docker images (only if the containers have been removed successfully). The images can be recreated by using the script `dbuild.cmd` / `dbuild.sh` . 

## 4.5 TR-ESOR-C.2-Testbed usage 

Following Table 4 describes the action steps to be done in order to perform the test cases. 

- # Action 

- 1 Do start SoapUI application (cf. chapter 4.1) • Notice : The provided C.2-Testbed project (cf. chapter 4.2.8) has been created with the open source version of the SoapUI tool and hasn't been tested with the commercial version "ReadyAPI" of the software. 

- 2 Do load the SoapUI project into the started SoapUI tool: 

   - a) Do chose "File->Import Project" or use the shortcut "STRG+I" 

   - b) Do chose the file TR-ESOR-1.3.0-C2-Testbed-soapui-project.xml (cf. chapter 4.2.8) from the root directory of this project and press the "Open" button. The Project with name TR-C2-1.3-u2 will appear in the "Navigator" panel of SoapUI. The project consists of 15 test suites with 122 test cases in total. 

- 3 Do set up the necessary security settings for the sommuniaction between C2-Testbed and TOT. Please consult the SoapUI documentation for further advice, how to do that. 

Federal Office for Information Security 

221 

TR-ESOR-C.2-Testbed how-to 

Action 

- # 

- 4 Do load the generated SoapUI project property file: 

   - a) Do double click on the TR-C2-1.3-u2 project in the "Navigator" panel. 

   - b) Do make sure, the "Overview" tab at the top and the "Properties" tab at the bottom of the project configuration dialog are activated. 

   - c) Do click the next-to-last icon in the icon bar of the "Properties" tab -> the "Load Properties"-Dialog will appear. 

   - d) Do browse to the generated SoapUI project property file, as result of step 20 in the Table 3 and do activate both checkboxes Creates Missing Properties as well as Deletes properties not in file . 

   - e) Do press "OK" button 

- 5 Do execute the test suites. 

   - Notice : depending of your test strategy you can try to perform all the tests at once, doing it suite by suite, execute them test case by test case or even execute the single steps in the particular test cases manually. It is important to keep the execution, which is top-down, beginning by chapter 3.4.1.1 and ending by chapter 3.4.1.8, to preserve the interdependencies of the particular test cases. 

   - Notice : In order to create the final documentation of the achieved test results please refer to the following chapter 4.6. This documentation shall be created and presented to the BSI in parts or as a whole, if required. 

Table 4: TR-ESOR-C.2-Testbed list of steps to be performed during the test execution. 

## 4.6 TR-ESOR-C.2-Testbed final documentation 

In order to create a sufficient documentation of the execution and the results of the relevant test cases following steps have to be performed. 

Please notice , it is recommended to execute those steps as a final task, after it has been made sure, the relevant test cases will deliver positive results. In the preparation phase, it is more comfortable to use the graphical interface of SoapUI tool. 

It is assumed, that the steps defined in sections 4.1, 4.3, 4.4 and 4.5 have been positive finished. 

- # Action 

- 0 Please take care to have an environment variable `JAVA_HOME` properly set. It requires at least a version 1.8 of Java. The given test environment has been tested with Java version 17. 

- 1 Do change to directory `RUN-DATA/bin` and edit the file: `env.cmd[39]` or `env[40]` . Check and set the following variables: 

   - a) `SOAPUI_HOME` shall contain the path pointing to the SoapUI installation folder. 

After that has been done, call the script `clean-all.cmd` or `clean-all.sh[41]` . This will take care of all the potentially remained results. 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0222-20.png)


> 39 `cmd` 40 In case of using Linux or Apple. 

> 41 `sh` 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0222-22.png)


Federal Office for Information Security 

222 

TR-ESOR-C.2-Testbed how-to 

# 

Action 

- 2 Do execute the script `run-all-tests.cmd` or `run-all-tests.sh` . It will start the execution of one test case after another, according to the configuration stored in the subfolder `data[42]` . The configuration has been made in the section 4.3 will control the execution flow and skip the not supported testcases. 

At the beginning, there will be created two folders: 

- a) `RUN-TEST/TEST-RUN-EVALUATION` this folder will contain all evaluation reports of the tests execution in form of kind of summary as depicted in the following Figure 10. It allows to gain a rapid overview if a given test case has been executed or skipped and which result has it produced. 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0223-06.png)


Figure 10: Example of evaluation summary for test case M-RI-01. 

For every existing test suite will be created a separate folder, which contains the summaries of the particular test cases, e.g.: `RUN-TEST/TEST-RUN-EVALUATION/3.4.1.1-S4-RetrieveInfoTestSuite/M-RI-01/M-RI-01-Evaluation.txt` 

b) `RUN-TEST/TEST-RUN-REPORTS` this folder contains the execution documentation incl. the corresponding requests and responses. For every test case will be created a separate folder, e.g. for M-RI-01: `RUN-DATA\TEST-RUN-REPORTS\REPORTS\3.4.1.1-S4-RetrieveInfo-TestSuite\M-RI01` . The directory does contain a detailed execution report for every step of the particular test case. For M-RI-01 it would be: 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0223-10.png)


Figure 11: Example of a reports folder for test case M-RI-01. 

During the test execution, there is a user interaction necessary at some steps. E.g. M-SU-01 request the permission to continue after the evidence records creation process in TOE has been successfully initiated and finished (c.f. following Figure 12): 


![](markdown/tr/BSI_TR_03125_Anlage_C2_V1_3/BSI_TR_03125_Anlage_C2_V1_3.pdf-0223-13.png)


Figure 12: Example of the user interaction dialog while executing the test cases. 

- 42 Please do not make any changes on this configuration. 

Federal Office for Information Security 

223 

TR-ESOR-C.2-Testbed how-to 

|#|Action|
|---|---|
|3|In case an execution of a one test case has to be repeated, it can be done by executing the script run-<br>chosen-test.cmd or run-chosen-test.sh, e.g. for repeating the test case M-RI-01 please call:<br>•<br>`run-chosen-test.cmd -TS 3.4.1.1-S4-RetrieveInfo-TestSuite -TC M-RI-01`, or<br>•<br>`run-chosen-test.sh -TS 3.4.1.1-S4-RetrieveInfo-TestSuite -TC M-RI-01`.<br>Pleasenotice, the potentially already existing results will be overwritten!|
|4.|Please preserve the whole content of the following artefacts as a documentation:<br>a) SoapUI-configuration used (c.f. section 4.3)<br>b) The whole content of the folder:`RUN-TEST/TEST-RUN-EVALUATION`<br>c) The whole content of the folder:`RUN-TEST/TEST-RUN-REPORTS`|



## 4.7 TR-ESOR-C.2-Testbed results 

In order to get the [TR-ESOR-C.2] passed, following tests have to be performed successfully: 

1. In case the TOT does support TR-S.4 -interface, all tests specified in the chapters 3.4.1.1 - 3.4.1.8 which M-SU-01 or M-DE-02 etc. 

2. In case the TOT does support the additional S.512 -interface, all tests specified in the chapters 3.4.2.1 - 3.4.2.7 M-SU-01b or M-DE-02b. 

3. In case the TOT does support LXAIP container and TR-S.4 -interface, all tests specified in chapters 3.4.1.1 - 3.4.1.8 which id does end w M-DE-01a or M-SU-06a. 

4. In case the TOT does support LXAIP container and TR-S.512 -interface, all tests specified in chapters 3.4.2.1 - 3.4.2.7 M-SU-01ab or M-DE-02ab. 

The final documentation shall be preserved as a confirmation of the certification test cases have been performed and shall be presented to the BSI, if required. 

In order to protected the integrity of the documentation, it is recommended to (at least) timestamp the documentation. 

Federal Office for Information Security 

224 


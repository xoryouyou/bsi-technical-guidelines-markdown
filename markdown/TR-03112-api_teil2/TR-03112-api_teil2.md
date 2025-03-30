![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_2.jpeg)

# Technical Guideline TR-03112-2 eCard-API-Framework – eCard-Interface Version 1.1.5

7. April 2015

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn

E-Mail: ecard.api@bsi.bund.de Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2015

| 1              | Overview of the eCard-API-Framework4  |  |
|----------------|---------------------------------------|--|
| 1.1            | Key Words4                            |  |
| 1.2            | XML-Schema5                           |  |
| 2              | Overview of the eCard-Interface6      |  |
| 2.1            | Objective6                            |  |
| 2.2            | Functions6                            |  |
| 2.2.1          | Functions for identity management6    |  |
| 2.2.2          | Signature functions6                  |  |
| 2.2.3          | Encryption functions7                 |  |
|                |                                       |  |
| 3              | Specification of the eCard-Interface8 |  |
| 3.1            | Functions for identity management8    |  |
| 3.1.1          | GetCertificate8                       |  |
| 3.2            | Signature functions9                  |  |
| 3.2.1          | SignRequest9                          |  |
| 3.2.2          | VerifyRequest22                       |  |
| 3.2.3          | ShowViewer32                          |  |
| 3.3            | Encryption functions35                |  |
| 3.3.1<br>3.3.2 | EncryptRequest35<br>DecryptRequest43  |  |

# <span id="page-3-0"></span>**1 Overview of the eCard-API-Framework**

The objective of the eCard-API-Framework is the provision of a simple and homogeneous interface to enable standardised use of the various smart cards (eCards) for different applications.

The eCard-API-Framework is sub-divided into the following layers:

- **•** Application-Layer
- **•** Identity-Layer
- **•** Service-Access-Layer
- **•** Terminal-Layer

The **Application-Layer** contains the various applications which use the eCard-API-Framework to access the eCards and their associated functions. Application-specific "convenience interfaces", in which the recurring invocation sequences may be encapsulated in application-specific calls, may also exist in this layer. However, these interfaces are currently *not* within the scope of the e-Card-API-framework.

The **Identity-Layer** comprises the eCard-Interface and the Management interface, and therefore functions for the use and management of electronic identities as well as for management of the eCard-API-Framework.

The *eCard-Interface* (refer to [TR-03112-2]) allows to request certificates as well as the encryption, signature and time-stamping of documents.

In the M*anagement-Interface* (refer to [TR-03112-3]), functions for updating the framework and the management of trusted identities, smart cards, card terminals, and default behaviour are available.

The **Service-Access-Layer** provides, in particular, functions for cryptographic primitives and biometric mechanisms in connection with cryptographic tokens, and comprises the ISO24727-3-Interface and the Support-Interface.

The *ISO24727-3-Interface* defined in the present document is a webservice-based implementation of the standard of the same name [ISO24727-3]. This interface contains functions to establish (cryptographically protected) connections to smart cards, to manage card applications, to read or write data, to perform cryptographic operations and to manage the respective key material (in the form of so-called "differential identities"). In the process, all functions which use or manage "differential identities" are parameterised by means of protocol-specific object identifiers so that the different protocols which are defined in the present document MAY be used with a standardised interface (refer to [TR-03112-7]).

The S*upport-Interface* (refer to [TR-03112-5]) contains a range of supporting functions.

The **Terminal-Layer** primarily contains the *IFD-Interface* (refer to [TR-03112-6]). This layer takes over the generalisation of specific card terminal types and various interfaces as well as communication with the smart card. For the user it is unimportant whether the card is addressed by PC/SC, a SICCT terminal or a proprietary interface, or whether it has contacts or is contact-less.

# **1.1 Key Words**

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC2119]. The key word "CONDITIONAL" is to be interpreted as follows:

CONDITIONAL: The usage of an item is dependent on the usage of other items. It is therefore further qualified under which conditions the item is REQUIRED or RECOMMENDED.

## **1.2 XML-Schema**

A XML-Schema is provided together with this Technical Guideline. In case of incongruencies, the specifications in this text take precedence. The graphical representations of the XML-Schema illustrate the schema. Note that the text of this Guideline might further restrict the presence or mulitplicity of elements as compared to the schema definition.

# <span id="page-5-0"></span>**2 Overview of the eCard-Interface**

# **2.1 Objective**

The eCard-Interface encapsulates important document related functions of the eCard-API-Framework in an application-orientated manner.

### **2.2 Functions**

The eCard-Interface encapsulates the main functions of the eCard-API-Framework in an application-orientated manner. For this purpose the eCard-Interface provides the following function groups:

- **•** Functions for identity management
- **•** Signature functions
- **•** Encryption functions

With the GetCertificate function, certificate applications can be transferred to a certification authority, from where they obtain their certificates.

In addition, the invocations specified by [DSS] can be used for the creation and verification of (qualified) electronic signatures in the formats according to [RFC3275] and [RFC3369], as well as the corresponding extensions from ETSI. This functional group also contains an interface to a trustworthy display component which can be used in particular for the displaying the data and test results requiring a signature.

Finally, with the encryption functions documents can be easily encrypted and decrypted in accordance with [RFC3369] and [XMLEnc] by simple function invocations.

#### **2.2.1 Functions for identity management**

**•** With the GetCertificate function, certificate applications can be transferred to a certification authority, from which certificates are obtained.

### **2.2.2 Signature functions**

- **•** The SignRequest function conforms with [DSS], and related profiles and permits the creation of (qualified) electronic signatures in popular high-level formats such as XML-DSig in accordance with [RFC3275], or cryptographic message syntax in accordance with [RFC3369]. These signatures may also contain time stamps, which can also be requested separately with this function.
- **•** The VerifyRequest function conforms with [DSS] and related profiles and enables verification of signed objects (e.g. signatures, time stamps, certificates, blacklists).
- **•** Th ShowViewer function enables display of documents in a trustworthy manner, which can be used for the creation and verification of signatures.

### **2.2.3 Encryption functions**

- **•** The EncryptRequest function enables encryption of data in accordance with [XMLEnc] or [RFC3369].
- **•** The DecryptRequest function enables decryption of data encrypted in accordance with [XMLEnc] or [RFC3369].

# <span id="page-7-0"></span>**3 Specification of the eCard-Interface**

# **3.1 Functions for identity management**

### **3.1.1 GetCertificate**

| Name                     | GetCertificate                                                                                                                                                                                  |                                                                                              |                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description              | The GetCertificate function is used to request and obtain certificates. A<br>wide range of protocols can be used for this purpose. Please refer to [TR-03112-7]<br>for protocol specifications. |                                                                                              |                                                                                                                                                                                                                                                                                                                                                                  |
| Invocation<br>parameters | Invocation of the GetCertificate function.                                                                                                                                                      |                                                                                              |                                                                                                                                                                                                                                                                                                                                                                  |
|                          | Name                                                                                                                                                                                            | Description                                                                                  |                                                                                                                                                                                                                                                                                                                                                                  |
|                          | Input                                                                                                                                                                                           | <complexContent><br>use="required" /><br></extension><br></complexContent><br></complexType> | Contains the protocol's input parameters and is of the abstract<br>ProtocolDataType, which is defined as follows:<br><complexType name="ProtocolDataType" abstract="true"><br><extension base="anyType"><br><attribute name="Protocol" type="anyURI"<br>The input format depends on the protocol used for certificate<br>enquiries (also refer to [TR-03112-7]). |
| Return                   |                                                                                                                                                                                                 | Return of the CardUpdate function.                                                           |                                                                                                                                                                                                                                                                                                                                                                  |
|                          | Name                                                                                                                                                                                            |                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                      |
|                          | dss:Result                                                                                                                                                                                      |                                                                                              | Contains the status information and the errors of an<br>executed action. This element is described in more<br>detail below.                                                                                                                                                                                                                                      |

|                     | Output                                                                                                  | Contains the protocol's output parameters and is of<br>the abstract ProtocolDataType (see above).         |  |
|---------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|--|
|                     |                                                                                                         | The output format depends on the protocol used for<br>certificate enquiries (also refer to [TR-03112-7]). |  |
|                     | Status information and errors with GetCertificate (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2). |                                                                                                           |  |
| Name<br>Error codes |                                                                                                         |                                                                                                           |  |
| ResultMajor         |                                                                                                         | •<br>/resultmajor#ok                                                                                      |  |
|                     |                                                                                                         | •<br>/resultmajor#error                                                                                   |  |
|                     |                                                                                                         | •<br>/resultmajor#warning                                                                                 |  |
|                     | ResultMinor                                                                                             | •<br>/resultminor/al/common#noPermission                                                                  |  |
|                     |                                                                                                         | •<br>/resultminor/al/common#internalError                                                                 |  |
|                     |                                                                                                         | •<br>/resultminor/al/common#parameterError                                                                |  |
|                     |                                                                                                         | In addition, other specific protocol error messages MAY<br>exist.                                         |  |
|                     | ResultMessage                                                                                           | MAY contain more detailed information on the occurred<br>error if required.                               |  |
| Precondition        |                                                                                                         |                                                                                                           |  |
| Postcondition       |                                                                                                         |                                                                                                           |  |
| Note                |                                                                                                         |                                                                                                           |  |

# **3.2 Signature functions**

### **3.2.1 SignRequest**

| Name        | SignRequest                                                                                                                                                                                    |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | The SignRequest function conforms largely1<br>with [DSS], [AdES], [SigGer]<br>and [SigPol] and serves to create (qualified) electronic signatures or time<br>stamps for transmitted documents. |

<span id="page-8-0"></span><sup>1</sup> Deviations are due to the resolution of restrictions which seem to be unnecessary. For example, according to [DSS] (refer to section 3.2) only one dss:SignatureObject may be returned and the return of dss:Timestamp elements is not permitted in accordance with [AdES] (refer to section 3.4.1.2). The necessity of these restrictions is currently being discussed in the OASIS DSS-X working group.

<span id="page-9-0"></span>![](_page_9_Figure_0.jpeg)

![](_page_10_Figure_0.jpeg)

<span id="page-11-1"></span><span id="page-11-0"></span>![](_page_11_Figure_0.jpeg)

| The SignatureForm-element MAY appear in dss:OptionalInputs<br>and is defined and explained in [AdES].                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| If the SignatureType–element defined below is urn:ietf:rfc:3275<br>or<br>urn:ietf:rfc:3369 the SignatureForm-element, can be used to specify more<br>precisely which form of the advanced electronic signature is to be generated<br>according to [XAdES] or [TS101733] for XML and CMS signatures. With<br>other SignatureTypes a warning<br>/resultminor/il/signature#signatureTypeDoesNotSupportSignatureFormClarific<br>ationWarning is returned. |
| The URI specified in Section 7.1 of [AdES] MUST be used for specification of<br>the SignatureForm. Other URIs produce an error message<br>/resultminor/il/signature#unknownSignatureForm.                                                                                                                                                                                                                                                             |

| The SignatureType-element MAY appear in dss:OptionalInputs<br>and is defined in [DSS].                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As explained in [DSS] (Section 3.5.1) it is used to specify the type of signature<br>or time stamp, which is to be created. The following types of signatures and<br>time stamps are supported:                                                                                                                                                                                                                                 |
| 1. Signature types                                                                                                                                                                                                                                                                                                                                                                                                              |
| •<br>XML signature. If the URI urn:ietf:rfc:3275 is transmitted, the<br>generation of an XML signature is initiated in accordance with<br>[RFC3275] (or in connection with the SignatureForm described<br>above in accordance with [XAdES]). Such a signature is returned as a<br>ds:Signature element.                                                                                                                         |
| •<br>CMS signature. If the URI urn:ietf:rfc:3369 is transmitted, a CMS<br>signature according to [RFC3369] (or in connection with the<br>SignatureForm described above in accordance with [TS101733]) is<br>requested, whereby the signature is returned as a<br>dss:Base64Signature with the URI stated above as Type.                                                                                                         |
| •<br>PDF signature. If the URI http://ns.adobe.com/pdf is transmitted, an<br>integrated PDF signature is initiated in accordance with [PDF],<br>whereby the signature is returned as dss:Base64Signature with<br>the URI stated above as Type. If the transmitted document is not a<br>Base64Data element with MIME type "application/pdf", an error<br>/resultminor/il/signature#PDFSignatureForNonPDFDocument is<br>returned. |
| 2. Time stamp types                                                                                                                                                                                                                                                                                                                                                                                                             |
| All time stamps are returned as a dss:Timestamp element in accordance<br>with [DSS] Section 5.1, whereby the eCard-API-Framework creates the<br>requested time stamp itself or MAY use an external time stamping service<br>depending on the default configuration (also refer to [TR-03112-3]). In this<br>context, it is necessary to distinguish between the following cases:                                                |
| •<br>RFC3161 time stamp. If the URI urn:ietf:rfc:3161 is transmitted, the<br>creation of a time stamp for each transmitted document is initiated in<br>accordance with [RFC3161] and returned in the child element<br>RFC3161TimeStampToken of Timestamp.                                                                                                                                                                       |
| •<br>XML time stamp. If the URI<br>urn:oasis:names:tc:dss:1.0:core:schema:XMLTimeStampToken is<br>transmitted, the creation of an XML-based time stamp according to<br>[DSS] Section 5.1.1 is initiated and the time stamp is returned as a<br>ds:Signature element.                                                                                                                                                            |

![](_page_14_Figure_0.jpeg)

![](_page_15_Figure_0.jpeg)

![](_page_16_Figure_0.jpeg)

![](_page_17_Figure_0.jpeg)

![](_page_18_Figure_0.jpeg)

| Status information and errors with SignResponse (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2). |                           |
|-------------------------------------------------------------------------------------------------------|---------------------------|
| Name                                                                                                  | Error code                |
| ResultMajor                                                                                           | •<br>/resultmajor#ok      |
|                                                                                                       | •<br>/resultmajor#error   |
|                                                                                                       | •<br>/resultmajor#warning |

| ResultMinor                                         | •<br>/resultminor/al/common#noPermission                                                        |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------|
|                                                     | •<br>/resultminor/al/common#internalError                                                       |
|                                                     | •<br>/resultminor/al/common#parameterError                                                      |
|                                                     | •<br>/resultminor/dp#unknownChannelHandle                                                       |
|                                                     | •<br>/resultminor/dp#communicationError                                                         |
|                                                     | •<br>/resultminor/dp#<br>trustedChannelEstablishmentFailed                                      |
|                                                     | •<br>/resultminor/dp#unknownProtocol                                                            |
|                                                     | •<br>/resultminor/dp#unknownWebserviceBinding                                                   |
|                                                     | •<br>/resultminor/sal#unknownDIDName                                                            |
|                                                     | •<br>/resultminor/sal#unknownDataSetName                                                        |
|                                                     | •<br>/resultminor/sal#unknownDSIName                                                            |
|                                                     | •<br>/resultminor/il/signature#<br>signatureFormatNotSupported                                  |
|                                                     | •<br>/resultminor/il/signature#<br>PDFSignatureForNonPDFDocument                                |
|                                                     | •<br>/resultminor/il/signature#<br>unableToIncludeEContent                                      |
|                                                     | •<br>/resultminor/il/signature#<br>ignoredSignaturePlacementFlag                                |
|                                                     | •<br>/resultminor/il/signature#certificateNotFound                                              |
|                                                     | •<br>/resultminor/il/service#<br>timeStampServiceUnreachable                                    |
|                                                     | •<br>/resultminor/il/signature#<br>resolutionOfObjectReferenceImpossible                        |
|                                                     | •<br>/resultminor/il/signature#<br>transformationAlgorithmNotSupported                          |
|                                                     | •<br>/resultminor/il/signature#unknownViewer                                                    |
|                                                     | •<br>/resultminor/il/signature#signatureTypeDoes<br>NotSupportSignatureFormClarificationWarning |
|                                                     | •<br>/resultminor/il/signature#<br>unknownSignatureForm                                         |
|                                                     | •<br>/resultminor/il/signature#includeObjectOnly<br>ForXMLSignatureAllowedWarning               |
|                                                     | •<br>/resultminor/il/algorithm#<br>hashAlgorithmNotSupported                                    |
|                                                     | •<br>/resultminor/il/signature#<br>hashAlgorithmNotSuitable                                     |
|                                                     | •<br>/resultminor/il/algorithm#<br>signatureAlgorithmNotSupported                               |
|                                                     | •<br>/resultminor/il/signature#signatureAlgorithm<br>NotSuitable                                |
|                                                     |                                                                                                 |
| Bundesamt für Sicherheit in der Informationstechnik |                                                                                                 |

|               | ResultMessage                                                                                                                                                                                                                                                                                                                          | MAY contain more detailed information on the error<br>that occurred if required.                                                                                                                                                                                                                       |  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Precondition  | to [TR-03112-4]).                                                                                                                                                                                                                                                                                                                      | The ConnectionHandle MAY address a linked card application or a<br>signature service. In the first case, the respective DID and a corresponding<br>authorisation for use of the key MUST be provided or be obtainable by<br>implicitly initiated authentication steps with DIDAuthenticate (also refer |  |
| Postcondition |                                                                                                                                                                                                                                                                                                                                        | Signatures or time stamps are created for the transmitted documents in<br>accordance with the transmitted child elements of dss:OptionalInputs<br>and returned in dss:SignatureObject or<br>dss:DocumentWithSignature elements.                                                                        |  |
| Note          | The SignRequest function invokes the functions Sign, Hash and, if<br>applicable (for reading the certificates to be included in the signatures)<br>DataSetSelect and DSIRead (also refer to [ISO24727-3] and<br>[TR-03112-4]) and, if required, the ShowViewer function (refer to Section<br>3.2.3).                                   |                                                                                                                                                                                                                                                                                                        |  |
|               | Note that the eCard-API-Framework MUST return a warning message (…<br>{hash/signature}AlgorithmNotSuitable), if the applied<br>algorithms do not fulfil the requirements for qualified electronic signatures as<br>defined by the BSI (Federal Office for Information Security) and the<br>Bundesnetzagentur (Federal Network Agency). |                                                                                                                                                                                                                                                                                                        |  |

### **3.2.2 VerifyRequest**

| Name        | VerifyRequest                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | The VerifyRequest function is used to verify signed objects (signatures,<br>time stamps, certificates, etc.). In some circumstances, a number of different<br>verification operations must be performed. Depending on the transmitted<br>dss:OptionalInputs or the configured default VerifyOptions<br>(refer to [TR-03112-3]) the results of these individual verification steps MAY<br>be returned. |

<span id="page-22-0"></span>![](_page_22_Figure_0.jpeg)

| dss:InputDocuments<br>MAY contain the documents required for<br>verification of the signatures or time stamps<br>if the respective documents are not part of<br>the signatures transmitted in<br>dss:SignatureObject.                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This element MAY also contain<br>XML-signatures according to [RFC3275]<br>wrapped in a dss:Document-element with<br>a child element dss:Base64XML- or<br>dss:EscapedXML.                                                                                                        |
| In this case there MUST be a corresponding<br>dss:SignaturePtr-element which<br>indicates the presence of such an<br>XML-signature. This option is necessary to<br>avoid verification failures due to namespace<br>rewriting (please refer to the note on page 39<br>of [DSS]). |
| Details on the<br>dss:InputDocuments-element can be<br>found in Section 2.4 of [DSS].                                                                                                                                                                                           |

<span id="page-24-1"></span>

| dss:SignatureObject2 | Contains the signed object which is to be<br>verified. The following signed objects<br>MUST be supported:                                                                                                                                                                                               |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | •<br>XML-based signatures according to<br>[RFC3275] (and possibly [XAdES])<br>indicated by a<br>dss:SignaturePointer-eleme<br>nt, which points to a<br>ds:Signature-element wrapped<br>in a dss:Base64XML- or<br>dss:EscapedXML-element inside<br>the<br>dss:InputDocuments-element<br>specified above, |
|                      | •<br>a time stamp according to<br>[RFC3161] or [DSS] (Section 5.1.1)<br>in a single<br>dss:Timestamp-element,                                                                                                                                                                                           |
|                      | •<br>CMS-based signatures according to<br>[RFC3369] (and possibly<br>[TS101733]) in the<br>dss:Base64Signature-element<br>,                                                                                                                                                                             |
|                      | •<br>Certificates (e.g. according to<br>[RFC3280] or [RFC3281]) in a<br>child-element<br>CertificateValues (cf.<br>[XAdES]) of the Other-element,                                                                                                                                                       |
|                      | •<br>OCSP-Responses according to<br>[RFC2560] and CRLs according to<br>[RFC3280] in a child-element<br>RevocationValues (cf.<br>[XAdES]) of the Other-element,                                                                                                                                          |
|                      | •<br>an Evidence Record according to<br>[RFC4998] or [RFC6283] in a<br>child-element EvidenceRecord<br>(see below) of the Other-element,<br>which protects the content of all<br>dss:Document-elements provided<br>in the<br>dss:InputDocuments-element<br>above.                                       |

<span id="page-24-0"></span><sup>2</sup> Note that unlike in the VerifyRequest specified in [DSS] the dss:SignatureObject-element MAY in case of non-detached signatures, certificates or OCSP-responses appear multiple times here such that it is possible to verify a batch of signed objects with a single request. For the verification of a detached signature, a time-stamp or an evidence record there MUST exactly be one dss:SignatureObject or an error (/resultminor/al/common#parameterError) is returned.

<span id="page-25-0"></span>![](_page_25_Figure_0.jpeg)

<span id="page-26-0"></span>![](_page_26_Figure_0.jpeg)

<span id="page-27-0"></span>![](_page_27_Figure_0.jpeg)

![](_page_28_Figure_0.jpeg)

![](_page_29_Figure_0.jpeg)

| ResultMinor | •<br>/resultminor/al/common#noPermission                                 |
|-------------|--------------------------------------------------------------------------|
|             | •<br>/resultminor/al/common#internalError                                |
|             | •<br>/resultminor/al/common#parameterError                               |
|             | •<br>/resultminor/dp#communicationError                                  |
|             | •<br>/resultminor/il/signature#<br>certificateNotFound                   |
|             | •<br>/resultminor/il/signature#<br>certificateFormatNotCorrect           |
|             | •<br>/resultminor/il/signature#<br>invalidCertificateReference           |
|             | •<br>/resultminor/il/signature#<br>certificateChainInterrupted           |
|             | •<br>/resultminor/il/signature#<br>resolutionOfObjectReferenceImpossible |
|             | •<br>/resultminor/il/signature#<br>transformationAlgorithmNotSupported   |
|             | •<br>/resultminor/il/signature#unknownViewer                             |
|             | •<br>/resultminor/il/signature#<br>certificatePathNotValidated           |
|             | •<br>/resultminor/il/signature#<br>certificateStatusNotChecked           |
|             | •<br>/resultminor/il/signature#<br>signatureManifestNotCheckedWarning    |
|             | •<br>/resultminor/il/signature#<br>suitabilityOfAlgorithmsNotChecked     |
|             | •<br>/resultminor/il/signature#<br>detachedSignatureWithoutEContent      |
|             | •<br>/resultminor/il/signature#<br>improperRevocationInformation         |
|             | •<br>/resultminor/il/signature#<br>SignatureManifestNotCorrect           |
|             | •<br>/resultminor/il/algorithm#<br>hashAlgorithmNotSupported             |
|             | •<br>/resultminor/il/algorithm#<br>signatureAlgorithmNotSupported        |
|             | •<br>/resultminor/il/signature#<br>signatureAlgorithmNotSuitable         |
|             | •<br>/resultminor/il/signature#<br>hashAlgorithmNotSuitable              |
|             | •<br>/resultminor/il/signature#<br>wrongMessageDigest                    |
|             | •<br>/resultminor/sal#invalidSignature                                   |

|               | ResultMessage                                                                                                                                                                                                                                                                                                                                        | MAY contain more detailed information on the<br>occurred error if required. |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Precondition  |                                                                                                                                                                                                                                                                                                                                                      |                                                                             |
| Postcondition | The signed objects transmitted in VerifyRequest are verified in<br>accordance to the provided dss:OptionalInputs-element.                                                                                                                                                                                                                            |                                                                             |
| Note          | Note that the eCard-API-Framework MUST return a warning message (…<br>{hash/signature}AlgorithmNotSuitable), if the algorithms used<br>in the signature do not fulfil the requirements for qualified electronic<br>signatures as defined by the BSI (Federal Office for Information Security)<br>and the Bundesnetzagentur (Federal Network Agency). |                                                                             |

### <span id="page-31-0"></span>**3.2.3 ShowViewer**

| Name                     | ShowViewer                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| Description              | With the ShowViewer function, documents (refer to [DSS], Section 2.4.2),<br>signed objects (refer to dss:SignatureObject on page 25) or corresponding<br>verification results in form of a VerificationReport element according to<br>[SigVer] MAY be displayed in a trustworthy manner. This functionality MAY, for<br>example, be used in SignRequest (for displaying the signed data) or in the<br>VerifyRequest function (for displaying signed objects and verification |  |  |
| Invocation<br>parameters | results).<br>Invocation of the ShowViewer function.<br>Name<br>Description                                                                                                                                                                                                                                                                                                                                                                                                   |  |  |

| ChannelHandle                                                                                                            | Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed,<br>the parameter is omitted.                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TrustedViewerId                                                                                                          | Contains the unique ID of the trusted viewer used for<br>display purposes. If this element is missing, the<br>configured default viewer is used (also refer to<br>[TR-03112-3]).                                                                                                                                                                                                |
| Document                                                                                                                 | The Document element, which MAY occur several<br>times, contains a document for display (for details<br>refer to [DSS], Section 2.4.2). If this is permitted by<br>the applicable security policy, equivalent documents<br>MAY be shown in an overview list (also refer to<br>[gemKon]) or only a certain random sample of the<br>transmitted documents can be fully displayed. |
| StyleSheetContent                                                                                                        | An XSL stylesheet MAY be transmitted in this element<br>which MAY be used to display XML documents. If the<br>transmitted stylesheet is not suitable for displaying the<br>transmitted documents, a corresponding error message<br>/resultminor/il/viewer#unsuiteableSylesheetForDocum<br>ent is returned.                                                                      |
| ViewerMessage                                                                                                            | MAY contain additional, short messages which the<br>trusted viewer displays in addition to the used data<br>(see below for details). If a transmitted message is too<br>long to be displayed by the viewer (e.g. at the top of<br>the window), this produces the error message<br>/resultminor/il/viewer#viewerMessageTooLong.                                                  |
|                                                                                                                          | If this element is missing, corresponding standard<br>messages are used by the trusted viewer.                                                                                                                                                                                                                                                                                  |
| Timeout                                                                                                                  | States whether the display on the viewer should be<br>switched off automatically after a specific time (in<br>seconds) in the event of no user interaction. If this<br>element is missing, the display SHOULD be cancelled<br>after 30 seconds.                                                                                                                                 |
|                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                 |
| With the ViewerMessage element the trusted viewer MAY be given additional<br>messages for the top or body of the window. |                                                                                                                                                                                                                                                                                                                                                                                 |
| Name                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                     |
| FrameMessage                                                                                                             | MAY contain a text which is displayed at the top of a<br>window.                                                                                                                                                                                                                                                                                                                |
|                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                 |

|               | BodyMessage                                                                                                                                                                                             | window. | MAY contain a text which is displayed in the body of a                                                |  |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------|--|
| Return        |                                                                                                                                                                                                         |         |                                                                                                       |  |
|               | Return of the ShowViewer function.                                                                                                                                                                      |         |                                                                                                       |  |
|               | Name<br>Description<br>dss:Result<br>more detail below.<br>Status information and errors with ShowViewerResponse (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).                                  |         |                                                                                                       |  |
|               |                                                                                                                                                                                                         |         | Contains the status information and the errors of<br>an executed action. This element is described in |  |
|               |                                                                                                                                                                                                         |         |                                                                                                       |  |
|               | Name<br>Error code                                                                                                                                                                                      |         |                                                                                                       |  |
|               | ResultMajor                                                                                                                                                                                             | •       | /resultmajor#ok                                                                                       |  |
|               |                                                                                                                                                                                                         | •       | /resultmajor#error                                                                                    |  |
|               |                                                                                                                                                                                                         | •       | /resultmajor#warning                                                                                  |  |
|               | ResultMinor                                                                                                                                                                                             | •       | /resultminor/al/common#noPermission                                                                   |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/al/common#internalError                                                                  |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/al/common#parameterError                                                                 |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/dp#unknownChannelHandle                                                                  |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/dp#communicationError                                                                    |  |
|               |                                                                                                                                                                                                         | •<br>•  | /resultminor/dp#trustedChannelEstablishmentFailed<br>/resultminor/dp#unknownProtocol                  |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/dp#unknownWebserviceBinding                                                              |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/il/viewer#timeout                                                                        |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/il/viewer#cancelationByUser                                                              |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/il/signature#unknownViewer                                                               |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/il/viewer#<br>unsuiteableSylesheetForDocument                                            |  |
|               |                                                                                                                                                                                                         | •       | /resultminor/il/viewer#viewerMessageTooLong                                                           |  |
|               | ResultMessage                                                                                                                                                                                           |         | MAY contain more detailed information on the error that<br>occurred if required.                      |  |
| Precondition  |                                                                                                                                                                                                         |         |                                                                                                       |  |
| Postcondition |                                                                                                                                                                                                         |         |                                                                                                       |  |
| Note          | For security reasons this function SHOULD NOT be made available to the Client<br>application, but only be invoked in a precisely defined context within the functions<br>SignRequest and VerifyRequest. |         |                                                                                                       |  |

Note that the user interface of the eCard-API-Framework in the ShowViewer-function MUST provide an appropriate warning message to the user, if the algorithms related to a qualified electronic signature do not fulfil the requirements defined by the BSI (Federal Office for Information Security) and the Bundesnetzagentur (Federal Network Agency).

# **3.3 Encryption functions**

### **3.3.1 EncryptRequest**

<span id="page-34-0"></span>

| Name                     | EncryptRequest                                                           |                                                                                                                                                                                                                                   |
|--------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description              | Transmitted documents are encrypted with the EncryptDocument function.   |                                                                                                                                                                                                                                   |
| Invocation<br>parameters | Invocation of the EncryptRequest function.<br>Name<br>dss:OptionalInputs | Description<br>MAY contain any or all of the following<br>elements, for which detailed information is<br>provided below:<br>•<br>ConnectionHandle<br>•<br>EncryptionKey<br>•<br>ContentEncryptionMethod<br>•<br>EncryptionContent |
|                          | dss:InputDocuments                                                       | Contains a series of dss:Document<br>elements, which are to be (partly) encrypted<br>(refer to [DSS], Section 2.4.2).                                                                                                             |

![](_page_35_Figure_0.jpeg)

| ds:KeyInfo          | Specifies the key of the recipient. Refer to<br>[RFC3275] for details concerning the structure<br>of this element. Among the various possibilities<br>at least the following two options MUST be<br>supported:                                            |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     | •<br>ds:KeyValue contains a symmetric<br>key, which serves as content encryption<br>key used for ciphering the data and<br>MUST be suitable for the applied<br>ContentEncryptionMethod (see<br>below).                                                    |
|                     | •<br>ds:X509Data/ds:X509Certific<br>ate contains an X.509-certificate,<br>which is used for encrypting the content<br>encryption key, which is either provided<br>in the ds:KeyValue-element<br>mentioned above or generated at<br>random.                |
| Other               | Specifies the key of the recipient using some<br>other means. This document specifies two<br>possibilities:                                                                                                                                               |
|                     | •<br>In order to address a Differential Identity<br>(DID) in a connected card application<br>(cf. [ISO24727-3] and [TR-03112-4])<br>specified by the<br>ConnectionHandle-element above<br>the following two elements appear as<br>child-element of Other: |
|                     | •<br>Contains the name of the<br>DIDName -<br>DID which is to be used for generating<br>the signature.                                                                                                                                                    |
|                     | •<br>MAY be used to resolve<br>DIDScope -<br>any ambiguity between local and global<br>DIDs with the same name.                                                                                                                                           |
|                     | •<br>In order to address a certificate stored on<br>a connected card application the<br>CertificateRef-element appears as<br>child-element of Other. Please refer to<br>[TR-03112-7] for details with respect to<br>the CertificateRef-element.           |
| KeyEncryptionMethod | This element is optional and MAY be used to<br>specify how the content encryption key is to be<br>enciphered.                                                                                                                                             |

![](_page_37_Figure_0.jpeg)

|        | xenc:Encryption<br>Properties                                                | MAY be used to provide more information on the<br>generation of the xenc:EncryptedData or<br>xenc:EncryptedKey-elements. Please refer<br>to [XMLEnc] Section 3.7 for details.                                                                                  |
|--------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | EncryptAndReplace<br>Data                                                    | States which parts of a transmitted XML<br>document should be encrypted. Details on the<br>dsse:SelectorType can be found in<br>[SigEnc].                                                                                                                      |
|        |                                                                              | If a document is to be encrypted with CMS<br>[RFC3369] for example, this element is ignored.                                                                                                                                                                   |
|        | InsertEncryptedData                                                          | References an input content to be encrypted and<br>specifies where to insert the resulting<br>xenc:EncryptedData within the<br>dsse:EncryptedDocument, which is to be<br>returned. Details on the<br>dsse:InsertEncryptedDataType can be<br>found in [SigEnc]. |
|        |                                                                              | If a document is to be encrypted with CMS<br>[RFC3369] for example, this element is ignored.                                                                                                                                                                   |
| Return |                                                                              |                                                                                                                                                                                                                                                                |
|        | The EncryptResponse element is the return of the function<br>EncryptRequest. |                                                                                                                                                                                                                                                                |
|        | Name                                                                         | Description                                                                                                                                                                                                                                                    |
|        | dss:Result                                                                   | Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.                                                                                                                                    |
|        | dss:OptionalOutputs                                                          | The optional element<br>dss:OptionalOutputs contains the results<br>of the encryption process in form of<br>EncryptedDocument-elements.                                                                                                                        |

![](_page_39_Figure_0.jpeg)

| Status information and errors with EncryptResponse (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2). |                           |
|----------------------------------------------------------------------------------------------------------|---------------------------|
| Name                                                                                                     | Error codes               |
| ResultMajor                                                                                              | •<br>/resultmajor#ok      |
|                                                                                                          | •<br>/resultmajor#error   |
|                                                                                                          | •<br>/resultmajor#warning |

|    | ResultMinor | •<br>/resultminor/al/common#noPermission                                           |
|----|-------------|------------------------------------------------------------------------------------|
|    |             | •<br>/resultminor/al/common#internalError                                          |
|    |             | •<br>/resultminor/al/common#parameterError                                         |
|    |             | •<br>/resultminor/dp#unknownChannelHandle                                          |
|    |             | •<br>/resultminor/dp#communicationError                                            |
|    |             | •<br>/resultminor/dp#                                                              |
|    |             | trustedChannelEstablishmentFailed                                                  |
|    |             | •<br>/resultminor/dp#unknownProtocol                                               |
|    |             | •<br>/resultminor/dp#unknownWebserviceBinding                                      |
|    |             | •<br>/resultminor/sal#unknownDataSetName                                           |
|    |             | •<br>/resultminor/sal#unknownDSIName                                               |
|    |             | •<br>/resultminor/il/signature#certificateNotFound                                 |
|    |             | •<br>/resultminor/il/signature#<br>certificateFormatNotCorrect                     |
|    |             | •<br>/resultminor/il/signature#<br>invalidCertificateReference                     |
|    |             | •<br>/resultminor/il/signature#<br>certificateChainInterrupted                     |
|    |             | •<br>/resultminor/il/service#<br>ocspResponderUnreachable                          |
|    |             | •<br>/resultminor/il/service#<br>directoryServiceUnreachable                       |
|    |             | •<br>/resultminor/il/signature#<br>certificatePathNotValidated                     |
|    |             | •<br>/resultminor/il/signature#<br>certificateStatusNotChecked                     |
|    |             | •<br>/resultminor/sal#digitalSignatureNotCorrect                                   |
|    |             | •<br>/resultminor/il/signature#<br>signatureAlgorithmNotSuitable                   |
|    |             | •<br>/resultminor/il/signature#invalidCertificatePath                              |
|    |             | •<br>/resultminor/il/signature#certificateRevoked                                  |
|    |             | •<br>/resultminor/il/signature#referenceTime<br>NotWithinCertificateValidityPeriod |
|    |             | •<br>/resultminor/il/encryption#encryptionO<br>fCertainNodesOnlyForXMLDocuments    |
|    |             | •<br>/resultminor/il/encryption#<br>encryptionFormatNotSupported                   |
|    |             | •<br>/resultminor/il/encryption#invalidCertificate                                 |
|    |             | •<br>/resultminor/il/key#keyGenerationNotPossible                                  |
|    |             | •<br>/resultminor/il/key#<br>encryptionAlgorithmNotSupported                       |
|    |             |                                                                                    |
| 42 |             | Bundesamt für Sicherheit in der Informationstechnik                                |

|               | ResultMessage                                                                                                                                                                                                                           | MAY contain more detailed information on the error<br>that occurred if required. |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Precondition  | If the encryption is to be performed for or with a connected card, a<br>corresponding, valid ConnectionHandle MUST exist.                                                                                                               |                                                                                  |
| Postcondition | The encrypted documents are returned in form of EncryptedDocument<br>elements.                                                                                                                                                          |                                                                                  |
| Note          | This function MAY use the [ISO24727-3] functions Encipher, DIDGet,<br>DataSetSelect, DSIRead and, for generation of message keys,<br>GetRandom (also refer to [TR-03112-4]).<br>Also refer to the EncryptDocument function in [gemKon]. |                                                                                  |

### **3.3.2 DecryptRequest**

| Name                     | DecryptRequest                             |                                                                                                                                                                                                                                                                |
|--------------------------|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description              |                                            | Encrypted documents are decrypted with the DecryptDocument function.                                                                                                                                                                                           |
| Invocation<br>parameters |                                            |                                                                                                                                                                                                                                                                |
|                          | Invocation of the DecryptRequest function. |                                                                                                                                                                                                                                                                |
|                          | Name                                       | Description                                                                                                                                                                                                                                                    |
|                          | dss:OptionalInputs                         | MAY contain any or all of the following elements,<br>for which detailed information is provided below:                                                                                                                                                         |
|                          |                                            | •<br>ConnectionHandle                                                                                                                                                                                                                                          |
|                          |                                            | •<br>KeySelector                                                                                                                                                                                                                                               |
|                          |                                            | If these elements are missing, the<br>eCard-API-Framework MUST try to determine<br>suitable keys in the connected card applications for<br>decrypting the data. If this fails, a corresponding<br>error /resultminor/sal#decryptionNotPossible is<br>returned. |
|                          | dss:InputDocuments                         | Contains a sequence of dss:Document elements,<br>which are to be decrypted (refer to [DSS], Section<br>2.4.2).                                                                                                                                                 |

![](_page_43_Figure_0.jpeg)

| Return       |                                         |                    |                                                                                                                                             |
|--------------|-----------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
|              |                                         |                    |                                                                                                                                             |
|              | Return of the DecryptResponse function. |                    |                                                                                                                                             |
|              | Name                                    |                    | Description                                                                                                                                 |
|              | dss:Result                              |                    | Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.                 |
|              | dss:OptionalOutputs                     |                    | The element dss:OptionalOutputs<br>contains the decrypted documents in form of<br>dss:Document-elements (refer to [DSS],<br>Section 2.4.2). |
|              | [TR-03112-1] Sections 4.1 and 4.2).     |                    | Status information and errors with DecryptResponse (also refer to                                                                           |
|              | Name                                    | Error code         |                                                                                                                                             |
|              | ResultMajor                             | •                  | /resultmajor#ok                                                                                                                             |
|              |                                         | •                  | /resultmajor#error                                                                                                                          |
|              | ResultMinor                             | •                  | /resultminor/al/common#noPermission                                                                                                         |
|              |                                         | •                  | /resultminor/al/common#internalError                                                                                                        |
|              |                                         | •                  | /resultminor/al/common#parameterError                                                                                                       |
|              |                                         | •                  | /resultminor/dp#unknownChannelHandle                                                                                                        |
|              |                                         | •                  | /resultminor/dp#communicationError                                                                                                          |
|              |                                         | •                  | /resultminor/dp#<br>trustedChannelEstablishmentFailed                                                                                       |
|              |                                         | •                  | /resultminor/dp#unknownProtocol                                                                                                             |
|              |                                         | •                  | /resultminor/dp#unknownWebserviceBinding                                                                                                    |
|              |                                         | •                  | /resultminor/sal#namedEntityNotFound                                                                                                        |
|              |                                         | •                  | /resultminor/il/encryption#<br>encryptionFormatNotSupported                                                                                 |
|              |                                         | •                  | /resultminor/sal#decryptionNotPossible                                                                                                      |
|              |                                         | •                  | /resultminor/sal#securityConditionsNotSatisfied                                                                                             |
|              |                                         | •                  | /resultminor/ifdl/terminal#noCard                                                                                                           |
|              | ResultMessage                           | error if required. | MAY contain more detailed information on the occurred                                                                                       |
| Precondition |                                         |                    | Suitable keys MUST be available to the eCard-API-Framework for decryption of                                                                |

|               | the documents as differential identity on a connected card application.                |
|---------------|----------------------------------------------------------------------------------------|
| Postcondition | The decrypted documents are returned.                                                  |
| Note          | This function uses the [ISO24727-3] function Decipher (also refer to<br>[TR-03112-4]). |
|               | Also refer to the DecryptDocument function in [gemKon].                                |

### **References**

| [SigEnc]     | A-SIT: C. Orthacker: Proposal for an Encryption Profile for OASIS DSS (including<br>schema)                                                                     |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PDF]        | Adobe: Portable Document Format Reference Manual                                                                                                                |
| [TR-03112-1] | BSI: TR-03112-1: eCard-API-Framework – Part 1: Overview and Generic Mechanisms                                                                                  |
| [TR-03112-2] | BSI: TR-03112-2: eCard-API-Framework – Part 2: eCard-Interface                                                                                                  |
| [TR-03112-3] | BSI: TR-03112-3: eCard-API-Framework – Part 3: Management-Interface                                                                                             |
| [TR-03112-4] | BSI: TR-03112-4: eCard-API-Framework – Part 4: ISO24727-3-Interface                                                                                             |
| [TR-03112-5] | BSI: TR-03112-5: eCard-API Framework – Part 5: Suppor- Interface                                                                                                |
| [TR-03112-6] | BSI: TR-03112-6: eCard-API-Framework – Part 6: IFD-Interface                                                                                                    |
| [TR-03112-7] | BSI: TR-03112-7: eCard-API-Framework – Part 7: Protocols                                                                                                        |
| [TR-03114]   | BSI: TR-03114: Stapelsignatur mit dem Heilberufsausweis                                                                                                         |
| [TS101733]   | ETSI: TS 101 733: Electronic Signature Formats, Electronic Signatures and<br>Infrastructures (ESI) – Technical Specification                                    |
| [gemKon]     | gematik: Connector specification                                                                                                                                |
| [RFC2119]    | IETF: RFC 2119: S. Bradner: Key words for use in RFCs to Indicate Requirement Levels                                                                            |
| [RFC2560]    | IETF: RFC 2560: M. Myers, R. Ankney, A. Malpani, S. Galperin, C. Adams: X.509<br>Internet Public Key Infrastructure - Online Certificate Status Protocol – OCSP |
| [RFC3161]    | IETF: RFC 3161: C. Adams, P. Cain, D. Pinkas, R. Zuccherato: Internet X.509 Public<br>Key Infrastructure Time-Stamp Protocol (TSP)                              |
| [RFC3275]    | IETF: RFC 3275: D. Eastlage, J. Reagle, D. Solo: (Extensible Markup Language)<br>XMLSignature Syntax and Processing                                             |
| [RFC3280]    | IETF: RFC 3280: R. Housley, W. Polk, W. Ford, D. Solo: Internet X.509 Public Key<br>Infrastructure, Certificate and Certificate Revocation List (CRL) Profile   |
| [RFC3281]    | IETF: RFC 3281: S. Farrell, R. Housley: An Internet Attribute Certificate Profile for<br>Authorization                                                          |
| [RFC3369]    | IETF: RFC 3369: R. Housley: Cryptographic Message Syntax (CMS)                                                                                                  |
| [RFC4998]    | IETF: RFC 4998: T. Gondrom, R. Brandner, U. Pordesch: Evidence Record Syntax (ERS)                                                                              |
| [RFC6283]    | IETF: RFC 6283: A. Jerman Blazic, S. Saljic, T. Gondrom: Extensible Markup Language<br>Evidence Record Syntax                                                   |
| [ISO24727-3] | ISO: ISO/IEC 24727-3: Identification Cards — Integrated Circuit Cards Programming<br>Interfaces — Part 3: Application Interface                                 |
| [AdES]       | OASIS: Advanced Electronic Signature Profiles of the OASIS Digital Signature Service<br>Version 1.0                                                             |
| [DSS]        | OASIS: Digital Signature Service Core Protocols, Elements, and Bindings                                                                                         |
| [SigGer]     | OASIS: German Signature Law Profile of the OASIS Digital Signature Service                                                                                      |
| [SigVer]     | OASIS: Profile for comprehensive multi-signature verification reports for OASIS Digital<br>Signature Services                                                   |
|              |                                                                                                                                                                 |

| [SigPol] | OASIS: Signature Policy Profile of the OASIS Digital Signature Services |
|----------|-------------------------------------------------------------------------|
| [XAdES]  | W3C: W3C Note: XML Advanced Electronic Signatures (XAdES)               |
| [XMLEnc] | W3C: W3C Recommendation: XML Encryption Syntax and Processing           |
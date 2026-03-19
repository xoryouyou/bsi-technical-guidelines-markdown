
![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0001-00.png)


Technical Guideline TR-03112-2 eCard-API-Framework – eCard-Interface 

Version 1.1.5 

7. April 2015 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn 

E-Mail: ecard.api@bsi.bund.de Internet: https://www.bsi.bund.de 

© Bundesamt für Sicherheit in der Informationstechnik 2015 

## **Contents** 

|1|Overview of the eCard-API-Framework.................................................................................................4|
|---|---|
|1.1|Key Words.........................................................................................................................................4|
|1.2|XML-Schema....................................................................................................................................5|
|2|Overview of the eCard-Interface............................................................................................................6|
|2.1|Objective...........................................................................................................................................6|
|2.2|Functions...........................................................................................................................................6|
|2.2.1|Functions for identity management..............................................................................................6|
|2.2.2|Signature functions.......................................................................................................................6|
|2.2.3|Encryption functions....................................................................................................................7|
|3|Specification of the eCard-Interface.......................................................................................................8|
|3.1|Functions for identity management...................................................................................................8|
|3.1.1|GetCertificate...............................................................................................................................8|
|3.2|Signature functions............................................................................................................................9|
|3.2.1|SignRequest..................................................................................................................................9|
|3.2.2|VerifyRequest.............................................................................................................................22|
|3.2.3|ShowViewer...............................................................................................................................32|
|3.3|Encryption functions.......................................................................................................................35|
|3.3.1|EncryptRequest..........................................................................................................................35|
|3.3.2|DecryptRequest..........................................................................................................................43|



## **Table of Figures** 

Bundesamt für Sicherheit in der Informationstechnik 

3 

## **1 Overview of the eCard-API-Framework** 

The objective of the eCard-API-Framework is the provision of a simple and homogeneous interface to enable standardised use of the various smart cards (eCards) for different applications. 

The eCard-API-Framework is sub-divided into the following layers: 

- Application-Layer 

- Identity-Layer 

- Service-Access-Layer 

- Terminal-Layer 

The **Application-Layer** contains the various applications which use the eCard-API-Framework to access the eCards and their associated functions. Application-specific "convenience interfaces", in which the recurring invocation sequences may be encapsulated in application-specific calls, may also exist in this layer. However, these interfaces are currently _not_ within the scope of the e-Card-API-framework. 

The **Identity-Layer** comprises the eCard-Interface and the Management interface, and therefore functions for the use and management of electronic identities as well as for management of the eCard-API-Framework. 

The _eCard-Interface_ (refer to [TR-03112-2]) allows to request certificates as well as the encryption, signature and time-stamping of documents. 

In the M _anagement-Interface_ (refer to [TR-03112-3]), functions for updating the framework and the management of trusted identities, smart cards, card terminals, and default behaviour are available. 

The **Service-Access-Layer** provides, in particular, functions for cryptographic primitives and biometric mechanisms in connection with cryptographic tokens, and comprises the ISO24727-3-Interface and the Support-Interface. 

The _ISO24727-3-Interface_ defined in the present document is a webservice-based implementation of the standard of the same name [ISO24727-3]. This interface contains functions to establish (cryptographically protected) connections to smart cards, to manage card applications, to read or write data, to perform cryptographic operations and to manage the respective key material (in the form of so-called "differential identities"). In the process, all functions which use or manage "differential identities" are parameterised by means of protocol-specific object identifiers so that the different protocols which are defined in the present document MAY be used with a standardised interface (refer to [TR-03112-7]). 

The S _upport-Interface_ (refer to [TR-03112-5]) contains a range of supporting functions. 

The **Terminal-Layer** primarily contains the _IFD-Interface_ (refer to [TR-03112-6]). This layer takes over the generalisation of specific card terminal types and various interfaces as well as communication with the smart card. For the user it is unimportant whether the card is addressed by PC/SC, a SICCT terminal or a proprietary interface, or whether it has contacts or is contact-less. 

## **1.1 Key Words** 

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC2119]. The key word “CONDITIONAL” is to be interpreted as follows: 

CONDITIONAL: The usage of an item is dependent on the usage of other items. It is therefore further qualified under which conditions the item is REQUIRED or RECOMMENDED. 

Bundesamt für Sicherheit in der Informationstechnik 

4 

## **1.2 XML-Schema** 

A XML-Schema is provided together with this Technical Guideline. In case of incongruencies, the specifications in this text take precedence. The graphical representations of the XML-Schema illustrate the schema. Note that the text of this Guideline might further restrict the presence or mulitplicity of elements as compared to the schema definition. 

Bundesamt für Sicherheit in der Informationstechnik 

5 

## **2 Overview of the eCard-Interface** 

## **2.1 Objective** 

The eCard-Interface encapsulates important document related functions of the eCard-API-Framework in an application-orientated manner. 

## **2.2 Functions** 

The eCard-Interface encapsulates the main functions of the eCard-API-Framework in an application-orientated manner. For this purpose the eCard-Interface provides the following function groups: 

- Functions for identity management 

- Signature functions 

- Encryption functions 

With the GetCertificate function, certificate applications can be transferred to a certification authority, from where they obtain their certificates. 

In addition, the invocations specified by [DSS] can be used for the creation and verification of (qualified) electronic signatures in the formats according to [RFC3275] and [RFC3369], as well as the corresponding extensions from ETSI. This functional group also contains an interface to a trustworthy display component which can be used in particular for the displaying the data and test results requiring a signature. 

Finally, with the encryption functions documents can be easily encrypted and decrypted in accordance with [RFC3369] and [XMLEnc] by simple function invocations. 

## **2.2.1 Functions for identity management** 

- With the GetCertificate function, certificate applications can be transferred to a certification authority, from which certificates are obtained. 

## **2.2.2 Signature functions** 

- The SignRequest function conforms with [DSS], and related profiles and permits the creation of (qualified) electronic signatures in popular high-level formats such as XML-DSig in accordance with [RFC3275], or cryptographic message syntax in accordance with [RFC3369]. These signatures may also contain time stamps, which can also be requested separately with this function. 

- The VerifyRequest function conforms with [DSS] and related profiles and enables verification of signed objects (e.g. signatures, time stamps, certificates, blacklists). 

- Th ShowViewer function enables display of documents in a trustworthy manner, which can be used for the creation and verification of signatures. 

Bundesamt für Sicherheit in der Informationstechnik 

6 

## **2.2.3 Encryption functions** 

- The EncryptRequest function enables encryption of data in accordance with [XMLEnc] or [RFC3369]. 

- The DecryptRequest function enables decryption of data encrypted in accordance with [XMLEnc] or [RFC3369]. 

Bundesamt für Sicherheit in der Informationstechnik 

7 

## **3 Specification of the eCard-Interface** 

## **3.1 Functions for identity management** 

## **3.1.1 GetCertificate** 

**Name GetCertificate Description** The GetCertificate function is used to request and obtain certificates. A wide range of protocols can be used for this purpose. Please refer to [TR-03112-7] for protocol specifications. **Invocation parameters** Invocation of the GetCertificate function. **Name Description** Input Contains the protocol's input parameters and is of the abstract ProtocolDataType, which is defined as follows: <complexType name="ProtocolDataType" abstract="true"> <complexContent> <extension base="anyType"> <attribute name="Protocol" type="anyURI" use="required" /> </extension> </complexContent> </complexType> The input format depends on the protocol used for certificate enquiries (also refer to [TR-03112-7]). **Return** 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0008-04.png)


**----- Start of picture text -----**<br>
Return of the CardUpdate function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more<br>detail below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

8 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0009-00.png)


**----- Start of picture text -----**<br>
Output Contains the protocol's output parameters and is of<br>the abstract ProtocolDataType (see above).<br>The output format depends on the protocol used for<br>certificate enquiries (also refer to [TR-03112-7]).<br>Status information and errors with GetCertificate (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>In addition, other specific protocol error messages MAY<br>exist.<br>ResultMessage MAY contain more detailed information on the occurred<br>error if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.2 Signature functions** 

## **3.2.1 SignRequest** 

**Name SignRequest Description** The SignRequest function conforms largely **[1]** with [DSS], [AdES], [SigGer] and [SigPol] and serves to create (qualified) electronic signatures or time stamps for transmitted documents. 

> 1 Deviations are due to the resolution of restrictions which seem to be unnecessary. For example, according to [DSS] (refer to section 3.2) only one dss:SignatureObject may be returned and the return of dss:Timestamp elements is not permitted in accordance with [AdES] (refer to section 3.4.1.2). The necessity of these restrictions is currently being discussed in the OASIS DSS-X working group. 

Bundesamt für Sicherheit in der Informationstechnik 

9 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0010-00.png)


**----- Start of picture text -----**<br>
Description<br>Invocation of the SignRequest function<br>Name Description<br>dss:Optional MAY contain any or all of the following elements, for<br>Inputs which detailed information is provided below:<br>• ConnectionHandle<br>• KeySelector<br>• GenerateUnderSignaturePolicy<br>• ReturnSupportedSignaturePolicies<br>• SignatureForm<br>• SignatureType<br>• Properties<br>• IncludeEContent<br>• IncludeObject<br>• SignaturePlacement<br>• Schemas<br>• TrustedViewerInfo<br>dss:Input If a signature is to be generated this element MUST<br>Documents contain one or more dss:Document elements (refer to<br>[DSS], Section 2.4.2).<br>Note that according to [SigGer] one MAY NOT use<br>elements of type dss:DocumentHash if (qualified)<br>electronic signatures are to be generated. Therefore, no<br>signature is generated in this case, and instead the error<br>message<br>/resultminor/il/signature#documentHashForSignature is<br>returned.<br>The dss:DocumentHash option MAY therefore ONLY<br>be used for requesting time stamps.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

10 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0011-00.png)


The ConnectionHandle-element MAY appear in dss:OptionalInputs. It contains a handle with which the connection to a card application can be addressed. If it is up to the eCard-API-Framework to choose an appropriate card application this element MAY be omitted. The ConnectionHandleType is defined and explained in [TR-03112-4]. 

Bundesamt für Sicherheit in der Informationstechnik 

11 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0012-00.png)


The KeySelector-element MAY appear in dss:OptionalInputs. Addresses the key used for generating the signature. If it is up to the eCard-API-Framework to choose an appropriate key this element MAY be omitted. The KeySelector-element is defined and explained in [DSS] (Section 3.5.4). 

In order to address a Differential Identity (DID) in a connected card application (cf. [ISO24727-3] and [TR-03112-4]) specified by the 

ConnectionHandle-element above the following two elements appear as child-element of Other: 

- DIDName - Contains the name of the DID which is to be used for generating the signature. 

- DIDScope - MAY be used to resolve any ambiguity between local and global DIDs with the same name. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0012-06.png)


The GenerateUnderSignaturePolicy-element MAY appear in dss:OptionalInputs and is defined and explained in [SigPol]. As explained in [SigPol] this element specifies the signature policy under which the signature is to be generated. 

While the eCard-API-Framework SHOULD be implemented in a way such that the set of supported signature policies can be easily extended, at least the signature policies defined in [gemKon] Annex A MUST be supported. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0012-09.png)


The ReturnSupportedSignaturePolicies-element MAY appear in dss:OptionalInputs and is defined and explained in [SigPol]. As explained in [SigPol] this element is used to ask for the set of supported signature policies. 

Bundesamt für Sicherheit in der Informationstechnik 

12 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0013-00.png)


The SignatureForm-element MAY appear in dss:OptionalInputs and is defined and explained in [AdES]. 

If the SignatureType–element defined below is urn:ietf:rfc:3275 or urn:ietf:rfc:3369 the SignatureForm-element, can be used to specify more precisely which form of the advanced electronic signature is to be generated according to [XAdES] or [TS101733] for XML and CMS signatures. With other SignatureTypes a warning /resultminor/il/signature#signatureTypeDoesNotSupportSignatureFormClarific ationWarning is returned. 

The URI specified in Section 7.1 of [AdES] MUST be used for specification of the SignatureForm. Other URIs produce an error message /resultminor/il/signature#unknownSignatureForm. 

Bundesamt für Sicherheit in der Informationstechnik 

13 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0014-00.png)


The SignatureType-element MAY appear in dss:OptionalInputs and is defined in [DSS]. 

As explained in [DSS] (Section 3.5.1) it is used to specify the type of signature or time stamp, which is to be created. The following types of signatures and time stamps are supported: 

## **1. Signature types** 

- **XML signature** . If the URI urn:ietf:rfc:3275 is transmitted, the generation of an XML signature is initiated in accordance with [RFC3275] (or in connection with the SignatureForm described above in accordance with [XAdES]). Such a signature is returned as a ds:Signature element. 

- **CMS signature** . If the URI urn:ietf:rfc:3369 is transmitted, a CMS signature according to [RFC3369] (or in connection with the SignatureForm described above in accordance with [TS101733]) is requested, whereby the signature is returned as a dss:Base64Signature with the URI stated above as Type. 

- **PDF signature** . If the URI http://ns.adobe.com/pdf is transmitted, an integrated PDF signature is initiated in accordance with [PDF], whereby the signature is returned as dss:Base64Signature with the URI stated above as Type. If the transmitted document is not a Base64Data element with MIME type "application/pdf", an error /resultminor/il/signature#PDFSignatureForNonPDFDocument is returned. 

## **2. Time stamp types** 

All time stamps are returned as a dss:Timestamp element in accordance with [DSS] Section 5.1, whereby the eCard-API-Framework creates the requested time stamp itself or MAY use an external time stamping service depending on the default configuration (also refer to [TR-03112-3]). In this context, it is necessary to distinguish between the following cases: 

- **RFC3161 time stamp** . If the URI urn:ietf:rfc:3161 is transmitted, the creation of a time stamp for each transmitted document is initiated in accordance with [RFC3161] and returned in the child element RFC3161TimeStampToken of Timestamp. 

- **XML time stamp** . If the URI 

   - urn:oasis:names:tc:dss:1.0:core:schema:XMLTimeStampToken is transmitted, the creation of an XML-based time stamp according to [DSS] Section 5.1.1 is initiated and the time stamp is returned as a ds:Signature element. 

Bundesamt für Sicherheit in der Informationstechnik 

14 

- **RFC4998 archive time stamp** . If the URI urn:ietf:rfc:4998 is transmitted, a single ArchiveTimeStamp is created from the transmitted documents or hash values in accordance with [RFC4998] and saved in a child element RFC4998ArchiveTimeStamp of Other type base64Binary with MIME type "application/ers". 

Other SignatureType information results in an error message /resultminor/il/signature#signatureFormatNotSupported. 

If the element is missing, the default behaviour is implemented (also refer to [TR-03112-3]). 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0015-03.png)


The Properties-element MAY appear in dss:OptionalInputs and is defined in [DSS]. 

As explained in [DSS] (Section 3.5.5) it may contain instructions for inserting signed and non-signed attributes (refer to [DSS], Section 3.5.5). In addition to the cases described in [AdES] Section 3.3.1.1.2.3, the URI http://www.bsi.bund.de/ecard/api/1.1/properties/ 

previousTimeStampHash MUST be supported for the insertion of a hash value of a previously generated time stamp into a signed attribute. For this purpose the element PreviousTimeStampHash 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0015-07.png)


of type XAdES:DigestAlgAndValueType defined in [XAdES] is inserted, whereby the hash value is created over the TimeStampToken or the Signature element. Note that in the latter case the canonicalization algorithm, which is used for creating the signature MUST be applied before the hash calculation takes place. 

As a result it can be proven that the signature was created _after_ the time stated in the time stamp. 

The time stamp to be included in the signature MAY be transmitted in the form of a dss:Timestamp element in accordance with [DSS] Section 5.1 or provided by the eCard-API-Framework itself. 

Bundesamt für Sicherheit in der Informationstechnik 

15 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0016-00.png)


The IncludeEContent-element MAY appear in dss:OptionalInputs and is defined in [DSS]. 

As explained in [DSS] (Section 3.5.7) it states that the document shall be inserted into the CMS-signature. With time stamps (according to [RFC3161] or [DSS] Section 5.1), XML signatures or PDF signatures, this element is ignored and a warning /resultminor/il/signature#unableToIncludeEContentWarning is returned. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0016-03.png)


The IncludeObject-element MAY appear multiple times in dss:OptionalInputs if an XML-signature according to [RFC3275] is requested (cf. SignatureType-element above). This element is defined and explained in [DSS] (Section 3.5.6). 

This element points to an object, which is transmitted in the InputDocuments element and shall be included in the signature. 

If the element is provided and a different signature type requested, this element is ignored and a warning 

/resultminor/il/signature#includeObjectOnlyForXMLSignatureAllowedWarnin g is returned. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0016-08.png)


The SignaturePlacement-element MAY appear in dss:OptionalInputs and is defined in [DSS] (Section 3.5.8). 

With this optional element, positioning of the signature in the document MAY be specified for XML based signatures in accordance with [RFC3275] and XML time stamps in accordance with [DSS] Section 5.1 (for details refer to [DSS] Section 3.5.8). With other signature types the element is ignored and a warning /resultminor/il/signature#ignoredSignaturePlacementFlagWarning is returned. 

If the element is missing, the signature is inserted as an additional node at the end of the document (directly in front of the document's end tag). 

Bundesamt für Sicherheit in der Informationstechnik 

16 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0017-00.png)


The Schemas-element MAY appear in dss:OptionalInputs and is defined in [DSS] (Section 2.8.5). 

It contains a number of XML schemata which can be used for validation of the transmitted XML documents (for details refer to [DSS], Section 2.8.5). If this element is missing, the configured default schemata are used for validation (also refer to [TR-03112-3]). 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0017-03.png)


The TrustedViewerInfo-element MAY appear in dss:OptionalInputs and is described below. 

If this element is present the document(s) transmitted in the InputDocuments-element MUST be displayed in a trusted viewer before signing. If this element is missing, no trusted viewer is invoked. 

**Name Description** TrustedViewerId States which trusted viewer is to be used for displaying the documents, which are to be signed. If the element is missing, the viewer configured in DefaultSignOptions is used (also refer to [TR-03112-3]). StyleSheet Contains a stylesheet which is to be used for visualisation of XML documents. 

Bundesamt für Sicherheit in der Informationstechnik 

17 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0018-00.png)


**----- Start of picture text -----**<br>
IncludeViewerManifest In the case of an XML signature and<br>visualisation of the document to be signed<br>in a stylesheet as described in [gemKon]<br>(Section 5.4.6.3.1 and Annex A) in more<br>detail, this states whether a reference to<br>this stylesheet shall be inserted into the<br>signature as a signature manifest. If the<br>element is missing, or if it has the value<br>TRUE, the style sheet reference is inserted<br>as a signature manifest.<br>If the element is FALSE or if a CMS<br>based signature should be generated, no<br>reference to the trusted viewer or any used<br>style sheet is included in the signature.<br>Return<br>SignResponse is the response to the SignRequest invocation<br>Name Description<br>dss:Result Contains the status information and the<br>errors of an executed action. This element is<br>described in more detail below.<br>dss:OptionalOutputs MAY contain optional output elements.<br>Depending on the<br>dss:OptionalInputs element (see<br>page 10) the following optional output<br>elements MAY appear:<br>• DocumentWithSignature<br>• UsedSignaturePolicy<br>• SupportedSignaturePolici<br>es<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

18 

dss:SignatureObject In case of success this element contains the generated signatures or time stamps in the form of one or more dss:SignatureObject elements (refer to [DSS] Section 3.2 for details). Unlike in [DSS] this element MAY appear multiple times such that it is possible to implement batch signature scenarios as specified in [TR-03114]. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0019-01.png)


The DocumentWithSignature-element MAY appear multiple times in dss:OptionalOutputs if the generation of enveloped XML signatures or PDF signatures was requested. This element is defined and explained in [DSS] (Section 3.5.8). 

In this case the dss:SignaturePtr alternative in dss:SignatureObject (also refer to [DSS] Section 2.5) MUST be used to provide a reference to the signatures contained in the documents. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0019-04.png)


The UsedSignaturePolicy-element appears in dss:OptionalOutputs if the GenerateUnderSignaturePolicy-element (see page 12) was provided in dss:OptionalInputs. Please refer to [SigPol] for more details. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0019-06.png)


The SupportedSignaturePolicies-element appears in dss:OptionalOutputs if the ReturnSupportedSignature Policies-element (see page 12) was provided in dss:OptionalInputs. Please refer to [SigPol] for more details. 

Bundesamt für Sicherheit in der Informationstechnik 

19 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0020-00.png)


**----- Start of picture text -----**<br>
Status information and errors with SignResponse (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error code<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

20 

|ResultMinor|**•**<br>/resultminor/al/common#noPermission<br>**•**<br>/resultminor/al/common#internalError<br>**•**<br>/resultminor/al/common#parameterError<br>**•**<br>/resultminor/dp#unknownChannelHandle<br>**•**<br>/resultminor/dp#communicationError<br>**•**<br>/resultminor/dp#<br>trustedChannelEstablishmentFailed<br>**•**<br>/resultminor/dp#unknownProtocol<br>**•**<br>/resultminor/dp#unknownWebserviceBinding<br>**•**<br>/resultminor/sal#unknownDIDName<br>**•**<br>/resultminor/sal#unknownDataSetName<br>**•**<br>/resultminor/sal#unknownDSIName<br>**•**<br>/resultminor/il/signature#<br>signatureFormatNotSupported<br>**•**<br>/resultminor/il/signature#<br>PDFSignatureForNonPDFDocument<br>**•**<br>/resultminor/il/signature#<br>unableToIncludeEContent<br>**•**<br>/resultminor/il/signature#<br>ignoredSignaturePlacementFlag<br>**•**<br>/resultminor/il/signature#certificateNotFound<br>**•**<br>/resultminor/il/service#<br>timeStampServiceUnreachable<br>**•**<br>/resultminor/il/signature#<br>resolutionOfObjectReferenceImpossible<br>**•**<br>/resultminor/il/signature#<br>transformationAlgorithmNotSupported<br>**•**<br>/resultminor/il/signature#unknownViewer<br>**•**<br>/resultminor/il/signature#signatureTypeDoes<br>NotSupportSignatureFormClarificationWarning<br>**•**<br>/resultminor/il/signature#<br>unknownSignatureForm<br>**•**<br>/resultminor/il/signature#includeObjectOnly<br>ForXMLSignatureAllowedWarning<br>**•**<br>/resultminor/il/algorithm#<br>hashAlgorithmNotSupported<br>**•**<br>/resultminor/il/signature#<br>hashAlgorithmNotSuitable<br>**•**<br>/resultminor/il/algorithm#<br>signatureAlgorithmNotSupported<br>**•**<br>/resultminor/il/signature#signatureAlgorithm<br>NotSuitable||
|---|---|---|



Bundesamt für Sicherheit in der Informationstechnik 

21 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0022-00.png)


**----- Start of picture text -----**<br>
ResultMessage MAY contain more detailed information on the error<br>that occurred if required.<br>Precondition The ConnectionHandle MAY address a linked card application or a<br>signature service. In the first case, the respective DID and a corresponding<br>authorisation for use of the key MUST be provided or be obtainable by<br>implicitly initiated authentication steps with DIDAuthenticate (also refer<br>to [TR-03112-4]).<br>Postcondition Signatures or time stamps are created for the transmitted documents in<br>accordance with the transmitted child elements of dss:OptionalInputs<br>and returned in dss:SignatureObject or<br>dss:DocumentWithSignature elements.<br>Note The SignRequest function invokes the functions Sign, Hash and, if<br>applicable (for reading the certificates to be included in the signatures)<br>DataSetSelect and DSIRead (also refer to [ISO24727-3] and<br>[TR-03112-4]) and, if required, the ShowViewer function (refer to Section<br>3.2.3).<br>Note that the eCard-API-Framework MUST return a warning message (…<br>{hash/signature}AlgorithmNotSuitable), if the applied<br>algorithms do not fulfil the requirements for qualified electronic signatures as<br>defined by the BSI (Federal Office for Information Security) and the<br>Bundesnetzagentur (Federal Network Agency).<br>**----- End of picture text -----**<br>


## **3.2.2 VerifyRequest** 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0022-02.png)


**----- Start of picture text -----**<br>
Name VerifyRequest<br>Description The VerifyRequest function is used to verify signed objects (signatures,<br>time stamps, certificates, etc.). In some circumstances, a number of different<br>verification operations must be performed. Depending on the transmitted<br>dss:OptionalInputs or the configured default VerifyOptions<br>(refer to [TR-03112-3]) the results of these individual verification steps MAY<br>be returned.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

22 

## **Invocation parameters** 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0023-01.png)


Invocation of the VerifyRequest function 

## **Name** 

dss:OptionalInputs 

## **Description** 

MAY contain any or all of the following elements, for which detailed information is provided below: 

- VerifyManifests 

- UseVerificationTime 

- AdditionalKeyInfo 

- ReturnUpdatedSignature 

- VerifyUnderSignaturePoli cy 

- ReturnVerificationReport 

Bundesamt für Sicherheit in der Informationstechnik 

23 

|||dss:InputDocuments|MAY contain the documents required for<br>verification of the signatures or time stamps<br>if the respective documents are not part of<br>the signatures transmitted in<br>dss:SignatureObject.<br>This element MAY also contain<br>XML-signatures according to [RFC3275]<br>wrapped in adss:Document-element with<br>a child elementdss:Base64XML- or<br>dss:EscapedXML.<br>In this case there MUST be a corresponding<br>dss:SignaturePtr-element which<br>indicates the presence of such an<br>XML-signature. This option is necessary to<br>avoid verification failures due to namespace<br>rewriting (please refer to the note on page 39<br>of [DSS]).<br>Details on the<br>dss:InputDocuments-element can be<br>found in Section 2.4 of [DSS].||
|---|---|---|---|---|



Bundesamt für Sicherheit in der Informationstechnik 

24 

|||dss:SignatureObject2|Contains the signed object which is to be<br>verified. The following signed objects<br>MUST be supported:<br>**•**<br>XML-based signatures according to<br>[RFC3275] (and possibly [XAdES])<br>indicated by a<br>dss:SignaturePointer-eleme<br>nt, which points to a<br>ds:Signature-element wrapped<br>in adss:Base64XML- or<br>dss:EscapedXML-element inside<br>the<br>dss:InputDocuments-element<br>specified above,<br>**•**<br>a time stamp according to<br>[RFC3161] or [DSS] (Section 5.1.1)<br>in a single<br>dss:Timestamp-element,<br>**•**<br>CMS-based signatures according to<br>[RFC3369] (and possibly<br>[TS101733]) in the<br>dss:Base64Signature-element<br>,<br>**•**<br>Certificates (e.g. according to<br>[RFC3280] or [RFC3281]) in a<br>child-element<br>CertificateValues(cf.<br>[XAdES]) of theOther-element,<br>**•**<br>OCSP-Responses according to<br>[RFC2560] and CRLs according to<br>[RFC3280] in a child-element<br>RevocationValues(cf.<br>[XAdES]) of theOther-element,<br>**•**<br>an Evidence Record according to<br>[RFC4998] or [RFC6283] in a<br>child-elementEvidenceRecord<br>(see below) of theOther-element,<br>which protects the content of all<br>dss:Document-elements provided<br>in the<br>dss:InputDocuments-element<br>above.|
|---|---|---|---|



- 2 Note that unlike in the VerifyRequest specified in [DSS] the dss:SignatureObject-element MAY in case of non-detached signatures, certificates or OCSP-responses appear multiple times here such that it is possible to verify a batch of signed objects with a single request. For the verification of a detached signature, a time-stamp or an evidence record there MUST exactly be one dss:SignatureObject or an error (/resultminor/al/common#parameterError) is returned. 

Bundesamt für Sicherheit in der Informationstechnik 

25 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0026-00.png)


**----- Start of picture text -----**<br>
The EvidenceRecord-element MAY appear as child-element of the<br>Other-element within dss:SignatureObject and contains an<br>evidence record according to [RFC4998] and [RFC6283].<br>Name Description<br>xmlEvidenceRecord Is an evidence record according to<br>[RFC6283].<br>asn1EvidenceRecord Is an evidence record according to<br>[RFC4998].<br>The VerifyManifests-element MAY appear in<br>dss:OptionalInputs and is defined in [DSS] (Section 4.5.1). The<br>presence of this element instructs the eCard-API-Framework to validate<br>manifests in an XML signature.<br>The UseVerificationTime-element MAY appear in<br>dss:OptionalInputs and is defined in [DSS] (Section 4.5.2). The<br>presence of this element instructs the eCard-API-Framework to use the<br>specified time to verify the signature.<br>If this element is missing, the verification time is either determined from an<br>existing time stamp or another trustworthy time after the creation date<br>(so-called assumed creation time). If such information is missing, the current<br>time MUST be taken as the verification time. In this case, however, the<br>verification data must be supplemented with trustworthy time information<br>(time stamp or statement of time) on which subsequent verification can be<br>based, and which then provides the same verification result.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

26 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0027-00.png)


The AdditionalKeyInfo-element MAY appear in dss:OptionalInputs and is defined in [DSS] (Section 4.5.4). 

This element provides the eCard-API-Framework with additional data (such as certificates and CRLs) which it can use to validate the signature. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0027-03.png)


The ReturnUpdatedSignature-element MAY appear in dss:OptionalInputs and is defined in [DSS] (Section 4.5.8). 

Using the optional Type-attribute in this element with the values defined in [AdES] (Section 7.1, Table 1) it is possible to update a basic XML- or CMS-based signature during verification such that the result is an advanced electronic signature according to [XAdES] or [TS101733]. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0027-06.png)


The VerifyUnderSignaturePolicy-element MAY appear in dss:OptionalInputs and is defined in [SigPol]. 

The eCard-API-Framework MUST fulfil the requirements for Conformance Level 1 defined in Section 3.1 of [SigPol] and SHOULD implement the additional requirements of Conformance Level 2. 

Bundesamt für Sicherheit in der Informationstechnik 

27 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0028-00.png)


The ReturnVerificationReport-element MAY appear in dss:OptionalInputs and is defined in [SigVer]. The eCard-API-Framework MUST fulfil the requirements for Conformance Level 2 (“Comprehensive”) defined in [SigVer] and SHOULD implement the additional requirements of Conformance Level 3 (“Convenient”). **Return** 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0028-02.png)


Return of the VerifyRequest function 

**Name Description** dss:Result Contains the status information and the errors of an executed action. This element is described in more detail below. 

Bundesamt für Sicherheit in der Informationstechnik 

28 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0029-00.png)


**----- Start of picture text -----**<br>
dss:Optional MAY contain optional output elements. Depending<br>Outputs on the dss:OptionalInputs element (see page<br>23) the following optional output elements MAY<br>appear:<br>• VerifyManifestResults<br>• DocumentWithSignature<br>• UpdatedSignature<br>• VerifiedUnderSignaturePolicy<br>• VerificationReport<br>The VerifyManifestResults-element appears in<br>dss:OptionalOutputs if the VerifyManifests-element (see page<br>26) was provided in dss:OptionalInputs. Please refer to [DSS]<br>Section 4.5.1 for more details.<br>The DocumentWithSignature-element appears in<br>dss:OptionalOutputs if the ReturnUpdatedSignature-element<br>(see page 27) was provided in dss:OptionalInputs in case an<br>enveloped  signature was verified. Please refer to [DSS] Section 4.5.8 for<br>more details.<br>The UpdatedSignature-element appears in dss:OptionalOutputs<br>if the ReturnUpdatedSignature-element (see page 27) was provided<br>in dss:OptionalInputs in case an  enveloping  or  detached  signature<br>was verified. Please refer to [DSS] Section 4.5.8 for more details.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

29 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0030-00.png)


The VerifiedUnderSignaturePolicy-element appears in dss:OptionalOutputs if the VerifyUnderSignaturePolicy-element (see page 27) was provided in dss:OptionalInputs. Please refer to [SigPol] for more details. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0030-02.png)


The VerificationReport-element appears in dss:OptionalOutputs if the ReturnVerificationReport-element (see page 28) was provided in dss:OptionalInputs. Please refer to [SigVer] for more details. Status information and errors with VerifyResponse (also refer to [TR-03112-1] Sections 4.1 and 4.2). **Name Error codes** ResultMajor **•** /resultmajor#ok **•** /resultmajor#error **•** /resultmajor#warning 

Bundesamt für Sicherheit in der Informationstechnik 

30 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0031-00.png)


**----- Start of picture text -----**<br>
ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#communicationError<br>• /resultminor/il/signature#<br>certificateNotFound<br>• /resultminor/il/signature#<br>certificateFormatNotCorrect<br>• /resultminor/il/signature#<br>invalidCertificateReference<br>• /resultminor/il/signature#<br>certificateChainInterrupted<br>• /resultminor/il/signature#<br>resolutionOfObjectReferenceImpossible<br>• /resultminor/il/signature#<br>transformationAlgorithmNotSupported<br>• /resultminor/il/signature#unknownViewer<br>• /resultminor/il/signature#<br>certificatePathNotValidated<br>• /resultminor/il/signature#<br>certificateStatusNotChecked<br>• /resultminor/il/signature#<br>signatureManifestNotCheckedWarning<br>• /resultminor/il/signature#<br>suitabilityOfAlgorithmsNotChecked<br>• /resultminor/il/signature#<br>detachedSignatureWithoutEContent<br>• /resultminor/il/signature#<br>improperRevocationInformation<br>• /resultminor/il/signature#<br>SignatureManifestNotCorrect<br>• /resultminor/il/algorithm#<br>hashAlgorithmNotSupported<br>• /resultminor/il/algorithm#<br>signatureAlgorithmNotSupported<br>• /resultminor/il/signature#<br>signatureAlgorithmNotSuitable<br>• /resultminor/il/signature#<br>hashAlgorithmNotSuitable<br>• /resultminor/il/signature#<br>wrongMessageDigest<br>• /resultminor/sal#invalidSignature<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

31 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0032-00.png)


**----- Start of picture text -----**<br>
ResultMessage MAY contain more detailed information on the<br>occurred error if required.<br>Precondition<br>Postcondition The signed objects transmitted in VerifyRequest are verified in<br>accordance to the provided dss:OptionalInputs-element.<br>Note Note that the eCard-API-Framework MUST return a warning message (…<br>{hash/signature}AlgorithmNotSuitable), if the algorithms used<br>in the signature do not fulfil the requirements for qualified electronic<br>signatures as defined by the BSI (Federal Office for Information Security)<br>and the Bundesnetzagentur (Federal Network Agency).<br>**----- End of picture text -----**<br>


## **3.2.3 ShowViewer** 

**Name ShowViewer Description** With the ShowViewer function, documents (refer to [DSS], Section 2.4.2), signed objects (refer to dss:SignatureObject on page 25) or corresponding verification results in form of a VerificationReport element according to [SigVer] MAY be displayed in a trustworthy manner. This functionality MAY, for example, be used in SignRequest (for displaying the signed data) or in the VerifyRequest function (for displaying signed objects and verification results). **Invocation parameters** Invocation of the ShowViewer function. **Name Description** 

Bundesamt für Sicherheit in der Informationstechnik 

32 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0033-00.png)


**----- Start of picture text -----**<br>
ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed,<br>the parameter is omitted.<br>TrustedViewerId Contains the unique ID of the trusted viewer used for<br>display purposes. If this element is missing, the<br>configured default viewer is used (also refer to<br>[TR-03112-3]).<br>Document The Document element, which MAY occur several<br>times, contains a document for display (for details<br>refer to [DSS], Section 2.4.2). If this is permitted by<br>the applicable security policy, equivalent documents<br>MAY be shown in an overview list (also refer to<br>[gemKon]) or only a certain random sample of the<br>transmitted documents can be fully displayed.<br>StyleSheetContent An XSL stylesheet MAY be transmitted in this element<br>which MAY be used to display XML documents. If the<br>transmitted stylesheet is not suitable for displaying the<br>transmitted documents, a corresponding error message<br>/resultminor/il/viewer#unsuiteableSylesheetForDocum<br>ent is returned.<br>ViewerMessage MAY contain additional, short messages which the<br>trusted viewer displays in addition to the used data<br>(see below for details). If a transmitted message is too<br>long to be displayed by the viewer (e.g. at the top of<br>the window), this produces the error message<br>/resultminor/il/viewer#viewerMessageTooLong.<br>If this element is missing, corresponding standard<br>messages are used by the trusted viewer.<br>Timeout States whether the display on the viewer should be<br>switched off automatically after a specific time (in<br>seconds) in the event of no user interaction. If this<br>element is missing, the display SHOULD be cancelled<br>after 30 seconds.<br>With the ViewerMessage element the trusted viewer MAY be given additional<br>messages for the top or body of the window.<br>Name Description<br>FrameMessage MAY contain a text which is displayed at the top of a<br>window.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

33 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0034-00.png)


**----- Start of picture text -----**<br>
BodyMessage MAY contain a text which is displayed in the body of a<br>window.<br>Return<br>Return of the ShowViewer function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Status information and errors with ShowViewerResponse (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error code<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/dp#communicationError<br>• /resultminor/dp#trustedChannelEstablishmentFailed<br>• /resultminor/dp#unknownProtocol<br>• /resultminor/dp#unknownWebserviceBinding<br>• /resultminor/il/viewer#timeout<br>• /resultminor/il/viewer#cancelationByUser<br>• /resultminor/il/signature#unknownViewer<br>• /resultminor/il/viewer#<br>unsuiteableSylesheetForDocument<br>• /resultminor/il/viewer#viewerMessageTooLong<br>ResultMessage MAY contain more detailed information on the error that<br>occurred if required.<br>Precondition<br>Postcondition<br>Note For security reasons this function SHOULD NOT be made available to the Client<br>application, but only be invoked in a precisely defined context within the functions<br>SignRequest and VerifyRequest.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

34 

Note that the user interface of the eCard-API-Framework in the ShowViewer-function MUST provide an appropriate warning message to the user, if the algorithms related to a qualified electronic signature do not fulfil the requirements defined by the BSI (Federal Office for Information Security) and the Bundesnetzagentur (Federal Network Agency). 

## **3.3 Encryption functions** 

## **3.3.1 EncryptRequest** 

**Name EncryptRequest Description** Transmitted documents are encrypted with the EncryptDocument function. **Invocation parameters** Invocation of the EncryptRequest function. **Name Description** dss:OptionalInputs MAY contain any or all of the following elements, for which detailed information is provided below: **•** ConnectionHandle **•** EncryptionKey **•** ContentEncryptionMethod **•** EncryptionContent dss:InputDocuments Contains a series of dss:Document elements, which are to be (partly) encrypted (refer to [DSS], Section 2.4.2). 

Bundesamt für Sicherheit in der Informationstechnik 

35 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0036-00.png)


The ConnectionHandle-element MAY appear in dss:OptionalInputs. It contains a handle with which the connection to a card application is addressed. If the encryption is not performed by a smart card this element is to be omitted. The ConnectionHandleType is defined and explained in [TR-03112-4]. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0036-02.png)


For each pair of document and recipient the EncryptionKey-element (refer to [SigEnc]) is included in dss:OptionalInputs. **Name Description** 

Bundesamt für Sicherheit in der Informationstechnik 

36 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0037-00.png)


**----- Start of picture text -----**<br>
ds:KeyInfo Specifies the key of the recipient. Refer to<br>[RFC3275] for details concerning the structure<br>of this element. Among the various possibilities<br>at least the following two options MUST be<br>supported:<br>• ds:KeyValue contains a symmetric<br>key, which serves as content encryption<br>key used for ciphering the data and<br>MUST be suitable for the applied<br>ContentEncryptionMethod (see<br>below).<br>• ds:X509Data/ds:X509Certific<br>ate contains an X.509-certificate,<br>which is used for encrypting the content<br>encryption key, which is either provided<br>in the ds:KeyValue-element<br>mentioned above or generated at<br>random.<br>Other Specifies the key of the recipient using some<br>other means. This document specifies two<br>possibilities:<br>• In order to address a Differential Identity<br>(DID) in a connected card application<br>(cf. [ISO24727-3] and [TR-03112-4])<br>specified by the<br>ConnectionHandle-element above<br>the following two elements appear as<br>child-element of Other:<br>• DIDName - Contains the name of the<br>DID which is to be used for generating<br>the signature.<br>• DIDScope - MAY be used to resolve<br>any ambiguity between local and global<br>DIDs with the same name.<br>• In order to address a certificate stored on<br>a connected card application the<br>CertificateRef-element appears as<br>child-element of Other. Please refer to<br>[TR-03112-7] for details with respect to<br>the CertificateRef-element.<br>KeyEncryptionMethod This element is optional and MAY be used to<br>specify how the content encryption key is to be<br>enciphered.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

37 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0038-00.png)


The element ContentEncryptionMethod MAY be included in dss:OptionalInputs to specify which content encryption algorithm is to be used in this request. If the element is missing, the configured DefaultContentEncryptionMethod is used (see [TR-03112-3]). Please refer to [XMLEnc] for details of the EncryptionMethodType. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0038-02.png)


The element EncryptionContent MAY be used to specify details of the encryption process. Using the EncryptionSyntax-Attribute it is possible to specify whether a given (XML-) document is to be encrypted with [XMLEnc] or [RFC3369] for example. Please refer to [SigEnc] for more details. 

**Name Description** DetachEncryptedKeys MAY be used to specify where the encrypted keys shall be inserted into an encrypted XML-document. If this element is missing, the xenc:EncryptedKey elements will be added directly to xenc:EncryptedData (under ds:KeyInfo). If a document is to be encrypted with CMS [RFC3369] for example, this element is ignored. 

Bundesamt für Sicherheit in der Informationstechnik 

38 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0039-00.png)


**----- Start of picture text -----**<br>
xenc:Encryption MAY be used to provide more information on the<br>Properties generation of the xenc:EncryptedData or<br>xenc:EncryptedKey-elements. Please refer<br>to [XMLEnc] Section 3.7 for details.<br>EncryptAndReplace States which parts of a transmitted XML<br>Data document should be encrypted. Details on the<br>dsse:SelectorType can be found in<br>[SigEnc].<br>If a document is to be encrypted with CMS<br>[RFC3369] for example, this element is ignored.<br>InsertEncryptedData References an input content to be encrypted and<br>specifies where to insert the resulting<br>xenc:EncryptedData within the<br>dsse:EncryptedDocument, which is to be<br>returned. Details on the<br>dsse:InsertEncryptedDataType can be<br>found in [SigEnc].<br>If a document is to be encrypted with CMS<br>[RFC3369] for example, this element is ignored.<br>Return<br>The EncryptResponse element is the return of the function<br>EncryptRequest.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>dss:OptionalOutputs The optional element<br>dss:OptionalOutputs contains the results<br>of the encryption process in form of<br>EncryptedDocument-elements.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

39 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0040-00.png)


**----- Start of picture text -----**<br>
For each encrypted document an EncryptedDocument-element is returned in<br>dss:OptionalOutputs. The EncryptedDocumentType is an extension<br>of the dss:DocumentType (refer to [DSS], Section 2.4.2) by the two optional<br>elements EncryptedKeyParentSelector and<br>EncryptedDataSelector explained below. The chosen alternative for the<br>document-format (InlineXML, Base64XML etc.) MUST be identical to the<br>alternative provided in dss:InputDocuments (refer to page 35).<br>Name Description<br>EncryptedKeyParent This optional element MAY be used to provide<br>Selector an XPath expression which points to the parent<br>of the encrypted content keys<br>(xenc:EncryptedKey-elements)..<br>EncryptedData This optional element MAY be used to provide<br>Selector XPath expressions which point to the encrypted<br>data (xenc:EncryptedData) elements.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

40 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0041-00.png)


**----- Start of picture text -----**<br>
Status information and errors with EncryptResponse (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

41 

|||ResultMinor|**•**<br>/resultminor/al/common#noPermission<br>**•**<br>/resultminor/al/common#internalError<br>**•**<br>/resultminor/al/common#parameterError<br>**•**<br>/resultminor/dp#unknownChannelHandle<br>**•**<br>/resultminor/dp#communicationError<br>**•**<br>/resultminor/dp#<br>trustedChannelEstablishmentFailed<br>**•**<br>/resultminor/dp#unknownProtocol<br>**•**<br>/resultminor/dp#unknownWebserviceBinding<br>**•**<br>/resultminor/sal#unknownDataSetName<br>**•**<br>/resultminor/sal#unknownDSIName<br>**•**<br>/resultminor/il/signature#certificateNotFound<br>**•**<br>/resultminor/il/signature#<br>certificateFormatNotCorrect<br>**•**<br>/resultminor/il/signature#<br>invalidCertificateReference<br>**•**<br>/resultminor/il/signature#<br>certificateChainInterrupted<br>**•**<br>/resultminor/il/service#<br>ocspResponderUnreachable<br>**•**<br>/resultminor/il/service#<br>directoryServiceUnreachable<br>**•**<br>/resultminor/il/signature#<br>certificatePathNotValidated<br>**•**<br>/resultminor/il/signature#<br>certificateStatusNotChecked<br>**•**<br>/resultminor/sal#digitalSignatureNotCorrect<br>**•**<br>/resultminor/il/signature#<br>signatureAlgorithmNotSuitable<br>**•**<br>/resultminor/il/signature#invalidCertificatePath<br>**•**<br>/resultminor/il/signature#certificateRevoked<br>**•**<br>/resultminor/il/signature#referenceTime<br>NotWithinCertificateValidityPeriod<br>**•**<br>/resultminor/il/encryption#encryptionO<br>fCertainNodesOnlyForXMLDocuments<br>**•**<br>/resultminor/il/encryption#<br>encryptionFormatNotSupported<br>**•**<br>/resultminor/il/encryption#invalidCertificate<br>**•**<br>/resultminor/il/key#keyGenerationNotPossible<br>**•**<br>/resultminor/il/key#<br>encryptionAlgorithmNotSupported||
|---|---|---|---|---|
||42||Bundesamt für Sicherheit in der Informationste|chnik|




![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0043-00.png)


**----- Start of picture text -----**<br>
ResultMessage MAY contain more detailed information on the error<br>that occurred if required.<br>Precondition If the encryption is to be performed for or with a connected card, a<br>corresponding, valid ConnectionHandle MUST exist.<br>Postcondition The encrypted documents are returned in form of EncryptedDocument<br>elements.<br>Note This function MAY use the [ISO24727-3] functions Encipher, DIDGet,<br>DataSetSelect, DSIRead and, for generation of message keys,<br>GetRandom (also refer to [TR-03112-4]).<br>Also refer to the EncryptDocument function in [gemKon].<br>**----- End of picture text -----**<br>


## **3.3.2 DecryptRequest** 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0043-02.png)


**----- Start of picture text -----**<br>
Name DecryptRequest<br>Description Encrypted documents are decrypted with the DecryptDocument function.<br>Invocation<br>parameters<br>Invocation of the DecryptRequest function.<br>Name Description<br>dss:OptionalInputs MAY contain any or all of the following elements,<br>for which detailed information is provided below:<br>• ConnectionHandle<br>• KeySelector<br>If these elements are missing, the<br>eCard-API-Framework MUST try to determine<br>suitable keys in the connected card applications for<br>decrypting the data. If this fails, a corresponding<br>error /resultminor/sal#decryptionNotPossible is<br>returned.<br>dss:InputDocuments Contains a sequence of dss:Document elements,<br>which are to be decrypted (refer to [DSS], Section<br>2.4.2).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

43 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0044-00.png)


The ConnectionHandle-element MAY appear in dss:OptionalInputs. It contains a handle with which the connection to a card application is addressed. The ConnectionHandleType is defined and explained in [TR-03112-4]. 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0044-02.png)


The KeySelector-element MAY appear in dss:OptionalInputs and addresses the key used for decrypting. If it is up to the eCard-API-Framework to choose an appropriate key this element MAY be omitted. The KeySelector-element is defined and explained in [DSS] (Section 3.5.4). 

In order to address a Differential Identity (DID) in a connected card application (cf. [ISO24727-3] and [TR-03112-4]) specified by the 

ConnectionHandle-element above the following two elements appear as child-element of Other: 

- DIDName - Contains the name of the DID which is to be used for decryption. 

- DIDScope - MAY be used to resolve any ambiguity between local and global DIDs with the same name. 

Bundesamt für Sicherheit in der Informationstechnik 

44 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0045-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the DecryptResponse function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>dss:OptionalOutputs The element dss:OptionalOutputs<br>contains the decrypted documents in form of<br>dss:Document-elements (refer to [DSS],<br>Section 2.4.2).<br>Status information and errors with DecryptResponse (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error code<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/dp#communicationError<br>• /resultminor/dp#<br>trustedChannelEstablishmentFailed<br>• /resultminor/dp#unknownProtocol<br>• /resultminor/dp#unknownWebserviceBinding<br>• /resultminor/sal#namedEntityNotFound<br>• /resultminor/il/encryption#<br>encryptionFormatNotSupported<br>• /resultminor/sal#decryptionNotPossible<br>• /resultminor/sal#securityConditionsNotSatisfied<br>• /resultminor/ifdl/terminal#noCard<br>ResultMessage MAY contain more detailed information on the occurred<br>error if required.<br>Precondition Suitable keys MUST be available to the eCard-API-Framework for decryption of<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

45 


![](markdown/tr/TR-03112-api_teil2/TR-03112-api_teil2.pdf-0046-00.png)


**----- Start of picture text -----**<br>
the documents as differential identity on a connected card application.<br>Postcondition The decrypted documents are returned.<br>Note This function uses the [ISO24727-3] function Decipher (also refer to<br>[TR-03112-4]).<br>Also refer to the DecryptDocument function in [gemKon].<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

46 

## **References** 

|[SigEnc]|A-SIT: C. Orthacker: Proposal for an Encryption Profile for OASIS DSS (including|
|---|---|
||schema)|
|[PDF]|Adobe: Portable Document Format Reference Manual|
|[TR-03112-1]|BSI: TR-03112-1: eCard-API-Framework – Part 1: Overview and Generic Mechanisms|
|[TR-03112-2]|BSI: TR-03112-2: eCard-API-Framework – Part 2: eCard-Interface|
|[TR-03112-3]|BSI: TR-03112-3: eCard-API-Framework – Part 3: Management-Interface|
|[TR-03112-4]|BSI: TR-03112-4: eCard-API-Framework – Part 4: ISO24727-3-Interface|
|[TR-03112-5]|BSI: TR-03112-5: eCard-API Framework – Part 5: Suppor- Interface|
|[TR-03112-6]|BSI: TR-03112-6: eCard-API-Framework – Part 6: IFD-Interface|
|[TR-03112-7]|BSI: TR-03112-7: eCard-API-Framework – Part 7: Protocols|
|[TR-03114]|BSI: TR-03114: Stapelsignatur mit dem Heilberufsausweis|
|[TS101733]|ETSI: TS 101 733: Electronic Signature Formats, Electronic Signatures and|
||Infrastructures (ESI) – Technical Specification|
|[gemKon]|gematik: Connector specification|
|[RFC2119]|IETF: RFC 2119: S. Bradner: Key words for use in RFCs to Indicate Requirement Levels|
|[RFC2560]|IETF: RFC 2560: M. Myers, R. Ankney, A. Malpani, S. Galperin, C. Adams: X.509|
||Internet Public Key Infrastructure - Online Certificate Status Protocol – OCSP|
|[RFC3161]|IETF: RFC 3161: C. Adams, P. Cain, D. Pinkas, R. Zuccherato: Internet X.509 Public|
||Key Infrastructure Time-Stamp Protocol (TSP)|
|[RFC3275]|IETF: RFC 3275: D. Eastlage, J. Reagle, D. Solo: (Extensible Markup Language)|
||XMLSignature Syntax and Processing|
|[RFC3280]|IETF: RFC 3280: R. Housley, W. Polk, W. Ford, D. Solo: Internet X.509 Public Key|
||Infrastructure, Certificate and Certificate Revocation List (CRL) Profile|
|[RFC3281]|IETF: RFC 3281: S. Farrell, R. Housley: An Internet Attribute Certificate Profile for|
||Authorization|
|[RFC3369]|IETF: RFC 3369: R. Housley: Cryptographic Message Syntax (CMS)|
|[RFC4998]|IETF: RFC 4998: T. Gondrom, R. Brandner, U. Pordesch: Evidence Record Syntax (ERS)|
|[RFC6283]|IETF: RFC 6283: A. Jerman Blazic, S. Saljic, T. Gondrom: Extensible Markup Language|
||Evidence Record Syntax|
|[ISO24727-3]|ISO: ISO/IEC 24727-3: Identification Cards — Integrated Circuit Cards Programming|
||Interfaces — Part 3: Application Interface|
|[AdES]|OASIS: Advanced Electronic Signature Profiles of the OASIS Digital Signature Service|
||Version 1.0|
|[DSS]|OASIS: Digital Signature Service Core Protocols, Elements, and Bindings|
|[SigGer]|OASIS: German Signature Law Profile of the OASIS Digital Signature Service|
|[SigVer]|OASIS: Profile for comprehensive multi-signature verification reports for OASIS Digital|
||Signature Services|



Bundesamt für Sicherheit in der Informationstechnik 

47 

[SigPol] OASIS: Signature Policy Profile of the OASIS Digital Signature Services [XAdES] W3C: W3C Note: XML Advanced Electronic Signatures (XAdES) [XMLEnc] W3C: W3C Recommendation: XML Encryption Syntax and Processing 

Bundesamt für Sicherheit in der Informationstechnik 

48 


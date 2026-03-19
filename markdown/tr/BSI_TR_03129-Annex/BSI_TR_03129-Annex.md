## Annex to BSI TR-03129 

Cryptographic Message Syntax profile for content signature 

Version 1.0 

## Document history 

|**Version**|**Date**|**Description**|
|---|---|---|
|0.9|2022|Initial Draft|
|1.0|2022|First Version|



Federal Office for Information Security Post Box 20 03 63 D-53133 Bonn E-Mail: eid@bsi.bund.de Internet: https://www.bsi.bund.de © Federal Office for Information Security 2022 

Table of Contents 

## Table of Contents 

||Document history.............................................................................................................................................................................. 2|
|---|---|
|1|Introduction......................................................................................................................................................................................... 5|
|1.1|Terminology.................................................................................................................................................................................... 5|
|2|CMS Container Profles................................................................................................................................................................... 6|
|2.1|Signed Data Container............................................................................................................................................................... 6|
|3|Additional Confgurations............................................................................................................................................................. 9|
|3.1|Content Types................................................................................................................................................................................ 9|
|3.2|Encapsulated Content Types................................................................................................................................................... 9|
|3.3|Signed Attributes........................................................................................................................................................................ 10|
|3.4|Cryptographic Details............................................................................................................................................................... 11|
|3.4.1|<br>Digest Algorithms................................................................................................................................................................ 11|
|3.4.2|<br>Signature Algorithms.........................................................................................................................................................11|
|3.4.3|<br>Domain Parameters............................................................................................................................................................ 11|
||Reference Documentation..........................................................................................................................................................12|



## Tables 

Table 1: Key Words.......................................................................................................................................................................................... 5 Table 2: General CMS Container............................................................................................................................................................... 8 Tabelle 3: ContentType and Object Identifiers..................................................................................................................................9 Tabelle 4: ContentType and Object Identifiers................................................................................................................................10 Table 5: Specific Attributes........................................................................................................................................................................ 10 Table 6: Specific Digest Algorithms......................................................................................................................................................11 Table 7: Specific Signature Algorithms...............................................................................................................................................11 Table 8: Specific Domain Parameters...................................................................................................................................................11 

Federal Office for Information Security 

3 

Introduction 1 

## 1 Introduction 

In the eID infrastructure, data exchange takes place between the entities of the associated PKI. This data exchange, which uses the SOAP messaging protocol, is specified in the BSI TR-03129 series [TR-03129-1], [TR-03129-2] and [TR-03129-3]. Certain messages within this data exchange include a Cryptographic Message Syntax (CMS) container, which contains a signed data structure. The respective content placed in these CMS containers is thereby signed by a dedicated private key. Now the receiving entity of the CMS container is able to verify the authenticity of the respective content if it possesses the corresponding certificate belonging to the sending entity. 

In the context of the eID infrastructure, the receiving entity refers to the DV (which in this case is called "BerCA"). The sending entity refers to the individual eID servers. A dedicated Request Signer Certificate (RSC) is used to sign the CMS container. 

This document specifies the profile of the CMS containers which are used for this purpose. The specification of the Request Signer Certificates for eID applications is defined in [CP-eID]. 

## 1.1 Terminology 

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119]. The key word “CONDITIONAL” is to be interpreted as follows: 

**CONDITIONAL:** The usage of an item is dependent on the usage of other items. It is therefore further qualified under which conditions the item is REQUIRED or RECOMMENDED. 

When used in tables (profiles), the key words are abbreviated as shown in Table 1. 

|**Key word**|**Equivalent**|**Abbrev.**|
|---|---|---|
|MUST / SHALL|REQUIRED|m|
|MUST NOT / SHALL NOT|–|x|
|SHOULD|RECOMMENDED|r|
|MAY|OPTIONAL|o|
|–|CONDITIONAL|c|



_Table 1: Key Words_ 

Federal Office for Information Security 

5 

2 CMS Container Profiles 

## 2 CMS Container Profiles 

CMS and the general structure of a CMS container is described in [RFC 5652]. A CMS container gets defined using the ASN.1 data structure described in [X.208-88]. In the following, the general profile of the applied CMS containers will be specified concretely. 

## 2.1 Signed Data Container 

Table 2 specifies the general profile of the applied CMS container with the type Signed Data. Using this CMS container type, it is possible to embed data in a CMS container and then sign that data digitally. 

According to [RFC 5652],the `SignedData` structure is defined within the sequence `ContentInfo,` 

```
ContentInfo ::= SEQUENCE {
contentType ContentType,
content [0] EXPLICIT ANY DEFINED BY contentType
}
```

The `ContentType` is application-specific and defined in chapter 3.1. The content itself is the `SignedData` structure according to table 2. 

|**Field**|**Comment**|**Type**|**Value**|
|---|---|---|---|
|`SignedData`|MUST|`SEQUENCE`||
|`version`|MUST|`CMSVersion`<br>`(= INTEGER)`|`‘3’`|
|`digestAlgorithms`|MUST|`DigestAlgorithmIdentifiers`<br>`(= SET OF`<br>`DigestAlgorithmIdentifier;`<br>`= AlgorithmIdentifier)`|Covered in chapter<br>3.4.1|
|`encapContentInfo`|MUST|`EncapsulatedContentInfo`<br>`(= SEQUENCE)`|Contains the<br>content to be<br>signed.|
|`eContentType`|MUST|`ContentType`<br>`(= OBJECT IDENTIFIER)`|Covered in chapter<br>3.2|
|`eContent`|MUST|`OCTET STRING`|Contains the<br>specifc content.|
|`certificates`|MAY|`CertificateSet`<br>`(= SET OF`<br>`CertificateChoices;`<br>`= CHOICE {`<br>`certificate Certificate`<br>`,`<br>`extendedCertificate`<br>`ExtendedCertificate,`<br>`v1AttrCert`<br>`AttributeCertificateV1,`<br>`v2AttrCert`<br>`AttributeCertificateV2,`<br>`other`<br>`OtherCertificateFormat })`|The feld is optional.<br>It can contain the<br>self-signed X.509<br>certifcate with<br>which the content<br>is signed (i.e. the<br>RSC). If the<br>certifcate is<br>included, a cross-<br>check must be<br>performed by the<br>recipient with the|



Federal Office for Information Security 

6 

CMS Container Profiles 2 

|**Field**|**Comment**|**Type**|**Value**|
|---|---|---|---|
||||stored certifcate.|
|`crls`|MUST NOT|`RevocationInfoChoices`<br>`(= SET OF`<br>`RevocationInfoChoice;`<br>`= CHOICE {`<br>`crl CertificateList,`<br>`other`<br>`OtherRevocationInfoFormat`<br>`})`|_(Not applicable)_|
|`signerInfos`|MUST|`SignerInfos`<br>`(= SET OF SignerInfo;`<br>`= SEQUENCE)`|Contains necessary<br>information<br>regarding the<br>signature. Only one<br>S`ignerInfo`shall<br>be provided within<br>this feld.|
|`version`|MUST|`CMSVersion`<br>`(= INTEGER)`|`‘1’`|
|`sid`|MUST|`SignerIdentifier`<br>`(= CHOICE {`<br>`issuerAndSerialNumber`<br>`IssuerAndSerialNumber`<br>`,`<br>`subjectKeyIdentifier`<br>`SubjectKeyIdentifier })`|Contains the DN of<br>the certifcate issuer<br>and an issuer-<br>specifc certifcate<br>serial number to<br>identify the<br>respective<br>certifcate.|
|`digestAlgorithm`|MUST|`DigestAlgorithmIdentifier`<br>`(= AlgorithmIdentifier)`|Covered in chapter<br>3.4.1|
|`signedAttrs`|MUST|`SignedAttributes`<br>`(= SET SIZE (1..MAX) OF`<br>`Attribute;`<br>`= SEQUENCE)`|Contains a<br>collection of<br>attributes which get<br>signed additionally.<br>The specifc<br>attributes are<br>covered in chapter<br>3.3.|
|`attrType`|MUST|`OBJECT IDENTIFIER`|Contains the type of<br>the respective<br>attribute.|
|`attrValues`|MUST|`SET OF AttributeValue`<br>`(= ANY)`|Contains the value<br>of the respective<br>attribute.|
|`signatureAlgorithm`|MUST|`SignatureAlgorithmIdentifier`<br>`(= AlgorithmIdentifier)`|Covered in chapter<br>3.4.2|
|`signature`|MUST|`SignatureValue`<br>`(= OCTET STRING)`|Contains the result<br>of the signature<br>generation.|



Federal Office for Information Security 

7 

2 CMS Container Profiles 

|**Field**|**Comment**|**Type**|**Value**|
|---|---|---|---|
|`unsignedAttrs`|MUST NOT|`UnsignedAttributes`<br>`(= SET SIZE (1..MAX) OF`<br>`Attribute:`<br>`= SEQUENCE)`|_(Not applicable)_|



_Table 2: General CMS Container_ 

Federal Office for Information Security 

8 

Additional Configurations 3 

## 3 Additional Configurations 

This section specifies additional configurations, which are referred by table 2. 

## 3.1 Content Types 

_The_ _`ContentType` and the object identifier of the_ _`SignedData` element depends on the use case_ 

|**ContentType**|**Object Identifer**|**Description**|
|---|---|---|
|_`id-eIDServer-`_<br>_`webserverCertifica`_<br>_`te`_|_`itu-t(0) identified-`_<br>_`organization(4) etsi(0)`_<br>_`reserved(127) etsi-identified-`_<br>_`organization(0) bsi-de(7)`_<br>_`applications (3) eID (2)`_<br>_`id-eID-PKI (4) id-eID-PKI-`_<br>_`certificates (1) id-eIDServer-`_<br>_`certificates (1) id-eIDServer-`_<br>_`webserverCertificate(1)`_|TLS server certificate for the<br>entanglement|
|_`id-eIDServer-`_<br>_`PKIComTLSCertifica`_<br>_`teRequest`_|_`itu-t(0) identified-`_<br>_`organization(4) etsi(0)`_<br>_`reserved(127) etsi-identified-`_<br>_`organization(0) bsi-de(7)`_<br>_`applications (3) eID (2)`_<br>_`id-eID-PKI (4) id-eID-PKI-`_<br>_`certificates (1) id-eIDServer-`_<br>_`certificates (1) id-eIDServer-`_<br>_`PKIComTLSCertificate(2) id-`_<br>_`eIDServer-`_<br>_`PKIComTLSCertificateRequest(1)`_|Certificate Signing Request<br>(CSR) for the PKI<br>communication|
|_`id-eIDServer-`_<br>_`requestSignerCerti`_<br>_`ficate`_|_`itu-t(0) identified-`_<br>_`organization(4) etsi(0)`_<br>_`reserved(127) etsi-identified-`_<br>_`organization(0) bsi-de(7)`_<br>_`applications (3) eID (2)`_<br>_`id-eID-PKI (4) id-eID-PKI-`_<br>_`certificates (1) id-eIDServer-`_<br>_`certificates (1)id-eIDServer-`_<br>_`requestSignerCertificate(3)`_|Request Signer Certificate<br>(RSC)|



_Tabelle 3: ContentType and Object Identifiers_ 

## 3.2 Encapsulated Content Types 

_The_ _`ContentType` and the object identifier of the_ _`eContentType` element depends on the use case_ 

|**eContentType**|**Object Identifer**|**Description**|
|---|---|---|
|_`pkix(7)`_|_`{iso(1) identified-`_<br>_`organization(3) dod(6)`_<br>_`internet(1) security(5)`_|X.509 certificate according to<br>[RFC 5280]|



Federal Office for Information Security 

9 

3 Additional Configurations 

|**eContentType**|**Object Identifer**|**Description**|
|---|---|---|
||_`mechanisms(5) pkix(7)}`_||
|_`PKCS-10`_|_`{iso(1) member-body(2) us(840)`_<br>_`rsadsi(113549) pkcs(1) pkcs-`_<br>_`10(10) }`_|Certificate Signing Request<br>(CSR)according to [RFC 2986]|



_Tabelle 4: ContentType and Object Identifiers_ 

## 3.3 Signed Attributes 

Within the set of attributes to be signed, the following attributes have to be present. 

The object identifiers of these attributes were obtained from [RFC 5652]. 

|**Type**|**Value**|
|---|---|
|_content-type attribute_||
|`attrType`|`{ iso(1) member-body(2) us(840) rsadsi(113549)`<br>`pkcs(1) pkcs-9(9) id-contentType(3) }`|
|`attrValues`|Contains the '`eContentType`' of the respective container as type<br>OBJECT IDENTIFIER.|
|_message-digest attribute_||
|`attrType`|`{ iso(1) member-body(2) us(840) rsadsi(113549)`<br>`pkcs(1) pkcs-9(9) id-messageDigest(4) }`|
|`attrValues`|Contains the message digest of the '`eContent`' of the respective<br>container as type OCTET STRING.|



_Table 5: Specific Attributes_ 

## 3.4 Cryptographic Details 

Request Signer Certificates are self-signed X.509 certificates according to [RFC 5280]. The domain parameters of the public key of a Request Signer Certificate must correspond to the domain parameters of CVCA certificates. The domain parameters of CVCA certificates are specified in [TR-03116-2]. Depending on this, the matching cryptographic algorithms and parameters must be used within the CMS container. 

## 3.4.1 Digest Algorithms 

The digests algorithms listed in table 6 have to be applied. 

The object identifiers of these algorithms are obtained from [RFC 5754]. 

Federal Office for Information Security 

10 

Additional Configurations 3 

|**Algorithm**|**Length**|**Object Identifer**|
|---|---|---|
|SHA-256|256 Bit|`{ joint-iso-itu-t(2) country(16) us(840)`<br>`organization(1) gov(101) csor(3) nistAlgorithms(4)`<br>`hashalgs(2) sha256(1) }`|



_Table 6: Specific Digest Algorithms_ 

## 3.4.2 Signature Algorithms 

The signature algorithms listed in table 7 have to be applied. 

The object identifiers of these algorithms are obtained from [TR-03111]. 

|**Algorithm**|**Length**|**Object Identifer**|
|---|---|---|
|ECDSA|256 Bit|`{ itu-t(0) identified-organization(4) etsi(0)`<br>`reserved(127) etsi-identified-organization(0) bsi-`<br>`de(7) algorithms(1) id-ecc(1) signatures(4) ecdsa-`<br>`plain-signatures(1) ecdsa-plain-SHA256(3) }`|



_Table 7: Specific Signature Algorithms_ 

## 3.4.3 Domain Parameters 

The domain parameters for elliptic curves listed in table 8 have to be applied. 

The object identifiers of these specific curves are obtained from [RFC 5639]. 

|**Curve**|**Length**|**Object Identifer**|
|---|---|---|
|brainpoolP256r1|256 Bit|`{ iso(1) identified-organization(3) teletrust(36)`<br>`algorithm(3) signatureAlgorithm(3) ecSign(2)`<br>`ecStdCurvesAndGeneration(8)`<br>`ellipticCurve(1) versionOne(1)`<br>`brainpoolP256r1(7) }`|



_Table 8: Specific Domain Parameters_ 

Federal Office for Information Security 

11 

Reference Documentation 

## Reference Documentation 

TR-03129-1 BSI: Protocols for the Management of Certificates and CRLs in Public-KeyInfrastructures (PKIs), Part 1: Common Specifications, 2022 TR-03129-2 BSI: PKIs for Machine Readable Travel Documents, Part 2: Supplemental specifications for public and official authorities, 2017 TR-03129-3 BSI: Protocols for the Management of Certificates and CRLs in Public-KeyInfrastructures (PKIs), Part 3: Electronic Identity (eID) documents based on Extended Access Control (EAC), 2022 CP-eID BSI: Certificate Policy für die Country Verifying Certification Authority, eIDAnwendung, 2021 RFC 2119 S. Bradner: Key words for use in RFCs to Indicate Requirement Levels, 1997 RFC 5652 R. Housley: Cryptographic Message Syntax (CMS), 2009 X.208-88 CCITT: Recommendation X.208: Specification of Abstract Syntax Notation One (ASN.1), 1988 RFC 5280 D. Cooper, et al.: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile, 2008 RFC 2986 M. Nystrom, B. Kaliski: PKCS #10: Certification Request Syntax Specification Version 1.7, 2000 TR-03116-2 BSI: Kryptographische Vorgaben für Projekte der Bundesregierung, Teil 2: Hoheitliche und eID-Dokumente, 2022 RFC 5754 S. Turner: Using SHA2 Algorithms with Cryptographic Message Syntax, 2010 TR-03111 BSI: Elliptic Curve Cryptography, 2018 RFC 5639 M. Lochter, et al.: Elliptic Curve Cryptography (ECC) Brainpool Standard Curves and Curve Generation, 2010 

Federal Office for Information Security 

12 


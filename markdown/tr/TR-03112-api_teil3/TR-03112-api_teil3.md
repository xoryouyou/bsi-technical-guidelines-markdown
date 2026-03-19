
![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0001-00.png)


Technical Guideline TR-03112-3 eCard-API-Framework – Management-Interface Version 1.1.5 

7. April 2015 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn 

E-Mail: ecard.api@bsi.bund.de Internet: https://www.bsi.bund.de 

© Bundesamt für Sicherheit in der Informationstechnik 2015 

## **Contents** 

|1|Overview of the eCard-API-Framework.................................................................................................5|
|---|---|
|1.1|Key Words.........................................................................................................................................5|
|1.2|XML-Schema....................................................................................................................................6|
|2|Overview of the Management-Interface.................................................................................................7|
|2.1|Objective...........................................................................................................................................7|
|2.2|Functions...........................................................................................................................................7|
|2.2.1|Management of the eCard-API-Framework.................................................................................7|
|2.2.2|Card management.........................................................................................................................8|
|2.2.3|Card terminal management...........................................................................................................8|
|2.2.4|Trusted viewer management.........................................................................................................8|
|2.2.5|Identity management....................................................................................................................8|
|2.2.6|Service management.....................................................................................................................9|
|3|Specification of the eCard Management-Interface................................................................................10|
|3.1|Management of the eCard-API-Framework.....................................................................................10|
|3.1.1|InitializeFramework...................................................................................................................10|
|3.1.2|TerminateFramework..................................................................................................................11|
|3.1.3|APIACLList...............................................................................................................................12|
|3.1.4|APIACLModify.........................................................................................................................16|
|3.1.5|FrameworkUpdate......................................................................................................................18|
|3.1.6|GetDefaultParameters.................................................................................................................19|
|3.1.7|SetDefaultParameters.................................................................................................................26|
|3.2|Card management............................................................................................................................28|
|3.2.1|GetCardInfoList.........................................................................................................................28|
|3.2.2|SetCardInfoList..........................................................................................................................29|
|3.2.3|AddCardInfoFiles.......................................................................................................................31|
|3.2.4|DeleteCardInfoFiles...................................................................................................................33|
|3.3|Card terminal management..............................................................................................................34|
|3.3.1|RegisterIFD................................................................................................................................34|
|3.3.2|UnregisterIFD.............................................................................................................................37|
|3.4|Trusted viewer management............................................................................................................39|
|3.4.1|GetTrustedViewerList................................................................................................................39|
|3.4.2|GetTrustedViewerConfiguration.................................................................................................40|
|3.4.3|SetTrustedViewerConfiguration.................................................................................................42|
|3.4.4|AddTrustedViewer.....................................................................................................................44|
|3.4.5|DeleteTrustedViewer..................................................................................................................45|
|3.5|Identity management.......................................................................................................................46|
|3.5.1|GetTrustedIdentities...................................................................................................................46|
|3.5.2|AddTrustedCertificate................................................................................................................49|
|3.5.3|AddCertificate............................................................................................................................50|
|3.5.4|ExportCertificate........................................................................................................................54|
|3.5.5|DeleteCertificate.........................................................................................................................55|
|3.5.6|AddTSL......................................................................................................................................56|
|3.5.7|ExportTSL..................................................................................................................................59|
|3.5.8|DeleteTSL..................................................................................................................................60|
|3.6|Service management........................................................................................................................62|
|3.6.1|GetOCSPServices.......................................................................................................................62|
|3.6.2|SetOCSPServices.......................................................................................................................64|



Bundesamt für Sicherheit in der Informationstechnik 

3 

|3.6.3|GetDirectoryServices.................................................................................................................65|
|---|---|
|3.6.4|SetDirectoryServices..................................................................................................................66|
|3.6.5|GetTSServices............................................................................................................................68|
|3.6.6|SetTSServices.............................................................................................................................70|



## **Table of Figures** 

Bundesamt für Sicherheit in der Informationstechnik 

4 

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

5 

## **1.2 XML-Schema** 

A XML-Schema is provided together with this Technical Guideline. In case of incongruencies, the specifications in this text take precedence. The graphical representations of the XML-Schema illustrate the schema. Note that the text of this Guideline might further restrict the presence or mulitplicity of elements as compared to the schema definition. 

Bundesamt für Sicherheit in der Informationstechnik 

6 

## **2 Overview of the Management-Interface** 

## **2.1 Objective** 

The Management-Interface provides important administration functions for the eCard-API-Framework. 

## **2.2 Functions** 

The Management-Interface provides the following function groups: 

- Management of the eCard-API-Framework 

- Card management 

- Card terminal management 

- Trusted viewer management 

- Identity management 

- Service management 

## **2.2.1 Management of the eCard-API-Framework** 

This function group includes functions for the management of the eCard-API framework itself: 

- The InitializeFramework function initialises the eCard-API-Framework. 

- The TerminateFramework function terminates all sessions and services of the eCard-API-Framework. 

- The APIACLList function is OPTIONAL and MAY provide the currently defined access control regulations for access to the individual functions of the eCard-API-Framework. If this function is supported it MAY ONLY be made available to an _**administrator**_ who is authenticated in accordance with the applicable security policies for the operation of the eCard-API-Framework. 

- The ACLModify function is OPTIONAL and MAY be used to modify the access control rules which govern the access to the functions of the eCard-API-Framework. Via this access control mechanism it is possible, for example, to grant or refuse access of an application to the Transmit function in the IFD-Interface (also refer to [TR-03112-6]) for the implementation of a "transparent channel" to a card. As a consequence, it is also possible to define whether and under which circumstances remote eCard-API-Frameworks are allowed to access a local eCard-API-Framework. If this function is supported it MAY ONLY be made available to an _**administrator**_ who is authenticated in accordance with the applicable security policies applicable for operation of the eCard-API-Framework. 

- The FrameworkUpdate function checks whether an update is available for the eCard-API-Framework and performs such an update if necessary. The detailed processes during execution of this function are protocol-specific (refer to [TR-03112-7]). 

- GetDefaultParameters: Default behaviour can be specified for the eCard-API-Framework to also permit the easiest possible invocations by the client application for potentially complex operations (e.g. for creating and verifying electronic signatures, refer to [TR-03112-2], Section 

Bundesamt für Sicherheit in der Informationstechnik 

7 

3.2.1 - 3.2.2). The currently specified default parameters MAY be read out with the GetDefaultParameters function. 

- The SetDefaultParameters function is used to write the default parameters, which then determine the standard behaviour of the eCard-API-Framework. 

## **2.2.2 Card management** 

- The GetCardInfoList function supplies the list of card types which are known from the CardInfo files. 

- The SetCardInfoList function saves an ordered list of card types in form of URIs, which determine the steps during the card recognition procedure. 

- With the AddCardInfoFiles function it is possible to add a series of CardInfo files. 

- The DeleteCardInfoFiles function deletes a series of CardInfo files. 

## **2.2.3 Card terminal management** 

- With the RegisterIFD function it is possible to add a card terminal with all configuration information. 

- The UnregisterIFD function deletes a card terminal. 

## **2.2.4 Trusted viewer management** 

- The GetTrustedViewerList function provides a list of available trustworthy display components (trusted viewer). 

- The GetTrustedViewerConfiguration function reads the configuration information for a specific trusted viewer which is stored in the eCard-API-Framework. 

- The SetTrustedViewerConfiguration function writes the configuration information for a specific trusted viewer. 

- With the AddTrustedViewer function, a trusted viewer can be added with all configuration information. 

- The DeleteTrustedViewer function deletes a trusted viewer. 

## **2.2.5 Identity management** 

- The GetTrustedIdentities function provides a list of the trustworthy identities in form of Trust-Service status lists (TSL) and trustworthy certificates. 

- With the AddTrustedCertificate function, a certificate can be added to the list of trusted certificates. 

- With the AddCertificate function, a non-trustworthy certificate which can be used for signature verification or encryption can be added to the certificate database. 

- With the ExportCertificate function, a (trustworthy or non-trustworthy) certificate can be exported. 

Bundesamt für Sicherheit in der Informationstechnik 

8 

- The DeleteCertificate function deletes an existing (trustworthy or non-trustworthy) certificate from the certificate database. 

- With the AddTSL function, a Trust-Service status list can be added to the eCard-API-Framework. 

- With the ExportTSL function, a Trust-Service status list can be exported. 

- With the DeleteTSL function, a Trust-Service status list can be deleted from the list of trustworthy identities. 

## **2.2.6 Service management** 

- The GetOCSPServices function reads the list of available OCSP responders together with the corresponding configuration information. 

- The SetOCSPServices function writes the list of available OCSP responders together with the corresponding configuration information. 

- The GetDirectoryServices function reads the list of the directory services accessible via LDAP or HTTP with all corresponding configuration information. 

- The SetDirectoryServices function writes a list of the directory services accessible via LDAP or HTTP with all corresponding configuration information. 

- The GetTSServices function reads the list of time stamping services with all corresponding configuration information. 

- The SetTSServices function writes a list of time stamping services together with all corresponding configuration information. 

Bundesamt für Sicherheit in der Informationstechnik 

9 

## **3 Specification of the eCard Management-Interface** 

## **3.1 Management of the eCard-API-Framework** 

## **3.1.1 InitializeFramework** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0010-03.png)


**----- Start of picture text -----**<br>
Name InitializeFramework<br>Description The InitializeFramework function initialises the eCard-API-Framework<br>and can be used to query the version of the framework implementation.<br>Invocation<br>parameters<br>Invocation of the InitializeFramework function.<br>No invocation parameters<br>Return<br>Return of the InitializeFramework function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more<br>detail below.<br>Version States the version of the eCard-API-Framework started<br>with this function and comprises up to three integers<br>Major, Minor (optional) and SubMinor (optional).<br>Compliance to this version of the<br>eCard-API-Framework SHALL be indicated by (Ma-<br>jor.Minor.Subminor) = (1.1.5).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

10 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0011-00.png)


**----- Start of picture text -----**<br>
Status information and errors in InitializeFramework (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>ResultMessage MAY contain more detailed information on the<br>error which occurred if required.<br>Precondition The service required for initialisation of the eCard-API-Framework with<br>InitializeFramework is started by mechanisms of the operating system.<br>Postcondition The eCard-API-Framework is initialised, and the functions available according<br>to the APIACL (also refer to 3.1.3) can then be invoked by the client application.<br>Note For initialisation of the eCard-API-Framework, the function Initialize<br>(also refer to [ISO24727-3]) is primarily invoked, and a context with the IFD<br>layer is established with the function EstablishContext (also refer to<br>[ISO24727-4]).<br>As there is no error, if this function is called and the framework already has been<br>initialized, this function MAY be used at any time to query its version.<br>**----- End of picture text -----**<br>


## **3.1.2 TerminateFramework** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0011-02.png)


**----- Start of picture text -----**<br>
Name TerminateFramework<br>Description The TerminateFramework function terminates the eCard-API-Framework,<br>closes any open connections and executes any necessary updates (also refer to<br>[TR-03112-7]).<br>Invocation<br>parameters<br>Invocation of the TerminateFramework function.<br>No invocation parameters<br>Return<br>Return of the TerminateFramework function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more<br>detail below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

11 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0012-00.png)


**----- Start of picture text -----**<br>
Status information and errors in Terminate (also refer to [TR-03112-1]<br>Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor  • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>ResultMinor • /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/common#<br>sessionTerminatedWarning<br>• /resultminor/al/common#notInitialized<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition The eCard-API-Framework was initialised.<br>Postcondition The eCard-API-Framework was terminated so that only the<br>InitializeFramework function can be invoked.<br>Note This function terminates all open card connections using<br>CardApplicationDisconnect (also refer to [TR-03112-4]) and<br>Disconnect (also refer to [TR-03112-6]) and then finally invokes<br>Terminate (also refer to [TR-03112-4]), ReleaseContext (also refer to<br>[TR-03112-6]) and TC_API_Close (also refer to [TR-03112-2]). In addition,<br>any necessary updates are performed as a final action (also refer to<br>[TR-03112-7]); these updates apply the next time the system is started.<br>**----- End of picture text -----**<br>


## **3.1.3 APIACLList** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0012-02.png)


**----- Start of picture text -----**<br>
Name APIACLList<br>Description The APIACLList function is OPTIONAL and returns the access control list<br>for the stated APICall(s).<br>If this function is supported it MAY ONLY be made available to an<br>administrator  who is authenticated in accordance with the applicable<br>security policy for operation of the eCard-API-Framework.<br>Invocation<br>parameters<br>Invocation of the APIACLList function.<br>Name Description<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

12 

APICall MAY occur several times and contains the name of the APICall of the eCard-API framework for which the access control information is to be determined. In this context access control information for all functions defined in the framework of the eCard-API-Framework MUST be supported. In addition, access control information for functions MAY be managed in additional "convenience layers". **Return parameters** 

## Return of the APIACLList function. 

**Name Description** dss:Result Contains the status information and the errors of an executed action. This element is described in more detail below. APIAccessControlList Contains the access control information for all stated APICalls of the eCard-API-Framework (see below for details). 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0013-03.png)


The APIAccessControlList element comprises a series of APIAccessControlRule elements which each defines an access control rule for access to the APICalls (see below for details). 

**Name Description** APIAccessRule Contains an access control rule for an APICall (see below for details). In this context, the principle that an access which is not explicitly permitted is forbidden applies. 

Bundesamt für Sicherheit in der Informationstechnik 

13 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0014-00.png)


**----- Start of picture text -----**<br>
The APIAccessControlRule element is part of the<br>APIAccessControlList element above and contains the access control<br>information for an API function.<br>Name Description<br>APICall Contains the name of the API function. An<br>overview of the eCard-API-Framework is<br>provided in [TR-03112-1]. In addition, it<br>MUST be possible to manage access<br>control information for functions in<br>"convenience layers" so that in certain<br>application scenarios — and if necessary<br>for certain smart card types (e.g.<br>electronic health card) - only access to<br>well-defined and especially verified<br>special applications is possible.<br>Address MAY specify permissible IP addresses and<br>ports in the format  Address:Port  (d.h.<br>aaa.bbb.ccc.ddd:Port) to which the<br>respective access control rule refers.<br>In this context, the wildcard "*" MAY also<br>be used (e.g. "77.87.*.*:*").<br>If this element is missing, the access<br>control rule refers to local access to the<br>eCard-API-Framework via the C- or<br>Java-interface (also refer to<br>[TR-03112-1]).<br>TC_Protocol MAY specify to which trusted channel<br>protocol (also refer to<br>CardApplicationPath in<br>[TR-03112-4]) the access control rule<br>refers.<br>If this element is missing, no trusted<br>channel protocol is assumed for the<br>respective access control rule.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

14 

APISecurityCondition Contains the security condition for this access control rule. See below for details. 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0015-01.png)


APISecurityCondition is part of APIAccessControlRule (see above). With this structure any Boolean expression can be stated from elementary authentication conditions in a manner similar to the SecurityCondition for AccessRules in accordance with [ISO24727-3] (also refer to [TR-03112-4]). 

Such an APIAuthenticationState is defined as follows: 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0015-04.png)


**Name** 

**Description** 

DIDName Specifies the name of a DID in a _security module_ which is permanently assigned to the eCard-API-Framework. DIDScope Is an optional parameter which resolves any ambivalence between local and global DIDs with the same name. If the DID is already uniquely specified by the stated DIDName, this element MAY be omitted. 

Bundesamt für Sicherheit in der Informationstechnik 

15 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0016-00.png)


**----- Start of picture text -----**<br>
DIDStateQualifier MAY be used for certificate-based<br>authentication processes on cards (also refer<br>to [TR-03112-7]).<br>Certificate Specifies the certificate stored in the<br>certificate database which serves as trust<br>anchor in the event of a non-card based<br>authentication (e.g. by means of TLS, also<br>refer to CardApplicationPath in<br>[TR-03112-4] and TC_API_Open in<br>[TR-03112-7].).<br>AuthenticationState States whether the respective authentication<br>condition must be set or not (also refer to<br>[ISO24727-3] and [TR-03112-4]).<br>Status information and errors in APIACLList (also refer to [TR-03112-1]<br>Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>ResultMinor • /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al#unknownAPIFunction<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/sal#<br>securityConditionsNotSatisfied<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition For access to this function the  administrator  MUST be authenticated in<br>accordance with the applicable security policies for the operation of the<br>eCard-API-Framework.<br>Postcondition<br>Note Also refer to CardApplicationACL in [TR-03112-4].<br>For successful access to card application services (also refer to<br>[TR-03112-4], Section 3.1.3 ff), the access control conditions for the<br>APICalls AND the specific card access control conditions MUST be met.<br>For this reason access to these [ISO24727-3] functions SHOULD be<br>permitted without restriction in general cases.<br>**----- End of picture text -----**<br>


## **3.1.4 APIACLModify** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0016-02.png)


**----- Start of picture text -----**<br>
Name APIACLModify<br>Description With the aid of the OPTIONAL APIACLModify function an access rule<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

16 

MAY be modified for a specific API function. 

If this function is supported it MAY ONLY be made available to an _**administrator**_ who is authenticated in accordance with the applicable security policy for the operation of the eCard-API-Framework. Regardless of the support of this function it MUST be ensured that the applicable access control policy for API-calls is enforced. **Invocation** 

## **parameters** 

## Invocation of the APIACLModify function. 

**Name Description** APIAccessControlList Contains the modified access control list for APICalls, which is activated at the latest the next time the eCard-API-Framework is started. Details on the APIAccessControlListType are given on page 13. 

## **Return parameters** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0017-06.png)


Return of the APIACLModify function. 

**Name Description** dss:Result Contains the status information and the errors of an executed action. This element is described in more detail below. 

Status information and errors in APIACLModify (also refer to [TR-03112-1] Sections 4.1 and 4.2). 

**Name Error codes** ResultMajor **•** /resultmajor#ok **•** /resultmajor#error **•** /resultmajor#warning 

Bundesamt für Sicherheit in der Informationstechnik 

17 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0018-00.png)


**----- Start of picture text -----**<br>
ResultMinor • /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al#unknownAPIFunction<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/sal#<br>invalidAccessControlInformation<br>• /resultminor/sal#<br>securityConditionsNotSatisfied<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition For access to this function the  administrator  MUST be authenticated in<br>accordance with the definitive security policies applicable for operation of the<br>eCard framework.<br>Postcondition The modified access control information becomes effective when the<br>eCard-API-Framework is started the next time at the latest.<br>Note Also refer to CardApplicationACL in [TR-03112-4].<br>For successful access to card application services (also refer to [TR-03112-4],<br>Section 3.1.3 ff), the access control conditions for the APICalls AND the<br>specific card access control conditions MUST be met. For this reason access<br>to these [ISO24727-3] functions SHOULD be permitted without restriction as<br>a rule.<br>**----- End of picture text -----**<br>


## **3.1.5 FrameworkUpdate** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0018-02.png)


**----- Start of picture text -----**<br>
Name FrameworkUpdate<br>Description An installation of the eCard-API-Framework can be updated with the<br>FrameworkUpdate function. As a result of calling FrameworkUpdate the<br>eCard-API-Framework performs the “Basic Update Protocol” as specified in<br>[TR-03112-7] with the update server defined by the UpdateService-element of<br>the default parameters (cf. page 21).<br>Invocation<br>parameters<br>Invocation of the FrameworkUpdate function is performed without parameters.<br>Return<br>Return of the FrameworkUpdate function.<br>Name Description<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

18 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0019-00.png)


**----- Start of picture text -----**<br>
dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Status information and errors with FrameworkUpdate (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/dp#communicationError<br>• /resultminor/dp#trustedChannelEstablishmentFailed<br>• /resultminor/dp#unknownProtocol<br>• /resultminor/dp#unknownWebserviceBinding<br>• /resultminor/al/FrameworkUpdate#<br>serviceNotAvailable<br>• /resultminor/al/FrameworkUpdate#unknownModule<br>• /resultminor/al/FrameworkUpdate#<br>invalidVersionNumber<br>• /resultminor/al/FrameworkUpdate#<br>operationSystemNotSupported<br>• /resultminor/al/FrameworkUpdate#<br>noSpaceAvailable<br>• /resultminor/al/FrameworkUpdate#<br>securityConditionsNotSatisfied<br>• /resultminor/sal#digitalSignatureNotCorrect<br>• /resultminor/il/signature#invalidSignatureFormat<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.1.6 GetDefaultParameters** 

**Name GetDefaultParameters** 

Bundesamt für Sicherheit in der Informationstechnik 

19 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0020-00.png)


**----- Start of picture text -----**<br>
Description The default parameters of the eCard-API-Framework are read out with the aid<br>of the GetDefaultParameters function.<br>Invocation<br>parameters<br>Invocation of the GetDefaultParameters function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If<br>the local system is to be addressed, this parameter<br>is omitted.<br>Return parameters<br>Return of the GetDefaultParameters function.<br>Name Description<br>dss:Result Contains the status information and the errors<br>of an executed action. This element is described<br>in more detail below.<br>DefaultParameters Contains the configured default parameters of<br>the eCard-API-Framework (see below for<br>details).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

20 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0021-00.png)


**----- Start of picture text -----**<br>
The DefaultParamters element contains standard parameters and is part<br>of GetDefaultParametersResponse (see above).<br>Name Description<br>DefaultFrameworkBehaviour Specifies the general behaviour of<br>the eCard-API-Framework (see<br>below for details).<br>DefaultSignOptions Specifies the default signature<br>options. The configured default<br>content is automatically added to the<br>dss:OptionalInputs-element<br>in SignRequest (refer to<br>[TR-03112-2], Section 3.2.1) as it<br>would be provided by the client<br>application. The default values MAY<br>be overridden by explicitly<br>providing an element of the same<br>name in dss:OptionalInputs.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

21 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0022-00.png)


**----- Start of picture text -----**<br>
DefaultVerifyOptions Specifies the default verification<br>options. The configured default<br>content is automatically added to the<br>dss:OptionalInputs-element<br>in VerifyRequest (refer to<br>[TR-03112-2], Section 3.2.2) as it<br>would be provided by the client<br>application. The default values MAY<br>be overridden by explicitly<br>providing an element of the same<br>name in dss:OptionalInputs.<br>DefaultEncryptOptions Specifies the default encryption<br>options. The configured default<br>content is automatically added to the<br>dss:OptionalInputs-element<br>in EncryptRequest (refer to<br>[TR-03112-2], Section 3.2.1) as it<br>would be provided by the client<br>application. The default values MAY<br>be overridden by explicitly<br>providing an element of the same<br>name in dss:OptionalInputs.<br>DefaultDecryptOptions Specifies the default decryption<br>options. The configured default<br>content is automatically added to the<br>dss:OptionalInputs-element<br>in DecryptRequest (refer to<br>[TR-03112-2], Section 3.2.1) as it<br>would be provided by the client<br>application. The default values MAY<br>be overridden by explicitly<br>providing an element of the same<br>name in dss:OptionalInputs.<br>DefaultHashAlgorithm Defines the standard hash algorithm<br>(also refer to [TR-03112-4], Annex<br>A.3).<br>DefaultCipherSuite Defines the standard cipher suite<br>which is to be used in the<br>framework of TC_API_Open (also<br>refer to [TR-03112-2]).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

22 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0023-00.png)


**----- Start of picture text -----**<br>
DefaultTSA Defines the standard time stamping<br>services (also refer to Sections 3.6.5<br>and 3.6.6).<br>If several time stamping services are<br>configured for a corresponding time<br>stamp type, the first suitable service<br>in the list is addressed.<br>If a time stamp service is referred to<br>with the address 127.0.1.0, the<br>eCard-API-Framework is instructed<br>to generate the time stamp  itself .<br>DefaultMessages Defines the standard messages for<br>recording and modifying PINs on a<br>card terminal (see below for details).<br>UpdateService Contains information on the update<br>service to be used (see below for<br>details).<br>DefaultCardInfoRepository MAY specify the address of the<br>standard CardInfo repository server<br>(also refer to GetCardInfoOr<br>ACD in [TR-03112-5]).<br>OtherParameters MAY contain other<br>(manufacturer-specific) parameters.<br>DefaultFrameworkBehaviour is part of DefaultParameters<br>(see above).<br>Name Description<br>VerbosityLevel Specifies in how much detail the framework<br>reports on detailed processes. The following<br>values are provided:<br>• 0: No information is returned on the<br>individual steps<br>• >0: Information is returned on the<br>individual steps<br>An additional differentiation of the positive<br>values for VerbosityLevel MAY be<br>defined by the manufacturer.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

23 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0024-00.png)


**----- Start of picture text -----**<br>
VerifyAddedIdentity A digital identity (certificate or TSL) MAY<br>ONLY be added to the certificate data base,<br>if its digital signature is mathematically<br>correct. Furthermore there MAY be<br>additional verification steps required before<br>an identity is added. The<br>VerifyAddedIdentity-element states -element states<br>which additional verification steps MUST be<br>performed before a digital identity is added<br>(see below for details).<br>VerifyAddedIdentity is part of DefaultFrameworkBehaviour  is part of DefaultFrameworkBehaviour DefaultFrameworkBehaviour<br>(see above).<br>Name Description<br>AddTrustedIdentity States whether the suitability of the<br>CheckAlgorithm employed signature and hash algorithm<br>MUST be verified when adding a root<br>certificate, which is to be regarded as<br>trustworthy.<br>AddCertificate Specifies which verifications MUST be<br>performed when a certificate is added (also<br>refer to Section 3.5.3).<br>DefaultMessages is part of DefaultParameters (refer to page 21). is part of DefaultParameters (refer to page 21).DefaultParameters (refer to page 21). (refer to page 21).<br>Name Description<br>LocalizedMessages Contains a set of standard messages for<br>each supported language which is stated by<br>the mandatory xml:lang attribute (see xml:lang attribute (see  attribute (see<br>below for details).<br>**----- End of picture text -----**<br>



![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0024-01.png)


**----- Start of picture text -----**<br>
VerifyAddedIdentity A digital identity (certificate or TSL) MAY<br>ONLY be added to the certificate data base,<br>if its digital signature is mathematically<br>correct. Furthermore there MAY be<br>additional verification steps required before<br>an identity is added. The<br>VerifyAddedIdentity-element states -element states<br>which additional verification steps MUST be<br>performed before a digital identity is added<br>(see below for details).<br>VerifyAddedIdentity is part of DefaultFrameworkBehaviour  is part of DefaultFrameworkBehaviour DefaultFrameworkBehaviour<br>(see above).<br>Name Description<br>AddTrustedIdentity States whether the suitability of the<br>CheckAlgorithm employed signature and hash algorithm<br>MUST be verified when adding a root<br>certificate, which is to be regarded as<br>trustworthy.<br>AddCertificate Specifies which verifications MUST be<br>performed when a certificate is added (also<br>refer to Section 3.5.3).<br>DefaultMessages is part of DefaultParameters (refer to page 21). is part of DefaultParameters (refer to page 21).DefaultParameters (refer to page 21). (refer to page 21).<br>Name Description<br>LocalizedMessages Contains a set of standard messages for<br>each supported language which is stated by<br>the mandatory xml:lang attribute (see xml:lang attribute (see  attribute (see<br>below for details).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

24 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0025-00.png)


**----- Start of picture text -----**<br>
LocalizedMessages is part of DefaultMessages and contains<br>standard messages for a specific language.<br>Name Description<br>DefaultVUMessages Defines the standard messages which are<br>used for user verifications (also refer to<br>VerifyUser in [TR-03112-6]).<br>DefaultMVDMessages Defines the standard messages which are<br>used for modification of identification data<br>(also refer to<br>ModifyVerificationData in<br>[TR-03112-6]).<br>The UpdateService element is part of the DefaultParameters<br>element (refer to page 21) and contains information for the update service<br>which is to be used with the “Basic Update Protocol” specified in<br>[TR-03112-7].<br>Name Description<br>Address Specifies the address of the update service,<br>the applicable binding and the required<br>security parameters if applicable. Note<br>however that this MAY be a local address<br>so that an update is also possible without<br>network access.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

25 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0026-00.png)


**----- Start of picture text -----**<br>
UpdateFrequency Specifies the time interval after which an<br>enquiry request is to be automatically sent<br>to the update service.<br>If this element is missing, no automatic<br>enquiry is sent to the update service.<br>AutomaticInstallation MAY specify which class of updates (also<br>refer to the UpdatePriority element in<br>[TR-03112-7]) should be automatically<br>loaded (when the eCard-API-Framework is<br>terminated with TerminateFramework,<br>also refer to Section 3.1.2).<br>If this element is missing, no updates are<br>automatically installed.<br>Other MAY contain other parameters.<br>Status information and errors in GetDefaultParameters (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>In addition, other protocol specific error messages<br>MAY exist.<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.1.7 SetDefaultParameters** 

**Name SetDefaultParameters Description** The default parameters of the eCard-API-Framework are stored with the aid of the SetDefaultParameters function. 

Bundesamt für Sicherheit in der Informationstechnik 

26 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0027-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the SetDefaultParameters function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote<br>system can be addressed (also refer to<br>CardApplicationPath in<br>[TR-03112-4]). If the local system is to be<br>addressed, this parameter is omitted.<br>DefaultParameters Contains the configured default parameters of<br>the eCard-API-Framework (refer to page 21<br>for details).<br>Return parameters<br>Return of the SetDefaultParameters function.<br>Name Description<br>dss:Result Contains the status information and the<br>errors of an executed action. This element is<br>described in more detail below.<br>Status information and errors in SetDefaultParameters (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

27 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0028-00.png)


**----- Start of picture text -----**<br>
ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/TrustedViewer#invalidID<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/il/algorithm#<br>hashAlgorithmNotSupported<br>• /resultminor/il/encryption#<br>encryptionFormatNotSupported<br>• /resultminor/il/key#<br>encryptionAlgorithmNotSupported<br>• /resultminor/il/signature#<br>signatureFormatNotSupported<br>• /resultminor/il/signature#c<br>ertificateFormatNotCorrect<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition The modified default parameters become effective the next time the<br>framework is started at the latest.<br>Note<br>**----- End of picture text -----**<br>


## **3.2 Card management** 

## **3.2.1 GetCardInfoList** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0028-03.png)


**----- Start of picture text -----**<br>
Name GetCardInfoList<br>Description The GetCardInfoList function supplies a list of known card types in the<br>form of CardInfo-files (also refer to [TR-03112-4], Annex A).<br>Invocation<br>parameters<br>Invocation of the GetCardInfoList function.<br>Name Description<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

28 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0029-00.png)


**----- Start of picture text -----**<br>
ChannelHandle Optional parameter with which a remote<br>system can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]).<br>If the local system is to be addressed, this<br>parameter is omitted.<br>Return<br>Return of the GetCardInfoList function.<br>Name Description<br>CardInfo Contains the CardInfo structure which is used for<br>mapping of generic SAL-calls to card-specific<br>APDUs. Details on this topic are contained in<br>[TR-03112-4] (Annex A).<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more<br>detail below.<br>Status information and errors in GetCardInfoList (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.2.2 SetCardInfoList** 

**Name SetCardInfoList Description** The SetCardInfoList function stores a list of CardInfo structures which 

Bundesamt für Sicherheit in der Informationstechnik 

29 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0030-00.png)


**----- Start of picture text -----**<br>
sequence may influence the sequence of steps and the performance of the card<br>recognition procedure (also refer to [TR-03112-4], Annex A).<br>Invocation<br>parameters<br>Invocation of the SetCardInfoList function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If<br>the local system is to be addressed, this parameter<br>is omitted.<br>CardInfo Contains the CardInfo structure which is used<br>for the mapping of generic ISO24727-3 calls to<br>card-specific APDUs. Details on this topic are<br>contained in [TR-03112-4] (Annex A).<br>It must be noted that the sequence of the<br>CardInfo structures transmitted here MAY have<br>a significant influence on the sequence of steps in<br>the card recognition process.<br>Return<br>Return of the SetCardInfoList function.<br>Name Description<br>dss:Result Contains the status information and the errors<br>of an executed action. This element is<br>described in more detail below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

30 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0031-00.png)


**----- Start of picture text -----**<br>
Status information and errors in SetCardInfoList (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/CardInfo#incorrectFile<br>• /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition<br>Note The sequence of the transmitted CardInfo structures MAY have a significant<br>influence on the sequence of steps and the performance of the card recognition<br>process.<br>**----- End of picture text -----**<br>


## **3.2.3 AddCardInfoFiles** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0031-02.png)


**----- Start of picture text -----**<br>
Name AddCardInfoFiles<br>Description The AddCardInfoFiles function provides a sequence of additional<br>CardInfo structures to the eCard-API-Framework. The new CardInfo<br>structures are added to the end of the existing list. During import of the<br>CardInfo files, a series of semantic verifications must be performed which<br>ensure that the CardInfo files can be used safely. The following tests MUST be<br>performed in particular (also refer to [TR-03112-4], Annex A.7):<br>• Test for content-related consistency (e.g. that URIs for protocols and<br>algorithms are known)<br>• Verification of any signatures<br>• Verification that protected key references are not referenced from<br>unsigned parts of a CardInfo file.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

31 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0032-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the AddCardInfoFiles function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed, this<br>parameter is omitted.<br>CardInfo Contains the CardInfo structure which is used for the<br>mapping of generic ISO24727-3 invocations to<br>card-specific APDUs. Details on this topic are contained<br>in [TR-03112-4] (Annex A).<br>The new CardInfo structures are added to the end of<br>the existing list. CardInfo structures which are already<br>on this list are ignored, whereby a warning (error code<br>/resultminor/al/CardInfo#alreadyExisting) is returned in<br>this case.<br>Return<br>Return of the AddCardInfoFiles function.<br>Name Description<br>dss:Result Contains the status information and the errors<br>of an executed action. This element is<br>described in more detail below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

32 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0033-00.png)


**----- Start of picture text -----**<br>
Status information and errors in AddCardInfoFiles (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/CardInfo#addNotPossible<br>• /resultminor/al/CardInfo#alreadyExisting<br>• /resultminor/al/CardInfo#incorrectFile<br>• /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.2.4 DeleteCardInfoFiles** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0033-02.png)


**----- Start of picture text -----**<br>
Name DeleteCardInfoFiles<br>Description The DeleteCardInfoFiles function deletes a series of CardInfo files.<br>Invocation<br>parameters<br>Invocation of the DeleteCardInfoFiles function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If<br>the local system is to be addressed, this<br>parameter is omitted.<br>CardTypeIdentifier Contains a series of unique identifiers of the<br>CardInfo structures which are to be deleted<br>(also refer to [TR-03112-4], Annex A.3)<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

33 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0034-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the DeleteCardInfoFiles function.<br>Name Description<br>dss:Result Contains the status information and the<br>errors of an executed action. This element is<br>described in more detail below.<br>Status information and errors in DeleteCardInfoFiles (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/CardInfo#notExisting<br>• /resultminor/al/CardInfo#deleteNotPossible<br>• /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.3 Card terminal management** 

## **3.3.1 RegisterIFD** 

**Name RegisterIFD Description** With the RegisterIFD function it is possible to add a card terminal with all configuration information. Furthermore this function may be used to reactivate one or all suspended card terminals. 

Bundesamt für Sicherheit in der Informationstechnik 

34 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0035-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the RegisterIFD function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If<br>the local system is to be addressed, this parameter<br>is omitted.<br>IFDName If the IFDName-parameter is present the<br>referenced IFD is<br>• added  to the registry, if it has not been<br>present yet or<br>• reactivated , if it is present and suspended.<br>If the IFDName-parameter is missing, all<br>registered IFDs, including the ones which have<br>previously been suspended, will be reactivated.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

35 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0036-00.png)


**----- Start of picture text -----**<br>
IFDConfiguration Optionally contains the configuration information<br>for the card terminal addressed with IFDName.<br>The detailed specification of these configuration<br>parameters depends on the card terminal type and<br>is therefore dependent on the manufacturer.<br>The IFDConfigurationType is defined as<br>follows:<br><complexType<br>name="IFDConfigurationType"><br>  <complexContent><br>    <extension base="anyType"><br>      <attribute name="IFDType"<br>type="anyURI" use="required" /><br>    </extension><br>  </complexContent><br></complexType><br>Card terminal manufacturers SHOULD define<br>corresponding structures for their products if<br>required and register them at the Federal Office<br>for Information Security.<br>Return<br>Return of the RegisterIFD function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more<br>detail below.<br>Status information and errors in RegisterIFD (also refer to [TR-03112-1]<br>Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

36 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0037-00.png)


**----- Start of picture text -----**<br>
ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/IFD#<br>writeConfigurationNotPossible<br>• /resultminor/al/IFD#couldNotAdd<br>• /resultminor/al/IFD#addNotPossible<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/ifdl/terminal#accessError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition In case of a new IFD the IFDName and, if applicable, the configuration<br>parameters are added to the card terminal management of the<br>eCard-API-Framework. If the IFD addressed by the given IFDName has already<br>been registered and suspended it is reactivated. If no IFDName has been<br>provided all previously registered and possibly suspended IFDs are activated.<br>Note<br>**----- End of picture text -----**<br>


## **3.3.2 UnregisterIFD** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0037-02.png)


**----- Start of picture text -----**<br>
Name UnregisterIFD<br>Description The UnregisterIFD function temporarily or permanently removes a card<br>terminal from the card terminal management of the eCard-API-Framework.<br>Invocation<br>parameters<br>Invocation of the UnregisterIFD function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed, this<br>parameter is omitted.<br>IFDName The name of the card terminal which is to be suspended or<br>deleted.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

37 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0038-00.png)


**----- Start of picture text -----**<br>
Mode The Mode parameter specifies, whether the IFD is<br>temporarily or permanently deactivated. It is of type<br>UnregisterIFDModeType, which is defined as<br>follows:<br><simpleType name="UnregisterIFDModeType"><br><restriction base="string"><br><enumeration value="temporary" /><br><enumeration value="permanent" /><br></restriction><br></simpleType><br>Return<br>Return of the UnregisterIFD function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Status information and errors in UnregisterIFD (also refer to [TR-03112-1]<br>Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/IFD#deleteNotPossible<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>• /resultminor/ifdl/terminal#accessError<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition The card terminal addressed with IFDName was removed from card terminal<br>management of the eCard-API-Framework.<br>Note<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

38 

## **3.4 Trusted viewer management** 

## **3.4.1 GetTrustedViewerList** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0039-02.png)


**----- Start of picture text -----**<br>
Name GetTrustedViewerList<br>Description The GetTrustedViewerList function provides a list of available<br>trustworthy display components (trusted viewer).<br>Invocation<br>parameters<br>Invocation of the GetTrustedViewerList function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If<br>the local system is to be addressed, this parameter<br>is omitted.<br>Return<br>Return of the GetTrustedViewerList function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more<br>detail below.<br>TrustedViewerId Contains the ID of the trusted viewer. The<br>TrustedViewerId is defined as follows:<br><simpleType name="TrustedViewerIdType"><br>  <restriction base="string"><br><maxLength value="64" /><br>  </restriction><br></simpleType><br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

39 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0040-00.png)


**----- Start of picture text -----**<br>
Status information and errors in GetTrustedViewerList (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the<br>error which occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.4.2 GetTrustedViewerConfiguration** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0040-02.png)


**----- Start of picture text -----**<br>
Name GetTrustedViewerConfiguration<br>Description The GetTrustedViewerConfiguration function reads the<br>configuration information which is saved in the eCard-API-Framework for a<br>specific trusted viewer.<br>Invocation<br>parameters<br>Invocation of the GetTrustedViewerConfiguration function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can<br>be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If<br>the local system is to be addressed, this parameter is<br>omitted.<br>TrustedViewerId Contains the ID of the trusted viewer for which the<br>configuration data are to be returned.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

40 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0041-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the GetTrustedViewerConfiguration function.<br>Name Description<br>dss:Result Contains the status information and the errors<br>of an executed action. This element is<br>described in more detail below.<br>ViewerConfiguration Contains the configuration data of the trusted<br>viewer (see below for details).<br>The ViewerConfiguration element is part of GetTrustedViewer<br>ConfigurationResponse (see above).<br>Name Description<br>SupportedDocumentTypes Contains information on those document<br>types which are supported by the trusted<br>viewer (see below for details).<br>IFDName MAY contain a reference to a card terminal<br>which logically links to the trusted viewer.<br>The SupportedDocumentTypes is part of ViewerConfiguration<br>(see above).<br>Name Description<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

41 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0042-00.png)


**----- Start of picture text -----**<br>
MimeType States the supported document type in accordance with<br>[MIME].<br>Application MAY associate an application with this Mime type.<br>StyleSheet MAY contain a number of style sheets which are used<br>for depiction of specific XML-based data.<br>Status information and errors in GetTrustedViewerConfiguration<br>(also refer to [TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/TrustedViewer#invalidID<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.4.3 SetTrustedViewerConfiguration** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0042-02.png)


**----- Start of picture text -----**<br>
Name SetTrustedViewerConfiguration<br>Description The SetTrustedViewerConfiguration function stores the<br>configuration information for a specific trusted viewer.<br>Invocation<br>parameters<br>Invocation of the SetTrustedViewerConfiguration function.<br>Name Description<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

42 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0043-00.png)


**----- Start of picture text -----**<br>
ChannelHandle Optional parameter with which a remote<br>system can be addressed (also refer to<br>CardApplicationPath in<br>[TR-03112-4]). If the local system is to be<br>addressed, this parameter is omitted.<br>TrustedViewerId Contains the ID of the trusted viewer for<br>which the configuration data are stored.<br>ViewerConfiguration Contains the configuration information for the<br>stated trusted viewer (for details refer to page<br>41).<br>Return<br>Return of the SetTrustedViewerConfiguration function.<br>Name Description<br>dss:Result Contains the status information and the<br>errors of an executed action. This<br>element is described in more detail<br>below.<br>Status information and errors in SetTrustedViewerConfiguration<br>(also refer to [TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/TrustedViewer#invalidID<br>• /resultminor/al/TrustedViewer#<br>invalidConfiguration<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

43 

## **3.4.4 AddTrustedViewer** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0044-01.png)


**----- Start of picture text -----**<br>
Name AddTrustedViewer<br>Description With the AddTrustedViewer function, a trusted viewer can be added with all<br>configuration information.<br>Invocation<br>parameters<br>Invocation of the AddTrustedViewer function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If<br>the local system is to be addressed, this<br>parameter is omitted.<br>TrustedViewerId Contains the unique identifier of the trusted<br>viewer which is to be added to the<br>eCard-API-Framework.<br>ViewerConfiguration MAY contain the configurations of the trusted<br>viewer (for details refer to page 41).<br>Return<br>Return of the AddTrustedViewer function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more<br>detail below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

44 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0045-00.png)


**----- Start of picture text -----**<br>
Status information and errors in AddTrustedViewer (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/TrustedViewer#invalidConfiguration<br>• /resultminor/al/TrustedViewer#alreadyExisting<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.4.5 DeleteTrustedViewer** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0045-02.png)


**----- Start of picture text -----**<br>
Name DeleteTrustedViewer<br>Description The DeleteTrustedViewer function removes a trusted viewer.<br>Invocation<br>parameters<br>Invocation of the DeleteTrustedViewer function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]).<br>If the local system is to be addressed, this<br>parameter is omitted.<br>TrustedViewerId Contains the ID of the trusted viewer which is to<br>be removed.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

45 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0046-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the DeleteTrustedViewer function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Status information and errors in DeleteTrustedViewer (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/TrustedViewer#deleteNotPossible<br>• /resultminor/al/TrustedViewer#invalidID<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.5 Identity management** 

## **3.5.1 GetTrustedIdentities** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0046-03.png)


**----- Start of picture text -----**<br>
Name GetTrustedIdentities<br>Description The GetTrustedIdentities function creates a list of all trusted identities<br>in the form of Trust-Service status lists (TSL) and certificates.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

46 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0047-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the GetTrustedIdentities function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If<br>the local system is to be addressed, this parameter<br>is omitted.<br>Return<br>Return of the GetTrustedIdentities function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>MAY contain a series of Trust-Service Status Lists<br>TSL<br>. See below for details concerning the structure of<br>the TSLType.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

47 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0048-00.png)


**----- Start of picture text -----**<br>
Certificate MAY contain a series of trusted certificates.<br>The ec:Certificate element is defined as<br>follows:<br><element name="Certificate"><br> <complexType><br>  <simpleContent><br>   <extension<br>base="base64Binary"><br><attribute name="Type"<br>type="anyURI" use="optional"<br>default="urn:ietf:rfc:3280"><br>    </attribute><br>   </extension><br>  </simpleContent><br> </complexType><br></element><br>Here the type of the certificate MAY be specified<br>in the Type attribute (also refer to<br>CertificateType in [TR-03112-7]).<br>The TSLType is used in the definition of GetTrustedIdentities-<br>Response (see above), AddTSL (see Section 3.5.6).<br>Name Description<br>TSLv3.1.2 This element contains a TSL according to [TS102231]<br>Version 3.1.2 as it is used by Bundesnetzagentur and<br>other European accreditation and supervision bodies<br>for qualified electronic signatures.<br>Other This element can be used to handle all other<br>TSL-types.<br>Status information and errors in GetTrustedIdentities (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>In addition, other specific protocol error messages can exist.<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

48 

## **3.5.2 AddTrustedCertificate** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0049-01.png)


**----- Start of picture text -----**<br>
Name AddTrustedCertificate<br>Description With the AddTrustedCertificate function, a certificate can be added to<br>the list of trusted identities.<br>Invocation<br>parameters<br>Invocation of the AddTrustedCertificate function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can<br>be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If the<br>local system is to be addressed, this parameter is<br>omitted.<br>ec:Certificate Contains the trustworthy certificate which should be<br>added to the certificate database (also refer to page<br>48).<br>CheckAlgorithms Contains information on whether the current<br>suitability of the algorithms used in the certificate<br>should be verified.<br>If an error occurs during this verification, the<br>certificate is not added.<br>If this element is missing, the configured<br>DefaultParameters (refer to page 21) are used.<br>Return<br>Return of the AddTrustedCertificate function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

49 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0050-00.png)


**----- Start of picture text -----**<br>
Status information and errors in AddTrustedCertificate (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/il/algorithm#<br>hashAlgorithmNotSupported<br>• /resultminor/il/algorithm#<br>signatureAlgorithmNotSupported<br>• /resultminor/il/signature#<br>certificateFormatNotCorrect<br>• /resultminor/il/signature#<br>signatureAlgorithmNotSuitable<br>• /resultminor/il/signature#<br>hashAlgorithmNotSuitable<br>• /resultminor/il/signature#<br>invalidCertificateExtension<br>• /resultminor/sal#digitalSignatureNotCorrect<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition<br>Note Before the certificate is added to the list of trustworthy certificates, the digital<br>signature on the certificate is verified to ensure its mathematical validity and the<br>current suitability of the algorithms is checked if necessary.<br>**----- End of picture text -----**<br>


## **3.5.3 AddCertificate** 

**Name AddCertificate Description** With the AddCertificate function, a sequence of non-trusted certificates can be added to the certificate database. These certificates MAY be used for encryption or to support the signature verification. 

Bundesamt für Sicherheit in der Informationstechnik 

50 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0051-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the AddCertificate function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote<br>system can be addressed (also refer to<br>CardApplicationPath in<br>[TR-03112-4]). If the local system is to be<br>addressed, this parameter is omitted.<br>ec:Certificate Contains a series of certificates which should<br>be added to the certificate database (also refer<br>to page 48).<br>AddCertificateOptions This element MAY be present and defines<br>which verification steps MUST be performed<br>before a particular certificate is added (see<br>below for details). If no options are specified,<br>the configured DefaultParameters (refer<br>to page 21) are used.<br>AddCertificateOptions defines which verification steps are performed<br>before a certificate is added. This element MAY be part of AddCertificate.<br>Name Description<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

51 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0052-00.png)


**----- Start of picture text -----**<br>
CheckCertificatePath This option stipulates that the certificate path<br>should be verified before the certificate is<br>added to the certificate database.<br>If an error occurs during this verification, the<br>certificate is not added.<br>If this element is missing, the configured<br>DefaultParameters (refer to page 21)<br>are used.<br>CheckCertificateStatus This option stipulates that the status of a<br>certificate should be verified before it is<br>added to the certificate database. If the<br>address of an OCSP responder is included in<br>a certificate, it SHOULD be used for the<br>verification. Alternatively, a corresponding<br>CRL MAY be evaluated.<br>If an error occurs during this verification, the<br>certificate is not added.<br>If this element is missing, the configured<br>DefaultParameters (refer to page 21)<br>are used.<br>Return<br>Return of the AddCertificate function.<br>Name Description<br>dss:Result Contains the status information and the errors<br>of an executed action. This element is<br>described in more detail below.<br>Status information and errors in AddCertificate (also refer to [TR-03112-1]<br>Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

52 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0053-00.png)


**----- Start of picture text -----**<br>
ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/il/algorithm#<br>hashAlgorithmNotSupported<br>• /resultminor/il/algorithm#<br>signatureAlgorithmNotSupported<br>• /resultminor/il/service#ocspResponderUnreachable<br>• /resultminor/il/service#<br>directoryServiceUnreachable<br>• /resultminor/il/signature#certificateNotFound<br>• /resultminor/il/signature#<br>certificateFormatNotCorrect<br>• /resultminor/il/signature#<br>invalidCertificateReference<br>• /resultminor/il/signature#<br>certificateChainInterrupted<br>• /resultminor/il/signature#<br>improperRevocationInformation<br>• /resultminor/il/signature#<br>signatureAlgorithmNotSuitable<br>• /resultminor/il/signature#hashAlgorithmNotSuitable<br>• /resultminor/il/signature#invalidCertificatePath<br>• /resultminor/il/signature#certificateRevoked<br>• /resultminor/il/signature#<br>referenceTimeNotWithinCertificateValidityPeriod<br>• /resultminor/il/signature#<br>invalidCertificateExtension<br>• /resultminor/sal#digitalSignatureNotCorrect<br>• /resultminor/il/signature#<br>certificatePathNotValidatedWarning<br>• /resultminor/il/signature#<br>certificateStatusNotCheckedWarning<br>• /resultminor/il/signature#<br>suiteabilityOfAlgorithmsNotCheckedWarning.<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

53 

## **3.5.4 ExportCertificate** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0054-01.png)


**----- Start of picture text -----**<br>
Name ExportCertificate<br>Description A certificate may be exported with the ExportCertificate function.<br>Invocation<br>parameters<br>Invocation of the ExportCertificate function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed, this<br>parameter is omitted.<br>Certificate Specifies which certificates should be exported from the<br>database. The X509IssuerSerialType is defined in<br>[RFC3275].<br>Return<br>Return of the ExportCertificate function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>ec:Certificate MAY occur several times and contains the requested<br>certificate (also refer to page 48).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

54 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0055-00.png)


**----- Start of picture text -----**<br>
Status information and errors in ExportCertificate (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/il/signature#certificateNotFound<br>• /resultminor/il/signature#<br>invalidCertificateReference<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.5.5 DeleteCertificate** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0055-02.png)


**----- Start of picture text -----**<br>
Name DeleteCertificate<br>Description The DeleteCertificate function deletes an existing (trustworthy or<br>non-trustworthy) certificate from the certificate database.<br>Invocation<br>parameters<br>Invocation of the DeleteCertificate function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed, this<br>parameter is omitted.<br>Certificate Specifies which certificate is to be deleted from the<br>database. The X509IssuerSerialType is defined in<br>[RFC3275].<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

55 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0056-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the DeleteCertificate function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>Status information and errors in DeleteCertificate (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/il/signature#invalidCertificateReference<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.5.6 AddTSL** 

**Name AddTSL Description** A series of Trust-Service status lists according to [TS102231] can be added with the AddTSL function. 

Bundesamt für Sicherheit in der Informationstechnik 

56 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0057-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the AddTSL function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed,<br>this parameter is omitted.<br>TrustStatusList MAY occur several times and contains a Trust-Service<br>Status List according to [TS102231]. See page 48 for<br>more information on the TSLType.<br>Return<br>Return of the AddTSL function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Status information and errors in AddTSL (also refer to [TR-03112-1] Sections 4.1<br>and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

57 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0058-00.png)


**----- Start of picture text -----**<br>
ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/il/algorithm#<br>hashAlgorithmNotSupported<br>• /resultminor/il/algorithm#<br>signatureAlgorithmNotSupported<br>• /resultminor/il/service#ocspResponderUnreachable<br>• /resultminor/il/service#directoryServiceUnreachable<br>• /resultminor/il/service#<br>timeStampServiceUnreachable<br>• /resultminor/il/signature#certificateNotFound<br>• /resultminor/il/signature#<br>certificateFormatNotCorrect<br>• /resultminor/il/signature#<br>invalidCertificateReference<br>• /resultminor/il/signature#certificateChainInterrupted<br>• /resultminor/il/signature#<br>resolutionOfObjectReferenceImpossible<br>• /resultminor/il/signature#<br>transformationAlgorithmNotSupported<br>• /resultminor/il/signature#unknownViewer<br>• /resultminor/il/signature#<br>certificatePathNotValidated<br>• /resultminor/il/signature#<br>certificateStatusNotCheckedWarning<br>• /resultminor/il/signature#<br>suiteabilityOfAlgorithmsNotCheckedWarning<br>• /resultminor/il/signature#<br>improperRevocationInformation<br>• /resultminor/sal#securityConditionsNotSatisfied<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

58 

## **3.5.7 ExportTSL** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0059-01.png)


**----- Start of picture text -----**<br>
Name ExportTSL<br>Description With the ExportTSL function, a Trust-Service status list can be exported in<br>accordance with [TS102231].<br>Invocation<br>parameters<br>Invocation of the ExportTSL function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can<br>be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If the<br>local system is to be addressed, this parameter is<br>omitted.<br>SchemeName MAY contain the name of a specific TSL scheme<br>(also refer to [TS102231]) in order to specify what<br>TSLs are to be exported.<br>TSLSequenceNumber MAY contain the serial number of the requested<br>TSL, if the SchemeName is specified. If the<br>TSLSequenceNumber is present, but the<br>SchemeName is not specified, the<br>TSLSequenceNumber element will be ignored<br>and there will be a corresponding warning<br>(/resultminor/al/TSL#TSLSequence<br>NumberIgnoredWarning)<br>If this element is missing, all available TSLs (of the<br>specified TSL scheme) are exported.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

59 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0060-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the ExportTSL function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>TrustStatusList MAY occur several times and contain a Trust-Service<br>Status List according to [TS102231]. See page 48 for more<br>information on the TSLType.<br>Status information and errors in ExportTSL (also refer to [TR-03112-1] Sections 4.1<br>and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/<br>TSL#TSLSequenceNumberIgnoredWarning<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.5.8 DeleteTSL** 

**Name DeleteTSL Description** With the DeleteTSL function, a sequence of Trust-Service status lists can be deleted from the list of trusted identities. 

Bundesamt für Sicherheit in der Informationstechnik 

60 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0061-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the DeleteTSL  function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can<br>be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If the<br>local system is to be addressed, this parameter is<br>omitted.<br>SchemeName MAY contain the name of a specific TSL scheme<br>(also refer to [TS102231]) in order to specify what<br>TSLs are to be exported.<br>TSLSequenceNumber MAY contain the serial number of the requested<br>TSL, if the SchemeName is specified. If the<br>TSLSequenceNumber is present, but the<br>SchemeName is not specified, the<br>TSLSequenceNumber will be ignored and there will<br>be a corresponding warning (/resultminor/al/TSL<br>#TSLSequenceNumberIgnoredWarning).<br>If this element is missing, all available TSLs (of the<br>specified TSL scheme) are exported.<br>Return<br>Return of the DeleteTSL function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

61 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0062-00.png)


**----- Start of picture text -----**<br>
Status information and errors in DeleteTSL (also refer to [TR-03112-1] Sections<br>4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/al/<br>TSL#TSLSequenceNumberIgnoredWarning<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.6 Service management** 

## **3.6.1 GetOCSPServices** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0062-03.png)


**----- Start of picture text -----**<br>
Name GetOCSPServices<br>Description The GetOCSPServices function reads the list of known OCSP responders.<br>Invocation<br>parameters<br>Invocation of the GetOCSPServices function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed,<br>this parameter is omitted.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

62 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0063-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the GetOCSPServices function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>OCSPService Contains information on the available OCSP responders<br>which MAY be used if a certificate which is to be verified<br>does not contain the address of the OCSP responder in the<br>authority information access extension (also refer to<br>[RFC3280], Section 4.2.2.1). Details on the<br>ServiceType are given below.<br>An element of ServiceType is part of GetOCSPServicesResponse,<br>SetOCSPServices, GetDirectoryServicesResponse and<br>SetDirectoryServices.<br>Name Description<br>Name MAY contain the name of the service.<br>Address Contains the address of the service.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

63 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0064-00.png)


**----- Start of picture text -----**<br>
Status information and errors in GetOCSPServices (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.6.2 SetOCSPServices** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0064-02.png)


**----- Start of picture text -----**<br>
Name SetOCSPServices<br>Description The SetOCSPServices function writes the list of available OCSP responders.<br>Invocation<br>parameters<br>Invocation of the SetOCSPServices function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed,<br>this parameter is omitted.<br>OCSPService Contains information on the available OCSP responders<br>which MAY be used if a certificate which is to be<br>verified does not contain the address of the OCSP<br>responder in the authority information access extension<br>(also refer to [RFC3280], Section 4.2.2.1). Details on<br>the ServiceType are given on page 63.<br>When the list is written, the availability of the<br>configured OCSP responders is checked.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

64 

## **Return** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0065-01.png)


Return of the SetOCSPServices function. 

**Name Description** dss:Result Contains the status information and the errors of an executed action. This element is described in more detail below. 

Status information and errors in SetOCSPServices (also refer to [TR-03112-1] Sections 4.1 and 4.2). 

**Name Error codes** ResultMajor **•** /resultmajor#ok **•** /resultmajor#error ResultMinor **•** /resultminor/al/common#noPermission **•** /resultminor/al/common#internalError **•** /resultminor/al/common#parameterError **•** /resultminor/dp#unknownChannelHandle **•** /resultminor/il/service#ocspResponderUnreachable ResultMessage MAY contain more detailed information on the error which occurred if required. 

**Precondition Postcondition Note** 

## **3.6.3 GetDirectoryServices** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0065-08.png)


**----- Start of picture text -----**<br>
Name GetDirectoryServices<br>Description The GetDirectoryServices function reads the list of the directory services<br>accessible via LDAP or http.<br>Invocation<br>parameters<br>Invocation of the GetDirectoryServices function.<br>Name Description<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

65 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0066-00.png)


**----- Start of picture text -----**<br>
ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed, this<br>parameter is omitted.<br>Return<br>Return of the GetDirectoryServices function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>DirectoryService Contains information on the available directory services<br>which can be used for retrieval of certificates or<br>blacklists (details on the ServiceType can be found<br>on page 63).<br>Status information and errors in GetDirectoryServices (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.6.4 SetDirectoryServices** 

**Name SetDirectoryServices Description** The SetDirectoryServices function writes the list of available directory services. 

Bundesamt für Sicherheit in der Informationstechnik 

66 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0067-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the SetDirectoryServices function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]).<br>If the local system is to be addressed, this<br>parameter is omitted.<br>DirectoryService Contains information on the available directory<br>services (details on the ServiceType are<br>given on page 63).<br>When the list is written, the availability of the<br>configured directory services is checked.<br>Return<br>Return of the SetDirectoryServices function.<br>Name Description<br>dss:Result Contains the status information and the errors<br>of an executed action. This element is<br>described in more detail below.<br>Status information and errors in SetDirectoryServices (also refer to<br>[TR-03112-1] Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/il/service#directoryServiceUnreachable<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

67 

ResultMessage MAY contain more detailed information on the error which occurred if required. **Precondition Postcondition Note** 

## **3.6.5 GetTSServices** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0068-02.png)


**----- Start of picture text -----**<br>
Name GetTSService<br>Description The GetTSServices function reads the list of time stamping services with the<br>corresponding configuration information.<br>Invocation<br>parameters<br>Invocation of the GetTSServices function.<br>Name Description<br>ChannelHandle Optional parameter with which a remote system can be<br>addressed (also refer to CardApplicationPath in<br>[TR-03112-4]). If the local system is to be addressed, this<br>parameter is omitted.<br>Return<br>Return of the GetTSServices function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more<br>detail below.<br>TimeStampingService MAY occur more than once and contains information<br>in each case about one time stamp service (see below<br>for details).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

68 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0069-00.png)


**----- Start of picture text -----**<br>
The TimeStampingService element in GetTSServicesResponse and<br>SetTSServices is of the TSServiceType, which extends the ServiceType<br>(also refer to page 63) by the elements described below.<br>A unique name MUST be given here if the time stamp service is to be used as one of<br>the configured default time stamping services (also refer to Section 3.1.6).<br>Name Description<br>TimeStampType MAY contain the time stamp type (also refer to<br>SignOptions in [TR-03112-2]), which can be<br>requested from this time stamping service.<br>If TimeStampToken according to [RFC3161] are<br>issued this element MAY be omitted.<br>dss:KeySelector The presence of this optional element indicates, that the<br>time stamp request MUST be signed with the specified<br>key (refer to [DSS] and [TR-03112-2], Section 3.2.1). If<br>the element is missing, the time stamp request is not<br>signed.<br>PathSecurity MAY state how the channel to the time stamp service<br>should be protected (also refer to<br>CardApplicationPath in [TR-03112-4]).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

69 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0070-00.png)


**----- Start of picture text -----**<br>
Status information and errors in GetTSService (also refer to [TR-03112-1]<br>Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/dp#unknownCipherSuite<br>• /resultminor/il/service#timeStampServiceUnreachable<br>• /resultminor/il/signature#signatureFormatNotSupported<br>• /resultminor/sal#nameAlreadyExisting<br>• /resultminor/sal#unknownProtocol<br>• /resultminor/sal#unknownCardType<br>• /resultminor/sal#unknownDIDName<br>• /resultminor/sal#fileNotFound<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note<br>**----- End of picture text -----**<br>


## **3.6.6 SetTSServices** 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0070-02.png)


**----- Start of picture text -----**<br>
Name SetTSServices<br>Description The SetTSServices function writes a list of the time stamping services together<br>with all corresponding configuration information.<br>Invocation<br>parameters<br>Invocation of the SetTSServices function.<br>Name Description<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

70 


![](markdown/tr/TR-03112-api_teil3/TR-03112-api_teil3.pdf-0071-00.png)


**----- Start of picture text -----**<br>
ChannelHandle Optional parameter with which a remote system<br>can be addressed (also refer to<br>CardApplicationPath in [TR-03112-4]). If<br>the local system is to be addressed, this parameter<br>is omitted.<br>TimeStampingService MAY occur several times and contains information<br>on a time stamping service (for details on the<br>TSServiceType refer to page 69).<br>Return<br>Return of the SetTSServices function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>Status information and errors in SetTSServices (also refer to [TR-03112-1]<br>Sections 4.1 and 4.2).<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/al/common#noPermission<br>• /resultminor/al/common#internalError<br>• /resultminor/al/common#parameterError<br>• /resultminor/dp#unknownChannelHandle<br>• /resultminor/dp#unknownCipherSuite<br>• /resultminor/il/service#timeStampServiceUnreachable<br>• /resultminor/il/signature#signatureFormatNotSupported<br>• /resultminor/sal#nameAlreadyExisting<br>• /resultminor/sal#unknownProtocol<br>• /resultminor/sal#unknownCardType<br>• /resultminor/sal#unknownDIDName<br>• /resultminor/sal#fileNotFound<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition<br>Postcondition<br>Note When new time stamping services are added, their availability SHOULD be checked.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

71 

## **References** 

- [TR-03112-1] BSI: TR-03112-1: eCard-API-Framework – Part 1: Overview and Generic Mechanisms [TR-03112-2] BSI: TR-03112-2: eCard-API-Framework – Part 2: eCard-Interface [TR-03112-3] BSI: TR-03112-3: eCard-API-Framework – Part 3: Management-Interface 

- [TR-03112-4] BSI: TR-03112-4: eCard-API-Framework – Part 4: ISO24727-3-Interface [TR-03112-5] BSI: TR-03112-5: eCard-API Framework – Part 5: Suppor- Interface [TR-03112-6] BSI: TR-03112-6: eCard-API-Framework – Part 6: IFD-Interface [TR-03112-7] BSI: TR-03112-7: eCard-API-Framework – Part 7: Protocols [TS102231] ETSI: TS 102 231: Provision of harmonized Trust Service Provider (TSP) status information, Technical Specification 

- [MIME] IANA: MIME Media Types [RFC2119] IETF: RFC 2119: S. Bradner: Key words for use in RFCs to Indicate Requirement Levels [RFC3161] IETF: RFC 3161: C. Adams, P. Cain, D. Pinkas, R. Zuccherato: Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP) 

- [RFC3275] IETF: RFC 3275: D. Eastlage, J. Reagle, D. Solo: (Extensible Markup Language) XMLSignature Syntax and Processing 

- [RFC3280] IETF: RFC 3280: R. Housley, W. Polk, W. Ford, D. Solo: Internet X.509 Public Key Infrastructure, Certificate and Certificate Revocation List (CRL) Profile 

- [ISO24727-3] ISO: ISO/IEC 24727-3: Identification Cards — Integrated Circuit Cards Programming Interfaces — Part 3: Application Interface 

- [ISO24727-4] ISO: ISO/IEC 24727-4: Identification Cards — Integrated Circuit Cards Programming Interfaces — Part 4: Application programming interface (API) administration 

- [DSS] OASIS: Digital Signature Service Core Protocols, Elements, and Bindings 

Bundesamt für Sicherheit in der Informationstechnik 

72 



![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0001-00.png)


Technical Guideline TR-03112-6 eCard-API-Framework – IFD-Interface Version 1.1.5 

7. April 2015 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn 

E-Mail: ecard.api@bsi.bund.de Internet: https://www.bsi.bund.de 

© Bundesamt für Sicherheit in der Informationstechnik 2015 

## **Contents** 

|1|Overview of the eCard-API-Framework.................................................................................................4|
|---|---|
|1.1|Key Words.........................................................................................................................................4|
|1.2|XML-Schema....................................................................................................................................5|
|2|Overview of the IFD-Interface...............................................................................................................6|
|2.1|Objective...........................................................................................................................................6|
|2.2|Functions...........................................................................................................................................6|
|2.2.1|Card terminal functions................................................................................................................6|
|2.2.2|Card functions..............................................................................................................................7|
|2.2.3|User interaction functions.............................................................................................................7|
|2.2.4|IFD callback interface for card terminal events............................................................................7|
|3|Specification of the IFD-Interface..........................................................................................................8|
|3.1|Card terminal functions.....................................................................................................................8|
|3.1.1|EstablishContext...........................................................................................................................8|
|3.1.2|ReleaseContext.............................................................................................................................9|
|3.1.3|ListIFDs......................................................................................................................................11|
|3.1.4|GetIFDCapabilities.....................................................................................................................12|
|3.1.5|GetStatus....................................................................................................................................17|
|3.1.6|Wait............................................................................................................................................20|
|3.1.7|Cancel.........................................................................................................................................23|
|3.1.8|ControlIFD.................................................................................................................................25|
|3.2|Card functions.................................................................................................................................26|
|3.2.1|Connect......................................................................................................................................26|
|3.2.2|Disconnect..................................................................................................................................28|
|3.2.3|BeginTransaction........................................................................................................................30|
|3.2.4|EndTransaction...........................................................................................................................32|
|3.2.5|Transmit.....................................................................................................................................33|
|3.3|User interaction functions................................................................................................................35|
|3.3.1|VerifyUser..................................................................................................................................35|
|3.3.2|ModifyVerificationData..............................................................................................................42|
|3.3.3|Output.........................................................................................................................................47|
|3.4|IFD-Callback-Interface for card terminal events.............................................................................50|
|3.4.1|SignalEvent................................................................................................................................50|



## **Table of Figures** 

Figure 1: Internal architecture of the IFD-Layer (informative).......................................................................52 

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

## **2 Overview of the IFD-Interface** 

## **2.1 Objective** 

The IFD-Interface generalises the specific card terminal types and various interfaces and communicates with the smart card. For the user it is not relevant whether the card is addressed by PC/SC, CT-API, in a SICCT card terminal or via a proprietary interface, or whether it has contacts or is contactless. 

## **2.2 Functions** 

The IFD-Interface provides the following function groups: 

- Card terminal functions 

- Card functions 

- User interaction functions 

In addition, there is an IFD-Callback-Interface for card terminal events and additional functions for the management of card terminals which are specified in the management interface [TR-03112-3]: 

- With the RegisterIFD function it is possible to add a card terminal with all configuration information. 

- The UnregisterIFD function deletes a card terminal. 

## **2.2.1 Card terminal functions** 

- The EstablishContext function opens a session with the Terminal-Layer and returns a ContextHandle which is used to address this session during subsequent function invocations. 

- The ReleaseContext terminates a session with the Terminal-Layer which had been addressed by a ContextHandle. 

- With the ListIFDs function a list of available card terminals is returned to the calling layer. 

- The GetIFDCapabilities function returns information on a specific card terminal and its functional units to the calling layer. 

- The GetStatus function determines the current status of the card terminal. 

- With the Wait function the invoking layer can be informed about card terminal events by the return of the wait function or by means of the SignalEvent callback function. 

- The Cancel function terminates waiting for card terminal events or attempts to terminate processing of the last command sent via the current handle to a specific card terminal. In this case the success of the operation depends on the type of command and the time at which Cancel was invoked. 

- The ControlIFD function sends a (proprietary) command to the card terminal. This serves to permit access to proprietary and application-specific functions for which there is no separate command in the IFD-Interface without changing the interface. 

Bundesamt für Sicherheit in der Informationstechnik 

6 

## **2.2.2 Card functions** 

- The Connect function activates a card captured by the IFD and returns a SlotHandle with which the card can be addressed in the future. 

- The Disconnect function invalidates a SlotHandle and optionally performs an additional action (e.g. eCard ejection, if the IFD features the corresponding mechanical functionality). 

- The BeginTransaction function starts a transaction within the framework of which several commands can be sent to the eCard. If an error occurs, the transaction is terminated and any modifications are reset. 

- The EndTransaction function terminates an existing transaction. 

- The Transmit function sends APDUs to an eCard addressed via a SlotHandle. 

## **2.2.3 User interaction functions** 

- The VerifyUser function verifies the user by means of a PIN or a biometric characteristic. 

- The ModifyVerificationData modifies the identification data (PIN or biometric characteristic). 

- The Output function may be used to control the output units of a card terminal. 

## **2.2.4 IFD callback interface for card terminal events** 

- With the SignalEvent function, layers above the Terminal-Layer can be informed of card terminal events. For this purpose the SignalEvent function must be offered as a webservice by these layers. 

Bundesamt für Sicherheit in der Informationstechnik 

7 

## **3 Specification of the IFD-Interface** 

## **3.1 Card terminal functions** 

## **3.1.1 EstablishContext** 

**Name EstablishContext Description** The EstablishContext function opens a session with the Terminal-Layer and returns a ContextHandle which is used to address this session in further function invocations. **Invocation parameters** 

Invocation of the EstablishContext function. 

**Name Description** ChannelHandle Optional parameter with which a remote system can be addressed (also refer to CardApplicationPath in [TR-03112-4]). If the local system is to be addressed, this parameter MAY be omitted. 

## **Return** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0008-07.png)


Return of the EstablishContext function. 

**Name Description** dss:Result Contains the status information and the errors of an executed action. This element is described in more detail below. ContextHandle The session with the Terminal-Layer is addressed via the returned ContextHandle. 

Bundesamt für Sicherheit in der Informationstechnik 

8 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0009-00.png)


**----- Start of picture text -----**<br>
Status information and errors in EstablishContext<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/ifdl/common#unknownSessionIdentifier<br>• /resultminor/dp#invalidChannelHandle<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Preconditions<br>Postconditions A context is established with the IFD-Layer via which commands are sent to card<br>terminals and connections to cards can be established.<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the EstablishContext function in the PC/SC resource manager<br>(also refer to [PC/SC], Part 5, Section 3.2.1.2).<br>**----- End of picture text -----**<br>


## **3.1.2 ReleaseContext** 

**Name ReleaseContext Description** The ReleaseContext function terminates a session with the Terminal-Layer. **Invocation parameters** Invocation of the ReleaseContext function. **Name Description** 

Bundesamt für Sicherheit in der Informationstechnik 

9 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0010-00.png)


**----- Start of picture text -----**<br>
ContextHandle Handle with which the session with the Terminal-Layer<br>can be addressed.<br>Return<br>Return of the ReleaseContext function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Status information and errors in ReleaseContext<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/dp#invalidChannelHandle<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A context was established with EstablishContext.<br>Postconditions The ContextHandle loses its validity.<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the ReleaseContext function in the PC/SC resource manager<br>(also refer to [PC/SC], Part 5, Section 3.2.1.2).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

10 

## **3.1.3 ListIFDs** 

**Name ListIFDs Description** Returns the list of the card terminals assigned to the eCard-API-Framework, which at least contains the currently connected IFDs. **Invocation parameters** Invocation of the ListIFDs function. **Name Description** 

ContextHandle Handle with which the session with the Terminal-Layer can be addressed. **Return** Return of the ListIFDs function. **Name Description** dss:Result Contains the status information and the errors of an executed action. This element is described in more detail below. IFDName Unique name of the card terminal. Status information and errors in ListIFDs **Name Error codes** 

Bundesamt für Sicherheit in der Informationstechnik 

11 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0012-00.png)


**----- Start of picture text -----**<br>
ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/dp#invalidChannelHandle<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions The potentially available card terminals were assigned to the<br>eCard-API-Framework in an administrative operation (also refer to<br>[TR-03112-3]).<br>A context was established with EstablishContext.<br>Postconditions The status of the card terminals remains unchanged.<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the ListReaders function in the PC/SC resource manager (also<br>refer to [PC/SC], Part 5, Section 3.2.3.2).<br>Also refer to GetCardTerminals in [TR-03112-2].<br>**----- End of picture text -----**<br>


## **3.1.4 GetIFDCapabilities** 

**GetIFDCapabilities** 

**Name GetIFDCapabilities Description** Returns information on the capabilities of a specific card terminal and its functional units. **Invocation parameters** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0012-04.png)


**----- Start of picture text -----**<br>
Description Returns information on the capabilities of a specific card terminal and its<br>functional units.<br>Invocation<br>parameters<br>Invocation of the GetIFDCapabilities function.<br>Name Description<br>ContextHandle Handle with which the session with the Terminal-Layer<br>is addressed.<br>IFDName Unique name of the card terminal.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

12 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0013-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the GetIFDCapabilities function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>IFDCapabilities Contains information on the capabilities of the<br>terminal (see below for details).<br>The IFDCapabilities element contains information on the specified card<br>terminal.<br>Name Description<br>SlotCapability This element is of the<br>SlotCapabilityType and is provided for<br>each slot of the card terminal containing<br>information on the slot. See below for details.<br>DisplayCapability An entry of the DisplayCapabilityType<br>describing the display capabilities of the<br>terminal is provided for each display on the<br>IFD.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

13 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0014-00.png)


**----- Start of picture text -----**<br>
KeyPadCapability Such an entry with the capabilities of the<br>keypad exists for each card terminal keypad.<br>The entry is of the<br>KeyPadCapabilityType.<br>BioSensorCapability Such an entry of the<br>BioSensorCapabilityType with the<br>capabilities of the sensor exists for each<br>biometric sensor on the card terminal.<br>OpticalSignalUnit Contains information on whether the card<br>terminal has an optical signal unit (e.g. LED).<br>AcousticSignalUnit Contains information on whether the card<br>terminal has a unit for acoustic signals (e.g.<br>beeping).<br>SlotCapability is part of IFDCapabilities.<br>Name Description<br>Index Specifies the index of the slot in the range of 0<br>to the number of slots minus 1.<br>Protocol MAY be present multiple times and indicate the<br>supported transport protocols (see<br>Interface-element in [TR-03112-4]) or the<br>supported DID-protocols (see<br>[TR-03112-7]).Support of the IFD for PACE<br>according to [TR-03119]/[PC/SC], Part 10<br>AMD1 is indicated by the URI<br>urn:oid:0.4.0.127.0.7.2.2.4:xx,<br>where xx is the decimal representation of the<br>capabilites bitmap returned by GetReader-<br>PACECapabilites as defined in [PC/SC],<br>Part 10 AMD1.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

14 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0015-00.png)


**----- Start of picture text -----**<br>
The DisplayCapabilityType is part of IFDCapabilities.<br>Name Description<br>Index The index of the display in the range of 0 to the<br>number of displays minus 1.<br>Lines Contains the number of visible lines of the<br>display.<br>Columns Specifies the number of visible columns of the<br>display.<br>VirtualLines If applicable, this optional parameter contains<br>the number of lines which are supported by the<br>display including scrolling.<br>VirtualColumns If applicable, this optional parameter specifies<br>how many columns of the display are supported<br>with panning.<br>The KeyPadCapabilityType is part of IFDCapabilities.<br>Name Description<br>Index Specifies the keypad index in the range of 0 to<br>the number of keypads minus 1.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

15 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0016-00.png)


**----- Start of picture text -----**<br>
Keys Contains the number of keys on the keypad.<br>The BioSensorCapabilityType is part of IFDCapabilities.<br>Name Description<br>Index Specifies the biometric sensor index in the range of 0 to<br>the number of biometric sensors minus 1.<br>BiometricType Describes the type of the biometric characteristic in<br>accordance with Section 7.8 of [ISO19784-1].<br>Status information and errors in GetIFDCapabilities<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/dp#invalidChannelHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A context was established with EstablishContext.<br>Postconditions The status of the card terminals remain unchanged.<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the GetReaderCapabilities function in the PC/SC resource<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

16 

## manager (also refer to [PC/SC], Part 5, Section 3.2.5.2). 

## **3.1.5 GetStatus** 

**Name GetStatus Description** Determines the current status of one specific or all connected terminals. **Invocation parameters** 

Invocation of the GetStatus function. **Name Description** ContextHandle Handle with which the session with the Terminal-Layer is addressed. IFDName MAY contain the unique name of the card terminal. If this element is missing, the status of all connected terminals is returned. **Return** 

Return of the GetStatus function. **Name Description** dss:Result Contains the status information and the errors of an executed action. This element is described in more detail below. IFDStatus Contains information on the status of the respective terminal. 

Bundesamt für Sicherheit in der Informationstechnik 

17 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0018-00.png)


**----- Start of picture text -----**<br>
The IFDStatus element is part of GetStatusResponse and contains status<br>information on the respective terminal.<br>Name Description<br>IFDName MAY contain the unique name of the card terminal.<br>This element MUST be present, if more than one<br>terminal is present.<br>Connected Contains information on whether a connection is<br>currently established to the terminal. If the terminal is<br>directly connected to the host (e.g. via RS232, USB,<br>etc.), the parameter MAY be omitted.<br>SlotStatus Contains status information for a specific slot for<br>smart cards with contacts. The structure of<br>SlotStatusType is defined below.<br>ActiveAntenna Contains information on whether an existing radio<br>antenna is activated. If no radio antenna is available,<br>this element is omitted.<br>DisplayStatus Contains status information on the available displays.<br>See below for details. If no display is available, this<br>element is omitted.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

18 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0019-00.png)


**----- Start of picture text -----**<br>
KeyPadStatus Contains information on whether the existing keypads<br>are currently available for an invoker. See below for<br>details. If no keypad is available, this element is<br>omitted.<br>BioSensorStatus Contains information on the availability of the<br>biometric sensors. See below for details. If no<br>biometric sensors are available, this element is<br>omitted.<br>The SlotStatus element is of the SlotStatusType and is part of<br>IFDStatus.<br>Name Description<br>Index Contains the index of the slot under consideration.<br>The slots contain indexes in the range of 0 to the<br>number of slots minus 1.<br>CardAvailable Contains information on whether a card is currently<br>captured by this slot.<br>ATRorATS If a card is captured, this element contains the ATR or<br>ATS of the card if available. If no card is captured,<br>this element is omitted.<br>The DisplayStatus element, the KeyPadStatus element and the<br>BioSensorStatus element are part of IFDStatus and of the<br>SimpleFUStatusType.<br>Name Description<br>Index Contains the index of the functional unit in the range<br>of 0 to the number of functional units minus 1.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

19 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0020-00.png)


**----- Start of picture text -----**<br>
Available Specifies whether the functional unit is currently<br>available for the invoker or if it is already being used.<br>Status information and errors in GetStatusResponse<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/dp#invalidChannelHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A context was established with EstablishContext.<br>Postconditions The status of the card terminals remains unchanged.<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the Status function in the PC/SC resource manager (also refer to<br>[PC/SC], Part 5, Section 3.2.5.2).<br>**----- End of picture text -----**<br>


## **3.1.6 Wait** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0020-02.png)


**----- Start of picture text -----**<br>
Name Wait<br>Description The Wait function informs the invoking layer about events on specific card<br>terminals. Information on which events have occurred can be returned by the<br>return of the Wait function or – if a corresponding callback address was<br>transmitted – by the SignalEvent function.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

20 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0021-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the Wait function.<br>Name Description<br>ContextHandle Handle with which the session with the Terminal-Layer<br>is addressed.<br>TimeOut Optional parameter which contains the time until timeout<br>in milliseconds. If the parameter is missing, waiting<br>continues for an infinite period (until invocation of the<br>Cancel or ReleaseContext function or<br>termination of the complete framework with<br>TerminateFramework (also refer to<br>[TR-03112-3])).<br>IFDStatus Such an entry of type IFDStatusType is provided for<br>each card terminal requiring monitoring with the<br>currently assumed status information for this terminal.<br>Information on the IFDStatusType is given on page<br>18.<br>Callback MAY specify a callback address and other corresponding<br>parameters (also refer to ChannelHandle in<br>[TR-03112-4]) to which a SignalEvent invocation<br>specified in Annex A is sent when a card terminal event<br>occurs.<br>If this element is provided, the function immediately<br>returns with WaitResponse. Otherwise return is<br>delayed until a corresponding event or timeout occurs.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

21 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0022-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the Wait function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>IFDEvent IFDEvent can occur several times and contains<br>information on an event which occurred on a<br>card terminal. Similar to the input parameter<br>IFDStatus, this parameter is of the<br>IFDStatusType, and contains the status<br>information changed by the event.<br>SessionIdentifier Is available if a Callback address was<br>provided when the Wait function was invoked<br>and specifies an identifier unique in the<br>Terminal-Layer with which waiting for card<br>terminal events can be terminated with the<br>Cancel function.<br>Status information and errors in WaitResponse<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

22 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0023-00.png)


**----- Start of picture text -----**<br>
ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/dp#invalidChannelHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A context was established with EstablishContext.<br>Postconditions<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the GetStatusChange function in the PC/SC resource manager<br>(also refer to [PC/SC], Part 5, Section 3.2.4.2).<br>**----- End of picture text -----**<br>


## **3.1.7 Cancel** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0023-02.png)


**----- Start of picture text -----**<br>
Name Cancel<br>Description Terminates waiting for card terminal events started with Wait, or attempts to<br>cancel processing of the last command sent to a terminal.<br>Invocation<br>parameters<br>Invocation of the Cancel function.<br>Name Description<br>ContextHandle Handle with which the session with the<br>Terminal-Layer is addressed.<br>IFDName Unique name of the card terminal at which a<br>command currently being executed should be<br>terminated.<br>SessionIdentifier Specifies which waiting process should be<br>terminated with Wait.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

23 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0024-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the Cancel function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Status information and errors in Cancel<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/ifdl/IO#cancelNotPossible<br>• /resultminor/dp#invalidChannelHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A context was established with EstablishContext.<br>Postconditions Depending on the command and time of the request, the command is either<br>terminated or fully executed.<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the Cancel function in the PC/SC resource manager (also refer to<br>[PC/SC], Part 5, Section 3.2.4.2).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

24 

## **3.1.8 ControlIFD** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0025-01.png)


**----- Start of picture text -----**<br>
Name ControlIFD<br>Description Sends any arbitrary command directly to the card  terminal and returns the<br>corresponding result.<br>Invocation<br>parameters<br>Invocation of the ControlIFD function.<br>Name Description<br>ContextHandle Handle with which the session with the Terminal-Layer<br>is addressed.<br>IFDName Unique name of the card terminal to which a command<br>is to be sent.<br>Command Command protocol data unit for the card terminal.<br>Return<br>Return of the ControlIFD function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Response Response protocol data unit which was returned<br>from the card terminal.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

25 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0026-00.png)


**----- Start of picture text -----**<br>
Status information and errors in ControlIFD<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/dp#invalidChannelHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A context was established with EstablishContext.<br>Postconditions The command was executed by the card terminal.<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function using FEATURE_MCT_READERDIRECT (also refer to [PC/SC], Part<br>10, Section 2.14).<br>**----- End of picture text -----**<br>


## **3.2 Card functions** 

## **3.2.1 Connect** 

**Name Connect Description** Establishes a connection to an eCard in a specific card terminal slot and returns a corresponding SlotHandle to the calling layer. 

Bundesamt für Sicherheit in der Informationstechnik 

26 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0027-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the Connect function.<br>Name  Description<br>ContextHandle Handle with which the session with the Terminal-Layer<br>is addressed.<br>IFDName Unique name of the card terminal.<br>Slot Addresses the slot (ICC slot or PCD) of an IFD by which<br>a card is detected and with which a connection should be<br>established. Assignment of the slot indexes is explained<br>in the definition of the SlotStatusType (also refer<br>to page 19).<br>Exclusive Is TRUE if an exclusive connection should be established<br>to the eCard.<br>Return<br>Return of the Connect function.<br>Name  Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>SlotHandle If successful, a SlotHandle is returned with<br>which the connection established with Connect<br>to the eCard is addressed in future.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

27 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0028-00.png)


**----- Start of picture text -----**<br>
Status information and errors in Connect<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/ifdl/common#invalidContextHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>• /resultminor/ifdl/terminal#unknownSlot<br>• /resultminor/ifdl/terminal#IFDSharingViolation<br>• /resultminor/ifdl/terminal#noCard<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A context was established with EstablishContext.<br>Postconditions A logical connection to the card was established. APDUs can then be sent to the<br>card via the returned SlotHandle with the Transmit function. As a result,<br>the path to a card application can also be determined with<br>CardApplicationPath and established by means of<br>CardApplicationConnect (also refer to [TR-03112-4]).<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the Connect function in the PC/SC resource manager (also refer<br>to [PC/SC], Part 5, Section 3.2.5.2).<br>**----- End of picture text -----**<br>


## **3.2.2 Disconnect** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0028-02.png)


**----- Start of picture text -----**<br>
Name Disconnect<br>Description The Disconnect function terminates the connection to a card and MAY<br>execute an additional action (e.g. ejection of the card), if the corresponding<br>mechanical functionality is supported by the terminal.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

28 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0029-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the Disconnect function.<br>Name Description<br>SlotHandle With the SlotHandle the connection to the eCard<br>established with Connect is addressed.<br>Action Optional parameter which MAY specify an action which<br>is to be performed additionally. The ActionType is<br>defined as follows:<br><simpleType name="ActionType"><br><restriction base="string"><br><enumeration value="Reset" /><br><enumeration value="Unpower" /><br><enumeration value="Eject" /><br><enumeration value="Confiscate" /><br></restriction><br></simpleType><br>The values have the following meaning:<br>Value Meaning<br>Reset Reset of the eCard.<br>Unpower Interrupts the power supply of the<br>card.<br>Eject Ejection of the eCard from the<br>card terminal if the mechanical<br>functionality is available.<br>Confiscate Confiscation of the eCard if the<br>corresponding functionality is<br>available.<br>Return<br>Return of the Disconnect function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

29 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0030-00.png)


## Status information and errors in Disconnect 

**Name Error codes** ResultMajor **•** /resultmajor#ok **•** /resultmajor#error ResultMinor **•** /resultminor/ifdl/common#timeoutError **•** /resultminor/ifdl/common#invalidSlotHandle **•** /resultminor/ifdl/terminal#unknownAction **•** /resultminor/al/common#unknownError ResultMessage MAY contain more detailed information on the error which occurred if required. **Preconditions** A connection to an eCard was established with Connect. **Postconditions** The SlotHandle loses its validity. **Notes** A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this function with the Disconnect function in the PC/SC resource manager (also refer to [PC/SC], Part 5, Section 3.2.5.2). 

## **3.2.3 BeginTransaction** 

**Name BeginTransaction Description** The BeginTransaction function starts a transaction within which a series of commands can be sent to the eCard without permitting access of another process to the eCard. If a command is not successful in the transaction, the complete transaction is reset. **Invocation parameters** 

Invocation of the BeginTransaction function. 

Bundesamt für Sicherheit in der Informationstechnik 

30 

**Name Description** SlotHandle With the SlotHandle the connection established with Connect to the eCard is addressed. **Return** Return of the BeginTransaction function. **Name Description** dss:Result Contains the status information and the errors of an executed action. This element is described in more detail below. Status information and errors in BeginTransaction 

**Name Error codes** ResultMajor **•** /resultmajor#ok **•** /resultmajor#error ResultMinor **•** /resultminor/ifdl/common#timeoutError **•** /resultminor/ifdl/common#invalidSlotHandle **•** /resultminor/al/common#unknownError ResultMessage MAY contain more detailed information on the error which occurred if required. 

**Preconditions** A connection to an eCard was established with Connect. **Postconditions** A transaction is started. **Notes** A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this function with the BeginTransaction function in the PC/SC resource manager (also refer to [PC/SC], Part 5, Section 3.2.5.2). 

Bundesamt für Sicherheit in der Informationstechnik 

31 

## **3.2.4 EndTransaction** 

**Name EndTransaction Description** The EndTransaction function terminates an existing transaction with a selected eCard. **Invocation parameters** Invocation of the EndTransaction function. **Name Description** SlotHandle The SlotHandle addresses the connection to the eCard. **Return** Return of the EndTransaction function. **Name Description** dss:Result Contains the status information and the errors of an executed action. This element is described in more detail below. Status information and errors in EndTransaction **Name Error codes** ResultMajor **•** /resultmajor#ok **•** /resultmajor#error **•** /resultmajor#warning 

Bundesamt für Sicherheit in der Informationstechnik 

32 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0033-00.png)


**----- Start of picture text -----**<br>
ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/ifdl/common#invalidSlotHandle<br>• /resultminor/ifdl/IO#noTransactionStarted<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A connection to an eCard was established with Connect and a transaction<br>started for the thus-connected card with BeginTransaction.<br>Postconditions The transaction is terminated.<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the EndTransaction function in the PC/SC resource manager<br>(also refer to [PC/SC], Part 5, Section 3.2.5.2).<br>**----- End of picture text -----**<br>


## **3.2.5 Transmit** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0033-02.png)


**----- Start of picture text -----**<br>
Name Transmit<br>Description The Transmit function sends one or more APDU(s) to a connected eCard. In<br>order to support the batch processing a set of<br>AcceptableStatusCode-elements (9000 etc.) MAY be attached to each<br>InputAPDU. If the eCard returns some not expected status code it is – even in<br>case of secure messaging – clear that there is a serious error and it does not make<br>sense to feed the remaining InputAPDU-elements in the batch to the eCard.<br>Invocation<br>parameters<br>Invocation of the Transmit function.<br>Name Description<br>SlotHandle With the SlotHandle the connection established with<br>Connect to the eCard is addressed.<br>InputAPDUInfo MAY be present multiple times and contains the command<br>APDU, which is sent to the eCard and optionally<br>acceptable status codes. It is of type<br>InputAPDUInfoType, which is explained below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

33 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0034-00.png)


**----- Start of picture text -----**<br>
The InputAPDUInfo contains information about an APDU, which will be sent<br>to the card.<br>Name Description<br>InputAPDU Contains the APDU which is to be sent to the eCard.<br>AcceptableSta MAY be present multiple times per InputAPDU-element<br>tusCode in order to specify the set of expected status codes. If the<br>status code which is returned from the eCard is not among<br>the expected values the batch processing SHALL be<br>stopped and the result of the processing returned to the<br>caller as this indicates that there is a serious error<br>condition.<br>If the AcceptableStatusCode-element is omitted,<br>any returned status code is assumed to be acceptable.<br>AcceptableStatusCode-elements containing only<br>one byte match all status codes starting with this byte.<br>Return<br>Return of the Transmit function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>OutputAPDU MAY be present multiple times and contains the APDU<br>returned by the eCard. If the batch processing is stopped<br>because a non-acceptable status word (see above) was<br>returned, all response ADPUs including the one containing<br>the non-acceptable status word SHALL be included. A<br>successful call of the Transmit function MUST contain<br>exactly as many InputAPDU- as<br>OutputAPDU-elements.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

34 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0035-00.png)


**----- Start of picture text -----**<br>
Status information and errors in Transmit<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/ifdl/common#invalidSlotHandle<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A connection to an eCard was established with Connect.<br>Postconditions The commands specified by the batch of APDU are executed by the eCard.<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the Transmit function in the PC/SC resource manager (also refer<br>to [PC/SC], Part 5, Section 3.2.5.2).<br>**----- End of picture text -----**<br>


## **3.3 User interaction functions** 

## **3.3.1 VerifyUser** 

**Name VerifyUser Description** The VerifyUser function initiates user verification with a PIN or a biometric characteristic. 

Bundesamt für Sicherheit in der Informationstechnik 

35 

**Invocation parameters** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0036-01.png)


**----- Start of picture text -----**<br>
Invocation of the VerifyUser function.<br>Name Description<br>SlotHandle With the SlotHandle the connection (established<br>with Connect) to the eCard is addressed.<br>InputUnit Specifies the input unit which is to be used for user<br>verification and also contains additional<br>information on possible processing of user<br>verification data. The entry is of the<br>InputUnitType described below.<br>DisplayIndex Specifies the index of the display on which the<br>messages should be shown for user guidance. If no<br>information is to be displayed or if the card<br>terminal does not have a display, this parameter is<br>omitted.<br>AltVUMessages Is an optional parameter which specifies the various<br>messages which should be shown on the display<br>during the verification process (see below for<br>details). If this parameter is missing, standard texts<br>are displayed.<br>TimeoutUntilFirst Is an optional parameter which describes the<br>Key timeout in milliseconds before the first key<br>actuation.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

36 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0037-00.png)


**----- Start of picture text -----**<br>
TimeoutAfterFirst Is an optional parameter which describes the<br>Key timeout in milliseconds after the first key actuation.<br>Template If applicable, the acquired verification data are<br>entered into the template before the data are sent to<br>the eCard. The structure of the template<br>corresponds to the structure of an APDU for the<br>VERIFY command in accordance with<br>[ISO7816-4] (Section 7.5.6).<br>InputUnit is an invocation parameter of VerifyUser<br>Name Description<br>PinInput This parameter is used if the user is to be<br>authenticated by means of a PIN. It is of the<br>PinInputType described below.<br>BiometricInput If the user is authenticated by a biometric<br>characteristic, a parameter of the<br>BiometricInputType (see below for details)<br>must be specified.<br>The PinInput element is a possible child element of the InputUnit<br>element.<br>Name Description<br>Index The index of the PIN pad to be used.<br>PasswordAttributes Contains the password attributes as defined in<br>[ISO7816-15]. Also refer to [TR-03112-4]. See<br>below for details.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

37 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0038-00.png)


The PasswordAttributes element is part of the PinInputType (see above ) and of the PinCompareQualifierType (refer to [TR-03112-4]). **Name Description** 

Bundesamt für Sicherheit in der Informationstechnik 

38 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0039-00.png)


**----- Start of picture text -----**<br>
pwdFlags Contains information on the character of the PIN (also refer<br>to pwdFlags in accordance with [ISO7816-15]). The<br>PasswordFlagsType is defined as follows:<br><simpleType name="PasswordFlagsType"><br> <union memberTypes="iso:BitString"><br>  <simpleType><br>   <list><br>    <simpleType><br><restriction base="token"><br><enumeration value="case-sensitive" /><br><enumeration value="local" /><br><enumeration value="change-disabled" /><br><enumeration value="unblock-disabled" /><br><enumeration value="initialized" /><br><enumeration value="needs-padding" /><br><enumeration value="unblockingPassword" /><br><enumeration value="soPassword" /><br><enumeration value="disable-allowed" /><br><enumeration value="integrity-protected" /><br><enumeration<br>value="confidentiality-protected"/><br><enumeration value="exchangeRefData" /><br><enumeration value="resetRetryCounter1" /><br><enumeration value="resetRetryCounter2" /><br>     </restriction><br></simpleType><br>   </list><br>  </simpleType><br> </union><br></simpleType><br>pwdType Contains information on the type of PIN (also refer to<br>pwdType in accordance with [ISO7816-15]). The<br>PasswordTypeType is defined as follows:<br><simpleType name="PasswordTypeType"><br><restriction base="string"><br><enumeration value="bcd" /><br><enumeration value="ascii-numeric" /><br><enumeration value="utf8" /><br><enumeration value="half-nibble-bcd" /><br><enumeration value="iso9564-1" /><br></restriction><br></simpleType><br>minLength Contains the minimum length of the PIN.<br>storedLength Contains the length of the PIN as stored on the card.<br>maxLength MAY contain the maximum length.<br>padChar MAY contain the padding character which is to be used for<br>padding.<br>lastPassword MAY contain the time of the last PIN modification.<br>Change<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

39 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0040-00.png)


**----- Start of picture text -----**<br>
BiometricInput is a parameter of the InputUnitType<br>Name Description<br>Index The index of the biometric sensor which is to be<br>used.<br>BiometricSubtype Specifies the subtype of the biometric characteristic<br>in accordance with Section 7.14 of [ISO19784-1].<br>AltVUMessages is part of VerifyUser<br>Name Description<br>Authentication Prompts the user to perform user verification (e.g. by<br>RequestMessage entering a PIN). If this element is missing, the<br>configured default message is used.<br>SuccessMessage Informs the user that user verification was successful.<br>If this element is missing, the configured default<br>message is used.<br>AuthenticationFa Shows the user that the user verification was not<br>iledMessage successful and that the eCard MAY therefore be<br>blocked. If this element is missing, the configured<br>default message is used.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

40 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0041-00.png)


**----- Start of picture text -----**<br>
RequestConfirmat Prompts the user to repeat the entry. If this element is<br>ionMessage missing, the configured default message is used.<br>CancelMessage Shows the user that the entry was cancelled. If this<br>element is missing, the configured default message is<br>used.<br>Return<br>Return of the VerifyUser function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Response The response of the eCard (e.g. 9000 in the<br>event of successful user verification).<br>Status information and errors in VerifyUser<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/ifdl/common#invalidSlotHandle<br>• /resultminor/ifdl/IO#unknownInputUnit<br>• /resultminor/ifdl#cancellationByUser<br>• /resultminor/al/common#unknownError<br>• /resultminor/ifdl/IO#unknownPINFormat<br>• /resultminor/ifdl/IO#unknownBiometricSubtype<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

41 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0042-00.png)


**----- Start of picture text -----**<br>
ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions A connection to an eCard was established with Connect.<br>Postconditions The corresponding authentication status on the card was established by<br>invocation of VERIFY in accordance with [ISO7816-4].<br>Notes A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with FEATURE_VERIFY_PIN_START specified in [PC/SC], Part 10<br>(Section 2.9) using the PIN_VERIFY_STRUCTURE defined in [PC/SC], Part<br>10 (Section 2.5).<br>**----- End of picture text -----**<br>


## **3.3.2 ModifyVerificationData** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0042-02.png)


**----- Start of picture text -----**<br>
Name ModifyVerificationData<br>Description With this function the data for user authentication (PIN or biometric reference<br>data) on an eCard are changed.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

42 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0043-00.png)


**----- Start of picture text -----**<br>
Invocation<br>parameters<br>Invocation of the ModifyVerificationData function.<br>Name Description<br>SlotHandle With the SlotHandle the connection to the<br>eCard (established with Connect) is<br>addressed.<br>InputUnit Specifies the input unit (for details refer to page<br>37).<br>DisplayIndex Specifies the index of the display on which the<br>messages should be shown for user guidance. If<br>no information is to be displayed or if the card<br>terminal does not have a display, this parameter<br>can be omitted.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

43 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0044-00.png)


**----- Start of picture text -----**<br>
AltMVDMessages Is an optional parameter which specifies the<br>various messages which should be shown on<br>the display if the identification data are<br>modified (see below for details). If this element<br>is missing, standard texts are displayed.<br>OldReferenceData MAY contain the old reference data so that it is<br>only necessary to enter the new data on the<br>terminal. In this case the data is formatted by<br>the calling layer. If this element is missing, the<br>old reference data are to be entered on the<br>terminal if necessary.<br>TimeoutUntilFirstKey Is an optional parameter which specifies the<br>timeout in milliseconds before the first key<br>actuation.<br>TimeoutAfterFirstKey Is an optional parameter which specifies the<br>timeout in milliseconds after the first key<br>actuation.<br>RepeatInput If this element is TRUE, repeated entry is<br>mandatory. If the element is missing, it is not<br>necessary to repeat the entry.<br>Template The acquired verification data are entered into<br>the template before the data are sent to the<br>eCard as APDU for the CHANGE<br>REFERENCE DATA command (also refer to<br>[ISO7816-4], Section 7.5.7) or the RESET<br>RETRY COUNTER command (also refer to<br>[ISO7816-4], Section 7.5.10).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

44 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0045-00.png)


**----- Start of picture text -----**<br>
AltMVDMessages can be used to transfer alternative messages. Part of<br>ModifyVerificationData (see above).<br>Name Description<br>AuthenticationRequest Prompts the user to perform user<br>Message verification (e.g. by entering a PIN). If<br>this element is missing, the configured<br>default message is used.<br>SuccessMessage Shows the user that user verification was<br>successful. If this element is missing, the<br>configured default message is used.<br>AuthenticationFailed Shows the user that the user verification<br>Message was not successful and that the eCard<br>MAY be blocked. If this element is<br>missing, the configured default message<br>is used.<br>EnterNewAuthentication If this element is missing, the configured<br>DataMessage default message is used.<br>RepeatInputMessage If this element is missing, the configured<br>default message is used.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

45 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0046-00.png)


**----- Start of picture text -----**<br>
ComparisonOfRepeatedData If this element is missing, the configured<br>Failed default message is used.<br>RequestConfirmation Prompts the user to repeat the entry. If<br>Message this element is missing, the configured<br>default message is used.<br>CancelMessage Shows the user that entry was canceled.<br>If this element is missing, the configured<br>default message is used.<br>Return<br>Return of the ModifyVerificationData function.<br>Name Description<br>dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>Response The response of the eCard.<br>Status information and errors in ModifyVerificationData<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

46 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0047-00.png)


**----- Start of picture text -----**<br>
ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/ifdl/common#invalidSlotHandle<br>• /resultminor/ifdl/IO#unknownInputUnit<br>• /resultminor/ifdl#cancellationByUser<br>• /resultminor/ifdl/IO#repeatedDataMismatch<br>• /resultminor/ifdl/IO#unknownPINFormat<br>• /resultminor/ifdl/IO#unknownBiometricSubtype<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error which<br>occurred if required.<br>Precondition A connection to an eCard was established with Connect.<br>Postcondition The corresponding command - CHANGE REFERENCE DATA or RESET<br>RETRY COUNTER in accordance with [ISO7816-4] – was executed on the card.<br>Note A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with FEATURE_MODIFY_PIN_START specified in [PC/SC], Part 10<br>(Section 2.9) using the PIN_MODIFY_STRUCTURE defined in [PC/SC], Part<br>10 (Section 2.6).<br>**----- End of picture text -----**<br>


## **3.3.3 Output** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0047-02.png)


**----- Start of picture text -----**<br>
Name Output<br>Description The command is used to output a message on the display of a card terminal<br>and/or output a visual or acoustic signal on a card terminal.<br>Invocation<br>parameters<br>Invocation of the Output function.<br>Name Description<br>ContextHandle Handle with which the session with the Terminal-Layer<br>is addressed.<br>IFDName Unique name of the card terminal.<br>OutputInfo Provides information about the output. Details are<br>specified below.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

47 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0048-00.png)


**----- Start of picture text -----**<br>
The OutputInfoType is used in the specification of the Output function<br>above and is used in addition in CardApplicationConnect (also refer<br>to [TR-03112-4]).<br>Name Description<br>Timeout MAY specify how long the output in milliseconds is<br>maintained. If this element is missing, the output<br>remains until Cancel or ReleaseContext is<br>invoked.<br>DisplayIndex MAY specify the index of the display on which any<br>existing message should be output. If there is only<br>one display, the parameter MAY be omitted.<br>Message Optionally contains the message which should be<br>output.<br>AcousticalSignal This optional parameter specifies whether an<br>acoustic signal should be output. If the card<br>terminal does not feature a suitable device, the<br>parameter is ignored.<br>OpticalSignal This optional parameter specifies whether a visual<br>signal should be output. If the card terminal does<br>not feature a suitable device, the parameter is<br>ignored.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

48 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0049-00.png)


**----- Start of picture text -----**<br>
Return<br>Return of the Output function.<br>Name Description<br>dss:Result Contains the status information and the errors of<br>an executed action. This element is described in<br>more detail below.<br>Status information and errors in Output.<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>• /resultmajor#warning<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /resultminor/ifdl/common#invalidContextHandle<br>• /resultminor/ifdl/terminal#unknownIFD<br>• /resultminor/ifdl/IO#unknownDisplayIndex<br>• /resultminor/al/common#unknownError<br>• /resultminor/ifdl/IO#unknownOutputDevice<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Precondition A context was established with EstablishContext.<br>Postcondition The respective output on the card terminal is completed.<br>Note A PC/SC handler in the IFD-Layer (also refer to Annex A) MAY implement this<br>function with the DisplayMessage function specified in [PC/SC], Part 9<br>(Section 4.1.8.2).<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

49 

## **3.4 IFD-Callback-Interface for card terminal events** 

The IFD-Callback-Interface is made available from layers above the Terminal-Layer and contains exactly the function SignalEvent. 

## **3.4.1 SignalEvent** 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0050-03.png)


**----- Start of picture text -----**<br>
Name SignalEvent<br>Description With the SignalEvent function layers above the Terminal-Layer can be<br>informed of card terminal events. The Terminal-Layer was informed with the<br>Wait function of the callback address provided for this invocation and additional<br>necessary parameters.<br>Invocation<br>parameters<br>Invocation of the SignalEvent function.<br>Name Description<br>ContextHandle Handle with which the session with the<br>Terminal-Layer is addressed.<br>SessionIdentifier Identifier transmitted during return of the Wait<br>function.<br>IFDEvent IFDEvent MAY occur several times and<br>contains information about an event which<br>occurred on a card terminal. The parameter is of<br>the IFDStatusType (refer to page 18), and<br>contains the status information modified by the<br>event.<br>Return<br>Return of the SignalEvent function.<br>Name Description<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

50 


![](markdown/tr/TR-03112-api_teil6/TR-03112-api_teil6.pdf-0051-00.png)


**----- Start of picture text -----**<br>
dss:Result Contains the status information and the errors of an<br>executed action. This element is described in more detail<br>below.<br>Status information and errors in SignalEventResponse<br>Name Error codes<br>ResultMajor • /resultmajor#ok<br>• /resultmajor#error<br>ResultMinor • /resultminor/ifdl/common#timeoutError<br>• /<br>resultminor/ifdl/common#invalidContextHandl<br>e<br>• /resultminor/ifdl/terminal#unknownIFD<br>• /resultminor/al/common#unknownError<br>ResultMessage MAY contain more detailed information on the error<br>which occurred if required.<br>Preconditions Registration for events was performed on specific terminals by means of Wait,<br>whereby the respective callback address was specified.<br>Postconditions When SignalEvent is invoked, waiting for events on the specified card<br>terminals is terminated and as a result the session identifier loses its validity.<br>Notes Also refer to Wait and Cancel.<br>**----- End of picture text -----**<br>


Bundesamt für Sicherheit in der Informationstechnik 

51 

## **References** 

- [TR-03112-2] BSI: TR-03112-2: eCard-API-Framework – Part 2: eCard-Interface [TR-03112-3] BSI: TR-03112-3: eCard-API-Framework – Part 3: Management-Interface [TR-03112-4] BSI: TR-03112-4: eCard-API-Framework – Part 4: ISO24727-3-Interface [TR-03112-5] BSI: TR-03112-5: eCard-API Framework – Part 5: Suppor- Interface [TR-03112-6] BSI: TR-03112-6: eCard-API-Framework – Part 6: IFD-Interface [TR-03112-7] BSI: TR-03112-7: eCard-API-Framework – Part 7: Protocols [TR-03119] BSI: TR-03119: Anforderungen an Chipkartenleser mit ePA-Unterstützung [RFC2119] IETF: RFC 2119: S. Bradner: Key words for use in RFCs to Indicate Requirement Levels [ISO19784-1] ISO: ISO/IEC 19784-1: Information technology — Biometric application programming interface — Part 1: BioAPI specification 

- [ISO24727-3] ISO: ISO/IEC 24727-3: Identification Cards — Integrated Circuit Cards Programming Interfaces — Part 3: Application Interface 

- [ISO7816-15] ISO: ISO/IEC 7816-15: Identification cards - Integrated circuit(s) cards with contacts — Part 15: Cryptographic information application 

- [ISO7816-4] ISO: ISO/IEC 7816-4: Identification cards — Integrated circuit cards — Part 4:Organization, security and commands for interchange 

- [PC/SC] PC/SC Workgroup: PC/SC Workgroup Specifications 1.0/2.0 

Bundesamt für Sicherheit in der Informationstechnik 

52 


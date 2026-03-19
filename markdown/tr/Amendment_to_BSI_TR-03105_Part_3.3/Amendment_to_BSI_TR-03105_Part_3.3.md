
![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0001-00.png)


Amendment to BSI TR-03105 Part 3.3 

_Version:_ **Release 3** _Status:_ f **inal** _Date:_ **04.06.2012** 

Bundesamt für Sicherheit in der Informationstechnik Postfach 20 03 63 53133 Bonn Internet: https://www.bsi.bund.de © Bundesamt für Sicherheit in der Informationstechnik 2012 

Amendment to BSI TR-03105 Part 3.3 

## **Content** 

|**Amendment to BSI TR-03105 Part 3.3**<br>**................................................................................**<br>**1**|
|---|
|**1 Introduction**<br>**..........................................................................................................................**<br>**4**|
|**2 Profiles**<br>**..................................................................................................................................**<br>**5**|
|2.1 Protocol profiles<br>.......................................................................................................................<br>5|
|**3 Certificates**<br>**............................................................................................................................**<br>**6**|
|3.1 Certificate Set 17<br>......................................................................................................................<br>6|
|3.1.1 DV_CERT_17<br>....................................................................................................................................<br>6|
|3.1.2 AT_CERT_17h<br>..................................................................................................................................<br>7|
|3.2 Certificate Set 21<br>......................................................................................................................<br>8|
|3.2.1 DV_CERT_21<br>....................................................................................................................................<br>8|
|3.3 Certificate Set 22<br>......................................................................................................................<br>9|
|3.3.1 DV_CERT_22<br>....................................................................................................................................<br>9|
|3.4 Certificate Set 23<br>....................................................................................................................<br>10|
|3.4.1 LINK_CERT_23a<br>............................................................................................................................<br>10|
|3.4.2 LINK_CERT_23b<br>............................................................................................................................<br>11|
|**4 Test cases**<br>**............................................................................................................................**<br>**13**|
|4.1 Unit EAC2_ISO7816_I Chip Authentication<br>.........................................................................<br>13|
|4.1.1 Test case EAC2_ISO7816_I_17<br>......................................................................................................<br>13|
|4.2 Unit EAC2_ISO7816_K Terminal Authentication<br>.................................................................<br>14|
|4.2.1 Test case EAC2_ISO7816_K_13<br>.....................................................................................................<br>14|
|4.2.2 Test case EAC2_ISO7816_K_14<br>.....................................................................................................<br>15|
|4.2.3 Test case EAC2_ISO7816_K_15<br>.....................................................................................................<br>16|
|4.3 Unit EAC2_ISO7816_L Effective Access Conditions<br>...........................................................<br>18|
|4.3.1 Test case EAC2_ISO7816_L_29<br>.....................................................................................................<br>18|
|4.3.2 Test case EAC2_ISO7816_L_30<br>.....................................................................................................<br>18|
|4.3.3 Test case EAC2_ISO7816_L_31<br>.....................................................................................................<br>18|
|4.3.4 Test case EAC2_ISO7816_L_32<br>.....................................................................................................<br>18|
|4.3.5 Test case EAC2_ISO7816_L_33<br>.....................................................................................................<br>18|
|4.3.6 Test case EAC2_ISO7816_L_34<br>.....................................................................................................<br>18|
|4.3.7 Test case EAC2_ISO7816_L_37<br>.....................................................................................................<br>18|
|4.4 Unit EAC2_EIDDATA_B eID Data Groups<br>.........................................................................<br>20|
|4.4.1 Test case EAC2_EIDDATA_B_18<br>..................................................................................................<br>20|
|4.5 Unit EAC2_DATA_C EF.ChipSecurity<br>.................................................................................<br>20|
|4.5.1 Test case EAC2_DATA_C_1<br>..........................................................................................................<br>20|
|4.5.2 Test cases EAC2_DATA_C_2 to EAC2_DATA_C_7<br>....................................................................<br>21|
|4.5.3 Test case EAC2_DATA_C_8<br>..........................................................................................................<br>21|
|4.5.4 Test case EAC2_DATA_C_9<br>..........................................................................................................<br>22|



3/22 

Amendment to BSI TR-03105 Part 3.3 

## **1 Introduction** 

This amendment defines changes of test cases and certificate descriptions of **BSI TR-03105 Part 3.3 Version 1.03** . The amendment does add or replace the herein described test case and certificates. The purpose of this amendment is to collect corrections and clarifications of the TR-03105 Part 3.3 to provide a systematic and formal document in addition. The changes defined in this document will be taken as comments and eventually be adopted to a new version of the TR-03105 Part 3.3. 

4/22 

Amendment to BSI TR-03105 Part 3.3 

## **2 Profiles** 

## **2.1 Protocol profiles** 

Add the following profile to the protocol profile table (chapter 2.2.2 in TR-03105 Part 3.3): 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0005-04.png)


**----- Start of picture text -----**<br>
Profile-ID Profile Remark<br>CS Chip Security A MRTD which which stores a ChipSecurity file<br>containing PrivilegedTerminalInfo with chip-<br>individual keys and eIDSecurityInfo.<br>**----- End of picture text -----**<br>


Annex A shall be extended in order to declare the support of this new profile. 

5/22 

Amendment to BSI TR-03105 Part 3.3 

## **3 Certificates** 

All certificates described in this chapter replace the certificates with the same ID in the BSI TR-03105 Part 3.3. 

## **3.1 Certificate Set 17** 

## **3.1.1 DV_CERT_17** 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0006-05.png)


**----- Start of picture text -----**<br>
ID DV_CERT_17<br>Purpose This certificate is a regular DV certificate, which validity period starts at the<br>effective date of the CVCA and expires after one month. The certificate permits<br>access to all eID special functions. It also permits read access to DG1 for testing<br>access permissions.<br>Version Am_3<br>Referred  Test case EAC2_ISO7816_L_17, Test case EAC2_ISO7816_L_18, Test case<br>by EAC2_ISO7816_L_19, Test case EAC2_ISO7816_L_20, Test case<br>EAC2_ISO7816_L_21, Test case EAC2_ISO7816_L_22, Test case<br>EAC2_ISO7816_L_23, Test case EAC2_ISO7816_L_24, Test case<br>EAC2_ISO7816_L_25, Test case EAC2_ISO7816_L_26, Test case<br>EAC2_ISO7816_L_27, Test case EAC2_ISO7816_L_28, Test case<br>EAC2_ISO7816_M_6, Test case EAC2_ISO7816_O_9, Test case<br>EAC2_ISO7816_O_10, Test case EAC2_ISO7816_O_11, Test case<br>EAC2_ISO7816_O_12, Test case EAC2_ISO7816_P_15, Test case<br>EAC2_ISO7816_P_16, Test case EAC2_ISO7816_P_17, Test case<br>EAC2_ISO7816_P_18, Test case EAC2_ISO7816_Q_1, Test case<br>EAC2_ISO7816_Q_2, Test case EAC2_ISO7816_Q_3, Test case<br>EAC2_ISO7816_Q_4, Test case EAC2_ISO7816_Q_6, Test case<br>EAC2_ISO7816_Q_7, Test case EAC2_ISO7816_Q_8, Test case<br>EAC2_ISO7816_Q_10, Test case EAC2_ISO7816_Q_11, Test case<br>EAC2_ISO7816_Q_12, Test case EAC2_ISO7816_Q_13, Test case<br>EAC2_ISO7816_Q_15, Test case EAC2_ISO7816_R_1, Test case<br>EAC2_ISO7816_R_3, Test case EAC2_ISO7816_R_5, Test case<br>EAC2_ISO7816_R_6<br>Content  7F 21 aa<br>definition 7F 4E bb<br>5F 29  01 00<br>42 cc dd<br>7F 49 ee ff<br>5F 20 xx yy<br>7F 4C  0E 06 09 04 00 7F 00 07 03 01 02 02 53 05 80<br>00 00 01 FF<br>5F 25  06  gg<br>5F 24  06  hh<br>5F 37 ii jj<br>aa  is the encoded combined length of certificate body and signature objects<br>bb  is the encoded length the certificate body object<br>cc  is the encoded length of the Certificate Authority Reference<br>**----- End of picture text -----**<br>


6/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0007-01.png)


**----- Start of picture text -----**<br>
dd  is the placeholder for the Certificate Authority Reference (cc bytes)<br>ee  is the encoded length of the certificate's public key,<br>ff  is the placeholder for the certificate's public key bytes (ee bytes),<br>xx  is the encoded length of the Certificate Holder Reference<br>yy  is the placeholder for the Certificate Holder Reference (xx bytes)<br>gg  is the placeholder for the BCD encoded effective date of the certificate<br>hh  is the placeholder for the BCD encoded expiration date of the certificate<br>ii  is the encoded length of the certificates signature object,<br>jj  is the placeholder for the certificates signature (ii bytes)<br>Parameter Certificate Authority Reference As defined by the initial AT CVCA reference<br>Certificate Holder Reference DETESTDVDE017<br>Certificate Holder Authorization Official domestic DV, read DG1, eID-Specials<br>(all)<br>Certificate effective date CVCAeff<br>Certificate expiration date CVCAeff + 1 month<br>Public Key reference Public key of key pair DV_KEY_17<br>Signing Key reference Signed with the private key of key pair<br>CVCA_KEY_17<br>**----- End of picture text -----**<br>


## **3.1.2 AT_CERT_17h** 

This certificate was added in release 3 of this amendment. 

**ID** AT_CERT_17h **Purpose** This certificate is a regular terminal certificate, which is issued by the DV_CERT_17. It encodes access rights for the eID special function “CAN allowed” and “Privileged Terminal”. **Version** Am_3 **Referred** Test case EAC2_ISO7816_L_37 **by Content 7F 21** _aa_ **definition 7F 4E** _bb_ **5F 29** 01 00 **42** _cc dd_ **7F 49** _ee ff_ **5F 20** _xx yy_ **7F 4C** 0E 06 09 04 00 7F 00 07 03 01 02 02 53 05 00 00 00 00 18 **5F 25** 06 _gg_ **5F 24** 06 _hh_ **5F 37** _ii jj_ 

_aa_ is the encoded combined length of certificate body and signature objects _bb_ is the encoded length the certificate body object _cc_ is the encoded length of the Certificate Authority Reference _dd_ is the placeholder for the Certificate Authority Reference (cc bytes) _ee_ is the encoded length of the certificate's public key, _ff_ is the placeholder for the certificate's public key bytes (ee bytes), _xx_ is the encoded length of the Certificate Holder Reference 

7/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0008-01.png)


**----- Start of picture text -----**<br>
yy  is the placeholder for the Certificate Holder Reference (xx bytes)<br>gg  is the placeholder for the BCD encoded effective date of the certificate<br>hh  is the placeholder for the BCD encoded expiration date of the certificate<br>ii  is the encoded length of the certificates signature object,<br>jj  is the placeholder for the certificates signature (ii bytes)<br>Parameter Certificate Authority Reference DETESTDVDE017<br>Certificate Holder Reference DETESTATDE017<br>Certificate Holder Authorization Terminal, CAN allowed, Privileged Terminal<br>Certificate effective date CVCAeff<br>Certificate expiration date CVCAeff + 1 month<br>Public Key reference Public key of key pair AT_KEY_17<br>Signing Key reference Signed with the private key of key pair<br>DV_KEY_17<br>**----- End of picture text -----**<br>


## **3.2 Certificate Set 21** 

## **3.2.1 DV_CERT_21** 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0008-04.png)


**----- Start of picture text -----**<br>
ID DV_CERT_21<br>Purpose This certificate is a regular DV certificate, which validity period starts at the<br>effective date of the CVCA and expires after one month. The certificate permits<br>write access to all elementary files<br>Version Am_1<br>Referred  Test case EAC2_ISO7816_L_15 Template, Test case EAC2_ISO7816_O_7<br>by Template<br>Content  7F 21 aa<br>definition 7F 4E bb<br>5F 29  01 00<br>42 cc dd<br>7F 49 ee ff<br>5F 20 xx yy<br>7F 4C  0E 06 09 04 00 7F 00 07 03 01 02 02 53 05 BE<br>1F FF FF 10<br>5F 25  06  gg<br>5F 24  06  hh<br>5F 37 ii jj<br>aa  is the encoded combined length of certificate body and signature objects<br>bb  is the encoded length the certificate body object<br>cc  is the encoded length of the Certificate Authority Reference<br>dd  is the placeholder for the Certificate Authority Reference (cc bytes)<br>ee  is the encoded length of the certificate's public key,<br>ff  is the placeholder for the certificate's public key bytes (ee bytes),<br>xx  is the encoded length of the Certificate Holder Reference<br>yy  is the placeholder for the Certificate Holder Reference (xx bytes)<br>gg  is the placeholder for the BCD encoded effective date of the certificate<br>hh  is the placeholder for the BCD encoded expiration date of the certificate<br>ii  is the encoded length of the certificates signature object,<br>**----- End of picture text -----**<br>


8/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0009-01.png)


**----- Start of picture text -----**<br>
jj  is the placeholder for the certificates signature (ii bytes)<br>Parameter Certificate Authority  As defined by the initial AT CVCA reference<br>Reference<br>Certificate Holder  DETESTDVDE021<br>Reference<br>Certificate Holder  Official domestic DV, write access (all), CAN<br>Authorization allowed<br>Certificate effective date CVCAeff<br>Certificate expiration date CVCAeff + 1 month<br>Public Key reference Public key of key pair DV_KEY_21<br>Signing Key reference Signed with the private key of key pair<br>CVCA_KEY_17<br>**----- End of picture text -----**<br>


## **3.3 Certificate Set 22** 

## **3.3.1 DV_CERT_22** 

**ID** DV_CERT_22 **Purpose** This certificate is a regular DV certificate, which validity period starts at the effective date of the CVCA and expires after one month. The certificate permits write access to all elementary files **Version** Am_1 **Referred** Test case EAC2_ISO7816_L_16 Template, Test case EAC2_ISO7816_O_8 **by** Template **Content 7F 21** _aa_ **definition 7F 4E** _bb_ **5F 29** 01 00 **42** _cc dd_ **7F 49** _ee ff_ **5F 20** _xx yy_ **7F 4C** 0E 06 09 04 00 7F 00 07 03 01 02 02 53 05 7E 1F FF FF 10 **5F 25** 06 _gg_ **5F 24** 06 _hh_ **5F 37** _ii jj_ 

aa is the encoded combined length of certificate body and signature objects bb is the encoded length the certificate body object cc is the encoded length of the Certificate Authority Reference dd is the placeholder for the Certificate Authority Reference (cc bytes) ee is the encoded length of the certificate's public key, ff is the placeholder for the certificate's public key bytes (ee bytes), xx is the encoded length of the Certificate Holder Reference yy is the placeholder for the Certificate Holder Reference (xx bytes) gg is the placeholder for the BCD encoded effective date of the certificate hh is the placeholder for the BCD encoded expiration date of the certificate ii is the encoded length of the certificates signature object, jj is the placeholder for the certificates signature (ii bytes) 

9/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0010-01.png)


**----- Start of picture text -----**<br>
Parameter Certificate Authority  As defined by the initial AT CVCA reference<br>Reference<br>Certificate Holder  DETESTDVDE022<br>Reference<br>Certificate Holder  Commercial DV, write access (all), CAN allowed<br>Authorization<br>Certificate effective date CVCAeff<br>Certificate expiration date CVCAeff + 1 month<br>Public Key reference Public key of key pair DV_KEY_22<br>Signing Key reference Signed with the private key of key pair<br>CVCA_KEY_17<br>**----- End of picture text -----**<br>


## **3.4 Certificate Set 23** 

## **3.4.1 LINK_CERT_23a** 

**ID** LINK_CERT_23a **Purpose** This certificate is a link certificate, which validity period starts one day before the original CVCA certificate expires. **Version** Am_3 **Referred** Test case EAC2_ISO7816_M_7 **by Content 7F 21** _aa_ **definition 7F 4E** _bb_ **5F 29** 01 00 **42** _cc dd_ **7F 49** _ee ff_ **5F 20** _xx yy_ **7F 4C** 0E 06 09 04 00 7F 00 07 03 01 02 02 53 05 FE 1F FF FF FF **5F 25** 06 _gg_ **5F 24** 06 _hh_ **5F 37** _ii jj_ 

_aa_ is the encoded combined length of certificate body and signature objects _bb_ is the encoded length the certificate body object 

_cc_ is the encoded length of the Certificate Authority Reference _dd_ is the placeholder for the Certificate Authority Reference (cc bytes) _ee_ is the encoded length of the certificate's public key, _ff_ is the placeholder for the certificate's public key bytes (ee bytes), _xx_ is the encoded length of the Certificate Holder Reference _yy_ is the placeholder for the Certificate Holder Reference (xx bytes) _gg_ is the placeholder for the BCD encoded effective date of the certificate _hh_ is the placeholder for the BCD encoded expiration date of the certificate _ii_ is the encoded length of the certificates signature object, _jj_ is the placeholder for the certificates signature (ii bytes) **Parameter** Certificate Authority As defined by the initial AT CVCA reference Reference 

10/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0011-01.png)


**----- Start of picture text -----**<br>
Certificate Holder  DETESTLINKDE23A<br>Reference<br>Certificate Holder  CVCA, Unrestricted rights<br>Authorization<br>Certificate effective date CVCAexp - 1 day<br>Certificate expiration date CVCAexp + 3 month<br>Public Key reference Public key of key pair AT_CVCA_KEY_23a<br>Signing Key reference Signed with the private key of key pair<br>AT_CVCA_KEY_17<br>**----- End of picture text -----**<br>


## **3.4.2 LINK_CERT_23b** 

**ID** LINK_CERT_23b **Purpose** This certificate is a link certificate, which validity period starts one month before the previous CVCA certificate expires. **Version** Am_3 **Referred** Test case EAC2_ISO7816_M_7 **by Content 7F 21** _aa_ **definition 7F 4E** _bb_ **5F 29** 01 00 **42** _cc dd_ **7F 49** _ee ff_ **5F 20** _xx yy_ **7F 4C** 0E 06 09 04 00 7F 00 07 03 01 02 02 53 05 FE 1F FF FF FF **5F 25** 06 _gg_ **5F 24** 06 _hh_ **5F 37** _ii jj_ 

_aa_ is the encoded combined length of certificate body and signature objects _bb_ is the encoded length the certificate body object _cc_ is the encoded length of the Certificate Authority Reference _dd_ is the placeholder for the Certificate Authority Reference (cc bytes) _ee_ is the encoded length of the certificate's public key, _ff_ is the placeholder for the certificate's public key bytes (ee bytes), _xx_ is the encoded length of the Certificate Holder Reference _yy_ is the placeholder for the Certificate Holder Reference (xx bytes) _gg_ is the placeholder for the BCD encoded effective date of the certificate _hh_ is the placeholder for the BCD encoded expiration date of the certificate _ii_ is the encoded length of the certificates signature object, _jj_ is the placeholder for the certificates signature (ii bytes) **Parameter** Certificate Authority Reference DETESTLINKDE23A Certificate Holder Reference DETESTLINKDE23B Certificate Holder Authorization CVCA, Unrestricted rights Certificate effective date CVCAexp + 2 month Certificate expiration date CVCAexp + 5 month Public Key reference Public key of key pair AT_CVCA_KEY_23b 

11/22 

Amendment to BSI TR-03105 Part 3.3 

Signing Key reference 

Signed with the private key of key pair AT_CVCA_KEY_23a 

12/22 

Amendment to BSI TR-03105 Part 3.3 

## **4 Test cases** 

All test cases described in this chapter replace the test cases with the same Test-ID in the BSI TR03105 Part 3.3. Test cases with new Test-ID have to be performed in addition. 

## **4.1 Unit EAC2_ISO7816_I Chip Authentication** 

## **4.1.1 Test case EAC2_ISO7816_I_17** 

This test case was added in release 3 of this amendment. 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0013-06.png)


**----- Start of picture text -----**<br>
Test - ID EAC2_ISO7816_I_17<br>Purpose MSE:Set AT / General Authenticate commands with correct ephemeral public<br>key using ChipAuthenticationPublicKeyInfo encapsulate in<br>PrivilegedTerminalInfo<br>Version Am_3<br>Profile PACE, TA2, CA2, CS<br>Preconditions 1. The PACE mechanism MUST have been performed.<br>2. The Terminal Authentication MUST have been performed<br>(DV_CERT_1, IS_CERT_1)<br>3. The ChipAuthenticationPublicKeyInfo encapsulated in<br>PrivilegedTerminalInfo stored in ChipSecurity file MUST have been<br>read to be able to generate an ephemeral key pair.<br>4. All commands are encoded as legally structured Secure Messaging<br>APDUs.<br>Test scenario 1. Send the given MSE:Set AT APDU to the eID Card.<br>‘0C 22 41 A4 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>80 <L80> <cryptographic mechanism reference><br>84 <L84> <private key reference><br>• The private key reference MUST be included in the APDU if and<br>only if it is specified in the ChipAuthenticationPublicKeyInfo<br>structure encapsulated in the PriviledTerminalInfo stored in<br>EF.ChipSecurity file.<br>2. Send the given General Authenticate APDU to the eID Card.<br>‘0C 86 00 00 <Lc> 87 <L87> 01 <Cryptogram> 97<br><L97> <Ne> 8E 08 <Checksum> <Le>’<br>• <Cryptogram> contains the following encrypted data objects<br>7C <L7C> 80 <L80> <ephemeral public key><br>3. Verify the returned authentication token TPICC<br>4. To verify the chips ability to continue the Secure Messaging with the<br>new session keys, an arbitrary SM APDU is send to the chip.<br>‘0C B0 (80 || <sfi.EF.CardAccess>) 00 0D 97 01<br>01 8E 08 <checksum> 00’<br>Expected  1. ’90 00’ in a valid Secure Messaging response. The returned data MUST<br>results be encoded with the OLD session keys.<br>**----- End of picture text -----**<br>


13/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0014-01.png)


2. 7C <L7C> ’81 <L81> <Nonce> 82 <L82> <Authentication Token> 90 00’ in a valid Secure Messaging response. The returned data MUST be encoded with the OLD session keys. 3. True 4. ’90 00’ and a valid Secure Messaging response. The returned data MUST be encoded with the NEW session keys. 

## **4.2 Unit EAC2_ISO7816_K Terminal Authentication** 

## **4.2.1 Test case EAC2_ISO7816_K_13** 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0014-05.png)


**----- Start of picture text -----**<br>
Test - ID EAC2_ISO7816_K_13<br>Purpose This test case checks if the eID card does not accept more than one execution of<br>Terminal Authentication within the same session, same certificate set.<br>Version Am_2<br>Profile PACE, TA2<br>Preconditions 1. The PACE mechanism MUST have been performed.<br>2. The Terminal Authentication mechanism MUST have been performed<br>(DV_CERT_15, IS_CERT_15a).<br>3. All APDUs are sent as valid SecureMessaging APDUs.<br>Test scenario 1. Send the given MSE: Set DST APDU to the eID Card.<br>‘0C 22 81 B6 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>83 <L83> <certificate authority reference><br>• The Certificate Authority Reference MUST be used as returned by<br>the PACE mechanism.<br>2. Send the appropriate DV-Certificate as specified in the “Certificate Set<br>15” chapter as DV_CERT_15.<br>‘0C 2A 00 BE <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>7F 4E <L7F4E> <certificate body><br>5F 37 <L5F37> <certificate signature><br>3. Send the given MSE: Set DST APDU to the eID Card.<br>‘0C 22 81 B6 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>83 <L83> <certificate authority reference><br>• The Certificate Holder Reference stored inside the DV-Certificate<br>sent in step 2 has to be used.<br>4. Send the appropriate IS-Certificate as specified in the “Certificate Set<br>15” chapter as IS_CERT_15.<br>‘0C 2A 00 BE <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>7F 4E <L7F4E> <certificate body><br>5F 37 <L5F37> <certificate signature><br>**----- End of picture text -----**<br>


14/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0015-01.png)


**----- Start of picture text -----**<br>
5. Send the given MSE: Set AT APDU to the eID Card.<br>‘0C 22 81 A4 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>80 <L80> <Cryptographic Mechanism Reference><br>83 <L83> <Certificate Holder Reference ><br>91 <L91> <Compressed Ephemeral Public Key><br>• The Certificate Holder Reference stored inside the IS-Certificate<br>sent in step 4 has to be used.<br>6. Send the given Get Challenge APDU to the eID Card.<br>‘0C 84 00 00 0D 97 01 08 8E 08 <Checksum> 00’<br>7. Send the given external authenticate command to the eID Card.<br>‘0C 82 00 00 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the encrypted terminal generated signature<br>Expected  1. ’90 00’ within a valid SM response<br>results 2. ’90 00’ within a valid SM response<br>3. ’90 00’ within a valid SM response<br>4. ’90 00’ within a valid SM response<br>5. ’90 00’ or Checking error within a valid SM response. If this step<br>returns Checking error the following steps don't need to be performed.<br>6. ‘<Eight bytes of random data> 90 00’ within an SM response<br>7. Checking error within a valid SM response<br>**----- End of picture text -----**<br>


## **4.2.2 Test case EAC2_ISO7816_K_14** 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0015-03.png)


**----- Start of picture text -----**<br>
Test - ID EAC2_ISO7816_K_14<br>Purpose This test case checks if the eID card does not accept more than one execution of<br>Terminal Authentication within the same session, different certificate sets.<br>Version Am_2<br>Profile PACE, TA2<br>Preconditions 1. The PACE mechanism MUST have been performed.<br>2. The Terminal Authentication mechanism MUST have been performed<br>(DV_CERT_1, IS_CERT_1).<br>3. All APDUs are sent as valid SecureMessaging APDUs.<br>Test scenario 1. Send the given MSE: Set DST APDU to the eID Card.<br>‘0C 22 81 B6 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>83 <L83> <certificate authority reference><br>• The Certificate Authority Reference MUST be used as returned by<br>the PACE mechanism.<br>2. Send the appropriate DV-Certificate as specified in the “Certificate Set<br>15” chapter as DV_CERT_15.<br>‘0C 2A 00 BE <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>**----- End of picture text -----**<br>


15/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0016-01.png)


**----- Start of picture text -----**<br>
7F 4E <L7F4E> <certificate body><br>5F 37 <L5F37> <certificate signature><br>3. Send the given MSE: Set DST APDU to the eID Card.<br>‘0C 22 81 B6 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>83 <L83> <certificate authority reference><br>• The Certificate Holder Reference stored inside the DV-Certificate<br>sent in step 2 has to be used.<br>4. Send the appropriate IS-Certificate as specified in the “Certificate Set<br>15” chapter as IS_CERT_15b.<br>‘0C 2A 00 BE <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>7F 4E <L7F4E> <certificate body><br>5F 37 <L5F37> <certificate signature><br>5. Send the given MSE: Set AT APDU to the eID Card.<br>‘0C 22 81 A4 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>80 <L80> <Cryptographic Mechanism Reference><br>83 <L83> <Certificate Holder Reference ><br>91 <L91> <Compressed Ephemeral Public Key><br>• The Certificate Holder Reference stored inside the IS-Certificate<br>sent in step 4 has to be used.<br>6. Send the given Get Challenge APDU to the eID Card.<br>‘0C 84 00 00 0D 97 01 08 8E 08 <Checksum> 00’<br>7. Send the given external authenticate command to the eID Card.<br>‘0C 82 00 00 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the encrypted terminal generated signature<br>Expected  1. ’90 00’ within a valid SM response<br>results 2. ’90 00’ within a valid SM response<br>3. ’90 00’ within a valid SM response<br>4. ’90 00’ within a valid SM response<br>5. ’90 00’ or Checking error within a valid SM response. If this step<br>returns Checking error the following steps don't need to be performed.<br>6. ‘<Eight bytes of random data> 90 00’ within an SM response<br>7. Checking error within a valid SM response<br>**----- End of picture text -----**<br>


## **4.2.3 Test case EAC2_ISO7816_K_15** 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0016-03.png)


**----- Start of picture text -----**<br>
Test - ID EAC2_ISO7816_K_15<br>Purpose This test case checks if the eID card does not accept more than one execution of<br>Terminal Authentication within the same session, different auxiliary data.<br>Version Am_2<br>Profile PACE, TA2<br>Preconditions 1. The PACE mechanism MUST have been performed.<br>**----- End of picture text -----**<br>


16/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0017-01.png)


**----- Start of picture text -----**<br>
2. The Terminal Authentication mechanism MUST have been performed<br>(DV_CERT_15, IS_CERT_15b).<br>3. Auxiliary data with valid Date of Birth data object MUST have been<br>sent by authorized terminal during Terminal Authentication mechanism.<br>DOB MUST NOT fit the required age.<br>4. All APDUs are sent as valid SecureMessaging APDUs.<br>Test scenario 1. Send the given MSE: Set DST APDU to the eID Card.<br>‘0C 22 81 B6 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>83 <L83> <certificate authority reference><br>• The Certificate Authority Reference MUST be used as returned by<br>the PACE mechanism.<br>2. Send the appropriate DV-Certificate as specified in the “Certificate Set<br>15” chapter as DV_CERT_15.<br>‘0C 2A 00 BE <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>7F 4E <L7F4E> <certificate body><br>5F 37 <L5F37> <certificate signature><br>3. Send the given MSE: Set DST APDU to the eID Card.<br>‘0C 22 81 B6 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>83 <L83> <certificate authority reference><br>• The Certificate Holder Reference stored inside the DV-Certificate<br>sent in step 2 has to be used.<br>4. Send the appropriate IS-Certificate as specified in the “Certificate Set<br>15” chapter as IS_CERT_15b.<br>‘0C 2A 00 BE <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>7F 4E <L7F4E> <certificate body><br>5F 37 <L5F37> <certificate signature><br>5. Send the given MSE: Set AT APDU to the eID Card.<br>‘0C 22 81 A4 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>80 <L80> <Cryptographic Mechanism Reference><br>83 <L83> <Certificate Holder Reference><br>91 <L91> <Compressed Ephemeral Public Key><br>67 <L67> <Auxiliary Data><br>• The Certificate Holder Reference stored inside the IS-Certificate<br>sent in step 4 has to be used.<br>• Auxiliary data with valid Date of Birth data object DOB MUST fit<br>the required age.<br>6. Send the given Get Challenge APDU to the eID Card.<br>‘0C 84 00 00 0D 97 01 08 8E 08 <Checksum> 00’<br>7. Send the given external authenticate command to the eID Card.<br>‘0C 82 00 00 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br>**----- End of picture text -----**<br>


17/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0018-01.png)


**----- Start of picture text -----**<br>
<Checksum> 00’<br>• <Cryptogram> contains the encrypted terminal generated signature<br>Expected  1. ’90 00’ within a valid SM response<br>results 2. ’90 00’ within a valid SM response<br>3. ’90 00’ within a valid SM response<br>4. ’90 00’ within a valid SM response<br>5. ’90 00’ or Checking error within a valid SM response. If this step<br>returns Checking error the following steps don't need to be performed.<br>6. ‘<Eight bytes of random data> 90 00’ within an SM response<br>7. Checking error within a valid SM response<br>**----- End of picture text -----**<br>


## **4.3 Unit EAC2_ISO7816_L Effective Access Conditions** 

## **4.3.1 Test case EAC2_ISO7816_L_29** 

Deleted in Amendment Release 1 

## **4.3.2 Test case EAC2_ISO7816_L_30** 

Deleted in Amendment Release 1 

## **4.3.3 Test case EAC2_ISO7816_L_31** 

Deleted in Amendment Release 1 

## **4.3.4 Test case EAC2_ISO7816_L_32** 

Deleted in Amendment Release 1 

## **4.3.5 Test case EAC2_ISO7816_L_33** 

Deleted in Amendment Release 1 

## **4.3.6 Test case EAC2_ISO7816_L_34** 

Deleted in Amendment Release 1 

## **4.3.7 Test case EAC2_ISO7816_L_37** 

This test case was added in release 3 of this amendment. 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0018-17.png)


**----- Start of picture text -----**<br>
Test - ID EAC2_ISO7816_L_37<br>Purpose Positive test with a valid terminal authentication process with rights for special<br>functions if the DV certificate permits all special functions while the terminal<br>certificate restricts access to one special function. DV certificate is an official<br>domestic certificate. Special function allowed by terminal certificate is<br>“Privileged Terminal”.<br>**----- End of picture text -----**<br>


18/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0019-01.png)


**----- Start of picture text -----**<br>
Version Am_3<br>Profile eID, TA2, CS<br>Preconditions 1. The PACE mechanism MUST have been performed (CAN).<br>2. All APDUs are sent as valid SecureMessaging APDUs.<br>Test scenario 1. Send the given MSE: Set DST APDU to the eID Card.<br>‘0C 22 81 B6 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>83 <L83> <certificate authority reference><br>• The Certificate Authority Reference MUST be used as returned by<br>the PACE mechanism.<br>2. Send the appropriate DV-Certificate as specified in the “Certificate Set<br>17” chapter as DV_CERT_17.<br>‘0C 2A 00 BE <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> <Le>’<br>• <Cryptogram> contains the following encrypted data objects<br>7F 4E <L7F4E> <certificate body><br>5F 37 <L5F37> <certificate signature><br>• This DV-Certificate grants access to all eID special functions.<br>3. Send the given MSE: Set DST APDU to the eID Card.<br>‘0C 22 81 B6 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>83 <L83> <certificate authority reference><br>• The Certificate Holder Reference stored inside the DV-Certificate<br>sent in step 2 has to be used.<br>4. Send the appropriate Terminal-Certificate as specified in the “Certificate<br>Set 17” chapter as AT_CERT_17h.<br>‘0C 2A 00 BE <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> <Le>’<br>• <Cryptogram> contains the following encrypted data objects<br>7F 4E <L7F4E> <certificate body><br>5F 37 <L5F37> <certificate signature><br>• This Terminal-Certificate grants access to special function<br>“Privileged Terminal”<br>5. Send the given MSE: Set AT APDU to the eID Card.<br>‘0C 22 81 A4 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>• <Cryptogram> contains the following encrypted data objects<br>80 <L80> <Cryptographic Mechanism Reference><br>83 <L83> <Certificate Holder Reference ><br>91 <L91> <Compressed Ephemeral Public Key><br>• The Certificate Holder Reference stored inside the Terminal-<br>Certificate sent in step 4 has to be used.<br>6. Send the given Get Challenge APDU to the eID Card.<br>‘0C 84 00 00 0D 97 01 08 8E 08 <Checksum> 00’<br>7. Send the given external authenticate command to the eID Card.<br>‘0C 82 00 00 <Lc> 87 <L87> 01 <Cryptogram> 8E 08<br><Checksum> 00’<br>**----- End of picture text -----**<br>


19/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0020-01.png)


**----- Start of picture text -----**<br>
• <Cryptogram> contains the encrypted terminal generated signature<br>8. Send the given Read Binary APDU to the eID Card.<br>‘0C B0 (80 || <sfi.EF.ChipSecurity>) 00 0D 97 01<br>01 8E 08 <checksum> 00’<br>Expected  1. ’90 00’ within a valid Secure Messaging response.<br>results 2. ’90 00’ within a valid Secure Messaging response.<br>3. ’90 00’ within a valid Secure Messaging response.<br>4. ’90 00’ within a valid Secure Messaging response.<br>5. ’90 00’ within a valid Secure Messaging response.<br>6. ‘<Eight bytes of random data> 90 00’ within a valid Secure Messaging<br>response.<br>7. ’90 00’ within a valid Secure Messaging response.<br>8. ‘<One byte content of EF.ChipSecurity> 90 00’ within a valid Secure<br>Messaging response.<br>**----- End of picture text -----**<br>


## **4.4 Unit EAC2_EIDDATA_B eID Data Groups** 

## **4.4.1 Test case EAC2_EIDDATA_B_18** 

This test cases was added in release 3 of this amendment. 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0020-05.png)


**----- Start of picture text -----**<br>
Test - ID EAC2_EIDDATA_B_18<br>Purpose Test the ASN.1 encoding of the eID DG13 elementary file<br>Version Am_3<br>Profile eID, DG13<br>Preconditions 1. DG13 MUST have been read from the eID Card<br>Test scenario 1. The content of the data object MUST be encoded according to the<br>BirthName syntax definition.<br>Expected  1. true<br>results<br>**----- End of picture text -----**<br>


## **4.5 Unit EAC2_DATA_C EF.ChipSecurity** 

This test unit was added in release 3 of this amendment. This unit covers all tests about the coding of the optional file EF.ChipSecurity containing the signed SecurityInfos supported by the chip. 

## **4.5.1 Test case EAC2_DATA_C_1** 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0020-09.png)


**----- Start of picture text -----**<br>
Test - ID EAC2_DATA_C_1<br>Purpose Test the ASN.1 encoding of the SecurityInfos in EF.ChipSecurity<br>Version Am_3<br>Profile PACE, TA2, CA2, CS<br>Preconditions 1. EF.ChipSecurity MUST have been read from the eID Card<br>**----- End of picture text -----**<br>


20/22 

Amendment to BSI TR-03105 Part 3.3 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0021-01.png)


**----- Start of picture text -----**<br>
Test scenario 1. The content of the SecurityInfos object MUST be encoded according to<br>the SecurityInfos syntax definition.<br>2. EF.ChipSecurity MUST be implemented as SignedData according to the<br>EAC specification [R9].<br>3. The signature MUST be verified.<br>4. At least one PACEInfo object MUST exist<br>5. For each supported set of proprietary PACE domain parameters a<br>PACEDomainParameterInfo object MUST exist<br>6. At least one ChipAuthenticationInfo object MUST exist<br>7. At least one ChipAuthenticationDomainParameterInfo MUST exist<br>8. At least one ChipAuthenticationPublicKeyInfo MUST exist<br>9. At least one TerminalAuthenticationInfo MUST exist<br>10. Exactly one CardInfoLocator SHOULD be present.<br>Expected  1. true<br>results 2. true<br>3. true<br>4. true<br>5. true<br>6. true<br>7. true<br>8. true<br>9. true<br>10. true<br>**----- End of picture text -----**<br>


## **4.5.2 Test cases EAC2_DATA_C_2 to EAC2_DATA_C_7** 

Test cases EAC2_DATA_C_2 to EAC2_DATA_C_7 are equally performed on SecurityInfo objects from EF.CardSecurity like test cases EAC2_DATA_A_2 to EAC2_DATA_A_7 were performed on SecurityInfo objects EF.CardAccess before. References to EAC2_DATA_A_1 are replaced by references to EAC2_DATA_C_1. 

## **4.5.3 Test case EAC2_DATA_C_8** 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0021-05.png)


**----- Start of picture text -----**<br>
Test - ID EAC2_DATA_C_8<br>Purpose Test the ASN.1 encoding of the PrivilegedTerminalInfo<br>Version Am_3<br>Profile CS<br>Preconditions 1. Test case EAC2_DATA_C_1 MUST have been performed and exactly<br>one PrivilegedTerminalInfo object MUST exist.<br>2. The data object containing SecurityInfos is parsed.<br>Test scenario 1. The PrivilegedTerminalInfo element must follow the ASN.1 syntax<br>definition in the EAC specification [R9].<br>2. For each ChipAuthenticationInfo encapsulated in<br>PrivilegedTerminalInfo, the corresponding<br>ChipAuthenticationPublicKeyInfo MUST be also included in<br>PrivilegedTerminalInfo.<br>Expected  1. true<br>**----- End of picture text -----**<br>


21/22 

Amendment to BSI TR-03105 Part 3.3 

**results** 2. true 

## **4.5.4 Test case EAC2_DATA_C_9** 


![](markdown/tr/Amendment_to_BSI_TR-03105_Part_3.3/Amendment_to_BSI_TR-03105_Part_3.3.pdf-0022-03.png)


**----- Start of picture text -----**<br>
Test - ID EAC2_DATA_C_9<br>Purpose Test the ASN.1 encoding of the eIDSecurityInfo<br>Version Am_3<br>Profile CS<br>Preconditions 1. Test case EAC2_DATA_C_1 MUST have been performed and exactly<br>one eIDSecurityInfo object MUST exist<br>2. The data object containing SecurityInfos is parsed<br>Test scenario 1. The eIDSecurityInfo element must follow the ASN.1 syntax definition<br>in the EAC specification [R9].<br>Expected  1. true<br>results<br>**----- End of picture text -----**<br>


22/22 


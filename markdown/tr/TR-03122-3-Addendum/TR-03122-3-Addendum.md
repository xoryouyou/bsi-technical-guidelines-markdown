Technical Guideline TR-03122-3 

Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications 

Addendum Part 3: Additional Test Cases for FM AH-FI-DC2 

Version 6.0 

Federal Office for Information Security PO Box 20 03 63 53133 Bonn E-Mail: trbiometrics@bsi.bund.de Internet: https://bsi.bund.de © Federal Office for Information Security 2024 

Technical Guideline TR-03122-3 

Federal Office for Information Security 

iii 

Table of Content 

## Table of Content 

- 1 Test Cases Function Module TC-AH-FI-DC2 ................................................................................... 1 

Federal Office for Information Security 

iv 

1 Test Cases Function Module TC-AH-FI-DC2 

## 1 Test Cases Function Module TC-AH-FI-DC2 

The following section defines additional test cases for FM AH-FI-DC2 which shall be executed in case a smart phone or similar device is used instead of the DSLR or system camera originally intended by the FM. Note, the requirement to not use a wideangle-lens still applies. 

|**Test Case ID:**|**TC-AH-FI-DC2-003**|**TC-AH-FI-DC2-003**|
|---|---|---|
|_Scope_|Examination of the documents describing the image capturing features of the digital camera used||
||to|obtain facial biometrics. This test case covers the requirements for focal length (depending on|
||the size of the camera sensor) as described in [BIB_ICAO_TR_Portrait_Quality] (chapters 5.2.1 and||
||5.2.2).||
|_Applicability_|This TC applies to IUT which use a smartphone or a similar device instead of the DSLR or system||
||camera originally intended by the FM. Note: This TC does not extend to digital cameras which only||
||support a wide-angle lens (e.g. webcams).||
|_Preconditions_|**•**|Product documentation of the camera model (i.e. smartphone or similar device) provides relia|
|||ble information regarding focal length and sensor size.|
||**•**|The following test resources are necessary:|
|||**•**<br>Product documentation of IUT is at hand (e.g. data sheet, manual).|
|||**•**<br>Product documentation of camera model is at hand (e.g. data sheet, manual).|
|_CTS Mode_|**•**|not_supported|
|_Description_|**Step**<br>**Description / Expected Result**||
||1|_Description:_|
|||**•**<br>Examination of the provided product documentation regarding permitted|
|||camera-to-subject-distance.|
|||_Expected Result:_|
|||**•**<br>The permitted placement options of the biometric subject are limited in a|
|||way that the optical path of the image capturing system is at minimum 1 m|
|||and at maximum 4 m.|
||2|_Description:_|
|||**•**<br>Examination of the provided product documentation regarding effective|
|||focal length_feff_. If the document does not explicitly specify the used effec|
|||tive focal length (compared to a 35 mm full frame), calculate the used effec|
|||tive focal length via_f_e®=_f=cf_where_f_is the used focal length and_cf_the|
|||crop factor (the crop factor may be calculated from the sensor's physical di|
|||mensions). If the camera model uses different lenses, additional evidence on|
|||which lense is actually being used shall be collected. Note: In some cases the|
|||effective focal length may also be extracted from the EXIF data.|



_Expected Result:_ 

- The used effective focal length _f_ e® = _f=cf_ is above 50 mm and below 130 mm. 

## **Table 1.1** Test Case ID: TC-AH-FI-DC2-003 

Note: For test case 004, the usage of the CTS is OPTIONAL. When not using the CTS the results (i.e. images taken with the IUT in the desired configuration) are allowed to be provided in other ways than the defined bio:FaceAcquisition XML. 

## **Test Case ID: TC-AH-FI-DC2-004** 

_Scope_ Examination of the image quality of the digital camera used to obtain facial biometrics. This test ca se covers the requirements for focal length (depending on the size of the camera sensor) as descri bed in [BIB_ICAO_TR_Portrait_Quality] (chapters 5.2.1 and 5.2.2). 

_Applicability_ This TC applies to IUT which use a smartphone or a similar device instead of the DSLR or system camera originally intended by the FM. Note: This TC does not extend to digital cameras which only support a wide-angle lens (e.g. webcams). 

Federal Office for Information Security 

1 

1 Test Cases Function Module TC-AH-FI-DC2 

## **Test Case ID: TC-AH-FI-DC2-004** 

- _Preconditions_ **•** The IUT is in operation, required modules are loaded. 

   - Product documentation of the camera model provides information regarding permitted came ra-to-subject distances and zoom settings. 

   - The IUT implements an interface for conformance testing where a single image of the target (cf. [BIB_ICAO_TR_Portrait_Quality]) can be captured. 

   - The target is lit evenly from the front. A strong lightsource (i.e. softbox) is placed approximately 35° atop of the imaginary line between camera and target. 

   - The following test resources are necessary: 

      - A conformant test-target. 

      - An image-processing programm which allows to rotate a picture and crop it without quality loss. 

      - A script which allows to measure the size of a square in a picture. 

      - Product documentation of IUT is at hand (e.g. data sheet, manual). 

- _CTS Mode_ **•** interactive 

   - no provision of pre-defined input data 

   - `HTTP method: GET` 

   - test case variants: 

```
/TR03122/TC-AH-FI-DC2-004/1
```

**Table 1.3** TC-AH-FI-DC2-004 Test Case Variants 

_Description_ 

- **Step Description / Expected Result** 1 _Description:_ **•** The target is positioned directly in front of the camera at the desired working distance (cf. Evaluation Step). Camera and target are at the same height. 

- **•** The IUT including camera system is configured according to the documentation. 

- **•** Initiate test case by calling the IUT via the test interface. **•** A single image of the target is acquired. _Expected Result:_ **•** The IUT delivers a response that is conformant to the schema file trbio5v1.xsd. 

- **•** The response contains the correct number of elements based on the XPath expression `/bio:FaceAcquisition/bio:Records/bio:BinaryRecord[@type="BMP" or @type="JPEG"]/tradd:BinaryData/tradd:Value/node()` . Exactly 1 element is expected in accordance to the acquistion process. 

- 2 _Description:_ 

   - Examine the response returned by the IUT via the test interface. 

_Expected Result:_ 

- The image depicts the target. 

- In all depicted squares the 0.5 mm lines shall be distinguishable. 

- The depicted straight lines of the target (especially the lines further away from the center) shall appear straight to a human observer. The squares on the target shall be depicted with right angles to a human observer. No barrel distortion is visible. 

Federal Office for Information Security 

2 

1 Test Cases Function Module TC-AH-FI-DC2 

## **Test Case ID: TC-AH-FI-DC2-004** 

_Description:_ 

- 3 _Description:_ **•** The acquired images are prepared in a suitable way using the image proces sing program: If necessary, the images may be rotated slightly to appear ver tically upright in the picture. 

- **•** The acquired image is horizontally divided into four lines of three pictures containing a single pattern s.t. each of the patterns is depicted. Each line is then divided into two groups of images: One group containing the leftmost and center pattern, the other containing the center and rightmost pattern. 

   - For each of the groups: measure the magnification distortion, i.e. the diffe rences in height of the left/rightmost pattern in comparison to the center pattern. Note: To ensure comparability between different measurements a script shall be used for support. 

_Expected Result:_ 

- The average radiation distortion on the left and on the right are below 5%. 

- _Evaluation_ **Evaluation Step Description / Evaluation Result** 1 _Description:_ **•** If the product documentation permits several different CSD or zoom set tings, the TC shall be repeated for all of them. Alternatively, if this is not practicable, the TC shall be repeated for each combination of the respective minimum, medium and maximum values. 

- _Expected Result:_ 

   - For each combination of CSD and zoom setting the expected results are met. 

**Table 1.2** Test Case ID: TC-AH-FI-DC2-004 

Federal Office for Information Security 

3 

1 Test Cases Function Module TC-AH-FI-DC2 

Federal Office for Information Security 

4 


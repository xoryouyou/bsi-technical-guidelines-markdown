Technical Guideline TR-03122-3 

Conformance Test Specification for BSI TR-03121 Biometrics for Public Sector Applications 

Second Addendum Part 3: Additional Test Cases for FM AS-FI-ICS2 

Version 6.0 

Federal Office for Information Security PO Box 20 03 63 53133 Bonn E-Mail: trbiometrics@bsi.bund.de Internet: https://bsi.bund.de © Federal Office for Information Security 2025 

Technical Guideline TR-03122-3 

Federal Office for Information Security 

iii 

Table of Contents 

## Table of Contents 

- 1 Test Cases Function Module TC-AS-FI-ICS2 .................................................................................... 1 

Federal Office for Information Security 

iv 

1 Test Cases Function Module TC-AS-FI-ICS2 

## 1 Test Cases Function Module TC-AS-FI-ICS2 

The following section defines additional test cases for FM AS-FI-ICS2 which shall be executed in case a back ground elimination is used. 

|**Test Case ID:**|**TC-AS-FI-ICS2-009**|**TC-AS-FI-ICS2-009**||
|---|---|---|---|
|_Scope_|Examination of the software module used for acquisition of digitised facial images with focus on|||
||the background elimination.|||
|_Applicability_|This TC applies to IUT which perform a segmentation based on additional hardware (for example|||
||additional cameras for background information). It shall be executed as an alternative to TC-AS-FI-|||
||ICS2-008 when the image-based approach is not feasable.|||
|_Preconditions_|**•**|The IUT is in operation, required modules are loaded.||
||**•**|A reference implementation for background replacement is at hand.||
||**•**|The IUT is configured such that for every captured image two versions of the captured image are||
|||released: One of the images is an original presentation of the biometric subject during the captu||
|||re, the other one is the result of the application of the background elimination feature.||
||**•**|It is possible to perform this testcase under different conditions including: cluttered Back||
|||ground, uniform background in a distinct color (e.g. blue or green), subject with short hair (ear||
|||length or tied back), subject with long hair (not tied back), subject wearing glasses, subject wea||
|||ring patterned clothes||
|_CTS Mode_|**•**|interactive||
||**•**|no provision of pre-defined input data||
||**•**|`HTTP method: GET`||
||**•**|test case variants:||
|||`/TR03122/TC-AS-FI-ICS2-009/1`||
|||**Table 1.2**TC-AS-FI-ICS2-009 Test Case Variants||
|_Description_|**Step**<br>**Description / Expected Result**|||
||1|_Description:_||



- Caprture a facial image of a biometric subject using the IUT in order to test the segmentation. 

Federal Office for Information Security 

1 

1 Test Cases Function Module TC-AS-FI-ICS2 

## **Test Case ID: TC-AS-FI-ICS2-009** 

_Expected Result:_ 

- The IUT delivers a response that is conformant to the schema file trbio5v1.xsd. 

- The response contains the correct number of elements based on the XPath expression `.//bio:Records/bio:BinaryRecord[@type='jpeg']` . Exactly 2 elements are expected in accordance to the acquistion process. 

- The image in `.//bio:Records/bio:BinaryRecord[@type='jpeg' and @externalReference='segmentedImage']` in the response is the segmen ted image, i.e. an image of the same dimensions as the facial image with grey pixels. A pixel in the segmented image is grey if the corresponding pixel in the facial image is a background-pixel. 

- The image in `.//bio:Records/bio:BinaryRecord[@type='jpeg' and @externalReference='originalImage']` in the response is the non-seg mented image, i.e. a facial image without any added grey pixels. This is the only difference between the images (i.e. there is no difference regarding cropping, rotation, colorgrading etc.). 

- The image containing the facial image with background has a resolution of 1244 x 1600. 

- The image containing the facial image with eliminated background has a re solution of 1244 x 1600. 

- The pixels of facial image demarked as "background" and replaced by the IUT image are of the same gray color in between #A1A1A1 and #E1E1E1. It is allowed to blur the transition between original and segmented image. 

- The noise of the image is less than 0.5/FF. 

2 _Description:_ 

- Evaluate the segmented image for changes in the core facial region, i.e. the triangular region including eyes, nose and mouth; glasses are included. 

- Evaluate the segmented image for changes in the outline. This includes the head, shoulders, clothes and accesoires (i.e. earrings). 

_Expected Result:_ 

- No change is made in the core region. This includes individual pixels. 

- No area of at least 3px x 3px in the foreground is removed or blurred. This includes for example the removal of an accesoire, removal of parts of the shoulder or the head. The removal of hair does not alter the shape or hair style (for example by removing asymmetric parts). 

3 

_Description:_ 

- Use the reference implementation to remove the background in the original image. 

- Calculate the IoU and Hausdorff distance between the background replaced images from the IUT and the reference implementation. 

_Expected Result:_ 

- The IoU in between the IUT response and the reference implementation is less than 10%. 

- The Hausdorff distance in between the IUT response and the reference im plementation is less than 10. 

- Note: The difference in between the IUT response and the reference imple mentation may be greater in case the IUT response performs better than the reference implementation according to a check as per the evauation step. 

_Evaluation_ 

**Evaluation Step Description / Evaluation Result** 

Federal Office for Information Security 

2 

1 Test Cases Function Module TC-AS-FI-ICS2 

## **Test Case ID: TC-AS-FI-ICS2-009** 

1 

_Description:_ 

- Repeat this testcase 5 times under different conditions including: clutte red Background, uniform background in a distinct color (e.g. blue or green), subject with short hair (earlength or tied back), subject with long hair (not tied back), subject wearing glasses, subject wearing patterned clothes 

- In case the automatic evaluation of step 3 fails, the IUT reponse may be eva luated as better than the reference implementation according to the follo wing conditions: 

## _Expected Result:_ 

- No part of the core facial region is eliminated. 

- Hair, clothes and accessoires are kept coherently. 

- No broader (> 3px x 3px) part of the hair, clothes or accessoires is removed or blurred. This includes objects which are located behind the ear or with considerable distance to the facial region (e.g. part of the hairstyle, collar, earrings). 

- Singular small objects (e.g. individual hairs or fringes) may be altered. 

- Small gaps (< 3px x 3px) between hairs or between glasses and face do not have to be eliminated. 

- No object located in the background is kept as a whole. 

- The transition between foreground and background may be kept (distance 5px). 

- Blurred regions count as altered/eliminated. 

**Table 1.1** Test Case ID: TC-AS-FI-ICS2-009 

Federal Office for Information Security 

3 

1 Test Cases Function Module TC-AS-FI-ICS2 

Federal Office for Information Security 

4 


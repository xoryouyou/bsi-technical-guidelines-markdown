## Evaluation Guidance 

## BSI TR-03166 2.0 

Version: 2.0 

## Document history 

Table 1 Document history 

|Table 1 Document history||||
|---|---|---|---|
|Version|Date|Editor|Description|
|1.0|2024|BSI||
|1.1|2024|BSI||
|2.0 (Draft)|2025|BSI|Adaption of Testing IDs<br>and clarification of<br>terms|
|2.0|2026|BSI|Errors and<br>inconsistencies solved<br>Added notes and<br>clarifications based on<br>feedback.|



Federal Office for Information Security P.O. Box 20 03 63 53133 Bonn E-Mail: biometrie@bsi.bund.de Internet: https://www.bsi.bund.de © Federal Office for Information Security 2026 

Table of Contents 

## Table of Contents 

|1|Introduction ............................................................................................................................................................................................ 4|Introduction ............................................................................................................................................................................................ 4|
|---|---|---|
||1.1|Presentation Attack Instrument (PAI) Overview ........................................................................................................ 5|
||1.1.1|Modality Face ......................................................................................................................................................................... 5|
||1.1.2|Modality Finger ..................................................................................................................................................................... 6|
|2|Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) ................... 7||
||2.1|Documentation ........................................................................................................................................................................... 7|
||2.2|Initial Functional Test of the Biometric System ......................................................................................................... 7|
||2.3|Pre-Evaluation Process ........................................................................................................................................................... 8|
||2.3.1|Modality Face ......................................................................................................................................................................... 9|
||2.3.2|Modality Finger ................................................................................................................................................................... 13|
|3|Evaluation Phase (Normative) ...................................................................................................................................................... 19||
||3.1|Biometric Performance Evaluation ................................................................................................................................ 19|
||3.1.1|[BAL-1] Biometric Assurance Level 1 ........................................................................................................................ 19|
||3.1.2|[BAL-2] Biometric Assurance Level 2 ........................................................................................................................ 20|
||3.1.3|[BAL-3] Biometric Assurance Level 3 ........................................................................................................................ 21|
||3.2|Presentation Attack Detection Evaluation .................................................................................................................. 22|
||3.2.1|Evaluation Metric ............................................................................................................................................................... 22|
||3.2.2|Fixed Time Methodology: Pre-Evaluation and PAD-Evaluation ................................................................ 24|
||3.2.3|Minimal Test Coverage .................................................................................................................................................... 25|
||3.2.4|Expected Result for the Presentation Attack Detection Evaluation ........................................................... 27|
|4|Material List Including Relevant Technologies Covering Different Presentation Attack Instruments||
|(Informative) ................................................................................................................................................................................................... 28|||
||4.1|Modality Face ............................................................................................................................................................................. 28|
||4.2|Modality Finger ........................................................................................................................................................................ 28|
|5|Append<br>.......................................... 30||
||5.1|Creating Artefacts for the Modality Face ...................................................................................................................... 30|
||5.1.1|PAIs Based on a Frontal Face Image Printout ....................................................................................................... 30|
||5.1.2|.......... 31|
||5.1.3|PAIs based on 3D-Masks Containing Facial Biometric Characteristics of an Identity ...................... 32|
||5.1.4|Make-up Attack ................................................................................................................................................................... 35|
||5.2|Build Artefacts for the Modality Finger ........................................................................................................................ 36|
||5.2.1|Recommend Materials and Tools ............................................................................................................................... 36|
||5.2.2|Source Information ........................................................................................................................................................... 37|
||5.3|Apply the Artefact to the TOE ............................................................................................................................................ 39|
|6|Appendix: Minimal Information Requirements of a Testing Report ........................................................................ 40||
|7|Bibliography .......................................................................................................................................................................................... 43||



Federal Office for Information Security 

3 

1 Introduction 

## 1 Introduction 

This document serves as a supporting document to BSI TR-03166 for product manufacturers and as the testing specification for evaluations laboratories. Within this document best practices and guidelines are formulated for the currently covered biometric modalities fingerprint and face. 

The evaluation process itself consists of two parts covering the biometric performance of the system and the resistance against defined Presentation Attack Instruments (PAIs) or attack potentials as defined by the Common Criteria Evaluation Methodology (CEM) [1]. 

This document does not specify new methods for the performance evaluation, but uses international standards. In particular to evaluate the biometric performance of a biometric system several different assumptions and methods are standardised, e.g., for the composition of the test crew or the crew size to prove the biometric performance of the system. 

Content of this document is a brief description of a Presentation Attack Detection (PAD) pre-evaluation, where the evaluator creates initial PAI with the aim to create, from the given material characteristics / properties, artefacts with the highest potential to successfully circumvent the PAD and to pass as a valid biometric verification / authentication. In addition, the evaluator gains knowledge about the Target of Evaluation (TOE) to reduce the probability of failed authentication processes e.g., by knowing how to present artefacts in a suitable manner to the TOE. The pre-evaluation process is designed with the intention to reduce the impact by the differences in skills between evaluators on the evaluation results (limited attempts per artefact). In addition, this attempt supports our claim that the TOE is tested within the certification and not only the skill and experience of an evaluator. 

Further, this document defines best practices setting. This could be for example the image resolution to capture a biometric image or the printing quality of the PAI. Due to the variety of devices and materials (e.g., printer, ink and paper) this document does not define specific brands or models / types of products. Instead, general requirements and best practices systems. 

The overall intention of this document is to cover state-of-the-art artefacts, published via legal and public sources, for evaluating the robustness against presentation attacks on fingerprint scanners and face recognition systems. In contrast to other established standards, this evaluation is based on the premise that an attacker is in possession of the best data to create biometric artefacts and to attack the biometric system - that there is a huge number of potential materials, mixtures and variations for creating presentation attack instruments and that it is relatively easy in general to capture fingerprints and faces in many different ways and manufacture artefacts that produce high quality presentation attack instruments. Hence, in order to have a realistic chance to discover the vulnerabilities of a biometric system with a reasonable and practicable amount of effort, the evaluation uses the best available representations of each artefact species. 

In particular, for fingerprint artefacts that includes using direct casts or other means to acquire similar quality fingerprints as the basis for manufacturing artefacts in contrast to using latent fingerprints, which quality data and essentially reduce the comparability between evaluations. In terms of face recognition, this means that an evaluator uses face images with the quality of biometric frontal face images and 3D face data with the best possible quality e.g., acquired via photogrammetry. 

In conformance to the main document of the technical guideline BSI TR-03166 [2], only attacks with PAIs are part of the evaluation. The present discussions of video-injection attacks or attacks other than Presentation Attacks (PA) are not part of this evaluation, but can be possibly discussed and evaluated in the context of resistance against high attack potentials. 

Federal Office for Information Security 

4 

1 Introduction 

## 1.1 Presentation Attack Instrument (PAI) Overview 

The following subsection gives a general overview of the PAI Classes considered for the testing of the TOE via PAIs in front of the device sensor (attack vector 1). Exemplary materials, their properties and further possible modifications, for the modalities face and finger are summarised in Table 2 and Table 3. These overviews do not cover all possible PAI classes, materials with their different material properties or potential modifications of the created PAI. In conformance with the technical guideline an evaluator is free in his decision to create PAIs within the Biometric Assurance Levels (BALs) attack potential resistance. 

## 1.1.1 Modality Face 

Table 2 Overview of PAI Classes for the Modality Face 

|PAI Class|Materials / Material Properties|Modifications|
|---|---|---|
|Printed Photo of a Face|• Printer type<br>• Printing stocks<br>• Size|• Cut outs<br>• Source image manipulation /<br>modification<br>• Full / partial faces|
|Display to Present the<br>Modality Face|• Display technology<br>• Display size<br>• Framerate<br>• Pixel density|• Static (Images)<br>• Dynamic<br>• Video (recorded or from other public<br>source)<br>•<br>software<br>• Image / video manipulation /<br>modification<br>• Projection surface<br>• Full / partial faces|
|3D-Masks|• Printer type / technology<br>• Material|• Cut outs<br>• Colouring<br>• Image texture<br>• Full / partial faces|
|Non-permanent make<br>up|• Different brands<br>• Different Colour Schemes|• Face abstraction|



Federal Office for Information Security 

5 

1 Introduction 

## 1.1.2 Modality Finger 

Table 3 Overview of PAI Classes for the Modality Finger 

|PAI Class|Materials / Material Properties|Modifications<br>(for all classes)|
|---|---|---|
|Latent Fingermark1|• base material|• additives|
|Printed / Drawn<br>Fingerprint<br>Representation|• base material<br>• colour|• artefact thickness<br>• additives<br>• Mixture variations<br>(if applicable)|
|2<br>-Artefact|• direct positive or moulding<br>technology<br>• base material<br>• colour||
|3D-Artefact|• direct positive or moulding<br>technology<br>• base material<br>• colour||



- 1  A simple attack method is to utilise the latent fingermark a previous user left on the sensor. The sample quality of fingermarks can be increased by using additives like powders to enhance the contrast. 

- 2 The 2D information of fingerprints can also be used to generate so called 2.5D finger artefacts, where the 2D information is used to create a mould to cast fingerprint artefacts. 

Federal Office for Information Security 

6 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

## 2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

## 2.1 Documentation 

INI-DOC-01: For the pre-evaluation of the biometric authentication / verification system the evaluator SHALL document: 

- The evaluation environment 

Note: The environment can differ from the environment of the biometric performance testing. 

Example: The evaluation environment can be documented via a photo documentation and description of the equipment. 

- The Target of Evaluation including software and hardware version 

Note: This information has to be identical to the information regarding the system for the biometric performance evaluation, see. Appendix Chapter 6. During the evaluation of the PAD capability of the system the evaluator can use different applications, which contain more information e.g., PAD score to perform Hill-Climbing-Attacks. 

- PAI preparation and manufacturing processes including tools, materials and methods 

- PAI presentation 

INI-DOC-02 : The documentation SHALL be in a reproducible manner including the environment and the artefacts types. 

## 2.2 Initial Functional Test of the Biometric System 

INI-FUN-01: The evaluation laboratory SHALL evaluate the general functionality of the biometric system by bona fide tests. 

INI-FUN-02: The environment for enrolment and the biometric authentication / verification attempts SHALL be identical and well documented. 

INI-FUN-03: The basic functional test SHALL be performed with a sufficiently large number (at least 10 different identities) of different identities covering different general aspects. 

Note: The aim of INI-FUN-03 is to evaluate the existence of a notable bias among the test crew, which can be an indicator for an accidentally high false rejection rate of the biometric system. 

This list is not complete and open for further aspects. 

- General aspects to be considered for the Initial Functional Test: 

   - Gender 

   - Age 

   - Ethnic groups 

   - Skin conditions due to occupation / hobbies / medical conditions 

Additional to the general aspects, device and biometric modality specific aspects can influence the functionality of a biometric device. 

Federal Office for Information Security 

7 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

Table 4 Dependent on the biometric modality additional aspects can influence the functionality of the biometric system. 

|Face||Finger|
|---|---|---|
|•|Face hair (hair, eyebrows, beard)|• Technology (optical, conductive, supersonic,|
|•|Glasses|other)|
|•|Make-up3|• Sensor position on TOE|
|•|Tattoos|• Sensor size on TOE4|
|•|Technology|• Contactless or contact based sensor|



Note: The listed aspects are only informational for the evaluator and are not a requirement, which has to be tested during the evaluation. 

## 2.3 Pre-Evaluation Process 

PRE-PRO-01: Prior to the evaluation, the evaluator SHALL prepare PAIs for the pre-evaluation. 

PRE-PRO-01X: For the pre-evaluation of the TOE the evaluator SHALL have access to a TOE-like biometric system, which allows as specified in GEN-PAD-03 & GEN-COM-01, the access to biometric comparison scores and PAD scores 

PRE-PRO-02: Due to specific properties and characteristics of a TOE and the considered PAIs, the evaluator SHALL figure out the PAI classes, the materials and variants best suited to create the PAIs, which are likely be successful in a biometric verification / authentication process. 

Note: Some biometric systems using technologies intrinsically resistant against certain attack types. Therefore, more suitable artefact types have to the focus of the evaluation, although this does not mean this kind of artefacts do not have to be tested during the evaluation. 

PRE-PRO-03 : Additionally, each PAI designated for the evaluation SHALL be optimised in the preevaluation process, so that: 

- a sufficiently high comparison score can be achieved exceeding the TOEs comparison threshold 

- in case it is not possible to achieve a sufficient comparison score, the necessary attempts for the test case SHALL be performed and the TOE passes the evaluation for the test case. 

- the chance to overcome the PAD-component with a high probability (relative for this PAI-class) 

- changes in artefact quality based on age / time and wearing effects during testing SHALL be considered and minimized 

As specified in the main document BSI TR-03166 [2]: 

- For the Biometric Assurance Level (BAL) 1, the evaluator is restricted to certain Materials / Material Properties and Modifications. 

- In addition to the Presentation Attack Instruments for the BAL 1, the evaluator is free to create new Presentation Attack Instruments which would be classified in CEM [1] with an attack potential enhanced-basic for BAL 2 or moderate for BAL 3. 

- 3  Note: The make-up considered during the functionality is different from the mentioned Presentation Attack using make-up to impersonate a different identity. 

- 4  The sensor size in relation to the way the finger covers the sensor area during the scan could have an impact on usability aspects and defines how environmental parameters like lightning conditions could potentially interfere with the scanning process. 

Federal Office for Information Security 

8 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

## 2.3.1 Modality Face 

## 2.3.1.1 Pre-Evaluation Optimisation 

Table 5 includes parameters which can be considered during the pre-evaluation to improve the probability to achieve a false classification of a PAI as bona fide. The list is neither extensive nor normative. The preevaluation process is designed with the intention to reduce the impact by the differences in skills between evaluators on the evaluation results (limited attempts per artefact). Therefore, an evaluator can use the preevaluation phase to find based on an initial guess and expertise the most promising PAI to be used during the evaluation. 

Table 5 Pre-Evaluation Optimisation Aspects for each PAI Class of the Modality Face 

|PAI-<br>Nr.|PAI Class|Optimization Aspects|
|---|---|---|
|01|Paper|• try different paper types:<br>• size<br>• paper weight / thickness<br>• surface smoothness<br>• amount of wood-contingent<br>• amount of additives<br>• paper colours<br>• transparency<br>• different toner / ink types (esp. for the wet paper variant)<br>• presentation of real skin in combination with the PAI to attack PAD<br>mechanisms<br>• additives to mimic skin properties|
|02|Transparent Foil|• ink or toner types<br>• foil materials<br>• thickness<br>• presentation of real skin in combination with the PAI to attack PAD<br>mechanisms|
|03|Fabric|• face image transfer method and material<br>• different fabrics<br>• base colour<br>• material<br>• weave density<br>• additives to mimic skin properties|
|04|Display|• display technology<br>• brightness<br>• refresh rates / repetition rates<br>• PWM flickering|



Federal Office for Information Security 

9 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

|||• resolution<br>• Prevention / minimisation of Moiré effect|
|---|---|---|
|05|Projector|• Projector technology<br>• brightness<br>• refresh rates / repetition rates<br>• PWM flickering<br>• Resolution|
|06|3D-Masks|• Base material<br>• material<br>• thickness<br>• colour<br>• texture<br>• additional facial features<br>• eye brows<br>• eye lashes<br>• lipstick / lip gloss<br>• additives to mimic skin properties<br>• fit|



Example: A biometric system uses light in the human non-visible spectrum. An evaluator has the knowledge from previous evaluations with other systems that a certain combination of paper and ink or toner works best to at least generate an image which can be recognised by the capture device. 

2.3.1.2 Source for the Presentation Attack Instrument Manufacturing Process 

PRE-SOU-01: For testing, the test laboratory SHALL create PAIs under the assumption of a worst-case attack. This includes that an attacker having access to the best possible source data which suits the attack and the functionality of the PAD mechanisms / technologies. 

## 2.3.1.2.1 Source Requirements for 2D-Presentation Attack Instruments 

A guidance for creating frontal face images is given in ISO/IEC 19794-5:2011 [3], 29794-5:2010 [4] and 397945:2019 Annex D [5]. 

PRE-SOU-02: An evaluator SHALL define all acquisition settings to capture an image as good as possible to achieve a live-like representation of the identity for the evaluation and fitting to the TOE. 

PRE-SOU-03: The source image SHOULD contain a sufficient number of pixels to crop the image to the face area with respect to the aspect ratio of the original image. 

Examples: 

1. The presented image on a smartphone requires at least an image resolution matching the display resolution. 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0010-11.png)


2. An image printed on a paper requires at least the resolu 

Federal Office for Information Security 

10 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

## 2.3.1.2.2 Source Requirements for 3D-Presentation Attack Instruments 

The guidance to acquire a 2D image for the evaluation is defined in 2.3.1.2.1 and can be used for the artefacts texture. 

PRE-SOU-04: The technology to acquire the 3D data SHALL be state-of-the-art in order to provide a sufficient texture quality and 3D-accuracy. 

Therefore, this guideline does not define the use of a specific technology to acquire 3D-data of the identity to represent with a PAI. 

Note: A practical solution can be the use of photogrammetry to achieve a detailed texture and reconstruct 3D-data for creating a PAI. Therefore, it can be useful to apply the best practices for full frontal face images as well to other PAIs and their production steps. 

Note: For the creating process, the evaluation laboratory has to check for scaling errors of the created artefact, in particular if 3D technologies are used by the TOE for biometric comparison and PAD. 

## 2.3.1.3 Presentation Attack Instrument Manufacturing 

This section gives an overview and general requirements for specific manufacturing steps. 

PAI-QUA-01: The general definition for Presentation Attack Instruments is that the PAI SHALL exceed the necessary comparison score of the biometric system to achieve a positive biometric comparison with the enrolled reference. 

PAI-QUA-02: Additionally, the evaluator SHALL achieve the highest possible quality of a PAI for the evaluation by attempts to improve the PAI during the pre-evaluation phase. 

Note: Maximising the PAI quality can be beneficial to improve the evaluation, due to the fact that such a PAI can be used under various environmental conditions, e.g., low illumination conditions, and presentation angles. Furthermore, such PAIs can be used in evaluations with high biometric performance settings. 

Additional information regarding tools, materials and tips and tricks for the PAI can be found in Chapter 5. 

## 2.3.1.3.1 2D-Presentation Attack Instruments 

The subsection deals with the overview of requirements for the PAI manufacturing, variations and modifications to consider. The PAIs are limited to 2D materials / geometries and cover 2D identity representations on different materials and displays / projectors to present the PAI to the TOE. 

## 2.3.1.3.1.1 Print of a Frontal Face Image 

PAI-QUA-03: The evaluator SHOULD print the image with a colour calibrated printer using the best native printing quality. 

PAI-QUA-04: All other manufacturing parameters SHALL be identified during the pre-evaluation process, see 2.3 Pre-Evaluation Process. 

Note: Aim of the PAI creation is to achieve a live-like presentation of the identity or at least a PAI which fulfils the quality requirement PAI-QUA-01 . 

2.3.1.3.1.2 Display to Present a Facial Image 

PAI-QUA-05: The evaluator SHOULD present the facial representation on a colour calibrated display. 

PAI-QUA-06: Additional points SHALL be considered: 

PAI-QUA-06a: The display SHALL be chosen in a way that the TOE does not capture any artefacts (PWMflickering, black stripes (display refresh rates) and strong visible Moiré pattern). 

PAI-QUA-06b: The face presentation on the display SHOULD be performed with an optimised brightness of the PAI (display / projector). 

Note: Optimisation has to be done during the pre-evaluation phase. 

Federal Office for Information Security 

11 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

PAI-QUA-06c: The evaluator SHALL take care of effects with glare and non-glare displays. 

Note: In case a display shows too strong reflections, an anti-glare foil can be applied to the display surface. 

## 2.3.1.3.2 3D-Presentation Attack Instruments 

This subsection deals with requirements and recommendations for 3D PAIs, which are created and presented to the TOE during the evaluation. 

2.3.1.3.2.1 3D-Masks 

PAI-QUA-07: The geometry of the artefact SHOULD be as close as possible to the original form and size of the identities used in the evaluation. 

PAI-QUA-08: The evaluator SHOULD consider that it might be useful and can improve the biometric comparison score, if the 3Dsed for each evaluator. 

3D-masks can be produced with different processes. These possibilities are summarised in Table 6 Possible approaches to create a 3D mask from different sources with and without moulding process. 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0012-09.png)


Coloured 

PAI-QUA-09: SHOULD show a skin-like base colour, without further facial details. 

PAI-QUA-10: which might be part of the mask production step or due to a post-processing where the evaluator or an expert adds a texture to the mask representing the identity presented to the TOE. 

Note: The created masks have to achieve a sufficiently high comparison score to be used as an artefact during the evaluation ( PAI-QUA-01 ). 

Table 6 Possible approaches to create a 3D mask from different sources with and without moulding process. 

|Source|Mould (Negative)|Artefact (Positive)|
|---|---|---|
|Direct<br>mould|The face of the identity to represent<br>during the evaluation and the<br>evaluators face are necessary for the<br>moulding process to achieve a tight<br>fit between the mask and the<br>evaluators face. The result will be two<br>different moulds.|The positive can be cast based on the created<br>moulds with different materials. By post-<br>proces<br>can be done.|
|Photos|---|Via photogrammetry or other 3D reconstruction<br>methods a directly usable 3D positive is created,<br>which can be done e.g. with a 3D-printer.|
||A mould is created based on the 3D<br>reconstruction (photogrammetry or<br>other)|The positive can be casted with different<br>materials.|
|3D-scan|---|Directly 3D-printed positive|
||3D-printed mould based on the 3D-<br>scan of the evaluator.|The positive can be cast with different materials|
|Handcrafted<br>positive|The handcrafted positive may be<br>used to create a mould.|The result of the moulding process may be used<br>with different materials to cast a positive mask|



The moulding process is a specialised process to create highly specialised 3D-masks e.g created by make-up artists etc. 

Federal Office for Information Security 

12 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

## 2.3.2 Modality Finger 

## 2.3.2.1 Pre-Evaluation Optimisation 

Table 7 Pre-Evaluation Optimisation Aspects for each PAI Class of the Modality Finger 

|PAI-<br>Nr.|PAI Class|Optimization Aspects|
|---|---|---|
|01|Fingermarks|• amount of powder<br>• prepping the finger with a little bit of grease to produce a<br>more prominent fingermark<br>• find an optimal way to leave a clear fingermark<br>• try using similar techniques as in fingerprint forensic<br>procedures (brush, tape, etc.)<br>• try tape to protect the fingermark and real skin on top to<br>attack PAD mechanisms|
|02|Paper[2D-print]|• try different paper types:<br>• paper weight / thickness<br>• surface smoothness<br>• amount of wood-contingent<br>• amount of additives<br>• paper colours<br>• different toner types (esp. for the wet paper variant)<br>• amount of water for the wet paper variant<br>• try real skin on top to attack PAD mechanisms|
|03|Transparent Foil[2D-print]|• ink or toner types<br>• foil materials<br>• thickness<br>• try real skin on top (without fingerprints)<br>to attack PAD mechanisms|
|04|Gelatine[cast]<br>(mix with glycerine)|• gelatine-glycerine (-water) mixing ratio<br>• time after creation of the artefact<br>• reduce bubbles on the contact surface<br>• try real skin on top to attack PAD mechanisms with thin<br>artefacts<br>• different artefact thickness >2mm up to a full finger<br>artefact<br>• amount of additives|
|05|Gelafix[cast]<br>(transparent)|• time after creation of the artefact<br>• reduce bubbles on the contact surface|



Federal Office for Information Security 

13 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

|||• try real skin on top to attack PAD mechanisms with thin<br>artefacts<br>• different artefact thickness >2mm up to a full finger<br>artefact<br>• amount of additives|
|---|---|---|
|06|Gelafix[cast]<br>(coloured)|• time after creation of the artefact<br>• reduce bubbles on the contact surface<br>• try different available colours<br>• try real skin on top to attack PAD mechanisms with thin<br>artefacts<br>• different artefact thickness >2mm up to a full finger<br>artefact<br>• amount of additives|
|07|Silicone[cast]<br>(transparent, 2-components)|• different silicone types<br>• reduce bubbles on the contact surface<br>• try real skin on top to attack PAD mechanisms with thin<br>artefacts<br>• amount of additives|
|08|Silicone[cast]<br>(coloured)|• different silicone types<br>• reduce bubbles on the contact surface<br>• try different colour mixtures<br>• try real skin on top to attack PAD mechanisms with very<br>thin artefacts<br>• amount of additives|
|09|Latex[cast]|• different latex types<br>• reduce bubbles on the contact surface<br>(a vacuum chamber can help)<br>• try real skin on top to attack PAD mechanisms with very<br>thin artefacts<br>• amount of additives|
|10|Wood Glue[cast]<br>(added glycerine)|• wood-glue-glycerine mixing ratio<br>• time after creation of the artefact<br>(sometimes a dryer surface gets better results)<br>• reduce bubbles on the contact surface<br>• try real skin on top to attack PAD mechanisms with thin<br>artefacts<br>• different artefact thickness >2mm up to a full finger<br>artefact|



Federal Office for Information Security 

14 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

|||• amount of additives|
|---|---|---|
|11|Window Colour[cast]<br>(acrylic)|• different window colour types<br>• reduce bubbles on the contact surface<br>(a vacuum chamber can help)<br>• try real skin on top to attack PAD mechanisms with very<br>thin artefacts<br>• amount of additives|
|12|Conductive rubber|• different types of colours<br>• reduce bubbles in the material<br>• amount of additives|
|13|3D-printed positive<br>(full colour print, flexible<br>polymer material: shore<br>hardness A10-A20)|• material composition<br>• artefact colour / texture<br>• shore hardness<br>• model resolution (e.g., with pores), smooth edges|



## 2.3.2.2 Source Data for the Presentation Attack Instrument Manufacturing Process 

For the evaluation, the testing laboratory has to create Presentation Attack Instruments (PAIs) under the - having access to the best possible source data, suitable for the attack and the functionality of the fingerprint sensor and the implemented Presentation Attack Detection mechanisms / technologies. 

## 2.3.2.2.1 Source Requirements for 2D and 2.5D-Presentation Attack Instruments 

Source images for the PAI manufacturing process can be acquired based on different methods: 

1. Reference fingerprint images acquired with contacted-based fingerprint scanners fulfilling the following requirements: 

   - a. Minimal image resolution 500 PPI 

   - b. No image compression 

   - c. No automatized image enhancement 

2. Fingerprints digitalised from ink fingerprints 

   - a. Minimal scanner resolution 600 DPI 

   - b. No image compression 

   - c. No automatized image enhancement 

3. Contactless fingerprint acquisition with standard camera equipment 

   - a. The evaluation facility can take images directly from the fingers and extract fingerprints via image analysis. 

4. Contactless 3D fingerprint acquisition 

   - a. Various technologies enable a contactless 3D acquisition of the fingerprint. A 2D fingerprint can be achieved with different projection methods. 

5. Enhancement of latent fingermarks 

Federal Office for Information Security 

15 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

- a. By using different methods to enhance the visibility of a latent fingermarks, the ridge pattern can be digitized via a digital camera etc.. 

PAI-SOU-05: Image enhancing modifications on the fingerprint SHALL be documented. 

Note: Due to the requirement to work based on the worst-case assumption it is most likely to start with direct moulding. The laboratory can choose which method for fingerprint acquisition fits best TOE. 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0016-04.png)


create a biometric 

artefact to attack the biometric system, but can be used as the simplest possible attack. Therefore, the use of latent fingerprints as source data for fingerprint artefacts is out of scope of this toolbox. 

The 2D information of fingerprints can also be used to generate so called 2.5D finger artefacts, where the 2D information is used to create a mould to cast fingerprint artefacts. 

## 2.3.2.2.2 Source Requirements for 3D-Presentation Attack Instruments 

Source data for the PAI manufacturing process can be acquired based on different methods: 

1. Co-operative moulding with different materials is a valid method to create a high-quality 3Dfingerprint artefact 

   - a. Level of detail (ridges, valleys, sweat pores) 

   - b. Material durability 

   - c. No alteration over time 

2. Digital 3D-model acquisition 

   - a. Region of interest of the finger 

   - b. Achievable voxel resolution of the method has to fit to the application For example isotropic resolution 25 µm 

## 2.3.2.3 Presentation Attack Instrument Manufacturing 

This section gives an overview and general requirements for specific manufacturing steps. 

## 2.3.2.3.1 2D-Presentation Attack Instruments 

The subsection deals with the overview of requirements for the PAI manufacturing, variations and modifications to consider. The PAIs are limited to 2D materials / geometries and cover 2D prints on different materials presented to the TOE. 

2.3.2.3.1.1 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0016-22.png)


For some fingerprint scanner technologies, it can be sufficient to cover an old accepted genuine fingerprint with some sheet of plastics or paper. Additional enhancement steps like the use of fingerprint powder (possible use of different colours) to enhance the optical density of the latent fingerprint to achieve the necessary ridge pattern can be performed. Different materials in different colours can act as background for the latent fingerprint. 

2.3.2.3.1.2 Print of a Fingerprint PAI-QUA-11: Depending on the source information, the evaluator SHALL scale the fingerprint image to the fingerprint image size of the enrolled identity. 

PAI-QUA-12: The evaluator SHOULD print the image with a calibrated printer using the best native printing quality. 

PAI-QUA-13: The source image for a printed artefact SHALL be at least 1,000 PPI (pixel per inch). 

Due to the fine structure of used can play a crucial role in the printing result. 

Federal Office for Information Security 

16 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

PAI-QUA-14: The evaluation facility SHALL take care of the detail preservation of the final print. 

Depending of the technology used by the biometric system additives can be necessary to generate an image of the fingerprint. 

Exemplary Variations: 

- Different printer technologies (e.g., inkjet / laser) 

- Different pigment containing media / conductive additives 

- Different printing targets (paper, transparent sheets, plastics) including base colour and thickness of the material 

- Colour spaces (CMYK / BW / RGB) 

- Wetting the artefact 

- Partial artefacts 

Note: The exemplary variations are only examples, which can be changed for the PAI creation. Depending on the TOE some variations are more relevant than others. 

## 2.3.2.3.2 2.5D-Presentation Attack Instruments 

The evaluator presents so called 2.5D fingerprint artefacts to the TOE. This class of artefacts can be created based on the acquired fingerprints as described in 2.3.2.3.1 2D-Presentation Attack Instruments. In contrast to 2D artefacts this class of artefacts contains distinct depth information. 

## 2.3.2.3.2.1 Moulding Process 

The 2D fingerprint can be used as source to achieve 2.5D moulds in various materials. In this process the 2D fingerprint acts as a template for e.g., exposure etching processes, engraving or 3D printed moulds. 

Engraving can be done e.g. in plastic or metal (e.g., with laser engravers on Delrin or aluminium) or by using lithographic processes (e.g. for using UV-imprinting on Nyloprint plates as an alternative to using PCBs). 

Depending on the processing method, the template can be mirrored along the vertical axis and the binarized presentation can be inverted. 

## 2.3.2.3.2.2 Casting Process 

Due to material properties the moulding or the casting material can change in size during the drying processes. 

PAI-QUA-15: The evaluator SHALL take care that the fingerprint artefact enables a successful comparison with the enrolled fingerprint. 

PAI-QUA-16: For the casting process, the created mould SHALL be cleaned from dust or remaining residuals of a previous casting process. 

PAI-QUA-17: The evaluator SHALL take care that only cleaning methods are used which do not alter or influence the mould, or influence the casting material in its hardening or crosslinking process. 

PAI-QUA-18: Positive materials SHALL be used within in their best before period. 

Note: It is recommended to use always fresh components and materials. 

PAI-QUA-19: The evaluator SHALL use materials according to the instructions given by the manufacturer. evaluator SHALL document the deviations. 

Exemplary Variations: 

- Different technologies / methods to create a 2.5D mould 

- Different negative materials 

Federal Office for Information Security 

17 

2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms (Normative) 

- Different positive materials and additives 

## 2.3.2.3.3 3D-Presentation Attack Instruments 

PAI-QUA-20: The evaluator SHALL present finger artefacts to the TOE containing a partial or complete fingerprint. Different methods and processes are possible to create such artefacts. 

## 2.3.2.3.3.1 Mould-based Artefact Creation Mould Creation 

PAI-QUA-21: The evaluation laboratory SHALL prepare the moulding material as described by the product manufacturer. 

PAI-QUA-22: Materials SHALL be used according to their best before date. 

It is recommended to always use fresh / new materials to exclude variations in the mould quality based on the materials. 

Depending on the negative materials for the moulding process protective containers can be necessary in order to keep their physical properties. 

PAI-QUA-23: The fingerprints taken in a cooperative manner SHALL be taken from freshly washed hands. PAI-QUA-24: The evaluator SHALL wait instructions. 

PAI-QUA-25: During this period any movements of the finger SHALL be reduced to minimize / avoid alterations of the fingerprint artefact and overall reduction of the artefact quality. 

Release agents can help to remove the finger from the moulding material. It is recommended to test several release agents, since some could prevent the proper curation of some artefact materials. 

Besides the co-operative moulding process, the evaluation laboratory can create finger artefacts based on acquired 3D finger data with subsequent creation with 3D-printing or other technologies. 

Casting Process 

PAI-QUA-26: The evaluator SHALL only use materials and ingredients which have not reached their date of expiry. 

PAI-QUA-27: The evaluator SHOULD follow the instructions provided by the manufacturer. 

PAI-QUA-27a: If the evaluator changes SHALL be properly documented. 

2.3.2.3.3.2 Direct Artefact Creation from 3D Fingerprint Data 

In case 3D fingerprint data are acquired, the evaluator can directly create an artefact based on this data, for can be necessary. 

PAI-QUA-28: The evaluator SHALL take care that the used 3D printing technology fulfils necessary requirements to achieve a functional biometric artefact. 

PAI-QUA-29: The printing resolution SHALL be high enough to replicate the ridge pattern of the finger. 

2.3.2.3.4 Quality Check 

PAI-QUA-30: The created artefact SHALL be quality checked. 

PAI-QUA-31: Artefacts SHALL only be used for PAD-testing if the comparison score exceeds the threshold for the biometric comparison. 

Federal Office for Information Security 

18 

3 Evaluation Phase (Normative) 

## 3 Evaluation Phase (Normative) 

The following sections describe the Biometric Performance and the Presentation Attack Detection mechanism evaluation of the Target of Evaluation. Requirements regarding the biometric performance for the different Biometric Assurance Level are specified in the BSI TR-03166. 

EVA-GEN-01: In contrast to PRE-PRO-01X the evaluation of the biometric performance as described in 3.1 Biometric Performance Evaluation and 3.2 Presentation Attack Detection Evaluation SHALL be performed with the TOE, which will be available in the market, without the access to biometric comparison scores and PAD scores, but ignoring the organisational measures within the evaluation phase. 

## 3.1 Biometric Performance Evaluation 

For the biometric performance evaluation, the Evaluation Guidance distinguishes between different cases: 

1. Biometric Performance Evaluation (Product Manufacturer) 

   - a. Embedded Capture Device as a Part of the TOE 

   - b. The biometric system can be used with several different capture devices and therefore the capture device is not part of the TOE. 

2. Biometric Performance Plausibility Check by the Evaluation Laboratory 

   - a. Embedded Capture Device as a Part of the TOE 

   - b. The biometric system can be used with several different capture devices and therefore the capture device is not part of the TOE. 

EVA-PER-01: The test crew for all biometric performance tests SHALL be composed as defined by ISO/IEC 19795-1 chapter 7.4. 

EVA-PER-02: For the case where the capture device is not part of the TOE (1b. and 2b.), the evaluation laboratory SHALL use different capture devices covering at least the lowest hardware specification allowed by the product manufacturer up to state-of-the-art capture devices. 

Note: Each device taken into account with EVA-PER-02 has to be tested according to the given approximation for the test crew size . 

EVA-PER-03: The requirements for the minimal amount of Information, which SHALL be included in the testing report, are given in the Appendix (6 Appendix: Minimal Information Requirements of a Testing Report). 

EVA-PER-04X : The biometric performance of the TOE SHALL be evaluated based on the assumption of a single attempt per test subject. 

## 3.1.1 [BAL-1] Biometric Assurance Level 1 

## 3.1.1.1 Biometric Performance Evaluation by the Product Manufacturer 

To prove a sufficient biometric performance (1 false accept in 10,000 attempts) of the TOE the product manufacturer has to execute and document the performance. Testing of the biometric performance by the product manufacturer can be done with biometric characteristics captured by the product manufacturer or alternatively by using the NIST FRTE 1:1 biometric performance test executed with the VISA-scenario data set. 

## 3.1.1.1.1 Biometric Performance Evaluation via Technology Evaluation 

EVA-PER-04: The product manufacturer SHALL perform a technology evaluation of the biometric system (excluding the capture device) with 30,000 independent and different biometric characteristics to fulfil the rule of 3 to provide proof for a biometric performance of 1 false accept in 10,000 attempts. 

Note: This is an evaluation of the biometric performance using a database. 

Federal Office for Information Security 

19 

3 Evaluation Phase (Normative) 

As an alternative to EVA-PER-04 the evaluation of the biometric performance provided by the NIST FRTE 1:1 (face) or NIST PFT III (finger) test can be used, if the conditional requirements EVA-PER-05 and EVAPER-06 are met. 

EVA-PER-05 (Conditional): The biometric performance tested via NIST FRTE 1:1 methodology SHALL use the VISA-scenario. 

EVA-PER-06 (Conditional): The evaluated biometric performance SHALL go below 1 false accept in 30,000 attempts. 

## 3.1.1.1.2 Embedded Capture Device as a Part of the TOE 

EVA-PER-07: The product manufacturer SHALL capture the biometric characteristics of 245 test subjects with the intended and embedded capture device of the TOE. 

Note: The number of the required test crew size N can be approximated by the total number of comparisons K following the rule of 3 or rule of 30. Applying the rule of 3 to prove an FAR of 0.01% means 30,000 crosscomparisons have to be performed. The test crew size can be calculated by 

## 𝑁≈√2𝐾 

EVA-PER-08: The product manufacturer SHALL evaluated the achieved biometric performance based on the cross-comparison approach defined by ISO/IEC 19795. 

EVA-PER-09: The cross-comparison approach SHALL provide proof of a biometric performance of 1 false accept in 10,000 attempts. 

## 3.1.1.2 Biometric Performance Plausibility Check by the Testing Laboratory 

The evaluation laboratory performs independently from the product manufacturer a plausibility test of the biometric performance of the system including the capture device. 

Note: The plausibility check has to be performed in all cases by the evaluation laboratory. 

EVA-PER-10: The evaluation laboratory SHALL capture the biometric characteristics of 245 test subjects with the intended and embedded capture device of the TOE. 

EVA-PER-11: The evaluation laboratory SHALL evaluated the achieved biometric performance based on the cross-comparison approach defined by ISO/IEC 19795. 

EVA-PER-12: The cross-comparison approach SHALL provide proof of a biometric performance of 1 false accept in 10,000 attempts. 

The evaluation laboratory performs independently from the product manufacturer a plausibility test of the biometric performance of the system excluding the capture device. 

EVA-PER-13: EVA-PER-10 to EVA-PER-12 are performed with capture devices as specified in EVA-PER-02. 

## 3.1.2 [BAL-2] Biometric Assurance Level 2 

## 3.1.2.1 Biometric Performance Evaluation by the Product Manufacturer 

To prove a sufficient biometric performance (1 false accept in 33,333 attempts) of the TOE the product manufacturer has to execute and document the performance. Testing of the biometric performance by the product manufacturer can be done with biometric characteristics captured by the product manufacturer or alternatively by using the NIST FRTE 1:1 biometric performance test executed with the VISA-scenario data set. 

Federal Office for Information Security 

20 

3 Evaluation Phase (Normative) 

## 3.1.2.1.1 Biometric Performance Evaluation via Technology Evaluation 

EVA-PER-14: The Product Manufacturer SHALL perform a technology evaluation of the biometric system (excluding the capture device) with 100,000 independent and different biometric characteristics to fulfil the rule of 3 to provide proof for a biometric performance of 1 false accept in 33,333 attempts. 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0021-03.png)


formance using a database. 

As an alternative the evaluation of the biometric performance provided by the NIST FRTE 1:1 (face) or NIST PFT III (finger) test can be used, if the conditional requirements EVA-PER-15 and EVA-PER-16 are met. 

EVA-PER-15: The biometric performance tested via NIST FRTE 1:1 methodology SHALL use the VISAscenario. 

EVA-PER-16: The evaluated biometric performance SHALL go below 1 false accept in 100,000 attempts. 

## 3.1.2.1.2 Embedded Capture Device as a Part of the TOE 

EVA-PER-17: The product manufacturer SHALL capture the biometric characteristics of 448 test subjects with the intended and embedded capture device of the TOE. 

EVA-PER-18: The product manufacturer SHALL evaluated the achieved biometric performance based on the cross-comparison approach defined by ISO/IEC 19795. 

EVA-PER-19: The cross-comparison approach SHALL provide proof of a biometric performance of 1 false accept in 33,333 attempts. 

## 3.1.2.2 Biometric Performance Plausibility Check by the Evaluation Laboratory 

The evaluation laboratory performs independently from the product manufacturer a plausibility test of the biometric performance of the system including the capture device. 

EVA-PER-20: The evaluation laboratory SHALL capture the biometric characteristics of 448 test subjects with the intended and embedded capture device of the TOE. 

EVA-PER-21: The evaluation laboratory SHALL evaluated the achieved biometric performance based on the cross-comparison approach defined by ISO/IEC 19795. 

EVA-PER-22: The cross-comparison approach SHALL provide proof of a biometric performance of 1 false accept in 33,333 attempts. 

The evaluation laboratory performs independently from the product manufacturer a plausibility test of the biometric performance of the system excluding the capture device. 

EVA-PER-23: EVA-PER-19 to EVA-PER-21 are performed with capture devices as specified in EVA-PER-02. 

## 3.1.3 [BAL-3] Biometric Assurance Level 3 

## 3.1.3.1 Biometric Performance Evaluation by Product Manufacturer 

To prove a sufficient biometric performance (1 false accept in 333,333 attempts) of the TOE the product manufacturer has to execute and document the performance. Testing of the biometric performance by the product manufacturer can be done with biometric characteristics captured by the product manufacturer or alternatively by using the NIST FRTE 1:1 biometric performance test executed with the VISA-scenario data set. 

## 3.1.3.1.1 Biometric Performance Evaluation via Technology Evaluation 

EVA-PER-24: The Product Manufacturer SHALL perform a technology evaluation of the biometric system (excluding the capture device) with 1,000,000 independent and different biometric characteristics to fulfil the rule of 3 to provide proof for a biometric performance of 1 false accept in 333,333 attempts. 

Federal Office for Information Security 

21 

3 Evaluation Phase (Normative) 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0022-01.png)


As an alternative the evaluation of the biometric performance provided by the NIST FRTE 1:1 (face) or NIST PFT III (finger) test can be used, if the conditional requirements EVA-PER-25 and EVA-PER-26 are met. 

EVA-PER-25: The biometric performance tested via NIST FRTE 1:1 methodology SHALL use the VISAscenario. 

EVA-PER-26: The evaluated biometric performance SHALL go below 1 false accept in 333,333 attempts. 

## 3.1.3.1.2 Embedded Capture Device as a Part of the TOE 

EVA-PER-27: The product manufacturer SHALL capture the biometric characteristics of 1415 test subjects with the intended and embedded capture device of the TOE. 

EVA-PER-28: The product manufacturer SHALL evaluated the achieved biometric performance based on the cross-comparison approach defined by ISO/IEC 19795. 

EVA-PER-29: The cross-comparison approach SHALL provide proof of a biometric performance of 1 false accept in 333,333 attempts. 

## 3.1.3.2 Biometric Performance Plausibility Check by the Evaluation Laboratory 

The evaluation laboratory performs independently from the product manufacturer a plausibility test of the biometric performance of the system including the capture device. 

EVA-PER-30: The evaluation laboratory SHALL capture the biometric characteristics of 1415 test subjects with the intended and embedded capture device of the TOE. 

EVA-PER-31: The evaluation laboratory SHALL evaluated the achieved biometric performance based on the cross-comparison approach defined by ISO/IEC 19795. 

EVA-PER-32: The cross-comparison approach SHALL provide proof of a biometric performance of 1 false accept in 333,333 attempts. 

The evaluation laboratory performs independently from the product manufacturer a plausibility test of the biometric performance of the system excluding the capture device. 

EVA-PER-33: EVA-PER-28 to EVA-PER-30 are performed with capture devices as specified in EVA-PER-02. 

## 3.2 Presentation Attack Detection Evaluation 

After creating the best suited Presentation Attack Instruments for evaluating the TOE in the initial preevaluation phase, the evaluator uses these instruments for the testing process. The intention of this approach is to minimis can occur during the testing, but has to be performed during the Pre-Evaluation Process. 

EVA-PAD-01: The evaluator SHALL cover all PAI-species, which can be created from the material list in chapter 4 Material List Including Relevant Technologies Covering Different Presentation Attack Instruments. 

EVA-PAD-02: For the BALs 2 and 3 the evaluator SHALL follow the rating scheme of attack potentials as defined in CEM [1] every PAI is presented to the TOE and evaluated following the evaluation metric as described in 3.2.1 Evaluation Metric. 

## 3.2.1 Evaluation Metric 

The evaluation metric for this technical guideline is very similar to established vulnerability analysis procedures in Common Criteria. 

Federal Office for Information Security 

22 

3 Evaluation Phase (Normative) 

EVA-MET-01: Prior to the Evaluation Phase the evaluator SHALL perform the steps described in chapter 2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms. 

All steps of the evaluation, including the pre-evaluation phase, is depicted in Figure 1. 

EVA-MET-02: PAIs SHOULD be personalised to the presenting evaluator, see also PAI-QUA-08. 

Note: The requirement is in particular important for the use of 3D face masks. Flexible masks can deform if not fitting to the evaluator. Both hard masks and flexible masks can show hard edges which can be detected by the TOE as a PA attempt. 

EVA-MET-03: During the evaluation an evaluator SHALL present a PAI to the TOE with an identity different from his own. The metric regarding passing or failing a test is defined in Section 3.2.1 Evaluation Metric. 

EVA-MET-04: For the BALs 2 and 3, the evaluator SHALL define, create and optimise additional Presentation Attack Instruments in conformance to BSI TR-03166. 

EVA-MET-05: Criteria for pass or fail within the PAD evaluation are defined in the following schema: 

- Each artefact SHALL be applied at least 25 times with minimum 2 evaluators and 3 different identities. In the case that 3 presentation attacks are classified as bona-fide attempts for one evaluator (presented identity), the TOE has failed the test and the evaluator can stop testing with this artefact. 

Note: For clarification it is not required that each evaluator has to present 3 different identities. The biometric system has to be tested with 3 different identities, where the evaluators can impersonate each other. 

Note: PAIs which wear off during usage, the evaluator has to create a PAI species based on the same source, e.g. for fingerprints a mould. 

- If the TOE classifies a PA 1 or 2 times as bona-fide, the evaluator SHALL perform at least 25 additional attempts. 

   - If only 1 attempt out of 50 was classified as bona-fide, the TOE passes the test (provided the evaluators have no reason to doubt the results - otherwise they can add more attempts with variations until they are confident with the outcome. The evaluators SHALL document their decision). 

   - If two PAs were successful, the evaluator SHALL create new PAIs of the same species with varying parameters (see Toolbox) to optimise the PA further and to gain confidence about the reliability of the PA. 

The evaluator SHALL repeat the evaluation with at least 1 new PAI. 

- The TOE fails the test for an artefact if three or more attempts have been wrongly classified as bona-fide attempts. 

- If the PAD-mechanism classifies all PA attempts correctly as PA, the system passes the test. 

- If the TOE fails the test for a single artefact with an attack potential lower than the targeted BAL (esp. all PAIs of the functionality test), the TOE fails the evaluation and the evaluation lab can stop the tests. 

Federal Office for Information Security 

23 

3 Evaluation Phase (Normative) 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0024-01.png)


Figure 1 PAD Test Workflow including PAI creation during pre-evaluation and subsequent PAD evaluation. 

## 3.2.2 Fixed Time Methodology: Pre-Evaluation and PAD-Evaluation 

In addition to the Evaluation Metric, the Evaluation Guidance defines an upper time limit for each Biometric Assurance Level, which includes only the PAD vulnerability evaluation phase. The pre-evaluation phase as well as the plausibility check of the biometric performance of the biometric system is not part of the Fixed Time Methodology. 

## 3.2.2.1 Biometric Assurance Level 1 

EVA-FTM-01: The upper time limit for the PAD evaluation for BAL 1 SHALL be 15 person-days. 

## 3.2.2.2 Biometric Assurance Level 2 

EVA-FTM-02: The upper time limit for the PAD evaluation for BAL 2 SHALL be 30 person-days. 

Federal Office for Information Security 

24 

3 Evaluation Phase (Normative) 

## 3.2.2.3 Biometric Assurance Level 3 

EVA-FTM-03: The upper time limit for the PAD evaluation for BAL 3 SHALL be 60 person-days. 

## 3.2.3 Minimal Test Coverage 

The evaluation of the PAD functionality has to be performed with PAIs showing at least three different identities presented by at least two evaluators, see EVA-MET-02 . 

The following Table 8 gives an overview of the minimum number of PAI to create and optimise during the pre-evaluation phase. This table covers only the extent for the BAL 1. The additional PAIs freely created by the evaluator for the BALs 2 and 3 are not covered here. 

Table 8 Overview of minimal number of PAIs to create for test coverage of the modality face 

|Nr.|PAI Class|Identities|PAIs|Minimal number<br>of PAIs|
|---|---|---|---|---|
|01|Paper|3|• Size<br>• A4<br>• A3<br>• Cut outs (only A4)<br>• Eyes<br>• Mouth<br>• Nose<br>• Face contour<br>• Partial Faces<br>• Periocular<br>• Half mask|15|
|02|Foil|3|• Size<br>• A4|3|
|03|Fabric|3|• Size<br>• A4<br>• A3|6|
|04|Display|3|• Size|12|
|05|Projector|3||3|
|06|3D-Masks|3|• Base material<br>• PLA<br>• Resin<br>• Latex<br>• Silicon<br>• Gelatine<br>• Stiffness|30|



Federal Office for Information Security 

25 

3 Evaluation Phase (Normative) 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0026-01.png)


- Solid 

- • Flexible 

- • Surface properties • Colouring • Texture 

- • Cut outs • Eyes 

- • Completeness • Full face • Partial face 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0026-03.png)


Table 9 Overview of minimal number of PAIs to create for test coverage of the modality finger 

|Nr.|PAI Class|Identities|PAIs|Minimal<br>number of<br>PAIs|
|---|---|---|---|---|
|01|Fingermarks|3|• Pure marks<br>• with powder additives<br>(graphite, metal)|6|
|02|Paper[2D-print]|3|• dry paper<br>• wet paper|6|
|03|Transparent Foil[2D-print]|3|• ink / toner|3|
|04|Gelatine[cast]<br>(mix with glycerine)|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|
|05|Gelafix[cast]<br>(transparent)|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|
|06|Gelafix[cast]<br>(coloured)5|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|
|07|Silicone[cast]<br>(transparent)|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|



> 5  Gelafix is available in many different colours (different skin tones, red, green, etc.). In pre-evaluation, the evaluator has to determine the colour with the best chance for a successful attack. 

Federal Office for Information Security 

26 

3 Evaluation Phase (Normative) 

|08|Silicone[cast]<br>(coloured)6|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|
|---|---|---|---|---|
|09|Latex[cast]|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|
|10|Wood Glue[cast]<br>(added glycerine)|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|
|11|Window Colour[cast]<br>(acrylic)|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|
|12|Conductiv rubber|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|
|13|3D-printed positive<br>(full colour print, flexible<br>polymer material: shore<br>hardness A10-A20)|3|• thin (~0.3 mm)<br>• middle (~1 mm)<br>• thick (>2 mm)|9|



## 3.2.4 Expected Result for the Presentation Attack Detection Evaluation 

EVA-RES-01: As described in 3.2.1 Evaluation Metric each Presentation Attack Instrument SHALL be correctly classified, within the given tolerance of the defined schema, as a Presentation Attack. 

> 6  In pre-evaluation, the evaluator has to determine the colour with the best chance to successfully attack the TOE. For a neutral light skin tone, someone can find an exemplary mixture instruction in the appendix. 

Federal Office for Information Security 

27 

4 Material List Including Relevant Technologies Covering Different Presentation Attack Instruments (Informative) 

## 4 Material List Including Relevant Technologies Covering Different Presentation Attack Instruments (Informative) 

This chapter outlines the level of detail for communication between an evaluation laboratory and the manufacturer of the biometric system during a certification process. The general idea behind this limited amount of information is that manufacturers will use this exchange to evaluate and test their solutions in a more extensive manner to succeed in the evaluation process. Speaking in terms of presentation attacks, a manufacturer would likely present more and different artefacts to the TOE than the testing laboratory. 

## 4.1 Modality Face 

Print Frontal Face Images (PRT) 

- Inkjet- / Toner printer 

- Paper 

- Fabrics 

- Foils 

## Displays / Projectors Presenting a Frontal Face Image (DSP) 

- Different display technologies 

- Display Sizes 

- Pixel densities 

## 3D-Masks (MSK) 

- Different 3D-Printing technologies 

- Materials usable for fused material deposition 

- Resins 

- Plaster 

- Additives to fake skin properties 

- Texture and coloration 

## 4.2 Modality Finger 

## Fingermarks (FMA) 

- Fingermark enhancement and digitization with post-processing 

- Materials and methods to trigger the fingerprint acquisition when no real finger is presented to the sensor 

## Fingerprint Print Outs (PRT) 

- Inkjet- / Laser printer 

- Paper / Foil type 

## Cast Finger Artefacts (CAS) 

- Different materials and methods to create 2.5D and 3D moulds 

Federal Office for Information Security 

28 

4 Material List Including Relevant Technologies Covering Different Presentation Attack Instruments (Informative) 

- Casting materials and additives 

   - Gelatine like materials 

   - Silicones 

   - Latex 

   - Glues 

   - Polymers 

   - Conductive materials 

   - Variation in material thickness 

   - Mixtures of different materials 

Federal Office for Information Security 

29 

5 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0030-01.png)


## 5 Instrument Construction (Informative) 

This chapter is informative and gives a general overview of tools, materials and methods to create Presentation Attack Instruments for the modalities Face and Finger, but is not comprehensive. Evaluation facilities and their experts can have tools, materials and methods not mentioned in the following sections due to their expertise in the evaluation of biometric authentication components. 

## 5.1 Creating Artefacts for the Modality Face 

## 5.1.1 PAIs Based on a Frontal Face Image Printout 

## 5.1.1.1 Recommended Tools and Materials 

The following enumeration gives an example of tools and materials to create PAI variations based on a print of a frontal face. 

1. camera 6. photo printer 11. flashlight 2. diffused lights 7. white paper DIN A4 12. scissors 3. tripod 8. photo paper DIN A4 13. cord 4. laser printer colour 9. tripod adapter 14. hole puncher 

5. inkjet printer colour 10. scalpel 

## 5.1.1.2 Source Information 

For artefacts of this class, high quality pictures of the enrolled user are needed. For requirements see 2.3.1.2.1 Source Requirements for 2D-Presentation Attack Instruments. 

## 5.1.1.3 Print the Picture 

Depending on the PAD-technique used in the TOE, different sizes of prints can be recognised as a face. Therefore, different sizes of a printout can be necessary. A good starting point is an artefact that comes as close as possible to the realistic size of the person that is shown on the picture. The best way to achieve this is to try a full-size printout on DIN A4 paper. 

## 5.1.1.3.1 Possible Modifications 

In the following, possible / exemplary modifications on a print are described to achieve a modification of the PAI. 

Modifications: 

- Use a different printer 

- Print in black or colour 

- Print on different materials 

- Cut out the eye region of the printed face 

   - Cut out the shape of the face 

   - Take holes on each side of the cut of face with a hole puncher and draw one cord through each hole. The cord allows to carry the printout like a mask. 

- Cut out the mouth region of the printed face 

Federal Office for Information Security 

30 

uction (Informative) 

5 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0031-02.png)


## 5.1.1.4 Artefact Application to the TOE 

The evaluator can hold / wear the printed picture of the face in front of the TOE. It has to be ensured that only the PAI is recognized by the TOE and not the face of the evaluator. 

As the PAI varies in size, the evaluator evaluates the TOE using different distances between TOE and PAI, which is part of chapter 2 Pre-Evaluation Phase for Evaluating Presentation Attack Detection Mechanisms. 

The evaluator can move / tilt / pan the PAI in front of the TOE to find a position where the face comparison is successful. To evaluate the PAD-functionality of the TOE, a single parameter can be varied in increments. 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0031-07.png)


## 5.1.2 PAIs based on Video of an Identity 

## 5.1.2.1 Recommended Tools and Materials 

1. camera 3. diffused lights 5. tripod adapter 

2. tablet 4. tripod 

## 5.1.2.2 Source Information 

For artefacts of this class, high quality pictures / videos of the enrolled user are needed. For requirements see 2.3.1.3.1.2 Display to Present a Facial Image and for the source data 2.3.1.2.1 Source Requirements for 2DPresentation Attack Instruments. 

## Additional recommendations for videos 

A facial video of the enrolled identity can be recorded with a resolution at least exceeding the native resolution of the displaying device. The framerate and bitrate of the video has to fit the displaying device and the PAD-technology. To include potential challenge-response mechanisms the video can contain head movements in all directions, eye and eyelid movements and opening and closing of the mouth. 

1. The face has to be well illuminated without hotspots or shadows. 

2. The background has to have as few artefacts and distortions as possible. 

3. The face must be in focus. 

4. The person being filmed should look straight into the direction of the camera and move the head a little bit up, down and sideways during the video. 

5. The person being filmed should look relaxed with neutral face expression. During the image acquisition the person can close the eyes and move the face muscles a little bit. 

## 5.1.2.2.1 Possible Modifications 

In the following, possible / exemplary modifications on a static image are described to achieve a modification of the PAI. 

- Animate a static image with an appropriate software 

- Instead of a display, a projector may be used to project the image or video on a surface 

Closely related to a single static image is the usage of several images in a video / video stream. With this option further modifications are available like: 

- Video replay attack 

- Manipulated video streams by deepfakes 

Federal Office for Information Security 

31 

5 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0032-01.png)


## 5.1.2.3 Artefact Application to the TOE 

1. The evaluator can hold a display presenting the target identity in front of the TOE. It can be necessary to use displays with different sizes and pixel densities. Too small displays present the frontal facial image too small to be recognized by the facial comparison algorithm. 

2. Depending on the used display and camera / objective constellation, different distances between PAI and TOE can be necessary. The evaluator can test different distances between PAI and TOE for every PAI. 

3. The evaluator should move / tilt / pan the PAI in front of the TOE to find a position where the face comparison is successful. To evaluate the PAD-functionality of the TOE, a single parameter can be varied in increments. 

## 5.1.3 PAIs based on 3D-Masks Containing Facial Biometric Characteristics of an Identity 

The following subchapters explain how to build artefacts from this class. A general overview of different data / information sources, intermediate steps and a potential post-processing is given in 2.3.1.2.2 and 2.3.1.3.2. 

The first step in the process is getting a digital copy of the face. This can be done in different ways, ranging from a completely manual process to a fully automated one. One can for example take pictures of the person to be impersonated or one can scan the face of the person by using a 3D scanning system. 

Several service providers are on the market to acquire the necessary data and create a 3D-model of the enrolled identity. Further, 3D-printing services are on the market to print such artefacts. Due to the transfer of personal data, the GDPR has to be taken into account. 

The following subchapters explain how to generate a computer model of the head by photogrammetry and how to produce a 3D silicone mask as this is the process that showed the best results. 

Alternatively, there is a description how to build a 3D positive model of the face of an evaluator. 

## 5.1.3.1 Recommend Tools and Materials 

   14. bowls 

1. camera 

2. diffused lights 15. scoops 

3. tripod 

   16. vacuum pump 

4. tripod adapter 

   17. clamps 

   18. flocking colour for silicone 

5. swivel chair 

6. Photogrammetry software 

   19. silicone colorizer 

7. 3D Model Editing software 

   20. silicone release antiadhesive spray 

   21. isopropyl alcohol 

8. 3D printer 

9. PLA filament 

   22. marker pen 

   23. wrapping film 

10. towel 

11. softener 

   24. Vaseline 

12. silicone 13. scale 

25. Super Baldiez 

26. airbrush 

27. silicone adhesive neo 

28. dust mask 

29. protection googles 

30. cotton buds 

31. jam jar small and medium 

32. hair clip 

33. Neo Adhesive Remover 

34. sealer 

35. colour for airbrush 

36. Isopropylmyristate 

37. scalpel 

38. tissues 

39. medical gloves 

Federal Office for Information Security 

32 

5 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0033-01.png)


|40. nail scissors|43. paintbrush|46. make-up sponge|
|---|---|---|
|41. big garbage bags|44. liquid make-up|47. dust extraction for|
|42. crepe tape|45. powder|airbrush|



## 5.1.3.2 Source Information 

For photogrammetry, as one possibility to generate a 3D-model of a head, images from different angles of the head are necessary to calculate a 3D-modell. Therefore, different acquisition methods are mentioned in this description: 

- move around the person with a camera taking pictures 

- mount a camera on a tripod, and rotate the person using a swivel chair 

- use a dedicated portrait studio with several cameras taking simultaneously pictures from different angles 

For artefacts of this class, high quality pictures of the enrolled user are needed. For requirements see 2.3.1.2.1 Source Requirements for 2D-Presentation Attack Instruments 

To minimize possible artefacts during the computational 3D-model generation process, the person moves as little as possible and face the (central) camera (at the beginning) with neutral expression. In addition to the recommendations mentioned in 5.1.2.2 Source Information, the evaluator must take care that a sufficient number of images is captured to generate a 3D-model. 

- The person being photographed looks straight into one direction during the whole shooting. 

- The person being photographed looks relaxed with neutral face expression. They hold the same expression during the whole shooting. 

- The head is well illuminated without hotspots (overexposed) or shadows. 

- The background has as few artefacts and distortions as possible. 

- The face is in focus. 

- There is a sufficient overlap between the pictures. 

## 5.1.3.3 3D-Model Generation, Mould and Mask Creation 

Based on the captured images, a 3D-model can be generated with an appropriate photogrammetry software. Due to the variety of software solutions, the lab has to figure out the settings to achieve the best generated 3D-model. 

For further use post processing steps may be necessary to create a 3D-mask or a mould to cast a 3D-mask later on. 

- Repair the mesh 

- Simplify the mesh 

To create a mould from the 3D-model, expertise in 3D-modelling is necessary. Therefore, no general description about the modelling process can be given. 

To create the mould, or a 3D-mask directly, several options are available like: 

- 3D-Printing 

   - Fused Material Deposition (FMD) 

   - Stereolithography (SLA) 

   - Digital Light Processing (DLP) 

Federal Office for Information Security 

33 

) 

5 

A directly printed 3D-mask can be coloured and painted to create a face-like texture of the face. High-end 3D-printers can support multi-colour 3D-printing, which can make the post processing with colouring and painting unnecessary. 

The mould for the casting process should be prepared with a mould release agent to remove the cast mask from the mould. The mould can be used with different materials to create various masks. 

## 5.1.3.3.1 Colouring / Painting of the Mask 

The pieces of the mould can be used as support during the colouring / painting process. Due to health risks, it is not recommended to perform the airbrushing process while the evaluator wears the mask. 

Based on experience, painting the mask is a challenging process. It can be worth to consider asking a makeup artist for this step. 

1. By airbrush: 

   - a. The first step to paint the mask is to mix some isopropanol with colour for airbrush. It is recommended to choose the skin colour of the impersonated person. If the material s base tone of colour is not properly adjusted during the creation step, dispense it with a brush and mix it in a small jar with ca. 2 ml isopropanol. 

   - b. Then, one has to apply the colour mixture with airbrush on the mask with 10 pounds of pressure. 

2. By make-up 

   - a. To colourise the mask, it is recommended to use non-permanent make-up. 

   - b. For better results and easier removal of the make-up, one should moisturize the face and let it infiltrate into the skin for ca. 2 minutes. 

   - c. After this, it is recommended to use primer before putting on the make-up It makes the make-up application smoother and last longer. 

   - d. Liquid contour make-up that matches the skin colour of the enrolee should be applied to the entire face and the neckline with a make-up sponge or the powder brush. 

   - e. The next step is to apply highlighter to the parts of the face that should get accented. If needed, one has to mix up different colours of the cream colour make-up to find the right colour. 

   - f. After this, darker cream colour make-up is applied to the parts which stay in the background with a small brush . One has to blend over the edges of the different colours with the powder brush. 

Example: To make a face appear smaller, one has to put darker colour on the side of the face and brighter colour on the forehead and the chin. To make a face appear shorter, one has to put darker colour on the forehead and the chin. The Tutorial (How to contour for beginners, 2016) is recommended. 

- g. The next step is to shape the eyebrows and give them the needed contour with the eyelash comb. Then use cream colour make-up with the trumpet paste brush and, if needed, fill it up with mascara. 

- h. To remove small parts of make-up one can use cotton buds or tissues. 

- i. After these steps, every further make-up depends on the face of the enrolee. 

Further tutorials and information regarding the topic make-up can be found online. 

Federal Office for Information Security 

34 

5 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0035-01.png)


## 5.1.3.4 Artefact Application to the TOE 

1. The evaluator stays in front of the TOE. Basically, the evaluator behaves naturally as if they would normally use the TOE. 

2. One has to try to find the optimal position. If possible, one can test the best position of the attack on every TOE with the enrolee in front of the system (i.e., by means of a genuine attempt). 

## 5.1.3.4.1 Hard 3D-Masks 

A hard mask can be worn with attached straps to hold the mask in place of the evaluator s head. For a tighter fit between mask and evaluator, the inner part of the mask can be shaped with another inner stamp, showing the face shape of the evaluator. The big advantage of hard masks is that the masks outer shape is independent of evaluator, which may be helpful for the evaluation of biometric systems taking 3D information into account. 

## 5.1.3.4.2 Flexible 3D-Masks 

The application of flexible masks may require more effort and preparation steps depending on the PAD functionality. 

1. Before the flexible mask can be applied to the evaluator s face, it is important to clean the face and remove cream and / or make-up from the skin. 

2. To get the best result, one starts the application at the nose and then moves outwards in small steps in every direction. 

3. The first step to apply the flexible mask on the evaluator s face is to put some material specific adhesive on the tip of the nose and also in the inside tip of the mask nose with a small brush. 

4. Furthermore, one has to apply the mask onto the face of the evaluator step by step. It is required to fix every little part with adhesive without air bubbles between mask and skin. To press the mask on the skin, one can use a small sponge ball. 

5. buds. 

6. Finally, one has to paint sealer on the edges to smooth them down to the skin to fix the edges. 

## 5.1.4 Make-up Attack 

An impersonation via creating contours and facial details with make-up is an ongoing topic and relevant in - particular for evaluating TOE within evaluations against higher attack potentials defined BSI-list. To receive an impression of this kind of attacks some videos are available on the internet, where historic person and celebrities are impersonated applying make-up and wigs. 

1. For better results and easier removal of the make-up one should moisturise the face and let it infiltrate into the skin for ca. 2 minutes. 

2. After this it is recommended to use primer before putting on the make-up. It makes the make-up application smoother and last longer. 

3. Liquid contour make-up matching the skin colour of the enrolee is applied to the entire face and the neckline with a make-up sponge or a powder brush. 

4. The next step is to apply highlighter to the parts of the face, that gets accented (cream colour makeup applied with the eyeliner brush, brighter than the enrolees face colour). If needed, one has to mix up different colours of the Cream Colour make-up to find the right colour. 

5. After this, darker cream colour make-up is applied with a small brush to the parts which stay in the background. One has to blend over the edges of the different colours with the powder brush. 

Federal Office for Information Security 

35 

5 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0036-01.png)


6. The next step is to shape the eyebrows and give them the needed contour with the eyelash comb. Then use cream colour make-up with the trumpet paste brush and if needed to fill it up with mascara. 

7. To remove small parts of make-up one can use cotton buds or tissues. 

8. After these steps, every further make-up depends on the face of the enrolee. 

## 5.1.4.1 Recommend Tools and Materials 

1. tripod 

2. diffused lights 

3. tripod adapter 

4. make-up brushes 

5. moisturizer 

6. primer 

7. cream colour makeup 

8. liquid contour makeup 

9. make-up sponge 

10. translucent powder 

11. powder pad 

12. stipple sponge 

13. mascara 

14. cotton buds 

15. make-up remover wipes 

16. tissues 

Note: If the expertise of the evaluator is insufficient, a make-up artist may be consulted to learn the necessary skills or to apply the make-up to the evaluator. 

## 5.1.4.2 Artefact Application to the TOE 

This kind of artefact is highly dependent on the perspective of the biometric verification / authentication system. Therefore, the evaluator figures out the right position in relation to the TOE to achieve a sufficient biometric score, which matches the requirements regarding the definition of a PAI. 

1. The initial evaluation position should be a frontal image of the face. 

2. One has to try to find the right position. If possible, one can test the best position of the attack on every TOE with the enrolee in front of the system (e.g., by means of a genuine attempt). 

## 5.2 Build Artefacts for the Modality Finger 

## 5.2.1 Recommend Materials and Tools 

The following list gives an example of recommended tools and materials to create PAI variations: 

PAI-Materials: 

1. Transparency film for laser and inkjet printers / coloured 

2. Paper (white and coloured) 

3. Latex (Latex Milk) 

4. Wood glue (different brands, water based) 

5. Silicone (e.g., Dragon Skin, Dermasil, CPFlesh) 

   7. Window Colour (acrylic based) 

   8. Nanotips (different colours) 

6. Gelafix 

(different colours) 

## Mould-Materials: 

1. Luxatemp (direct mould) 

3. Alabaster Plaster 

4. Power Putty (Epoxy) 

   5. Nyloprint (with printed film) 

2. Cast silicone 

Federal Office for Information Security 

36 

5 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0037-01.png)


6. 3D-Print Materials (Resins, Polymers) 

   8. Mould Silicone (different brands) 

7. Laser engraver 9. UV-Photopolymer material (e.g. delrin) strips for stabilization 

   11. Indurent Gel 

   12. Zetalabor Silicone Putty 

10. Impregum 

Additives : 

1. Distilled Water 

2. Glycerine 

3. Graphite powder 

4. Iron powder 

5. Citric Acid (for preservation) 

6. Isopropanol (for cleaning) 

7. Release Agents (for casting) 

8. Silicone Colour 

9. Water based Colour 

## Tools: 

1. Fingerprint Powder 

   7. High-res Laser-Printer (different toners) 

2. Fingerprint paste (for pressed and scanned reference fingerprints) 

   8. Flatbed scanner (>1200 dpi) 

   9. 3D-Printer (resolution x/y:<30 µm, z:<15 µm) 

3. Brush 

4. Spatula 

10. Ideal: 3D- 

5. Lighter Measurement Tool 

6. High-res Inkjet(e.g. Profilometer) Printer (different inks) 

   11. Digital Scale 

12. Hygrometer 

13. Heat gun 

14. Oven / Microwave 

15. Fridge / Freezer 

16. UV-Lamp 

17. Small Vacuum Chamber (to prevent bubbles) 

## 5.2.2 Source Information 

For artefacts of this class, high quality pictures / scans of the user s enrolled fingerprint are needed. For requirements see 2.3.1.2.1 Source Requirements for 2D-Presentation Attack Instruments. For this class, different ways to create the source image can be followed: 

- Without cooperation 

   - Photography of a latent fingerprint on a surface without enhancement (lightning powder) 

   - Enhanced visibility of a latent fingerprint with lightning powder 

      - Transfer the fingerprint via tape on a sheet of paper 

         - Digitalize the latent fingerprint with a flatbed scanner 

Note: With this approach the achieved fingerprint artefact will directly feature the correct size. 

      - Direct photograph of the latent fingerprint Note: It is recommended to have an object for scale in the photograph to scale the latent fingerprint to the correct size. The evaluator must account for changes of the fingerprint due to the perspective or properties of the used camera. Depending on the camera used integrated enhancing algorithms are applied to the acquired image. 

- In cooperation 

   - Directly digitised fingerprint by using a fingerprint scanner, different technologies are possible 

Federal Office for Information Security 

37 

5 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0038-01.png)



![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0038-02.png)


- Cooperative mould creation 

   - Pressing the finger in modelling clay etc. 

Note: Analog and / or digital post processing steps can be necessary to achieve a sufficient comparison score and to create another type of artefact e.g., 2.5D artefacts. Here, the 2D image will be processed in a manner to create a mould where the fingerprint can be cast. 

## 5.2.2.1 2D Printed Finger Artefacts 

This subchapter contains information about the creation process of a 2D artefact, which can be printed with different printer technologies on different materials. 

## 5.2.2.1.1 Print the Fingerprint Artefact 

To achieve a sufficient comparison score between the enrolled and the presented fingerprint it is necessary to print the artefact in the correct size. Further, a mirroring and / or an inversion of the image can be necessary. 

A good starting point is a print with the printer s maximum native resolution on a white sheet of paper. 

## 5.2.2.1.2 Possible Modifications 

In the following, possible / exemplary modifications on a print are described to achieve a modification of the PAI. 

- Use a different printer / printer technology 

- Print in black or colour 

- Print on different materials 

   - colour 

   - thickness 

   - surface properties 

- Modify the printed artefact with additives like: 

   - Water 

   - Graphite 

   - Glycerol 

   - Contact Spray etc. 

   - Oil 

## 5.2.2.2 Post Processing Steps for 2.5D-Artefact Creation 

To create moulds from the captured 2D fingerprints it is possible to perform some easy post processing steps: 

- Binarization via thresholding 

- Line thinning 

- Height map calculation 

Based on these steps, moulds or fingerprint artefacts including the ridge / valley information of the fingerprint can be created. Moulds can be used with various castable materials. 

Federal Office for Information Security 

38 

5 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0039-01.png)


## 5.2.2.3 Moulds Taken in a Cooperative Scenario 

In a cooperative scenario the evaluator creates a finger mould by pressing the target finger in some plasticine or other material. A drying process at room temperature or at higher temperature may be necessary. During this process, the material can change its dimension (shrinking). 

Exemplary materials are plasticine, silicone with hardening additives, stearin, special plaster or pottery clay. 

## 5.2.2.4 Casting of Artefacts 

The following aspects should be considered for casting processes: 

- it is recommended to test the moulds for: 

   - 3D-accuracy (compared to the original finger) 

   - no surface distortions (e.g., bubbles, moulding/3D-printing artefacts) 

   - changes of physical properties in time (e.g., shrinking, decomposition) 

- in pre-evaluations it is recommended to test the chemical reaction between the artefact materials and the mould (also considering release agents), since some combinations would prevent the artefact from curing properly. 

- for mixed materials, a vacuum chamber can help to significantly reduce bubbles. 

- the right temperature can help to control the curing process (e.g., cooler temperatures lead to longer curing times for most materials, hence there is more time for properly mixing and preparing the artefact material for casting). 

## 5.3 Apply the Artefact to the TOE 

The created artefact will be pressed on the scanner surface. For some materials, it can be necessary to apply some additives to the contact surface. Using real skin behind the artefact can help attack certain PADtechnologies, especially with thin artefacts. 

During pre-evaluation the evaluators should optimise their presentation technique for every artefact, regarding e.g., approach angle, pressure and speed. 

Federal Office for Information Security 

39 

6 Appendix: Minimal Information Requirements of a Testing Report 

## 6 Appendix: Minimal Information Requirements of a Testing Report 

Table 10 in this chapter summarises the minimal information that needs to be contained in the testing report with regard to this Technical Guideline. Most parts of this testing report are based on the reporting result list for the biometric performance of a system published in ISO/IEC 19795-1:2021 [6] Clause 12. 

Table 10 Minimal Requirements of a Testing Report 

|Test Details|Details to Report|Information|
|---|---|---|
|The system(s) tested|Including details of algorithms,<br>biometric sensors, user interface,<br>supporting hardware, etc.|1. System Specification: Manufacturer, model,<br>version, firmware, biometric modality<br>2. Application software: provider, title, version,<br>build|
|Test organization<br>details|Test organization, location, date of<br>test.|<br>Company / Organization, Date evaluation<br>completed, Date test report published|
|Type of evaluation|In the case of technology<br>evaluation: details of the test<br>corpus used.<br>In the case of scenario evaluation:<br>details of the test scenario.<br>In the case of operational<br>evaluation: details of the<br>operational application.|As defined in Chapter 3 the use case SHALL be a<br>scenario evaluation.|
|Size of evaluation|Number of test subjects.<br>Number of instances (fingers,<br>hands or eyes, etc.) enrolled by<br>each test subject.<br>Number of visits made by test<br>subject.<br>Number of transactions per test<br>subject (or test subject instance) at<br>each visit.||
|Test crew|Demographics of the test crew<br>(age, gender, etc.)<br>The manner in which the test crew<br>was assembled, to include<br>exclusions, volunteers etc., as well<br>as the degree to which the test<br>crew mirrored the target<br>population.<br>The level of training, instruction,<br>familiarisation, and habituation of<br>test crew in the use of the system.||



Federal Office for Information Security 

40 

6 Appendix: Minimal Information Requirements of a Testing Report 

|Test Details|Details to Report|Information|
|---|---|---|
|Test environment||Comparison trial data shall be collected under<br>environmental conditions that closely<br>approximate those of the target application. This<br>test environment shall be consistent throughout<br>the collection process. The motivation of test<br>subjects, and their level of training and familiarity<br>with the system, should also mirror that of the<br>target application. Non-mated comparison trials<br>shall be made under the same conditions as mated<br>comparison trials.<br>The collection process should ensure that<br>presentation effects and channel effects are either<br>uniform across all subjects or randomly varying<br>across subjects. If the effects are held uniformly<br>across subjects, then the same presentation and<br>channel controls in place during enrolment<br>should be in place for the collection of the test<br>data. Systematic variation of presentation and<br>channel effects between enrolment and test data<br>can lead to results distorted by these factors. If the<br>presentation and channel effects are allowed to<br>vary randomly across test subjects, the evaluator<br>should analyse results and report on any<br>correlation in these effects between enrolment<br>and comparison sessions.|
|Time separation<br>between enrolment<br>and recognition<br>transactions|||
|Quality and decision<br>thresholds used<br>during data collection|The thresholds used, and those<br>recommended for the target<br>application (if different).||
|Control of factors<br>potentially affecting<br>performance|||
|Test procedures|E.g., policies for determining<br>enrolment failures.<br>Details of any abnormal cases<br>occurring during testing that are<br>excluded from performance<br>analysis.||



Federal Office for Information Security 

41 

6 Appendix: Minimal Information Requirements of a Testing Report 

|Test Details|Details to Report|Information|
|---|---|---|
|Deviation from<br>guidelines|Deviations from the guidelines of<br>this document should be<br>explained. Sometimes it is<br>necessary to make a compromise<br>on one aspect to achieve another;<br>for example, randomizing the<br>order of using fingers on a<br>fingerprint device might lead to<br>user confusion and a higher<br>number of labelling errors.||
|Reporting<br>verification system<br>performance|FAR and corresponding FRR shall<br>be reported over the range of<br>decision thresholds tested. A<br>detection error trade-off<br>(DET)<br>plot is recommended in the case<br>of multiple operating points.|False Acceptance Rate (FAR) and False Rejection<br>Rate (FRR)|
|Reporting<br>verification system<br>resistance against<br>presentation attacks|Documentation SHALL be in a<br>manner that the testing procedure<br>can be reproduced by others with<br>comparable expertise. For higher<br>BALs than BAL 1, the attack<br>potential must be calculated<br>according to CEM [1] for each<br>successful PAI.||



Federal Office for Information Security 

42 

7 Bibliography 

## 7 Bibliography 

- [1] Common Switzerland, 2022. 

- [2] -03166: Technical Guideline for Biometric 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0043-04.png)


- [3] 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0043-06.png)


- [4] International Organization for Standar Biometric sample quality 


![](markdown/tr/BSI-TR-03166_Evaluation-Guidance/BSI-TR-03166_Evaluation-Guidance.pdf-0043-08.png)


- [5] -5:2019 Information technology Extensible biometric data interchange formats for Standardization, Geneva, Switzerland, 2019. 

- [6] Biometric performance testing and reporting Part 1: Standardization, Geneva, Switzerland, 2021. 

- [7] Biometric performance testing and reporting Part 2: Testing methodologi 

- [8] Biometric performance testing and reporting Standardization, Geneva, Switzerland, 2019. 

Federal Office for Information Security 

43 


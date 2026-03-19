## Standalone Schemata: TR-ESOR V 1.2.2 (+xmlmime) 

Datum: 04.07.2019 

Version: 1.2.2 

Status: Final 

## 1 Änderungen gegenüber TR-ESOR V 1.2 

Es haben sich folgende Änderungen am XML-Schema gegenüber der Version 1.2 der TR-ESOR ergeben: 

|**1**|**tr-esor-interfaces-v1.2.xsd**→**tr-esor-interfaces-v1.2+xmlmime.xsd**|
|---|---|
|||
|**2**|**tr-esor-S-4-v1.2.wsdl**→**tr-esor-S-4-v1.2+xmlmime.wsdl**|



**3 tr-esor-xaip-v1.2.xsd** → **tr-esor-xaip-v1.2+xmlmime.xsd** 


![](markdown/tr/BSI_TR_03125_Schemata-1_2_2/BSI_TR_03125_Schemata-1_2_2.pdf-0002-01.png)



![](markdown/tr/BSI_TR_03125_Schemata-1_2_2/BSI_TR_03125_Schemata-1_2_2.pdf-0003-00.png)


**3 tr-esor-xaip-v1.2-Profil_XBDP_v1.0.xsd: import aus tr-esor-xaip-v1.2+xmlmime.xsd** 


![](markdown/tr/BSI_TR_03125_Schemata-1_2_2/BSI_TR_03125_Schemata-1_2_2.pdf-0003-02.png)


|**4**|**Neue Datei …deps/xmlmime.xsd**|
|---|---|
|||
|**5**|**Type des Attributes „dataObjectID“ des Elements xaip:metaDataObject in der Datei tr-esor-xaip-v1.2+xmlmime.xsd**|




![](markdown/tr/BSI_TR_03125_Schemata-1_2_2/BSI_TR_03125_Schemata-1_2_2.pdf-0005-00.png)


## 2 Hinweis zum Punkt 5. 

Die Änderung des Typs des Attributes „dataObjectID“ von „xs:IDREF“ in „xs:IDREFS“ lässt die Gültigkeit der bereits bestehenden Instanzen von XAIP (bis die Version 1.2.1 von TR-ESOR) unberührt, daher wird als unkritisch angesehen. 


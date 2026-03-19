
![](markdown/tr/TLS-Checkliste/TLS-Checkliste.pdf-0001-00.png)


## TLS nach TR-03116-4 Checkliste für Diensteanbieter 

## **Stand 2023** 

**Datum:** 7. März 2023 

## 1 Einleitung 

Ziel dieser Checkliste ist es, Diensteanbieter bei der Konfiguration von TLS gemäß den Vorgaben und Empfehlungen der Technischen Richtlinie BSI TR-03116-4 zu unterstützen. Der Fokus liegt hierbei auf der Konfiguration von TLS 1.2 sowie der Verwendung korrekter TLS-Versionen und Cipher Suites gemäß TR-03116-4. 

Für eine erfolgreiche Prüfung müssen grundsätzlich alle Kriterien der Abschnitte 2.1-2.5 mit „Ja“ beantwortet werden. Die Erfüllung der Kriterien aus Abschnitt 2.6 wird von TR-03116-4 empfohlen. Für die Interoperabilität mit TR-konformen TLS-Clients sind hierbei insbesondere die mit '*' gekennzeichneten Punkte von besonderer Relevanz. Diese Checkliste dient lediglich zur Unterstützung, eine vollständige Konformität zur TR-03116-4 kann durch die erfolgreiche Abarbeitung nicht garantiert werden. 

Hilfe bei der Konfiguration können auch entsprechende Prüfwerkzeuge (z.B. tls-check.de, ssllabs.com oder entsprechende Prüfwerkzeuge anderer Hersteller) bieten. 

## 2 Checkliste 

## 2.1 Server Schlüssel 

|2.1|Server Schlüssel|||
|---|---|---|---|
|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**||
|||**_Ja_**|**_Nein_**|
|2.1.1*|Der Schlüssel im Server-Zertifkat entspricht den kryptographischen Mindestan-<br>forderungen:<br>**•**<br>RSA-Schlüssel:<br>**◦**<br>Mindestens 30721Bitlänge<br>**•**<br>ECDSA-Schlüssel:<br>**◦**<br>Es wird eine der folgenden Kurven verwendet:<br>**▪**<br>brainpoolP256r1|||



1 Bis Ende 2023 sind 2048 Bit übergangsweise noch zulässig. 

© 2023 Bundesamt für Sicherheit in der Informationstechnik 

1 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**|**_Erfüllt_**|
|---|---|---|---|
|||**_Ja_**|**_Nein_**|
||**▪**<br>brainpoolP384r1<br>**▪**<br>brainpoolP512r1<br>**▪**<br>secp256r1<br>**▪**<br>secp384r1<br>**▪**<br>secp521r1<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung aller Einträge „Key“ in „Server Key“ und „Addi-_<br>_tional Certifcates“._|||
|2.1.2*|Der Signaturalgorithmus des Server-Zertifkats entspricht den Anforderungen:<br>**•**<br>Signaturalgorithmus:<br>**◦**<br>RSA<br>**◦**<br>ECDSA<br>**•**<br>Hashfunktion:<br>**◦**<br>SHA-256<br>**◦**<br>SHA-384<br>**◦**<br>SHA-512<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung aller Einträge „Signature Algorithm“ in „Server_<br>_Key“ und „Additional Certifcates“._|||
|2.1.3|Das Server-Zertifkat enthält keine Wildcards.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass die URLs in „Subject“ und „Common Name“_<br>_und „Alternative Names“ kein „*“ enthalten._|||
|2.1.4*|Das  Server-Zertifkat  enthält  Information  zur  Rückrufprüfung,  d.h.  einen<br>„CRLDistributionPoint“ oder eine „AuthorityInfoAccess“ (bei der Verwendung ei-<br>nes qualifzierten Webseitenzertifkats bzw.  Extended-Validation-Zertifkats au-<br>tomatisch erfüllt).<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass das Feld „Revocation Information“ „CRL“_<br>_und/oder „OCSP“ enthält._|<br>||
|2.1.5*|Das Server-Zertifkat ist nicht gesperrt.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass das Feld „Revocation Status“ die Information_<br>_„not revoked“ enthält._|||
|2.1.6|Das Server-Zertifkat enthält eine „KeyUsage“-Extension. Folgende Bits sind ge-<br>setzt:<br>**•**<br>„digitalSignature“: JA<br>**•**<br>„keyCertSign“: NEIN (bei Verwendung eines qualifzierten Webseitenzer-<br>tifkats bzw. Extended-Validation-Zertifkats automatisch erfüllt)<br>**•**<br>„cRLSign“: NEIN (bei Verwendung eines qualifzierten Webseitenzertif-|||



© 2023 Bundesamt für Sicherheit in der Informationstechnik 

2 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**|**_Erfüllt_**|
|---|---|---|---|
|||**_Ja_**|**_Nein_**|
||kats bzw. Extended-Validation-Zertifkats automatisch erfüllt)<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (sonst): Prüfung des o.g. Sachverhaltes direkt im Zertifkat._|||
|2.1.7|Das Server-Zertifkat enthält eine „Extended Key Usage“-Extension mit dem Ein-<br>trag „id-kp-serverAuth“. (Bei Verwendung eines qualifzierten Webseitenzertif-<br>kats bzw. Extended-Validation-Zertifkats automatisch erfüllt.)<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (sonst): Prüfung des o.g. Sachverhaltes  direkt im Zertifkat._|||
|2.1.8*|Das Server-Zertifkat enthält alle (Sub-)Domain Namen, für die das Zertifkat ge-<br>nutzt wird.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass jeder (Sub-)Domain-Name für den das Zerti-_<br>_fkat genutzt und im Rahmen von TLS ausgeliefert wird, im Feld „Alternatitve_<br>_Names“ enthalten ist._|||



© 2023 Bundesamt für Sicherheit in der Informationstechnik 

3 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

## 2.2 Zertifikatskette 

|2.2|Zertifkatskette|||
|---|---|---|---|
|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**||
|||**_Ja_**|**_Nein_**|
|2.2.1*|Alle Schlüssel der CA-Zertifkate der gesamten Zertifkatskette entsprechen den<br>Anforderungen:<br>**•**<br>RSA-Schlüssel:<br>**◦**<br>Mindestens  30722Bitlänge<br>**•**<br>ECDSA-Schlüssel:<br>**◦**<br>Es wird eine der folgenden Kurven verwendet:<br>**▪**<br>brainpoolP256r1<br>**▪**<br>brainpoolP384r1<br>**▪**<br>brainpoolP512r1<br>**▪**<br>secp256r1<br>**▪**<br>secp384r1<br>**▪**<br>secp521r1<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass die Schlüssel in „Certifcation Paths“ den o.g._<br>_Anforderungen entsprechen._|<br>||
|2.2.2*|Die Signaturalgorithmen aller untergeordneten CA-Zertifkate der Kette (d.h. CA-<br>Zertifkate außer dem Root-Zertifkat) entsprechen den Anforderungen:<br>**•**<br>Signaturalgorithmus<br>**◦**<br>RSA<br>**◦**<br>ECDSA<br>**•**<br>Hashfunktion:<br>**◦**<br>SHA-256<br>**◦**<br>SHA-384<br>**◦**<br>SHA-512<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass alle Signaturalgorithmen in „Certifcation_<br>_Paths“ den o.g. Anforderungen entsprechen._|||
|2.2.3|Alle CA-Zertifkate der Zertifkatskette enthalten keine Wildcards im „Subject“<br>oder „SubjectAltName“.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (sonst): Prüfung des o.g. Sachverhaltes direkt in den CA-Zertifkaten_<br>_der Kette._|<br>||
|2.2.4*|Alle untergeordneten CA-Zertifkate der Zertifkatskette (d.h. CA-Zertifkate au-<br>ßer dem Root-Zertifkat) enthalten Information zur Rückrufprüfung („CRLDistri-<br>butionPoint“ oder „AuthorityInfoAccess“). (Bei Verwendung von qualifzierten<br>Webseitenzertifkaten  bzw. Extended-Validation-Zertifkaten  automatisch  er-<br>füllt.)<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_|||



2 Bis Ende 2023 sind 2048 Bit übergangsweise noch zulässig. 

© 2023 Bundesamt für Sicherheit in der Informationstechnik 

4 

## TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**|**_Erfüllt_**|
|---|---|---|---|
|||**_Ja_**|**_Nein_**|
||_Prüfanweisung (sonst): Prüfung des o.g. Sachverhaltes direkt allen untergeordneten_<br>_CA-Zertifkaten der Kette._|||
|2.2.5|Alle CA-Zertifkate enthalten eine als kritisch markierte „Basic Constraints“-Ex-<br>tension. (Bei Verwendung von qualifzierten Webseitenzertifkaten bzw.  Exten-<br>ded-Validation-Zertifkaten automatisch erfüllt.)<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (sonst): Prüfung des o.g. Sachverhaltes direkt in den CA-Zertifkaten_<br>_der Kette._|||
|2.2.6|Alle CA-Zertifkate enthalten eine als kritisch markierte „Key Usage“-Extension<br>mit den gesetzten Bits „keyCertSign“ und „cRLSign“. (Bei Verwendung von quali-<br>fzierten Webseitenzertifkaten bzw.  Extended-Validation-Zertifkaten automa-<br>tisch erfüllt.)<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (sonst): Prüfung des o.g. Sachverhaltes direkt in den CA-Zertifkaten_<br>_der Kette._|<br>||



© 2023 Bundesamt für Sicherheit in der Informationstechnik 

5 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

|2.3<br>TLS-Version und Cipher Suites|2.3<br>TLS-Version und Cipher Suites|||
|---|---|---|---|
|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**||
|||**_Ja_**|**_Nein_**|
|2.3.1|Die verpfichtend zu unterstützenden TLS-Versionen werden unterstützt:<br>**•**<br>TLS 1.2: JA<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass die verpfichtend zu unterstützenden TLS-_<br>_Versionen im Eintrag „Protocols“ enthalten sind._|||
|2.3.2*|Es werden nur erlaubte TLS-Versionen unterstützt:<br>**•**<br>TLS 1.3: JA<br>**•**<br>TLS 1.2: JA<br>**•**<br>TLS 1.1: NEIN<br>**•**<br>TLS 1.0: NEIN<br>**•**<br>SSL 3: NEIN<br>**•**<br>SSL 2: NEIN<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass nur erlaubte TLS-Versionen im Eintrag „Pro-_<br>_tocols“ enthalten sind._|||
|2.3.3*|Die verpfichtend zu unterstützenden  Cipher Suites für TLS 1.2 werden unter-<br>stützt.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass die verpfichtend zu unterstützenden Cipher_<br>_Suites aus Kapitel 3 (s.u.) im Feld „Cipher Suites“  für TLS 1.2 gelistet sind._|||
|2.3.4|Es werden nur erlaubte Cipher Suites für TLS 1.2 unterstützt.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass das Feld „Cipher Suites“ für TLS 1.2 keine_<br>_Cipher Suites enthält, die nicht in Kapitel 3 gelistet sind._|||
|2.3.5|Die Priorisierung der Cipher Suites für TLS 1.2 ist korrekt, d.h. Cipher Suites mit<br>größerem Prioritätswert gemäß den Tabellen aus Kapitel 3 werden mit höherer<br>Priorität eingesetzt.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass die Cipher Suites im Feld „Cipher Suites“ in_<br>_„Server-preferred Order“ gelistet sind und dass die Reihenfolge den Prioritäten aus_<br>_Kapitel 3 entspricht._|<br> <br> <br>||
|2.3.6|Es werden nur erlaubte Cipher Suites für TLS 1.3 unterstützt.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass das Feld „Cipher Suites“ für TLS 1.3 keine_<br>_Cipher Suites enthält, die nicht in Kapitel 3 gelistet sind._|||
|2.3.7|Es werden keine Cipher Suites für SSL2, SSL3, TLS 1.0 oder TLS 1.1 unterstützt.|||



© 2023 Bundesamt für Sicherheit in der Informationstechnik 

6 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**|**_Erfüllt_**|
|---|---|---|---|
|||**_Ja_**|**_Nein_**|
||_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass das Feld „Cipher Suites“ für SSL2, SSL3, TLS_<br>_1.0 oder TLS 1.1 keinerlei Cipher Suites enthält._|||



© 2023 Bundesamt für Sicherheit in der Informationstechnik 

7 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

## 2.4 Algorithmen und Parameter des Handshakes 

|2.4|Algorithmen und Parameter des Handshakes|||
|---|---|---|---|
|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**||
|||**_Ja_**|**_Nein_**|
|2.4.1*|Die verwendeten ephemeren Parameter während des TLS-Handshakes bieten<br>ausreichende Sicherheit:<br>**•**<br>ECDHE-Cipher Suites:<br>**▪**<br>brainpoolP256r1<br>**▪**<br>brainpoolP384r1<br>**▪**<br>brainpoolP512r1<br>**▪**<br>secp256r1<br>**▪**<br>secp384r1<br>**▪**<br>secp521r1<br>**•**<br>DHE-Cipher Suites:<br>**▪**<br>Mindestens 3072 Bit<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass die angezeigten Parameter zu DHE- bzw._<br>_ECDHE-Cipher Suites in Feld „Cipher Suites“ den o.g. Anforderungen entsprechen._|<br>||
|2.4.2*|Für die Erstellung und Verifkation von Signaturen während des TLS-Hand-<br>shakes werden folgende Algorithmen verwendet:<br>**•**<br>Signaturalgorithmus:<br>**◦**<br>RSA<br>**◦**<br>ECDSA<br>**•**<br>Hashfunktion:<br>**◦**<br>SHA-256<br>**◦**<br>SHA-384<br>**◦**<br>SHA-512<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (sonst): Prüfung der Konfgurationseinstellungen der TLS-Bibliothek._|||



© 2023 Bundesamt für Sicherheit in der Informationstechnik 

8 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

|2.5<br>Vorgaben zu weiteren Protokoll-Details|2.5<br>Vorgaben zu weiteren Protokoll-Details|||
|---|---|---|---|
|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**||
|||**_Ja_**|**_Nein_**|
|2.5.1|Client-initiierte Session Renegotiation wird nicht unterstützt.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs):Prüfung, dass „Secure Client-initiated Renegotiation“ und_<br>_„Insecure Client-initiated Renegotiation” auf „No“ stehen._|||
|2.5.2|TLS-Kompression wird nicht unterstützt.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass der Eintrag „SSL/TLS compression“ auf „No“_<br>_steht._|||
|2.5.3|Die Heartbeat-Extension wird nicht unterstützt.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass der Eintrag „Heartbeat“ auf „No“ steht._|||
|2.5.4|Die „truncated_hmac“-Extension wird nicht unterstützt.<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (sonst): Prüfung der Konfgurationseinstellungen der TLS-Bibliothek._|||



© 2023 Bundesamt für Sicherheit in der Informationstechnik 

9 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

|2.6<br>Weitere Empfehlungen (nicht verpfichtend)|2.6<br>Weitere Empfehlungen (nicht verpfichtend)|||
|---|---|---|---|
|**_Nr._**|**_Zu prüfende Anforderungen_**|**_Erfüllt_**||
|||**_Ja_**|**_Nein_**|
|2.6.1|Es  werden  nur Cipher  Suites mit  „Perfect  Forward  Secrecy“  unterstützt  (nur<br>Cipher Suites, die mit „TLS_ECDHE“ oder „TLS_DHE“ beginnen) (EMPFOHLEN).<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass im Feld „Cipher Suites“ nur Cipher Suites ent-_<br>_halten sind, die den o.g. Anforderungen entsprechen._|||
|2.6.2|Die „Encrypt-then-MAC“-Extension wird unterstützt (EMPFOHLEN).<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (sonst): Prüfung der Konfgurationseinstellungen der TLS-Bibliothek_|||
|2.6.3|OCSP-Stapling wird unterstützt (EMPFOHLEN).<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass der Eintrag „OCSP stapling“ auf „Yes“ steht._|||
|2.6.4|Die „Extended-Master-Secret-Extension“ wird unterstützt (EMPFOHLEN).<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (sonst): Prüfung der Konfgurationseinstellungen der TLS-Bibliothek_|||
|2.6.5|Das Server-Zertifkat ist ein qualifziertes Webseiten-Zertifkat gemäß eIDAS-VO<br>oder ein Extended-Validation-Zertifkat (EMPFOHLEN).<br>_Prüfanweisung (tls-check): Prüfung des Kriteriums in der Checklisten-Ansicht_<br>_Prüfanweisung (ssllabs): Prüfung, dass der Eintrag „Extended Validation“ „Yes“ ent-_<br>_hält._|||



© 2023 Bundesamt für Sicherheit in der Informationstechnik 

10 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

## 3 Cipher Suites 

## 3.1 Cipher Suites für TLS 1.2 

|3.1<br>Cipher Suites für TLS 1.2|||
|---|---|---|
|**_Cipher Suites_**|**_Unterstützung_**|**_Priorität3_**|
|**Server mit EC-Public Key**|||
|`TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`|MUSS|2|
|`TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`|MUSS|2|
|`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`|EMPFOHLEN|2|
|`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`|EMPFOHLEN|2|
|`TLS_ECDHE_ECDSA_WITH_AES_128_CCM`|EMPFOHLEN|2|
|`TLS_ECDHE_ECDSA_WITH_AES_256_CCM`|EMPFOHLEN|2|
|**Server mit RSA-Public Key**|||
|`TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`|MUSS|2|
|`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`|MUSS|2|
|`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`|EMPFOHLEN|2|
|`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`|EMPFOHLEN|2|
|`TLS_DHE_RSA_WITH_AES_128_CBC_SHA256`|OPTIONAL|1|
|`TLS_DHE_RSA_WITH_AES_256_CBC_SHA256`|OPTIONAL|1|
|`TLS_DHE_RSA_WITH_AES_128_GCM_SHA256`|OPTIONAL|1|
|`TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`|OPTIONAL|1|
|`TLS_DHE_RSA_WITH_AES_128_CCM`|OPTIONAL|1|
|`TLS_DHE_RSA_WITH_AES_256_CCM`|OPTIONAL|1|
|Weitere Hinweise4|||



- 3 Ein größerer Prioritätswert impliziert eine höhere Priorität. 

- 4 Sofern mit TLS keine personenbezogenen Daten verarbeitet werden, ist prinzipiell auch möglich, zusätzlich Cipher Suites der Form TLS_ECDH_ECDSA*, TLS_DH_DSS_*, TLS_DH_RSA_* oder TLS_DH_RSA* zu unterstützen. Dies wird aber nicht empfohlen. Im Falle der Unterstützung sind diese Cipher Suites mit geringster Priorität zu verwenden, da sie keine Perfect Forward Secrecy bieten. Zudem sollten hierfür separate Schlüsselpaare und Zertifikate verwendet werden. 

© 2023 Bundesamt für Sicherheit in der Informationstechnik 

11 

TLS nach TR-03116-4 – Checkliste für Diensteanbieter 

## 3.2 Cipher Suites für TLS 1.3 

|3.2<br>Cipher Suites für TLS 1.3|||
|---|---|---|
|**_Cipher Suites_**|**_Unterstützung_**|**_Priorität3_**|
|`TLS_AES_128_GCM_SHA256`|EMPFOHLEN|1|
|`TLS_AES_256_GCM_SHA384`|EMPFOHLEN|1|
|`TLS_AES_128_CCM_SHA256`|EMPFOHLEN|1|



© 2023 Bundesamt für Sicherheit in der Informationstechnik 

12 


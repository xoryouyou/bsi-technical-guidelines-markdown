
![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0001-00.png)



![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0001-01.png)


## **Technical Guideline TR-03111** 

## **Elliptic Curve Cryptography** 

Version 2.0 

## **History** 

|**History**|||
|---|---|---|
|**Version**|**Date**|**Comment**|
|1.00|2007-02-14|Initial public version.|
|1.10|2009-02-03|Enhancements, corrections, and clarifcations.|
|1.11|2009-04-17|Bug fxes.|
|2.00|2012-06-28|Extension by further algorithms and protocols, corrections and updates.|



Bundesamt f¨ur Sicherheit in der Informationstechnik Postfach 20 03 63, 53133 Bonn, Germany Email: `EllipticCurveCrypto@bsi.bund.de` Internet: `http://www.bsi.bund.de` _⃝_ c Bundesamt f¨ur Sicherheit in der Informationstechnik 2012 

Technical Guideline - Elliptic Curve Cryptography 

## **Contents** 

|**1. **|**Introduction**|**Introduction**|**7**|
|---|---|---|---|
||1.1. Patents and side-channel attacks . . . . . . . . . . . . . . . . . . . . . . . . . . .||7|
||1.2. Standards . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||7|
||1.3. Symbols and Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||8|
||1.4. Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||9|
|**2. **|**Mathematical Foundations**||**10**|
||2.1. Modular Arithmetic<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||10|
||2.2. Groups|and Finite Fields<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
||2.2.1.|Groups<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
||2.2.2.|Group Order and Generators . . . . . . . . . . . . . . . . . . . . . . . . .|11|
||2.2.3.|Subgroups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
||2.2.4.|Finite Fields<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
||2.2.5.|The Discrete Logarithm Problem (DLP) . . . . . . . . . . . . . . . . . . .|12|
||2.3. Elliptic|Curves over prime felds . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
||2.3.1.|Elliptic Curve Groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
||2.3.2.|Elliptic Curve Domain Parameters . . . . . . . . . . . . . . . . . . . . . .|13|
||2.3.3.|Elliptic Curve Discrete Logarithm Problem . . . . . . . . . . . . . . . . .|14|
||2.3.4.|Cryptographically Strong EC Domain Parameters over F_p_ . . . . . . . . .|14|
|**3. **|**Data Types and Data Conversion**||**16**|
||3.1. Conversion Routines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||16|
||3.1.1.|Conversion between Bit Strings and Octet Strings<br>. . . . . . . . . . . . .|16|
||3.1.2.|Conversion between Integers and Octet Strings . . . . . . . . . . . . . . .|17|
||3.1.3.|Conversion between Field Elements and Octet Strings . . . . . . . . . . .|18|
||3.2. Encoding Elliptic Curve Points . . . . . . . . . . . . . . . . . . . . . . . . . . . .||18|
||3.2.1.|Uncompressed Encoding . . . . . . . . . . . . . . . . . . . . . . . . . . . .|18|
||3.2.2.|Compressed Encoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|
|**4. **|**Elliptic Curve Cryptography Algorithms**||**20**|
||4.1. Auxiliary Functions and Algorithms<br>. . . . . . . . . . . . . . . . . . . . . . . . .||20|
||4.1.1.|Random and Pseudo-Random Number Generators . . . . . . . . . . . . .|20|
||4.1.2.|Cryptographically Strong Hash Functions . . . . . . . . . . . . . . . . . .|21|
||4.1.3.|Elliptic Curve Key Pair Generation – ECKeyPair . . . . . . . . . . . . . .|22|
||4.2. Elliptic|Curve Based Signature Algorithms<br>. . . . . . . . . . . . . . . . . . . . .|22|
||4.2.1.|The Elliptic Curve Digital Signature Algorithm – ECDSA . . . . . . . . .|22|
|||4.2.1.1.<br>Signature Algorithm . . . . . . . . . . . . . . . . . . . . . . . . .|22|
|||4.2.1.2.<br>Verifcation Algorithm . . . . . . . . . . . . . . . . . . . . . . . .|23|
||4.2.2.|The Elliptic Curve German Digital Signature Algorithm - ECGDSA . . .|23|
|||4.2.2.1.<br>Signature Algorithm . . . . . . . . . . . . . . . . . . . . . . . . .|23|
|||4.2.2.2.<br>Verifcation Algorithm . . . . . . . . . . . . . . . . . . . . . . . .|24|
||4.2.3.|The Elliptic Curve Based Schnorr Signature Algorithm - EC-Schnorr . . .|24|
|||4.2.3.1.<br>Signature Algorithm . . . . . . . . . . . . . . . . . . . . . . . . .|24|
|||4.2.3.2.<br>Verifcation Algorithm . . . . . . . . . . . . . . . . . . . . . . . .|25|



Federal Office for Information Security 

3 

Technical Guideline - Elliptic Curve Cryptography 

|4.3.|The Elliptic Curve Key Agreement Algorithm – ECKA<br>. . . . . . . . . . . . . .|The Elliptic Curve Key Agreement Algorithm – ECKA<br>. . . . . . . . . . . . . .|The Elliptic Curve Key Agreement Algorithm – ECKA<br>. . . . . . . . . . . . . .|25|
|---|---|---|---|---|
||4.3.1.|Key Agreement Algorithm|. . . . . . . . . . . . . . . . . . . . . . . . . . .|26|
||4.3.2.|The Key Agreement Protocols ECKA-DH and ECKA-EG . . . . . . . . .||26|
|||4.3.2.1.<br>Anonymous Dife-Hellman Key Agreement (ECKA-DH). . . . .||26|
|||4.3.2.2.<br>ElGamal Key Agreement (ECKA-EG). . . . . . . . . . . . . . .||26|
||4.3.3.|Key Derivation Functions|. . . . . . . . . . . . . . . . . . . . . . . . . . .|27|
|||4.3.3.1.<br>Key Derivation for DES.<br>. . . . . . . . . . . . . . . . . . . . . .||28|
|||4.3.3.2.<br>Key Derivation for AES.<br>. . . . . . . . . . . . . . . . . . . . . .||28|
|4.4.|The Password Authenticated Connection Establishment – PACE . . . . . . . . .|||28|
||4.4.1.|The Generic Mapping – GMap() . . . . . . . . . . . . . . . . . . . . . . .||29|
|**5. Input and **||**Output Formats**||**30**|
|5.1.|Public|Key Format . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|30|
||5.1.1.|X9.62 Format . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|30|
||5.1.2.|ISO 7816 Format . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|32|
|5.2.|Signature Format . . . . . . . . .||. . . . . . . . . . . . . . . . . . . . . . . . . . .|32|
||5.2.1.|Plain Format . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|33|
|||5.2.1.1.<br>ECDSA . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|33|
|||5.2.1.2.<br>ECGDSA . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|33|
|||5.2.1.3.<br>EC-Schnorr . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|33|
||5.2.2.|X9.62 Format . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|33|
|5.3.|Key Agreement . . . . . . . . . .||. . . . . . . . . . . . . . . . . . . . . . . . . . .|34|
||5.3.1.|ElGamal Key Agreement|. . . . . . . . . . . . . . . . . . . . . . . . . . .|34|
|||5.3.1.1.<br>Message Format|. . . . . . . . . . . . . . . . . . . . . . . . . . .|34|
|||5.3.1.2.<br>Authentication .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|35|
|||5.3.1.3.<br>Encryption . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|35|
||5.3.2.|Anonymous Dife-Hellman|Key Agreement . . . . . . . . . . . . . . . . .|35|
|5.4.|PACE|. . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|35|
||5.4.1.|PACE on Smartcards<br>. .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|36|
|**6. Standardized Domain Parameters**||||**37**|
|**Appendix**||||**39**|
|A.|The Signature Algorithm – EC-KCDSA (Informative) . . . . . . . . . . . . . . .|||39|
||A.1.|Signature Algorithm . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|39|
||A.2.|Verifcation Algorithm . .|. . . . . . . . . . . . . . . . . . . . . . . . . . .|39|



Federal Office for Information Security 

4 

Technical Guideline - Elliptic Curve Cryptography 

## **List of Figures** 

2.1. Operations on an elliptic curve _E_ (R). . . . . . . . . . . . . . . . . . . . . . . . . 14 

Federal Office for Information Security 

5 

Technical Guideline - Elliptic Curve Cryptography 

## **List of Tables** 

|1.1.|Symbols and abbreviations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|9|
|---|---|---|
|2.1.|Elliptic curve domain parameters over F_p_. . . . . . . . . . . . . . . . . . . . . . .|14|
|3.1.|Conversion routines for data types used in this guideline.<br>. . . . . . . . . . . . .|16|
|4.1.|Supported hash functions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
|4.2.|ECKA-DH. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|26|
|4.3.|ECKA-EG. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|27|
|4.4.|PACE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|29|
|4.5.|Generic Mapping. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|29|
|5.1.|Tags for elliptic curve public keys and domain parameters over F_p_. . . . . . . . .|32|
|5.2.|Tags for messages protected by ECKA-EG. . . . . . . . . . . . . . . . . . . . . .|35|



Federal Office for Information Security 

6 

Technical Guideline - Elliptic Curve Cryptography 

## **1. Introduction** 

Elliptic curve cryptography (ECC) is a very efficient technology to realise public key cryptosystems and public key infrastructures (PKI). The security of a public key system using elliptic curves is based on the difficulty of computing discrete logarithms in the group of points on an elliptic curve defined over a finite field. The elliptic curve discrete logarithm problem (ECDLP), described in Section 2.3.3, is currently believed to be asymptotically harder than the factorization of integers or the computation of discrete logarithms in the multiplicative group of a finite field (DLP), described in Section 2.2.5. As a matter of fact key sizes of cryptosystems based on elliptic curves are short compared to cryptosystems based on integer factorization at the same level of security. 

The aim of this technical guideline is to facilitate the application of elliptic curve cryptography by giving recommendations on the secure deployment of elliptic curve cryptography in commercial applications. For that purpose, this guideline compiles 

- mathematical foundations of elliptic curves and 

- algorithms based on elliptic curves in one document. 

Furthermore, this guideline sets requirements on the suitable deployment of ECC in the context of official German documents. 

The algorithms described here are the elliptic curve based signature algorithms ECDSA, ECGDSA, EC-Schnorr and EC-KCDSA for generating and verifying digital signatures, the Elliptic Curve Key Agreement Algorithm (ECKA) for key establishment and the Password Authenticated Connection Establishment (PACE). 

The requirements that must be fulfilled by qualified electronic signatures according to the German signature law (cf. [14]) may differ in some details. The deployment of ECC to classified information is not in the scope of this guideline. 

## **1.1. Patents and side-channel attacks** 

In implementations, patents and side-channel attacks play an important role. 

The algorithms described in this guideline have been carefully selected to allow patent-free and/or license-free implementations. Nevertheless, some of the described algorithms or its particular implementations may be subject of patent rights. The BSI shall not be held responsible for identifying any or all such patent rights. 

Implementors and security evaluators shall also pay attention to [6], which gives a general guidance to assess the side-channel resistance of implementations on smartcards. 

## **1.2. Standards** 

This document refers to a number of international standards related to elliptic curve cryptography. Many national and international organizations have standardized the use of elliptic curves in cryptography. The most important organizations and the corresponding standards are: 

1. The International Organization for Standardization (ISO) has issued the following relevant standards: 

Federal Office for Information Security 

7 

Technical Guideline - Elliptic Curve Cryptography 

   - ISO 15946 [24] ( _Information technology – Security techniques – Cryptographic techniques based on elliptic curves_ )[1] 

      - Part 1 ( _General_ ) [22] 

   - ISO 14888 ( _Information technology – Security techniques – Digital signatures with appendix_ ) 

      - Part 3, including Amendment 1 ( _Discrete logarithm based techniques_ ) [20], [21] 

   - ISO 11770 ( _Information technology – Security techniques – Key Management_ ) 

      - Part 3 ( _Mechanisms using asymmetric techniques_ ) [19] 

2. The American National Standards Institute (ANSI) has standardized protocols for digital signatures and for key agreement. The following standards are relevant: 

   - X9.62 ( _Public Key Cryptography For The Financial Services Industry – The Elliptic Curve Digital Signature Algorithm (ECDSA))_ [4]. 

   - X9.63 ( _Public Key Cryptography For The Financial Services Industry – Key Agreement and Key Transport Using Elliptic Curve Cryptography_ ) [5]. 

3. The Institute of Electrical and Electronics Engineers (IEEE) has issued the standard P1363 ( _Standard Specifications for Public Key Cryptography_ ) [15] and its amendment P1363a [16]. The standards describe commonly used cryptosystems like RSA, DSA, and cryptosystems based on elliptic curves. 

4. The IETF published in RFC 5639 ( _Elliptic Curve Cryptography (ECC) Brainpool Standard Curves and Curve Generation_ ) [32] an set of domain parameters defining cryptographically strong groups on elliptic curves. 

## **1.3. Symbols and Abbreviations** 

The following notations and abbreviations are used in this document: 

|**Symbol**|**Comments**|
|---|---|
|N|The set of all natural numbers (without 0).|
|Z|The set of all integers.|
|Z_m_|The set of all integers modulo _m_.|
|_p_|A prime number.|
|F_p_|The fnite feld of _p_ elements.|
|F2_m_|The fnite feld of 2_m_ elements, with _m ∈_N.|
|_E_|An elliptic curve defned by a Weierstraß equation. If _E_ is<br>defned over a fnite feld of characteristic _p >_ 3, then the<br>Weierstraß equation is of the form<br>_y_2 =_x_3 +_ax_+_b,_<br>_a, b ∈_F_p ,_4_a_3 + 27_b_2 = 0_._<br>(1.1)<br>Essentially, this technical guideline considers elliptic curves<br>over prime felds of characteristic _p >_3.|
|continued on next page||



> 1Notice that parts of the ISO-standard 15946 are no longer relevant since they were replaced by other standards. _Part 2-Digital signatures_ [23] has been withdrawn as the content was incorporated into ISO 14888-3, and _Part 3-Key establishment_ [24] has been withdrawn since the information was incorporated into ISO 11770-3. 

Federal Office for Information Security 

8 

Technical Guideline - Elliptic Curve Cryptography 

|continued from page 8|continued from page 8|
|---|---|
|**Symbol**|**Comments**|
|_E_(F_p_)|An elliptic curve group over the feld F_p_ consisting of all<br>points (_x, y_) _∈_F2<br>_p_ solving the Weierstraß equation of _E_ to-<br>gether with the point at infnity _O_.|
|#_E_(F_p_)|The order (or cardinality) of the group _E_(F_p_).|
|_O_|The point at infnity. It is the identity element of the group<br>_E_(F_p_) and can not be described in afne coordinates.|
|_P_, _Q_|Points on the elliptic curve _E_(F_p_).|
|_xP_, _yP_|The _x_- and _y_-coordinates of _P_ in afne representation, if _P_<br>is diferent from _O_ .|
|_P_ + _Q_|The sum of two points _P_ and _Q_ in _E_(F_p_).|
|[_k_]_P_|The_k_-th multiple of a point_P ∈E_(F_p_), i.e. [_k_]_P_ =_P_+_P_+<br>_· · ·_+_P_, _k_ addends.|
|_G_|The base point is a generator of a subgroup of _E_(F_p_).|
|_n_|The order of the base point_G_. Typically, _n_is a prime of bit<br>length _≥_224.|
|A|The sender of a cryptographic message.|
|B|The receiver of a cryptographic message.|
|_d_A|The private key of entity A. This is an integer in the set<br>_{_1_, . . ., n −_1_}_.|
|_P_A|The public key of entity A. This is a point on _E_(F_p_). The<br>relation between _d_A and _P_A is given by the equation _P_A =<br>[_d_A]_G_ except for the signature schemes ECGDSA and EC-<br>KCDSA, where the relation is _P ′_<br>A =[_d−_1<br>A<br>mod _n_]_G_.|
|�<br>_P_A|An ephemeral public key of entity A.|
|H(_M_)|Hash value (digest) of the message _M_.|
|H_l_(_M_)|Truncated hash value of the message _M_. The hash value is<br>cropped to the _l_ leftmost bits of H(_M_).|
|_ℓ_|Bit length of the output of a hash function.|
|_κ_|Bit length of a symmetric key or key stream.|
|_τ_|Bit length of the order of the base point, i.e. _τ_ = _⌈_log2 _n⌉_.|
|_R ⊕S_|Bitwise sum of two octet or bit strings _R_, _S_.|



Table 1.1.: Symbols and abbreviations. 

## **1.4. Terminology** 

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119 [10]. 

Federal Office for Information Security 

9 

Technical Guideline - Elliptic Curve Cryptography 

## **2. Mathematical Foundations** 

This section introduces the mathematical foundations required to understand elliptic curve cryptography: First an overview on modular arithmetic is given in Section 2.1. Then the basic properties of groups and finite fields are introduced in Section 2.2. Finally, elliptic curves over finite fields F _p_ are described in Section 2.3. 

## **2.1. Modular Arithmetic** 

The following description is based on P1363 [15]. However, this guideline makes use of a slightly notation. 

Modular arithmetic fixes an integer _m >_ 1 called the _modulus_ . The fundamental operation in the context of modular arithmetic is the reduction modulo _m_ . Given an integer _a_ , one divides _a_ by _m_ and takes the remainder _r_ as the result of the reduction. Therefore, _r_ is in the range 0 _≤ r ≤ m −_ 1. The operation is written as 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0010-06.png)


Let _a_ and _b_ be two integers with remainders _r_ 1 and _r_ 2, respectively. Then _a_ and _b_ are said to be _congruent_ modulo _m_ , if and only if _r_ 1 = _r_ 2. This relationship is written as _a ≡ b_ mod _m_ . The following two properties of congruences can easily be seen: 

1. Integers _a_ and _b_ are congruent modulo _m_ if and only if _b − a_ is divisible by _m_ . 

2. If _r_ = _a_ mod _m_ then _r ≡ a_ mod _m_ . 

The integers modulo _m_ are the possible remainders modulo _m_ . They are denoted by Z _m_ . Thus the set of integers modulo _m_ is 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0010-11.png)


Next, we enumerate properties of addition, subtraction, multiplication, and division in Z _m_ . Let _a_ 0 _, b_ 0 _, a_ 1 _, b_ 1 be integers with _a_ 0 _≡ b_ 0 mod _m_ and _a_ 1 _≡ b_ 1 mod _m_ . Thus, _a_ 0 mod _m_ and _b_ 0 mod _m_ represent the same element in _Zm_ . The same holds for _a_ 1 and _b_ 1. 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0010-13.png)


Equation (2.2) shows that the order of adding and reducing modulo _m_ may be exchanged. Equations (2.3) and (2.4) show the same property for subtraction and multiplication modulo _m_ , respectively. 

Typically, one performs addition, subtraction, and multiplication in Z _m_ by performing the corresponding integer operation and reducing the result modulo _m_ . Then, all computations take place in the set _{_ 0 _,_ 1 _, . . . ,_ ( _m −_ 1)[2] _}_ , i.e. the largest number appearing in an intermediate result before reduction is ( _m −_ 1)[2] . 

Federal Office for Information Security 

10 

Technical Guideline - Elliptic Curve Cryptography 

## **2.2. Groups and Finite Fields** 

## **2.2.1. Groups** 

A _group_ (G _, ◦_ ) is a set G with a binary operation _◦_ : G _×_ G _→_ G such that the following four axioms are 

**Associativity:** For all _a, b, c ∈_ G the equation ( _a ◦ b_ ) _◦ c_ = _a ◦_ ( _b ◦ c_ ) holds. 

- **Identity element:** There is an element _e ∈_ G such that for all _a ∈_ G the equation _e◦a_ = _a◦e_ = _a_ holds. 

- **Inverse element:** For each _a ∈_ G there exists an element _b ∈_ G such that _a ◦ b_ = _b ◦ a_ = _e_ . 

It is easy to see that for a group the identity element _e_ is unique – and so is the inverse for each element of the group. 

- If (G _, ◦_ ) is a group, then _◦_ is called the _group law_ . Often a group satisfies _a ◦ b_ = _b ◦ a_ for all 

- _a, b ∈_ G. Then G is said to be _commutative_ or _Abelian_ . 

   - In practice, the group law is commonly written as an addition or a multiplication: 

**Additive Notation.** The identity is denoted by 0. If _g_ is an element of G, the inverse element is denoted by _−g_ . We define [ _k_ ] _g_ =[�] _[k]_ 1 _[g]_[,] _[k][∈]_[N][,][as][the][sum][of] _[k]_[times][the][element] _[g]_[.] 

**Multiplicative Notation.** The identity is denoted by 1. If _g_ is an element of G, the inverse element is denoted by _g[−]_[1] . We define _g[k]_ =[�] _[k]_ 1 _[g]_[,] _[k][∈]_[N][,][as][the][product][of] _[k]_[times][the][element] _g_ . 

## **2.2.2. Group Order and Generators** 

Let G be a finite group, i.e. G contains _n_ elements, _n ∈_ N. The number _n_ is called the _group order_ and #G = _n_ . As G is finite, for every _g ∈_ G an integer _s_ with 1 _≤ s ≤ n_ exists such that [ _s_ ] _g_ = 0. The smallest such number is written as # _g_ , called the _order_ of _g_ in G. If _s_ denotes the order of _g_ in G, then the following properties hold: 

1. The order of the group is a multiple of the order of all its elements, i.e. _s_ divides _n_ . 

2. For _g_ = 1, the representation [ _k_ ] _g_ is unique, i.e. [ _k_ 1] _g_ = [ _k_ 2] _g_ if and only if _k_ 1 _≡ k_ 2 mod _s_ . 

A finite group (G _,_ +) of order _n_ is called _cyclic_ , if there is a group element _g ∈_ G with 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0011-17.png)


In this case, the element _g_ is called a _generator_ of (G _,_ +). 

## **2.2.3. Subgroups** 

Let (G _,_ +) be a finite group. A non-empty subset S _⊆_ G is called a _subgroup_ , if for any two elements _a, b ∈_ S it holds that _a − b ∈_ S. Due to Lagrange’s theorem, #S is a divisor of #G . For every _a ∈_ G the set 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0011-21.png)


is a cyclic subgroup of G _._ 

Federal Office for Information Security 

11 

Technical Guideline - Elliptic Curve Cryptography 

## **2.2.4. Finite Fields** 

A field ( _F,_ + _, ·_ ) is a set _F_ together with two operations + and _·_ such that 

1. + : _F × F → F_ and _·_ : _F × F → F_ , 

2. ( _F,_ +) is an Abelian group, 

3. ( _F \ {_ 0 _}, ·_ ) is an Abelian group, 

4. ( _a_ + _b_ ) _· c_ = _a · c_ + _b · c_ holds for all _a, b, c ∈ F_ . 

A finite field is a field with finitely many elements. It is a fundamental theorem of the theory of finite fields that a finite field of _q_ elements exists if and only if _q_ is a prime power, i.e. _q_ = _p[m]_ where _p_ is a prime and _m_ is an integer with _m ≥_ 1. In addition, for a given prime power _q_ there exists up to isomorphism only one finite field consisting of _q_ elements. In the following, this field is denoted by _GF_ ( _q_ ) or F _q_ . 

As of today, two families of finite fields are used for elliptic curve cryptography in practice: 

- **Prime fields:** Finite fields F _p_ of _p_ elements with _p_ prime. In this case F _p_ is isomorphic to (Z _p,_ + _, ·_ ) (cf. Section 2.1), therefore in this Technical Guideline elements of F _p_ will be regarded as integers in _{_ 0 _,_ 1 _, . . . , p −_ 1 _}_ . 

**Extension fields of characteristic 2:** Finite fields F2 _[m]_ of 2 _[m]_ elements. 

In this technical guideline, we focus mainly on elliptic curve cryptography over prime fields. 

## **2.2.5. The Discrete Logarithm Problem (DLP)** 

The _discrete logarithm problem_ (DLP) is defined as follows: Let G be a cyclic group of order _n_ with generator _g_ . The discrete logarithm of _h ∈_ G to the base _g_ , denoted by log _g h_ , is the unique integer _k_ , 0 _≤ k ≤ n −_ 1, such that [ _k_ ] _g_ = _h_ . 

Given _g_ and _h_ , the discrete logarithm problem is to find _k_ , which is assumed to be computationally intractable for the relevant groups in ECC for large _n_ (cf. Section 2.3.3). 

## **2.3. Elliptic Curves over prime fields** 

According to this guideline, it is RECOMMENDED to use elliptic curves over prime fields F _p_ where _p ≡_ 3 mod 4 (cf. Section 3.2.2). 

The security of elliptic curve cryptography is based on the hardness of the elliptic curve discrete logarithm problem (cf. Section 2.3.3). 

## **2.3.1. Elliptic Curve Groups** 

We introduce the basic facts of elliptic curves over a finite field F _p_ . Let _E_ be an elliptic curve over F _p_ . In this section it is assumed, that _p_ = 2 _,_ 3. Then _E_ may be described in terms of the Weierstraß equation 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0012-20.png)


The requirement 4 _a_[3] + 27 _b_[2] = 0 ensures that _E_ is non-singular, this means in particular that one may compute the tangent in every point on the curve. 

Several different representations for elliptic curves exist. Within this guideline only the _affine representation_ (cf. Equation (2.5)) is used. 

Federal Office for Information Security 

12 

Technical Guideline - Elliptic Curve Cryptography 

The set of _rational points_ in _E_ over F _p_ denoted by _E_ (F _p_ ) is 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0013-02.png)


where _O_ is the point at infinity. It is the projective closure of the equation _y_[2] = _x_[3] + _ax_ + _b_ and may not be described in terms of two coordinates in F _p_ . 

_E_ (F _p_ ) carries a group structure with the point at infinity acting as the identity element. The binary operation of rational points in _E_ (F _p_ ) is commonly denoted as an addition. It turns out that the addition of points in _E_ (F _p_ ) has a simple geometric interpretation, as shown in Figure 2.1, visualizing the operations on a elliptic curve defined over R. 

Let _P ∈ E_ (F _p_ ) and _Q ∈ E_ (F _p_ ) be points on the elliptic curve. The addition law uses the _chord-tangent process_ where the following different cases have to be distinguished: 

1. Let _P_ + _O_ = _O_ + _P_ = _P_ for all _P ∈ E_ (F _p_ ). Thus _O_ acts as the identity element in the group _E_ (F _p_ ). 

2. Let _P_ = _O_ and _P_ = ( _xP , yP_ ). The point ( _xP , −yP_ ) is an element of _E_ (F _p_ ) _\ {O}_ and one defines _−P_ = ( _xP , −yP_ ) _._ Additionally, one sets _−O_ = _O_ . The identity _P_ + ( _−P_ ) = _O_ holds for all _P ∈ E_ (F _p_ ). 

3. Let _P_ = _O_ , and _Q_ = _O_ such that _P_ = _±Q_ , i.e. _P_ and _Q_ have different _x_ -coordinates. The line through _P_ and _Q_ intersects _E_ (F _p_ ) in a third point _R ∈ E_ (F _p_ ) _\ {O}._ One sets _P_ + _Q_ = _−R._ 

This definition leads to the following addition rule: Set _λ_ = ( _yQ − yP_ ) _/_ ( _xQ − xP_ ) and _P_ + _Q_ = ( _xR, yR_ ) (the denominator is different from zero, as _xP_ = _xQ_ ). Then _xR_ and _yR_ may be computed by the formulae 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0013-10.png)


4. Let _P_ = _O_ , _P_ = _−P_ . The tangent to _E_ (F _p_ ) in _P_ intersects _E_ (F _p_ ) in _R ∈ E_ (F _p_ ) _\ {O}_ , and we set [2] _P_ = _−R._ 

This description leads to the following doubling rule: Set _λ_ = (3 _x_[2] _P_[+] _[ a]_[)] _[/]_[(2] _[y][P]_[ )][and][[2]] _[P]_[=] ( _xR, yR_ ). Then _xR_ and _yR_ may be computed by the formulae 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0013-13.png)


The chord-tangent process for an elliptic curve over real numbers is shown in Figure 2.1. With the definitions above ( _E_ (F _p_ ) _,_ +) is an Abelian group. 

The order of _E_ (F _p_ ) may be estimated due to a theorem of Hasse: 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0013-16.png)


Hasse’s theorem shows # _E_ (F _p_ ) _≈ p_ , i.e. _p_ and # _E_ (F _p_ ) are of same order of magnitude. 

## **2.3.2. Elliptic Curve Domain Parameters** 

Elliptic curve domain parameters yield a set of information for communicating parties to identify a certain elliptic curve group for use in cryptography. The domain parameters comprise the finite field F _p_ , the coefficients _a_ and _b_ of the Weierstraß equation, a base point _G ∈ E_ (F _p_ ), its order _n_ , and finally the cofactor _h_ =[#] _[E] n_[(][F] _[p]_[)] . The base point _G_ generates a cyclic subgroup of order _n_ in _E_ (F _p_ ) denoted by _⟨G⟩_ , i.e.: 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0013-20.png)


Table 2.1 summarizes the domain parameters of an elliptic curve defined over F _p_ with _p >_ 3. 

Federal Office for Information Security 

13 

Technical Guideline - Elliptic Curve Cryptography 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0014-01.png)


**----- Start of picture text -----**<br>
 30<br>2 P<br> 20<br> 10 − ( P +  Q )<br>Q<br> 0<br>P<br>P +  Q<br>−10<br>−20<br>− 2 P<br>−30<br>−10 −5  0  5  10<br>**----- End of picture text -----**<br>


Figure 2.1.: Operations on an elliptic curve _E_ (R). 

|**Parameter**|**Comment**|
|---|---|
|_p_|A prime number specifying the underlying feld F_p_.|
|_a_|The frst coefcient of the Weierstraß equation _E_.|
|_b_|The second coefcient of the Weierstraß equation _E_.|
|_G_|A base point in _E_(F_p_).|
|_n_|The order of _G_ in _E_(F_p_).|
|_h_|The cofactor of _G_ in _E_(F_p_).|



Table 2.1.: Elliptic curve domain parameters over F _p_ . 

## **2.3.3. Elliptic Curve Discrete Logarithm Problem** 

The _elliptic curve discrete logarithm problem_ (ECDLP) is defined as follows: Given the elliptic curve domain parameters as described above and a point _P ∈⟨G⟩_ , find the unique integer _k_ , 0 _≤ k ≤ n −_ 1 such that _P_ = [ _k_ ] _G_ . 

This is a special case of the general discrete logarithm problem as explained in Section 2.2.5. An elliptic curve group is called _cryptographically strong_ if the underlying ECDLP is considered to be computationally intractable for the application in use. 

Cryptographically strong elliptic curve groups for different security levels are published by various standardization bodies (e.g. ANSI, ISO, IETF, NIST). 

## **2.3.4. Cryptographically Strong Elliptic Curve Domain Parameters over** F _p_ 

Cryptographically strong elliptic curve domain parameters SHALL be used (see also [7], [9] and [32] for the generation of suitable curves). The ECDLP is currently considered to be intractable, if at least the following conditions hold : 

1. The order _n_ of the base point _G_ MUST be a prime of at least 224 bits. 

2. To avoid the elliptic curve to be anomalous the order _n_ MUST be different from _p_ . 

3. The ECDLP MUST NOT be reducible to the DLP in a multiplicative group F _p[r]_ for a ’small’ integer _r_ . Thus, it is REQUIRED that _p[r] ̸≡_ 1 mod _n_ for all 1 _≤ r ≤_ 10[4] . 

Federal Office for Information Security 

14 

Technical Guideline - Elliptic Curve Cryptography 

4. The class number of the principal order belonging to the endomorphism ring of _E_ SHOULD be at least 200.[1] 

However, as the generation and validation of domain parameters is non-trivial (cf. for example [7]), it is RECOMMENDED to use standardized domain parameters, generated by trusted third parties. Cryptographically strong domain parameters can be found in Section 6. 

> 1If an elliptic curve is generated at random, this curve respects this requirement with a very high probability (cf. [7], [9] and [32] for the generation and validation of domain parameters, and the calculation of class numbers). 

Federal Office for Information Security 

15 

Technical Guideline - Elliptic Curve Cryptography 

## **3. Data Types and Data Conversion** 

The cryptographic algorithms specified in this guideline involve operations using several different data types. These data types are considered as abstract data types consisting of distinct sets of elements, e.g. an octet string is regarded as distinct from a bit string. This distinction helps to clarify the requirements placed on implementations and helps to avoid subtle coding errors. 

In all, five data types are employed in this document: 

1. Octet strings ( `OS` ) 

2. Bit strings ( `BS` ) 

3. Integers ( `I` ) 

4. Field elements ( `FE` ) 

5. Elliptic curve points ( `ECP` ) 

It is often necessary to convert one data type into another one. Section 3.1 describes the conversion routines as summarized in Table 3.1. Section 3.2 describes two encoding mechanisms for elliptic curve points. 

|**Conversion routine**|**Abbreviation**|**Section**|
|---|---|---|
|Bit String to Octet String|`BS2OS`|3.1.1|
|Octet String to Bit String|`OS2BS`|3.1.1|
|Integer to Octet String|`I2OS`|3.1.2|
|Octet String to Integer|`OS2I`|3.1.2|
|Finite Field Element to Octet String|`FE2OS`|3.1.3|
|Octet String to Finite Field Element|`OS2FE`|3.1.3|



Table 3.1.: Conversion routines for data types used in this guideline. 

## **3.1. Conversion Routines** 

The big endian notation is assumed to be used in the following conversion routines. 

## **3.1.1. Conversion between Bit Strings and Octet Strings** 

## `BS2OS` 

The data conversion primitive that converts a bit string to an octet string is called _Bit String to Octet String Conversion Primitive_ or `BS2OS` . It takes a bit string of length _d_ as input and outputs the corresponding octet string of length _l_ = _⌈d/_ 8 _⌉_ . The bit string and the octet string are written as _bd−_ 1 _bd−_ 2 _· · · b_ 1 _b_ 0 and _Ml−_ 1 _Ml−_ 2 _· · · M_ 1 _M_ 0, respectively. 

The conversion is quite simple: One simply pads enough zeros on the left of the bit string to make its length a multiple of 8, and then chops the padded bit string up into octets. More precisely, one proceeds as follows: 

Federal Office for Information Security 

16 

Technical Guideline - Elliptic Curve Cryptography 

1. _l_ = _⌈d/_ 8 _⌉_ . 

2. For 0 _≤ i ≤ l −_ 2 do _Mi_ = _b_ 8 _i_ +7 _b_ 8 _i_ +6 _· · · b_ 8 _i_ +2 _b_ 8 _i_ +1 _b_ 8 _i_ . 

3. _Ml−_ 1 = 0 _· · ·_ 0 _bd−_ 1 _· · · b_ 8( _l−_ 1)+1 _b_ 8( _l−_ 1), where the number of zeros at the left of _Ml−_ 1 is equal to 8 _l − d_ . 

4. Output _Ml−_ 1 _Ml−_ 2 _· · · M_ 1 _M_ 0. 

## `OS2BS` 

The data conversion primitive that converts an octet string to a bit string is called _Octet String to Bit String Conversion Primitive_ or `OS2BS` . It takes an octet string of length _l_ as input and outputs the corresponding bit string of length _d_ = 8 _l_ . Assume that the octet string and the bit string are written as _Ml−_ 1 _Ml−_ 2 _· · · M_ 1 _M_ 0 and _bd−_ 1 _bd−_ 2 _· · · b_ 1 _b_ 0, respectively. 

Each octet is interpreted as a bit string of length 8. The result is then the concatenation of these bit strings. More precisely, one proceeds as follows: 

1. _d_ = 8 _l_ . 

2. For 0 _≤ i ≤ l −_ 1 do _b_ 8 _i_ +7 _b_ 8 _i_ +6 _· · · b_ 8 _i_ +2 _b_ 8 _i_ +1 _b_ 8 _i_ = _Mi_ . 

3. Output _bd−_ 1 _bd−_ 2 _· · · b_ 1 _b_ 0. 

## **3.1.2. Conversion between Integers and Octet Strings** 

## `I2OS` 

The data conversion primitive that converts integers to octet strings is called _Integer to Octet String Conversion Primitive_ or `I2OS` . It takes a non-negative integer _x_ and the desired length _l_ of the octet string as input. The length _l_ has to satisfy 256 _[l] > x_ . `I2OS` outputs the corresponding octet string. If 256 _[l] ≤ x_ , the conversion algorithm SHALL output _error_ . 

The idea is to write a non-negative integer _x_ in its unique _l_ -digit representation to the base 256: 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0017-15.png)


As usual, the leftmost bit in each digit _xi_ is the most significant bit. We denote the octet string by _Ml−_ 1 _Ml−_ 2 _· · · M_ 1 _M_ 0. One sets _Mi_ = _xi_ for 0 _≤ i ≤ l −_ 1. 

**Note:** One or more leading digits will be zero if _x <_ 256 _[l][−]_[1] . 

## `OS2I` 

The primitive that converts octet strings to integers is called _Octet String to Integer Conversion Primitive_ or `OS2I` . It takes a non-empty octet string of length _l ∈_ N as input and outputs the corresponding integer _x_ as explained below. In addition, for empty octet strings, i.e. _l_ = 0, this guideline defines _x_ = 0. 

Let the octet string be _Ml−_ 1 _Ml−_ 2 _· · · M_ 1 _M_ 0. Each octet is interpreted as a non-negative integer to the base 256, where the leftmost bit is the most significant one, i.e. one sets _xi_ = _Mi_ for 0 _≤ i ≤ l −_ 1. Then 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0017-21.png)


Federal Office for Information Security 

17 

Technical Guideline - Elliptic Curve Cryptography 

**Note:** The octet string of length zero (the empty octet string) is converted to the integer 0. 

## **3.1.3. Conversion between Field Elements and Octet Strings** 

## `FE2OS` 

The primitive that converts field elements to octet strings is called _Field Element to Octet String Conversion Primitive_ or `FE2OS` . It takes a field element as input and outputs the corresponding octet string. 

A field element _x ∈_ F _p_ is converted to an octet string of length _l_ = _⌈_ log256 _p⌉_ by applying the conversion function `I2OS` as described in Section 3.1.2 with parameter _l_ , i.e. `FE2OS` ( _x_ ) = `I2OS` ( _x, l_ ). Here the element _x ∈_ F _p_ is represented as an integer _x ∈{_ 0 _,_ 1 _, . . . , p −_ 1 _}_ (cf. Section 2.2.4). 

## `OS2FE` 

The primitive that converts octet strings to field elements is called _Octet String to Field Element Conversion Primitive_ or `OS2FE` . It takes an octet string as input and outputs the corresponding element. 

An octet string _X_ is converted to a field element by applying the conversion function `OS2I` as described in Section 3.1.2 and reducing the output modulo _p_ , i.e. `OS2FE` ( _X_ ) = `OS2I` ( _X_ ) mod _p_ . 

## **3.2. Encoding Elliptic Curve Points** 

Let _p_ be a prime _p ̸_ = 2 _,_ 3 and let _E_ be an elliptic curve over F _p_ given by its Weierstraß equation _y_[2] = _x_[3] + _ax_ + _b_ . Let _P ∈ E_ (F _p_ ) be a point on the elliptic curve. This guideline represents the point _P_ by an octet string: 

- If _P_ = _O_ , the point is represented by its affine coordinate(s). Either a _compressed_ ( _PC_ ) or an _uncompressed_ ( _PU_ ) encoding is used. 

- If _P_ = _O_ , the point is always represented by the single octet 0 _x_ 00 independent of the encoding. 

## **3.2.1. Uncompressed Encoding** 

In uncompressed encoding the point _P_ is represented by two field elements, its _x_ -coordinate denoted by _xP_ and its _y_ -coordinate denoted by _yP_ . If _b_ is the bit length of _p_ , storing ( _xP , yP_ ) requires 2 _b_ bits (excluding additional data required for the encoding). 

## **Encoding** 

The uncompressed encoding _PU_ is defined as _PU_ = _C ∥ X ∥ Y_ , where 

- _C_ = 0 _x_ 04 

- _X_ = `FE2OS` ( _xP_ ) 

- _Y_ = `FE2OS` ( _yP_ ) 

## **Decoding** 

Given _PU_ the point _P_ is recovered as _P_ = ( `OS2FE` ( _X_ ) _,_ `OS2FE` ( _Y_ )). Before using _P_ it MUST be validated that _P_ is indeed a point on the elliptic curve _E_ by checking that _yP_[2][=] _[ x]_[3] _P_[+] _[ ax][P]_[+] _[ b]_[.] 

Federal Office for Information Security 

18 

Technical Guideline - Elliptic Curve Cryptography 

## **3.2.2. Compressed Encoding** 

In compressed encoding the point _P_ is represented by its _x_ -coordinate _xP_ and an additional bit to uniquely identify the _y_ -coordinate _yP_ . More precisely, the bit _yP[′]_[is][defined][to][be][the] rightmost bit of _yP_ , i.e. _yP[′]_[= 0][if][and][only][if] _[y][P]_[is][even.] 

## **Encoding** 

The compressed encoding _PC_ is defined as _PC_ = _C ∥ X_ , where 

- If _yP[′]_[= 0,][set] _[C]_[= 0] _[x]_[02] 

- If _yP[′]_[= 1,][set] _[C]_[= 0] _[x]_[03] 

- _X_ = `FE2OS` ( _xP_ ) 

## **Decoding** 

Given _PC_ the point _P_ is recovered as _P_ = ( `OS2FE` ( _X_ ) _, yP_ ), where the following algorithm is used to calculate _yP_ : 

1. Set _α_ = _x_[3] _P_[+] _[ ax][P]_[+] _[ b]_[.] 

2. Check whether _α_ is a square in F _p_ . If _α_ is a non-square, output error and terminate. 

3. If _α_ = 0, then _yP_ = 0. Output _yP_ and terminate. 

4. Compute a square root _β ∈_ F _p_ of _α_ in F _p_ . 

5. If the rightmost bit of _β_ is equal to _yP[′]_[,][then] _[y][P]_[=] _[ β]_[.][Otherwise,] _[y][P]_[=] _[ p][ −][β]_[.][Output] _[y][P]_ and terminate. 

To efficiently check whether _α_ is a square in F _p_ , the Legendre-Symbol 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0019-16.png)



![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0019-17.png)


**Note:** According to this guideline primes _p ≡_ 3 mod 4 are RECOMMENDED. In this case, the square roots _±β_ of _α_ can be efficiently computed as _β_ = _α_[(] _[p]_[+1)] _[/]_[4] mod _p_ . 

Federal Office for Information Security 

19 

Technical Guideline - Elliptic Curve Cryptography 

## **4. Elliptic Curve Cryptography Algorithms** 

This section specifies cryptographic algorithms for elliptic curves: Section 4.1 provides definitions for auxiliary functions, i.e. random number generators, hash functions, and key generation. In Section 4.2, the elliptic curve based digital signature algorithms ECDSA, ECGDSA and EC-Schnorr are specified. Subsequently, the key agreement algorithm ECKA and PACE are described in Sections 4.3 and 4.4, respectively. 

## **4.1. Auxiliary Functions and Algorithms** 

## **4.1.1. Random and Pseudo-Random Number Generators** 

Random number generators are often based on physical processes like radioactive decay or unpredictable events like the time between two strikes on a keyboard. 

In practice, pseudo-random number generators (non-physical) are often used for efficiency reasons. Roughly speaking, the output of a pseudo-random number generator should be indistinguishable from the output of a true random number generator. 

Functionality classes and evaluation methodologies for pseudo-random number generators and physical random number generators are published in an appendix to AIS 20/31 [3]. This document replaces the former appendices of AIS 20 [1] and AIS 31 [2], respectively. In this technical guideline, the notation RNG( _{_ 1 _,_ 2 _, . . . , n−_ 1 _}_ ) is used to denote both a random number generator and a pseudo-random number generator. The input of the function RNG is a finite set of positive integers, its output is a number randomly or pseudo-randomly chosen from this set. 

The outputs of RNG( _{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ ) SHALL be (almost) uniformly distributed within _{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ . For the generation of nonces and cryptographical keys (including ephemeral keys), it is RECOMMENDED to use a (pseudo-)random number generator of one of the following classes: 

- Pseudo-random number generators: 

   - DRG.2, 

   - DRG.3, 

   - **–** DRG.4. 

- Physical random number generators: 

   - PTG.3. 

**Note:** Beside the listed generators, also random number generators evaluated according to the former version (AIS 20 [1], AIS 31 [2]) of AIS20/31 MAY be used. Then, it is RECOMMENDED to take a pseudo-random number generator of the class K4 or a physical random number generator of the class P2 whose output is mathematical post-processed. 

In many applications RNG( _{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ ) is derived from RNG( _{_ 0 _,_ 1 _,_ 2 _, . . . ,_ 2 _[k] −_ 1 _}_ ) with 2 _[k] ≥ n_ . In this case the implementor MUST ensure that the (almost) uniform distribution of RNG( _{_ 0 _,_ 1 _,_ 2 _, . . . ,_ 2 _[k] −_ 1 _}_ ) is maintained in RNG( _{_ 1 _,_ 2 _, . . . , n−_ 1 _}_ ). The following two algorithms are provided as an example. More information and additional algorithms can be found in TR02102 [11]. 

Federal Office for Information Security 

20 

Technical Guideline - Elliptic Curve Cryptography 

- **Algorithm 1:** This algorithm maintains uniform distribution but has probabilistic run-time. 1. _r_ = RNG( _{_ 0 _,_ 1 _,_ 2 _, . . . ,_ 2 _[k] −_ 1 _}_ ) 

   2. If ( _r < n_ ) and ( _r >_ 0), output _r_ else goto 1. 

- **Algorithm 2:** This algorithm has deterministic run-time but does not fully maintain uniform distribution. 

   1. _r_ = RNG( _{_ 0 _,_ 1 _,_ 2 _, . . . ,_ 2 _[k]_[+64] _−_ 1 _}_ ) 

   2. Output ( _r_ mod ( _n −_ 1)) + 1 

**Note:** The usage of a non-uniformly distributed RNG( _{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ ) can enable an attack on signature algorithms (cf. Bleichenbacher’s attack on DSA, described e.g. in [29]). Algorithm 2 does not provide uniform distribution. It is however assumed that the deviation from uniform distribution produced by Algorithm 2 is too small to be exploited by an attacker. 

## **4.1.2. Cryptographically Strong Hash Functions** 

A hash function H maps a message _M_ to a hash value (digest) _D_ = H( _M_ ). The message _M_ is an octet string of arbitrary length[1] and the hash value _D_ is an octet string of fixed length _⌈ℓ/_ 8 _⌉_ , where _ℓ_ is the bit length of the hash values produced by H(): 


![](markdown/tr/BSI-TR-03111_V-2-0_pdf/BSI-TR-03111_V-2-0_pdf.pdf-0021-09.png)


In some cases the hash values have to be truncated. Let H _l_ ( _M_ ) be the _truncated hash value_ of _M_ , i.e. the hash value H( _M_ ) is cropped to the _l_ leftmost bits. H _l_ ( _M_ ) SHALL be encoded as octet string using the `BS2OS` conversion. 

A hash function suitable for cryptography, has to satisfy the following requirements: 

- **Preimage resistance:** For any hash value _D_ , it is computationally infeasible to find a message _M_ with H( _M_ ) = _D_ . 

- **Second preimage resistance:** For any message _M_ , it is computationally infeasible to find a message _M[′]_ with _M_ = _M[′]_ and H( _M_ ) = H( _M[′]_ ). 

- **Collision resistance:** It is computationally infeasible to find arbitrary messages _M_ and _M[′]_ with _M_ = _M[′]_ and H( _M_ ) = H( _M[′]_ ). 

If H fulfills all these requirements, it is said to be _cryptographically strong_ . 

Hash functions with an output length _ℓ ≥_ 224 SHALL be used. Some hash functions are weaker than previously believed (cf. [34]). The hash functions listed in Table 4.1 are supported by this specification. 

|**Hash Function**|**Hash Length (bit)**|**Reference**|
|---|---|---|
|SHA-224|224|[13]|
|SHA-256|256|[13]|
|SHA-384|384|[13]|
|SHA-512|512|[13]|



Table 4.1.: Supported hash functions. 

For session key derivation (cf. section 4.3.3), also the hash functions SHA-1 and RIPEMD-160 (cf. [13], [18]) MAY be used. 

> 1Most hash functions have a restriction on the length of _M_ . 

Federal Office for Information Security 

21 

Technical Guideline - Elliptic Curve Cryptography 

## **– 4.1.3. Elliptic Curve Key Pair Generation ECKeyPair** 

An elliptic curve key pair consists of a public key _P_ and a private key _d_ . A key pair is generated as follows. 

**Input:** Cryptographically strong elliptic curve domain parameters ( _p, a, b, G, n, h_ ). 

**Output:** The key pair ( _d, P_ ). 

**Actions:** The following actions are performed: 

1. _d_ = RNG( _{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ ) 

2. _P_ = [ _d_ ] _G_ (If _P_ is generated for ECGDSA or ECKCDSA, set _P_ = [ _d[−]_[1] mod _n_ ] _G_ instead). 

3. Output ( _d, P_ ) 

## **4.2. Elliptic Curve Based Signature Algorithms** 

This section specifies the signature algorithms ECDSA, ECGDSA and EC-Schnorr. For that purpose, it is assumed in the following that A sends B a message _M_ and the corresponding signature ( _r, s_ ). Furthermore, it is assumed that the message _M_ also includes information identifying the public key, the signature algorithm and the hash function H() to be used for the verification of the signature. An example for such a signature format is given in Section 5.2. 

**Note:** It is RECOMMENDED to use a hash function H() (cf. Section 4.1.2) with an output length _ℓ_ = _τ_ , i.e. the output length of the hash function and the bit length of the order of the base point _G_ SHOULD be equal. If for any reason the hash function has to be chosen such that _ℓ> τ_ , the hash value SHALL be truncated to H _τ_ ( _M_ ), the _τ_ leftmost bits of H( _M_ ). 

The hash function SHOULD NOT be chosen such that _ℓ< τ_ . 

## **– 4.2.1. The Elliptic Curve Digital Signature Algorithm ECDSA** 

This section describes the Elliptic Curve Digital Signature Algorithm abbreviated by ECDSA. The description is in conformance with [4]. 

## **4.2.1.1. Signature Algorithm** 

A proceeds as follows to generate the ECDSA signature ( _r, s_ ) on the message _M_ . 

**Input:** The following inputs are needed: 

1. A’s private key _d_ A and the elliptic curve domain parameters ( _p, a, b, G, n, h_ ). 

2. The message _M_ to be signed. 

**Output:** The ECDSA signature ( _r, s_ ) over _M_ . 

**Actions:** The following actions are performed: 

1. _k_ = RNG( _{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ ) 

2. _Q_ = [ _k_ ] _G_ 

3. _r_ = `OS2I` ( `FE2OS` ( _xQ_ )) mod _n_ If _r_ = 0 goto 1. 

4. _kinv_ = _k[−]_[1] mod _n_ 

Federal Office for Information Security 

22 

Technical Guideline - Elliptic Curve Cryptography 

5. _s_ = _kinv ·_ ( _r · d_ A + `OS2I` (H _τ_ ( _M_ ))) mod _n_ If _s_ = 0 goto 1. 

6. Output ( _r, s_ ) 

**Note:** The signature depends on the random number _k_ . If A signs the same document _M_ twice, both signatures differ with a very high probability. 

## **4.2.1.2. Verification Algorithm** 

B proceeds as follows to verify the received ECDSA signature ( _r, s_ ) on _M_ . 

**Input:** The following inputs are needed: 

1. A’s authentic public key _P_ A and the domain parameters ( _p, a, b, G, n, h_ ). 

2. The signed message _M_ . 

3. The ECDSA signature ( _r, s_ ). 

**Output:** `True` , if the signature is valid, and `False` otherwise. 

- **Actions:** The following actions are performed: 

   1. Verify that _r, s ∈{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ 

      - If the check fails, output `False` and terminate. 

   2. _sinv_ = _s[−]_[1] mod _n_ 

   3. _u_ 1 = _sinv ·_ `OS2I` (H _τ_ ( _M_ )) mod _n_ 

      - _u_ 2 = _sinv · r_ mod _n_ 

   4. _Q_ = [ _u_ 1] _G_ + [ _u_ 2] _P_ A 

If _Q_ = _O_ , output `Error` and terminate. 

5. _v_ = `OS2I` ( `FE2OS` ( _xQ_ )) mod _n_ 

6. Output `True` if _v_ = _r_ , and `False` otherwise. 

## **4.2.2. The Elliptic Curve German Digital Signature Algorithm - ECGDSA** 

This section introduces the Elliptic Curve German Digital Signature Algorithm. The specification matches with [23]. In the ECGDSA scheme, the elliptic curve point _P_ A _[′]_[:=][[] _[d][−]_ A[1][mod] _[ n]_[]] _[G]_ is used as public key. As a consequence, the signature creation requires no computation of a multiplicative inverse mod _n_ . 

## **4.2.2.1. Signature Algorithm** 

A proceeds as follows to generate the ECGDSA signature ( _r, s_ ) on a message _M_ . 

**Input:** The following information is required as input: 

1. A’s private key _d_ A and the elliptic curve domain parameters ( _p, a, b, G, n, h_ ). 

2. The message _M_ to be signed. 

**Output:** The ECGDSA signature ( _r, s_ ) over _M_ . 

**Actions:** The following actions are performed: 

1. _k_ = RNG( _{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ ) 

Federal Office for Information Security 

23 

Technical Guideline - Elliptic Curve Cryptography 

2. _Q_ = [ _k_ ] _G_ 

3. _r_ = `OS2I` ( `FE2OS` ( _xQ_ )) mod _n_ 

If _r_ = 0 goto 1. 

4. _s_ = ( _k · r −_ `OS2I` (H _τ_ ( _M_ ))) _· d_ A mod _n_ 

If _s_ = 0 goto 1. 

5. Output ( _r, s_ ) 

**Note:** The signature depends on the random number _k_ . If A signs the same document _M_ twice, both signatures differ with a very high probability. 

## **4.2.2.2. Verification Algorithm** 

To verify the received ECGDSA signature ( _e, s_ ) on a message _M_ , B has to proceed as follows. 

**Input:** The following inputs are needed: 

1. A’s authentic public key _P_ A and the domain parameters ( _p, a, b, G, n, h_ ). 

2. The signed message _M_ . 

3. The ECGDSA signature ( _r, s_ ). 

**Output:** `True` , if the signature is valid, and `False` otherwise. 

- **Actions:** The following actions are performed: 

   1. Verify that _r, s ∈{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ 

If the check fails, output `False` and terminate. 

2. _rinv_ = _r[−]_[1] mod _n_ 

3. _u_ 1 = _rinv ·_ `OS2I` (H _τ_ ( _M_ )) mod _n_ 

_u_ 2 = _rinv · s_ mod _n_ 

4. _Q_ = [ _u_ 1] _G_ + [ _u_ 2] _P_ A 

If _Q_ = _O_ , output `Error` and terminate. 

5. _v_ = `OS2I` ( `FE2OS` ( _xQ_ )) mod _n_ 

6. Output `True` if _v_ = _r_ , and `False` otherwise. 

## **4.2.3. The Elliptic Curve Based Schnorr Signature Algorithm - EC-Schnorr** 

This section describes the Elliptic Curve Based Schnorr Signature Algorithm (EC-Schnorr)[2] , which is described in the following. The scheme requires no computation of a multiplicative inverse modulo _n_ during the siganture creation. 

## **4.2.3.1. Signature Algorithm** 

A proceeds as follows to generate the EC-Schnorr signature ( _r, s_ ) on a message _M_ . 

**Input:** The following information is required as input: 

1. A’s private key _d_ A and the elliptic curve domain parameters ( _p, a, b, G, n, h_ ). 

2. The message _M_ to be signed. 

> 2For the Schnorr signature, see also [33]. 

Federal Office for Information Security 

24 

Technical Guideline - Elliptic Curve Cryptography 

**Output:** The EC-Schnorr signature ( _r, s_ ) over _M_ . 

**Actions:** The following actions are performed: 

1. _k_ = RNG( _{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ ) 

2. _Q_ = [ _k_ ] _G_ 

3. _r_ = `OS2I` (H _τ_ ( _M ∥_ `FE2OS` ( _xQ_ ))) 

If _r_ = 0 mod _n_ , goto 1. 

4. _s_ = _k − r · d_ A mod _n_ 

If _s_ = 0 goto 1. 

5. Output ( _r, s_ ) 

**Note:** The signature depends on the random number _k_ . If A signs the same document _M_ twice, both signatures differ with a very high probability. 

## **4.2.3.2. Verification Algorithm** 

Given a EC-Schnorr signature ( _r, s_ ) on a message _M_ , the verification procedure is the following 

**Input:** The following inputs are needed: 

1. A’s authentic public key _P_ A and the domain parameters ( _p, a, b, G, n, h_ ). 

2. The signed message _M_ . 

3. The EC-Schnorr signature ( _r, s_ ). 

**Output:** `True` , if the signature is valid, and `False` otherwise. 

**Actions:** The following actions are performed: 

1. Verify that _r ∈{_ 0 _, . . . ,_ 2 _[τ] −_ 1 _}_ and _s ∈{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ . 

If the check fails, output `False` and terminate. 

2. _Q_ = [ _s_ ] _G_ + [ _r_ ] _P_ A 

If _Q_ = _O_ , output `Error` and terminate. 

3. _v_ = `OS2I` (H _τ_ ( _M ∥_ `FE2OS` ( _xQ_ ))) 

4. Output `True` if _v_ = _r_ , and `False` otherwise. 

## **– 4.3. The Elliptic Curve Key Agreement Algorithm ECKA** 

This section describes the Elliptic Curve Key Agreement Algorithm (ECKA), key derivation functions, and the key agreement protocols of Diffie-Hellman (ECKA-DH) and ElGamal (ECKAEG). The description of ECKA is in conformance with [5]. 

**Note:** To prevent attacks based on invalid (ephemeral) public keys it MUST be checked that a received public key is indeed a point on the elliptic curve. This validation is already part of the point decoding algorithms (cf. Section 3.2). In addition to this, small subgroup attacks are prevented by using (compatible) cofactor multiplication in the key agreement algorithms. 

Federal Office for Information Security 

25 

Technical Guideline - Elliptic Curve Cryptography 

## **4.3.1. Key Agreement Algorithm** 

A and B proceed as follows to generate a shared secret point _S_ AB: 

**Input:** The private key _d_[�] , the public key _P_[�] , and the elliptic curve domain parameters ( _p, a, b, G, n, h_ ). The private key _d_[�] and the public key _P_[�] SHALL be either both ephemeral (ECKA-DH, cf. Section 4.3.2.1) or ephemeral-static (ECKA-EG, cf. Section 4.3.2.2). 

- **Output:** The output consists of: 

   1. The shared secret point _S_ AB. 

   2. The shared secret value _Z_ AB (OPTIONAL). 

- **Actions:** The following actions are performed: 

   1. _l_ = _h[−]_[1] mod _n_ 

   2. _Q_ = [ _h_ ] _P_[�] 

   3. _S_ AB = [ _d_[�] _· l_ mod _n_ ] _Q_ 

If _S_ AB = _O_ , output `Error` and terminate. 

4. _Z_ AB = `FE2OS` ( _xS_ AB) (OPTIONAL) 

5. Output _S_ AB and conditionally _Z_ AB 

**Note:** To derive keys for symmetric encryption and/or integrity protection the OPTIONAL generation of _Z_ AB MUST be performed. The shared secret value _Z_ AB MUST NOT be used directly for encryption or integrity protection, key derivation functions are described in Section 4.3.3. 

## **4.3.2. The Key Agreement Protocols ECKA-DH and ECKA-EG** 

To interactively generate a shared secret point _S_ AB (or a shared secret value _Z_ AB), A and B may use one of the following protocols. 

## **4.3.2.1. Anonymous Diffie-Hellman Key Agreement (ECKA-DH).** 

Both A and B agree on the domain parameters ( _p, a, b, G, n, h_ ), the key derivation algorithm, the cipher and/or message authentication code to be used and perform the following steps: 

|**Initiator A**||**Recipient B**|
|---|---|---|
|(�<br>_d_A_,_ �<br>_P_A) = ECKeyPair(_p, a, b, G, n, h_)<br>_S_AB = ECKA(�<br>_d_A_,_ �<br>_P_B_,_ (_p, a, b, G, n, h_))|�<br>_P_A<br>⇌<br>�<br>_P_B|(�<br>_d_B_,_ �<br>_P_B) = ECKeyPair(_p, a, b, G, n, h_)<br>_S_AB = ECKA(�<br>_d_B_,_ �<br>_P_A_,_ (_p, a, b, G, n, h_))|



Table 4.2.: ECKA-DH. 

## **4.3.2.2. ElGamal Key Agreement (ECKA-EG).** 

The recipient B must make the static public key _P_ B including the corresponding domain parameters ( _p, a, b, G, n, h_ ) publicly available in an authentic form and performs the steps of table 4.3. 

Federal Office for Information Security 

26 

Technical Guideline - Elliptic Curve Cryptography 

|**Initiator A**||**Recipient B**|
|---|---|---|
|(�<br>_d_A_,_ �<br>_P_A) = ECKeyPair(_p, a, b, G, n, h_)<br>_S_AB = ECKA(�<br>_d_A_, P_B_,_ (_p, a, b, G, n, h_))|_M_=(�<br>_P_A_,..._)<br>_−→_|_S_AB = ECKA(_d_B_,_ �<br>_P_A_,_ (_p, a, b, G, n, h_))|



Table 4.3.: ECKA-EG. 

To send B an encrypted and/or integrity protected message _M_ , A MUST include the ephemeral public key _P_[�] A and information identifying the key derivation algorithm, the cipher and/or the message authentication code to be used. An example for a message format is given in Section 5.3.1.1. 

## **4.3.3. Key Derivation Functions** 

The following algorithms are RECOMMENDED to derive keys from the shared secret value _Z_ AB: 

**X9.63 Key Derivation Function.** ANSI X9.63 [5] describes a method for converting a shared secret to a cryptographic key. The algorithm KDF _X_ 9 _._ 63() requires to select a hash function H() from Section 4.1.2. Let _ℓ_ denote the bit length of the hash value. 

**Input:** The following inputs are needed: 

1. An octet string _Z_ AB, which is the shared secret value. 

2. An integer _κ < ℓ ·_ (2[32] _−_ 1), which is the bit length of the keying data to be generated. 

3. An octet string _SharedInfo_ , which consists of some information shared between A and B (OPTIONAL). 

**Output:** The octet string _KeyData_ of length _k_ = _⌈κ/_ 8 _⌉_ . 

**Actions:** The following actions are performed: 

1. Let _counter_ be a 32 bit, big-endian integer, initialized with 0 _x_ 00000001. 

2. _j_ = _⌈κ/ℓ⌉_ 

3. For _i_ = 1 to _j −_ 1 do the following: 

   - a) _Hi_ = H( _Z_ AB _∥ counter ∥_ [ _SharedInfo_ ]) 

   - b) _counter_ = _counter_ + 1 

   - c) _i_ = _i_ + 1 

4. _l_ = _κ −_ ( _ℓ ·_ ( _j −_ 1)) 

5. _Hj_ = H _l_ ( _Z_ AB _∥ counter ∥_ [ _SharedInfo_ ]) 

6. _KeyData_ = _H_ 1 _∥ H_ 2 _∥· · · ∥ Hj−_ 1 _∥ Hj_ 

7. Output _KeyData_ 

**Key Derivation Function for Session Keys.** This paragraph describes a method for deriving cryptographic session keys of bit length _κ_ , i.e. keys for symmetric encryption and for computing message authentication codes (MAC). The algorithm KDF _Session_ requires to select a hash function H() from Section 4.1.2 with bit length _ℓ ≥ κ_ . 

Federal Office for Information Security 

27 

Technical Guideline - Elliptic Curve Cryptography 

**Input:** The following inputs are needed: 

1. An octet string _Z_ AB, which is a shared secret value. 

2. A 32-bit, big-endian integer _counter_ , which is initiated as follows: 

   - a) Default key used for encryption: 

      - _counter_ = 0 _x_ 00000001 

   - b) Default key used for authentication: 

      - _counter_ = 0 _x_ 00000002 

   - c) Alternative key used for encryption: 

      - _counter_ = 0 _x_ 00000003 

   - d) Alternative key used for authentication: 

      - _counter_ = 0 _x_ 00000004 

   - e) ... 

3. A nonce _r_ encoded as octet string (OPTIONAL). 

**Output:** An octet string _KeyData_ . 

- **Actions:** The following actions are performed: 

   1. _D_ = _Z_ AB _∥ r ∥ counter_ 

   2. _KeyData_ = H _κ_ ( _D_ ) 

   3. Output _KeyData_ 

## **4.3.3.1. Key Derivation for DES.** 

To derive 112-bit 3DES keys the hash function SHA-1 SHALL be used with _κ_ = 112. The parity bits of _KeyData_ MAY be adjusted to form correct DES keys. 

## **4.3.3.2. Key Derivation for AES.** 

- To derive 128-bit AES keys the hash function SHA-1 with _κ_ = 128 SHALL be used. 

- To derive 192-bit AES keys the hash function SHA-256 with _κ_ = 192 SHALL be used. 

- To derive 256-bit AES keys the hash function SHA-256 with _κ_ = 256 SHALL be used. 

## **– 4.4. The Password Authenticated Connection Establishment PACE** 

This section describes the Password Authenticated Connection Establishment protocol, abbreviated by PACE. The protocol establishes a secure channel with strong session keys based on an authentication by means of a secret password (which MAY have low entropy). 

A and B choose a key derivation function KDF _Session_ (e.g. the one of the section 4.3.3). Furthermore, they agree on a suitable mapping function Map() (e.g. the mapping function GMap() of section 4.4.1), a symmetric cipher (with encryption and decryption denoted by E() and E _[−]_[1] (), respectively), the message authentication code MAC(). Keys, input and output values of E() and MAC() are assumed to be octet strings. Let _v_ be a fixed multiple of the block size of E(). 

Federal Office for Information Security 

28 

Technical Guideline - Elliptic Curve Cryptography 

As input, the PACE protocol requires the shared password _π_ and the elliptic curve domain parameters _D_ = ( _p, a, b, G, n, h_ ). The following actions are performed to establish the secure channel: 

||**Initiator A**||**Recipient B**|
|---|---|---|---|
|0.<br>1.<br>2.<br>3.<br>4.|_Kπ_ = KDF_Session_(_π,_3)<br>_s_= RNG(_{_0_, . . . ,_2_v −_1_}_)<br>_z_ = E(_Kπ,_`FE2OS`(_s_))<br>Send _z_|_z_<br>_−→_|_Kπ_ = KDF_Session_(_π,_3)<br>_s_=`OS2FE`(E_−_1(_Kπ, z_))|
|5.|�_D_ =(_p, a, b,_ �_G, n, h_)= Map(_D, s_)|⇌|�_D_ =(_p, a, b,_ �_G, n, h_)= Map(_D, s_)|
|6.<br>7.|(�<br>_y_A_,_ �<br>_Y_A) = ECKeyPair( �_D_)<br>(_S_AB_, Z_AB)= ECKA(�<br>_y_A_, Y_B_,_ �_D_)|�<br>_Y_A<br>⇌<br>�<br>_Y_B|(�<br>_y_B_,_ �<br>_Y_B) = ECKeyPair( �_D_)<br>(_S_AB_, Z_AB)= ECKA(_y_B_,_ �<br>_Y_A_,_ �_D_)|
|8.<br>9.<br>10.<br>11.<br>12.<br>13.<br>14.<br>15.|_KEnc_ = KDF_Session_(_Z_AB_,_1)<br>_KMac_ = KDF_Session_(_Z_AB_,_2)<br>If _T_B = MAC(_KMac,_ �<br>_Y_A),<br>output `Error` and terminate.<br>_T_A = MAC(_KMac,_ �<br>_Y_B)<br>Send _T_A|_←−_<br>_T_B<br>_−→_<br>_T_A|_KEnc_ = KDF_Session_(_Z_AB_,_1)<br>_KMac_ = KDF_Session_(_Z_AB_,_2)<br>_T_B = MAC(_KMac,_ �<br>_Y_A)<br>Send _T_B<br>If _T_A = MAC(_KMac,_ �<br>_Y_B),<br>output `Error` and terminate.|



Table 4.4.: PACE. 

A detailed specification for an implementation of PACE on smartcards is contained in [12], a security proof of the protocol can be found in [8]. 

**Note:** For the generation of nonces in the PACE protocol, a (pseudo-)random number generator belonging to the classes K4, DRG.3, DRG.4 or PTG.3 MUST be used. 

## **– 4.4.1. The Generic Mapping GMap()** 

To map a nonce _s_ to a point of the elliptic curve A and B SHOULD use the generic mapping _GMap_ (). It is based on an anonynous Diffie-Hellman key agreement. The required input for the generic mapping are the domain parameters ( _p, a, b, G, n, h_ ) of the curve and the nonce _s_ that shall be mapped. Then, the protocol produces ephemeral domain parameters _D_[�] = _GMap_ ( _D, s_ ) by computing a new base point _G_[�] of the curve. 

||**Initiator A**||**Recipient B**|
|---|---|---|---|
|1.<br>2.<br>3.|(�<br>_d_A_,_ �<br>_P_A) = ECKeyPair(_p, a, b, G, n, h_)<br>_H_ = ECKA(�<br>_d_A_,_ �<br>_P_B_,_(_p, a, b, G, n, h_))<br>�_D_ =_GMap_(_D, s_)=(_p, a, b,_ [_s_]_G_+_H, n, h_)|�<br>_P_A<br>⇌<br>�<br>_P_B|(�<br>_d_B_,_ �<br>_P_B) = ECKeyPair(_p, a, b, G, n, h_)<br>_H_ = ECKA(�<br>_d_B_,_ �<br>_P_A_,_(_p, a, b, G, n, h_))<br>�_D_ =_GMap_(_D, s_)=(_p, a, b,_ [_s_]_G_+_H, n, h_)|



Table 4.5.: Generic Mapping. 

Federal Office for Information Security 

29 

Technical Guideline - Elliptic Curve Cryptography 

## **5. Input and Output Formats** 

This section specifies data structures and object identifiers for in- and output of public keys, signatures, and key agreement. 

The object identifier `bsi-de` represents the root of the subtree containing all objects defined in this specification: 

```
bsi-deOBJECTIDENTIFIER::={
```

```
itu-t(0)identified-organization(4)etsi(0)
```

```
reserved(127)etsi-identified-organization(0)7
```

```
}
```

The root identifier for elliptic curve cryptography is: 

```
id-eccOBJECTIDENTIFIER::={bsi-dealgorithms(1)1}
```

This guideline also supports the data structures and object identifiers specified in ANSI X9.62 [4]. The root identifier for ANSI X9.62 is: 

```
ansi-X9-62OBJECTIDENTIFIER::={
```

```
iso(1)member-body(2)us(840)10045}
```

## **5.1. Public Key Format** 

It is RECOMMENDED to store and exchange elliptic curve public keys in X9.62 format. In this case the data structures and object identifiers specified by X9.62 [4] SHALL be used. 

If, however, elliptic curve cryptography is performed on smartcards, public keys SHALL be encoded as data objects as defined in ISO 7816-8 [26]. 

## **5.1.1. X9.62 Format** 

Public keys represented in X.509 syntax have the following ASN.1 structure: 

```
SubjectPublicKeyInfo::=SEQUENCE{
algorithmAlgorithmIdentifier,
subjectPublicKeyBITSTRING
```

```
}
```

The component `algorithm` of type `AlgorithmIdentifier` specifies the type of the public key and its associated parameters. The component `subjectPublicKey` of type `BIT STRING` specifies the actual value of the public key. 

The elliptic curve public key is a value of type `ECPoint` , which is simply an `OCTET STRING` as defined in Section 3.2. The conversion routine `OS2BS` SHALL be used to map the value to a `BIT STRING` . 

Public keys in X9.62 format are identified by the object identifier `id-ecPublicKey` which is specified as follows: 

```
id-publicKeyTypeOBJECTIDENTIFIER::={ansi-X9-62keyType(2)}
```

```
id-ecPublicKeyOBJECTIDENTIFIER::={id-publicKeyType1}
```

Federal Office for Information Security 

30 

Technical Guideline - Elliptic Curve Cryptography 

The public key parameters contained in the `AlgorithmIdentifier` are defined as a choice of three alternatives: 

```
Parameters::=CHOICE{
ecParametersECParameters,
namedCurveOBJECTIDENTIFIER,
implicitlyCANULL
}
```

**ecParameters:** The domain parameters are explicitly described. 

**namedCurve:** Standardized domain parameters identified by an object identifier are used. **implicitlyCA:** The domain parameters are inherited or implicitly known. 

It is RECOMMENDED to use the alternatives `ecParameters` or `namedCurve` unless ephemeral public keys are exchanged. In this case `implicitlyCA` SHOULD be used instead. 

**Note:** These recommendations deviate from [31], 2.1.1. Implementations that strive for conformance to [31] MUST only support `namedCurve` . 

The structure `ECParameters` is used to describe domain parameters explicitly. Version 1 MUST be used. It is specified as follows: 

```
ECParameters::=SEQUENCE{
versionINTEGER{ecpVer1(1)}(ecpVer1),
fieldIDFieldID,
curveCurve,
baseECPoint,
orderINTEGER,
cofactorINTEGEROPTIONAL,
...
}
Curve::=SEQUENCE{
aFieldElement,
bFieldElement,
seedBITSTRINGOPTIONAL
}
```

`FieldElement ::= OCTET STRING ECPoint ::= OCTET STRING FieldID ::= SEQUENCE { fieldType OBJECT IDENTIFIER, parameters ANY DEFINED BY fieldType } id-fieldType OBJECT IDENTIFER ::= { ansi-X9-62 fieldType(1) } prime-field OBJECT IDENTIFIER ::= { id-fieldType 1 } Prime-p ::= INTEGER` If `FieldID` refers to a `prime-field` , `Prime-p` SHALL be used as parameter. 

Federal Office for Information Security 

31 

Technical Guideline - Elliptic Curve Cryptography 

## **5.1.2. ISO 7816 Format** 

For smartcards public keys and domain parameters MUST be exchanged as TLV (Tag-LengthValue) encoded data objects as described in ISO 7816-8 [26]. The tags and the encodings for data objects relevant to elliptic curves are given in Table 5.1. 

According to this guideline the data object for domain parameters MUST either be all present or all absent. Especially for ephemeral public keys the domain parameters are usually implicitly known and MUST be all absent. 

Public keys and domain parameters MUST be encapsulated in a constructed public key data object identified by tag 0 _x_ 7F49 unless the domain parameters and the key type are implicitly known and omitted. 

Unrestricted public keys data objects are identified by the object identifier `id-ecTLVPublicKey` which is specified as follows: 

```
id-ecTLVKeyFormatOBJECTIDENTIFIER::={id-ecckeyType(2)2}
id-ecTLVPublicKeyOBJECTIDENTIFIER::={id-ecTLVKeyFormatunrestricted(1)}
```

A restricted public key type for usage with dedicated ECC algorithms (for instance ECDSA, ECGDSA) may be defined in a later version of this specification. 

|**Object**|**Type**|**Symbol**|**Tag**|
|---|---|---|---|
|Algorithm|Object Identifer|–|0_x_06|
|Prime modulus|Integer|_p_|0_x_81|
|First coefcient|Integer|_a_|0_x_82|
|Second coefcient|Integer|_b_|0_x_83|
|Base point|Point|_G_|0_x_84|
|Order of the base point|Integer|_n_|0_x_85|
|Public Key|Point|_P_|0_x_86|
|Cofactor|Integer|_h_|0_x_87|



Table 5.1.: Tags for elliptic curve public keys and domain parameters over F _p_ . 

**Note:** This guideline deviates from ISO 7816 in the encoding of elliptic curve points. 

## **5.2. Signature Format** 

While this guideline supports the signature format specified by ANSI X9.62 [4] for ECDSA, the usage of the plain format is RECOMMENDED for all applications. The plain format MUST be used if the signature is generated or verified by a smartcard. 

The signature algorithm and the signature format are identified by an `AlgorithmIdentifier` , the hash function to be used is either referenced directly by the object identifier or by the parameters of the `AlgorithmIdentifier` . 

It is RECOMMENDED to reference the hash function to be used directly in the object identifier. In this case the parameters MAY be either absent or `null` . The recipient MUST be able to interpret both variants.[1] 

> 1 According to RFC 5480 [31], the parameters MUST be absent for algorithms identified by `ecdsa-with-SHAxxx` . According to ANSI X9.62 [4] the parameters SHOULD be absent, but implementations SHALL accept NULL parameters. This guideline explicitly allows both variants. 

Federal Office for Information Security 

32 

Technical Guideline - Elliptic Curve Cryptography 

**Note:** Signature algorithms with hash functions SHA-1 or RIPEMD-160 SHALL NOT be used anymore and are only included for backwards compatibility. 

## **5.2.1. Plain Format** 

In plain format the signature ( _r, s_ ) is encoded as octet string _R ∥ S_ , i.e. as concatenation of the octet strings _R_ = `I2OS` ( _r, l_ ) and _S_ = `I2OS` ( _s, l_ ) with _l_ = _⌈_ log256 _n⌉_ . Thus, the signature has a fixed length of 2 _l_ octets. 

To embed the signature in a `BIT STRING` the conversion routine `OS2BS` SHALL be used. 

The signature algorithm including the hash function to be used and the signature format is identified by the following object identifiers: 

## **5.2.1.1. ECDSA** 

```
ecdsa-plain-signaturesOBJECTIDENTIFIER::={id-eccsignatures(4)1}
ecdsa-plain-SHA1OBJECTIDENTIFIER::={ecdsa-plain-signatures1}
ecdsa-plain-SHA224OBJECTIDENTIFIER::={ecdsa-plain-signatures2}
ecdsa-plain-SHA256OBJECTIDENTIFIER::={ecdsa-plain-signatures3}
ecdsa-plain-SHA384OBJECTIDENTIFIER::={ecdsa-plain-signatures4}
ecdsa-plain-SHA512OBJECTIDENTIFIER::={ecdsa-plain-signatures5}
ecdsa-plain-RIPEMD160OBJECTIDENTIFIER::={ecdsa-plain-signatures6}
```

## **5.2.1.2. ECGDSA** 

```
ecgdsa-plain-signaturesOBJECTIDENTIFIER::={id-eccsignatures(4)2}
ecgdsa-plain-SHA224OBJECTIDENTIFIER::={ecgdsa-plain-signatures1}
ecgdsa-plain-SHA256OBJECTIDENTIFIER::={ecgdsa-plain-signatures2}
ecgdsa-plain-SHA384OBJECTIDENTIFIER::={ecgdsa-plain-signatures3}
ecgdsa-plain-SHA512OBJECTIDENTIFIER::={ecgdsa-plain-signatures4}
```

## **5.2.1.3. EC-Schnorr** 

```
ecschnorr-plain-signaturesOBJECTIDENTIFIER::={id-eccsignatures(4)3}
ecschnorr-plain-SHA224OBJECTIDENTIFIER::={ecschnorr-plain-signatures1}
ecschnorr-plain-SHA256OBJECTIDENTIFIER::={ecschnorr-plain-signatures2}
ecschnorr-plain-SHA384OBJECTIDENTIFIER::={ecschnorr-plain-signatures3}
ecschnorr-plain-SHA512OBJECTIDENTIFIER::={ecschnorr-plain-signatures4}
```

## **5.2.2. X9.62 Format** 

In X9.62 format the ECDSA-signature ( _r, s_ ) is encoded as ASN.1 structure with the following syntax: 

```
ECDSA-Sig-Value::=SEQUENCE{
```

```
rINTEGER,
sINTEGER
```

```
}
```

To embed the signature in a `BIT STRING` the DER encoded `ECDSA-Sig-Value` SHALL be the value of the bit string (including tag and length field). The following object identifiers are defined in X9.62 [4]. 

Federal Office for Information Security 

33 

Technical Guideline - Elliptic Curve Cryptography 

|`id-ecSigType`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ansi-x9-62 signatures(4) }`|
|---|---|---|---|---|---|
|`ecdsa-with-Sha1`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`id-ecSigType 1 }`|
|`ecdsa-with-Specified`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`id-ecSigType 3 }`|
|`ecdsa-with-Sha224`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecdsa-with-Specified 1 }`|
|`ecdsa-with-Sha256`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecdsa-with-Specified 2 }`|
|`ecdsa-with-Sha384`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecdsa-with-Specified 3 }`|
|`ecdsa-with-Sha512`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecdsa-with-Specified 4 }`|



For `ecdsa-with-Specified` the object identifier of the hash function to be used MUST be provided as parameter in the `AlgorithmIdentifier` . 

**Note:** X9.62 also provides `ecdsa-with-Recommended` which refers to ECDSA with ”the natural size” hash function. This alternative is not supported by this guideline and MUST NOT be used. 

## **5.3. Key Agreement** 

This section gives the object identifiers that SHALL be used for key agreement. Notice that the key agreement algorithms with block cipher 3DES SHOULD NOT be used in new applications and are only included for backward compatibility. 

## **5.3.1. ElGamal Key Agreement** 

The object identifier for the ElGamal key agreement protocol (ECKA-EG) is: 

```
ecka-egOBJECTIDENTIFIER::={id-ecckey-establishment(5)1}
```

The object identifiers for ECKA-EG with specified key derivation functions are: 

|`ecka-eg-X963KDF`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg 1 }`|
|---|---|---|---|---|---|
|`ecka-eg-X963KDF-SHA1`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-X963KDF 1 }`|
|`ecka-eg-X963KDF-SHA224`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-X963KDF 2 }`|
|`ecka-eg-X963KDF-SHA256`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-X963KDF 3 }`|
|`ecka-eg-X963KDF-SHA384`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-X963KDF 4 }`|
|`ecka-eg-X963KDF-SHA512`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-X963KDF 5 }`|
|`ecka-eg-X963KDF-RIPEMD160`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-X963KDF 6 }`|
|`ecka-eg-SessionKDF`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg 2 }`|
|`ecka-eg-SessionKDF-3DES`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-SessionKDF 1 }`|
|`ecka-eg-SessionKDF-AES128`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-SessionKDF 2 }`|
|`ecka-eg-SessionKDF-AES192`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-SessionKDF 3 }`|
|`ecka-eg-SessionKDF-AES256`|`OBJECT `|`IDENTIFIER `|`::= `|`{ `|`ecka-eg-SessionKDF 4 }`|



## **5.3.1.1. Message Format** 

The object identifiers beneath `SessionKDF` SHALL be associated with the message format as specified in Table 5.2 using the respective block cipher for encryption and authentication. 

**Note:** The message format is compatible to ISO 7816-4 Secure Messaging [25]. 

Federal Office for Information Security 

34 

Technical Guideline - Elliptic Curve Cryptography 

|**Object**|**Type**|**Symbol**|**Tag**|
|---|---|---|---|
|Ephemeral Public Key|ECPoint|�<br>_P_A|0_x_97|
|Padding indicator and ciphertext|Octet String|E(_KEnc, M_)|0_x_87|
|Integrity Protection|Octet String|MAC(_KMac, M_)|0_x_8E|



Table 5.2.: Tags for messages protected by ECKA-EG. 

## **5.3.1.2. Authentication** 

For message authentication the block cipher SHALL be used in CMAC-mode [28] with _KMac_ = KDF _Session_ ( _Z_ AB _,_ 2). 

## **5.3.1.3. Encryption** 

For message encryption the block cipher SHALL be used in CBC-mode [17] with key _KEnc_ = KDF _Session_ ( _Z_ AB _,_ 1) and _IV_ = E( _KEnc,_ 0). 

## **5.3.2. Anonymous Diffie-Hellman Key Agreement** 

The object identifier for the anonymous Diffie-Hellman key agreement protocol (ECKA-DH) is: 

```
ecka-dhOBJECTIDENTIFIER::={id-ecckey-establishment(5)2}
```

The object identifiers for ECKA-DH with specified key derivation functions are: 

```
ecka-dh-X963KDFOBJECTIDENTIFIER::={ecka-dh1}
ecka-dh-X963KDF-SHA1OBJECTIDENTIFIER::={ecka-dh-X963KDF1}
ecka-dh-X963KDF-SHA224OBJECTIDENTIFIER::={ecka-dh-X963KDF2}
ecka-dh-X963KDF-SHA256OBJECTIDENTIFIER::={ecka-dh-X963KDF3}
ecka-dh-X963KDF-SHA384OBJECTIDENTIFIER::={ecka-dh-X963KDF4}
ecka-dh-X963KDF-SHA512OBJECTIDENTIFIER::={ecka-dh-X963KDF5}
ecka-dh-X963KDF-RIPEMD160OBJECTIDENTIFIER::={ecka-dh-X963KDF6}
ecka-dh-SessionKDFOBJECTIDENTIFIER::={ecka-dh2}
ecka-dh-SessionKDF-3DESOBJECTIDENTIFIER::={ecka-dh-SessionKDF1}
ecka-dh-SessionKDF-AES128OBJECTIDENTIFIER::={ecka-dh-SessionKDF2}
ecka-dh-SessionKDF-AES192OBJECTIDENTIFIER::={ecka-dh-SessionKDF3}
ecka-dh-SessionKDF-AES256OBJECTIDENTIFIER::={ecka-dh-SessionKDF4}
```

## **5.4. PACE** 

This section gives the object identifiers that SHALL be used for PACE. Notice that the object identifier with block cipher 3DES SHOULD NOT be used in new applications and is only included for backward compatibility. 

The object identifiers for the PACE protocol with generic mapping are: 

```
id-PACE-KAOBJECTIDENTIFIER::={id-ecckey-establishment(5)3}
```

```
id-PACE-KA-GMOBJECTIDENTIFIER::={id-PACE-KA1}
id-PACE-KA-GM-SessionKDF-3DESOBJECTIDENTIFIER::={id-PACE-KA-GM1}
id-PACE-KA-GM-SessionKDF-AES-128OBJECTIDENTIFIER::={id-PACE-KA-GM2}
id-PACE-KA-GM-SessionKDF-AES-192OBJECTIDENTIFIER::={id-PACE-KA-GM3}
id-PACE-KA-GM-SessionKDF-AES-256OBJECTIDENTIFIER::={id-PACE-KA-GM4}
```

Federal Office for Information Security 

35 

Technical Guideline - Elliptic Curve Cryptography 

Here, public keys SHALL be structured according to section 5.1 and nonces SHALL be encoded as octet strings. The used encoding for the elliptic curve points MUST be negotiated in advance by the protocol parties. 

## **5.4.1. PACE on Smartcards** 

For smartcards, Part 2 of the Technical Guideline [12] gives a detailed specification of PACE. Implementations according to that specification SHALL use the corresponding object identifiers. 

```
id-PACEOBJECTIDENTIFIER::={bsi-deprotocols(2)smartcards(2)4}
```

For PACE with generic mapping and specified symmetric ciphers, [12] defines the following object identifiers: 

```
id-PACE-ECDH-GMOBJECTIDENTIFIER::={id-PACE2}
id-PACE-ECDH-GM-3DES-CBC-CBCOBJECTIDENTIFIER::={id-PACE-ECDH-GM1}
id-PACE-ECDH-GM-AES-CBC-CMAC-128OBJECTIDENTIFIER::={id-PACE-ECDH-GM2}
id-PACE-ECDH-GM-AES-CBC-CMAC-192OBJECTIDENTIFIER::={id-PACE-ECDH-GM3}
id-PACE-ECDH-GM-AES-CBC-CMAC-256OBJECTIDENTIFIER::={id-PACE-ECDH-GM4}
```

Here, elliptic curve points are always represented in uncompressed encoding. 

Federal Office for Information Security 

36 

Technical Guideline - Elliptic Curve Cryptography 

## **6. Standardized Domain Parameters** 

While this guideline supports domain parameters standardized by X9.62 [4] it is RECOMMENDED to use the domain parameters of the ECC Brainpool working group, which are standardized by the IETF RFC 5639 [32]: 

- `BrainpoolCurveNames CURVES ::= { {ID brainpoolP160r1} | {ID brainpoolP160t1} |` 

   - `{ID brainpoolP192r1} | {ID brainpoolP192t1} |` 

   - `{ID brainpoolP224r1} | {ID brainpoolP224t1} |` 

   - `{ID brainpoolP256r1} | {ID brainpoolP256t1} |` 

   - `{ID brainpoolP320r1} | {ID brainpoolP320t1} |` 

   - `{ID brainpoolP384r1} | {ID brainpoolP384t1} |` 

   - `{ID brainpoolP512r1} | {ID brainpoolP512t1}` 

```
...
```

```
}
```

The identifier `brainpoolP` _L_ `r` _j_ and `brainpoolP` _L_ `t` _j_ depend on two parameters: 

1. The integer _L_ denotes the bit length of the prime _p_ which is also the bit length of the order _n_ of the base point. 

2. The integer _j_ denotes the _j_ -th elliptic curve defined by Brainpool. Currently, only curves for _j_ = 1 are specified. 

The curve with curve identifier name `brainpoolP` _L_ `r` _j_ is F _p_ -isomorphic to the twisted curve with curve name `brainpoolP` _L_ `t` _j_ with coefficient _a_ = _−_ 3 mod _p_ . 

**Note:** In accordance to chapter 2.3.4, the subset of domain parameters with _L ≥_ 224 SHALL be used. 

The object identifier `versionOne` represents the tree containing the object identifiers for each set of elliptic curve domain parameters as specified in [32]. The object identifier has the following value: 

```
ecStdCurvesAndGenerationOBJECTIDENTIFIER::={
iso(1)identified-organization(3)teletrust(36)algorithm(3)
signature-algorithm(3)ecSign(2)ecStdCurvesAndGeneration(8)
```

```
}
```

```
ellipticCurveOBJECTIDENTIFIER::={ecStdCurvesAndGeneration1}
versionOneOBJECTIDENTIFIER::={ellipticCurve1}
brainpoolP160r1OBJECTIDENTIFIER::={versionOne1}
brainpoolP160t1OBJECTIDENTIFIER::={versionOne2}
brainpoolP192r1OBJECTIDENTIFIER::={versionOne3}
brainpoolP192t1OBJECTIDENTIFIER::={versionOne4}
```

Federal Office for Information Security 

37 

Technical Guideline - Elliptic Curve Cryptography 

```
brainpoolP224r1OBJECTIDENTIFIER::={versionOne5}
brainpoolP224t1OBJECTIDENTIFIER::={versionOne6}
brainpoolP256r1OBJECTIDENTIFIER::={versionOne7}
brainpoolP256t1OBJECTIDENTIFIER::={versionOne8}
brainpoolP320r1OBJECTIDENTIFIER::={versionOne9}
brainpoolP320t1OBJECTIDENTIFIER::={versionOne10}
brainpoolP384r1OBJECTIDENTIFIER::={versionOne11}
brainpoolP384t1OBJECTIDENTIFIER::={versionOne12}
brainpoolP512r1OBJECTIDENTIFIER::={versionOne13}
brainpoolP512t1OBJECTIDENTIFIER::={versionOne14}
```

Federal Office for Information Security 

38 

Technical Guideline - Elliptic Curve Cryptography 

## **Appendix** 

## **– A. The Signature Algorithm EC-KCDSA (Informative)** 

For informative reasons, this appendix describes the Elliptic Curve Korean Certificate Based Digital Signature Algorithm in conformance to [20]. The algorithm uses the public key _P_ A _[′]_[:=] [ _d[−]_ A[1][mod] _[ n]_[]] _[G]_[.] Let the value _z_ A be defined as _l_ leftmost bits of the sequence `FE2OS` ( _xP_ A) _∥_ `FE2OS` ( _yP_ A). In the following, _l_ ( _b_ ) denotes the length of a bit string _b_ . 

## **A.1. Signature Algorithm** 

A proceeds as follows to generate the EC-KCDSA signature ( _r, s_ ) on a message _M_ . 

**Input:** The following information is required as input: 

1. A’s private key _d_ A and the elliptic curve domain parameters ( _p, a, b, G, n, h_ ). 

2. The hash value _z_ A of the A’s certification data. 

3. The message _M_ to be signed. 

**Output:** The EC-KCDSA signature ( _r, s_ ) over _M_ . 

**Actions:** The following actions are performed: 

0. _e_ = H _τ_ ( _z_ A _∥ M_ ) 

1. _k_ = RNG( _{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ ) 

2. _Q_ = [ _k_ ] _G_ 

3. _c_ = H _τ_ ( `FE2OS` ( _xQ_ )) 

4. _r_ = `OS2I` ( _c_ ) 

5. _w_ = `OS2I` ( _c ⊕ e_ ) 

If _w ≥ n_ , set _w_ = _w − n_ . 

6. _s_ = ( _k − w_ ) _d_ A mod _n_ 

   - If _s_ = 0 goto 1. 

7. Output ( _r, s_ ) 

**Note:** The signature depends on the random number _k_ . If A signs the same document _M_ twice, both signatures differ with a very high probability. 

## **A.2. Verification Algorithm** 

B proceeds as follows to verify the received EC-KCDSA signature ( _r, s_ ) on _M_ . 

**Input:** The following input is necessary: 

1. A’s authentic public key _P_ A _[′]_[and][the][domain][parameters][(] _[p, a, b, G, n, h]_[).] 

2. The hash value _z_ A of the A’s certification data. 

3. The signed message _M_ . 

Federal Office for Information Security 

39 

Technical Guideline - Elliptic Curve Cryptography 

4. The EC-KCDSA signature ( _r, s_ ). 

**Output:** `True` , if the signature is valid, and `False` otherwise. 

**Actions:** The following actions are performed: 

1. Verify that _s ∈{_ 1 _,_ 2 _, . . . , n −_ 1 _}_ and _l_ ( `OS2BS` ( `I2OS` ( _r_ ))) _≤ τ._ 

If this is not the case, output `False` and terminate. 

2. _e_ = H _τ_ ( _z_ A _∥ M_ ) 

3. _w_ = `OS2I` ( `I2OS` ( _r_ ) _⊕ e_ ) mod _n_ 

4. _Q_ = [ _w_ ] _G_ + [ _s_ ] _P_ A 

5. _c_ = `FE2OS` ( _xQ_ )) 

6. _v_ = H _τ_ ( _c_ ) 

7. Output `True` if _v_ = _r_ , and `False` otherwise. 

Federal Office for Information Security 

40 

Technical Guideline - Elliptic Curve Cryptography 

## **Bibliography** 

- [1] BSI AIS 20. _Functionality classes and evaluation methodology for deterministic random number generators_ (Replaced by [3]). Federal Office for Information Security, 1999. Available at `https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ Zertifizierung/Interpretationen/ais20e_pdf.pdf?__blob=publicationFile` . 

- [2] BSI AIS 31. _Functionality classes and evaluation methodology for physical random number generators_ (Replaced by [3]). Federal Office for Information Security, 2001. Available at `https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ Zertifizierung/Interpretationen/ais31e_pdf.pdf?__blob=publicationFile` 

- [3] BSI. Appendix to AIS 20/31. _A proposal for: Functionality classes for random number generators_ . Federal Office for Information Security, 2011. Available at `https://www.bsi. bund.de/SharedDocs/Downloads/EN/BSI/Zertifizierung/Interpretationen/AIS20_ Functionality_classes_for_random_numbers_generators.pdf` 

- [4] ANSI X9.62. _Public Key Cryptography for the Financial Services Industry: The Elliptic Curve Digital Signature Algorithm (ECDSA)_ , 2005. 

- [5] ANSI X9.63. _Public Key Cryptography for the Financial Services Industry: Key Agreement and Key Transport Using Elliptic Curve Cryptography_ , 2011. 

- [6] BSI. Appendix to AIS 46. _Minimum Requirements for Evaluating Side-channel Attack Resistance of Elliptice Curve Implementations_ . Available at `https: //www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Zertifierung/Interpretation/ ECC-Guide.pdf?_blob=publicationFile` 

- [7] R. M. Avanzi, H. Cohen, C. Doche, G. Frey, T. Lange, K. Nguyen, and F. Vercauteren. _Handbook of Elliptic and Hyperelliptic Curve Cryptography_ . Chapman & Hall/CRC, 2005. 

- [8] J. Bender, M. Fischlin, D. K¨ugler. Security Analysis of the PACEv2 Key Agreement Protocol. ISC 2009. _Lecture Notes in Computer Science_ . Springer Verlag, 2009. 

- [9] I. F. Blake, G. Seroussi, N. P. Smart. Elliptic Curve Cryptography. Cambridge University Press, 1999. 

- [10] S. Bradner. _Key words for use in RFCs to indicate requirement levels (RFC2119)_ , 1999. Available at `http://www.ietf.org/rfc/rfc2119.txt` . 

- [11] BSI TR-02102. _Kryptographische Verfahren: Empfehlungen und Schl¨ussell¨angen_ , Version 1.0. Federal Office for Information Security, 2008. Available at `https://www.bsi.bund. de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/ BSI-TR-02102_V1_0_pdf.pdf?__blob=publicationFile` . 

- [12] BSI TR-03110. _Advanced Security Mechanisms for Machine Readable Travel Documents_ , Version 2.1, Parts 1-3. Federal Office for Information Security, 2012 Available at `https://www.bsi.bund.de/ContentBSI/EN/Publications/ Techguidelines/TR03110/BSITR03110.html` 

Federal Office for Information Security 

41 

Technical Guideline - Elliptic Curve Cryptography 

- [13] Federal Information Processing Standards Publication 180-3 (FIPS PUB 180-3). _Secure Hash Standard (SHS)_ , 2008. Available at `http://csrc.nist.gov/publications/fips/ fips180-3/fips180-3_final.pdf` . 

- [14] Geeignete Kryptoalgorithmen. _Bekanntmachung zur elektronischen Signatur nach dem Signaturgesetz und der Signaturverordnung ( Ubersicht[¨] ¨uber geeignete Algorithmen)_ . Bundesnetzagentur (Federal Network Agency for Electricity, Gas, Telecommunications, Post and Railway) Available at `http://www.bundesnetzagentur.de/cln_1912/EN/Areas/ ElectronicSignature/Publications/SuitableAlgorithms/suitable_algorithms_ node.html` . 

- [15] IEEE P1363. _Standard Specifications for Public Key Cryptography_ , 2000. 

- [16] IEEE P1363a. _Standard Specifications for Public Key Cryptography - Amendment 1: Additional Techniques_ , 2004. 

- [17] ISO/IEC 10116-2006. _Information technology – Security techniques – Modes of operation for an n-bit block cipher_ , 2006. 

- [18] ISO/IEC 10118-3-2004. _Information technology – Security techniques – Hash functions – Part 3: Dedicated hash functions_ , 2003. 

- _– –_ 

- [19] ISO/IEC 11770-3-2008. _Information technology Security techniques Key management Part 3: Mechanisms using asymmetric techniques_ , 2008. 

- _–_ 

- [20] ISO/IEC 14888-3-2006. _Information technology Security techniques Digital signatures with appendix – Part 3: Discrete logarithm based Mechanisms_ , 2006. 

- [21] ISO/IEC 14888-3-2006/Amd 1-2010. _Elliptic Curve Russian Digital Signature Algorithm, Schnorr Digital Signature Algorithm, Elliptic Curve Schnorr Digital Signature Algorithm, and Elliptic Curve Full Schnorr Digital Signature Algorithm_ , 2010. 

- [22] ISO/IEC 15946-1-2008. _Information technology – Security techniques – Cryptographic techniques based on elliptic curves – Part 1: General_ , 2008. 

- _–_ 

- [23] ISO/IEC 15946-2-2002 (Withdrawn). _Information technology Security techniques Cryptographic techniques based on elliptic curves – Part 2: Digital signatures_ , 2002. 

- _–_ 

- [24] ISO/IEC 15946-3-2002 (Withdrawn). _Information technology Security techniques Cryptographic techniques based on elliptic curves – Part 3: Key establishment_ , 2002. 

- [25] ISO/IEC 7816-4-2005. _Identification cards – Integrated circuit cards – Part 4: Organization, security and commands for interchange_ , 2005. 

- [26] ISO/IEC 7816-8-2004. _Identification cards – Integrated circuit cards – Part 8: Commands for security operations_ , 2004. 

- [27] A. Menezes. _Elliptic Curve Public Key Cryptosystems_ . Kluwer Academic Publishers, 1993. 

- [28] NIST. _Recommendation for Block Cipher Modes of Operation: The CMAC Mode for Authentication_ , Special Publication 800-38B, 2005. Available at `http://csrc.nist.gov/ publications/nistpubs/800-38B/SP_800-38B.pdf` . 

- [29] P. Nguyen and I. Shparlinski. The insecurity of the elliptic curve signature algorithm with partially known nonces. _Designs, Codes and Cryptography_ , 30(2):201–217, 2003. 

Federal Office for Information Security 

42 

Technical Guideline - Elliptic Curve Cryptography 

- [30] W. Polk, R. Housley, and L. Bassham. _Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile (RFC3279)_ , 2002. Available at `http://www.ietf.org/rfc/rfc3279.txt` . 

- [31] S. Turner, D. Brown, K. Yiu, R. Housley and T. Polk. _Elliptic Curve Cryptography Subject Public Key Information (RFC5480)_ , 2009. Available at `http://www.ietf.org/rfc/ rfc5480.txt` . 

- [32] M. Lochter, J. Merkle. _Elliptic Curve Cryptography (ECC) Brainpool Standard Curves and Curve Generation (RFC5639)_ , 2010. Available at `http://www.ietf.org/rfc/rfc5639. txt` . 

- [33] C. P. Schnorr. Efficient Signature Generation on Smart Cards. Journal of Cryptology 4(4), pp. 161-174, 1991. 

- [34] X. Wang, Y.L. Yin, and H. Yu. Collision search attacks on SHA-1. In _Proceedings of Crypto 2005_ . Springer Verlag, 2005. 

Federal Office for Information Security 

43 


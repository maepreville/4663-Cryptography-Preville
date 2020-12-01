  ## A07 – Finding Primes
### Mae-Jeanne Preville 
### Description:
Your assignment is to do a lit review of methods to find prime numbers in any and all of the above categories. There are plenty of algorithms to choose from, however, try and find algorithms other than obvious ones. That implies you need to dig a little bit and not turn in the first / easily locatable algorithms when you start searching. You should list a minimum of 7 algorithms with short descriptions of each including the category in which they exist. You need to find at least 2 deterministic algorithms, and the other 5 can be in both of the other two categories.


### 1. Certification:
#### Pratt Certificates:
The Pratt certificate is a primality certificate due to Fermat's little theorem converse. In 1975, Pratt showed that by applying Lehmer's primality heuristic recursively, it could be made a nondeterministic procedure to the factors of  . As a result, became the first to demonstrate that the resulting tree implies that prime factorization lies in the complexity class NP.
A prime (P) can be proven when the prime factors of P-1 along with a witness w such that   but   for each prime divisor   of   is displayed. These primes (q) are then proven to be prime in the same way, however 2 is assumed to be prime without having to be proof of it.

#### Atkin-Goldwasser-Kilian-Morain Certificates:
Atkin-Goldwasser-Kilian-Morain certificates are the type of certificates generated and verified by elliptic curve primality proving systems. It is used for numbers above a certain limit (  by default), while Pratt certificates are for smaller numbers. Atkin-Goldwasser-Kilian-Morain certificates are based on Goldwasser and Kilian.
A recursive primality certificate for a prime. The certificate consists of a list of
1. A point on an elliptic curve for some numbers and.
2. A prime with, such that for some other number  and with, is the identity on the curve, but   is not the identity. This guarantees primality of   by a theorem of Goldwasser and Kilian (1986).
3. Each   has its recursive certificate following it. So if the smallest   is known to be prime, all the numbers are certified prime up the chain.

### 2. Compositeness:
#### Fermat Primality Test:
The Fermat primality test is a primality test, giving a way to test if a number is a prime number, using Fermat's little theorem and modular exponentiation.
Fermat's Little Theorem states that if a is relatively prime to a prime number p, then ap−1≡1modp.
This primality test is known to be the simplest probabilistic primality test, and it is often used if a rapid screening of numbers is needed.
It can be determined whether the integer is composite if the result is different from 1, or possibly prime if the result is 1. If an−1 (modulo n) is 1 but n is not prime, then the integer is called a pseudoprime to base a. Usually, we observe that, if an−1 (modulo n) is 1 (then n is usually prime).

#### Miller-Rabin and Solovay-Strassen Primality Test:
The Miller-Rabin test is the most commonly used pseudoprimality test. However, it is known to have errors in some circumstances. The Miller–Rabin primality test and Solovay–Strassen primality test detect all composites (for every composite number n, at least 3/4 (Miller–Rabin) or 1/2 (Solovay–Strassen) of numbers a are witnesses of compositeness of n). These are also compositeness tests.

#### Frobenius Primality Test:
Due to the difficulty in proving that a number is prime, the usual recourse is a pseudoprimality test. This test is generally fast and easy but it may produce an incorrect answer (with very small probability). The Frobenius test is an extension of and improvement on the Lucas test of a previous exercise. The Frobenius test is a generalization of the Lucas pseudoprime test. It is common to combine it with a Miller-Rabin pseudoprime test to just a few small bases.

### 3. Deterministic:
#### AKS Primality Test:
The AKS primality test was the first that can provably determine whether any given number is prime or composite within polynomial time. It does not rely on the generalized Riemann hypothesis, or any mathematical conjecture nor any field of analysis.
The algorithm is as follows: 
Input: integer n > 1.
1.	Check if n is a perfect power: if n = ab for integers a > 1 and b > 1, output composite.
2.	Find the smallest r such that ordr(n) > (log2 n)2. (if r and n are not coprime, then skip this r)
3.	For all 2 ≤ a ≤ min (r, n−1), check that a does not divide n: If a|n for some 2 ≤ a ≤ min (r, n−1), output composite.
4.	If n ≤ r, output prime.
5.	For a = 1 to   do
if (X+a)n≠ Xn+a (mod Xr − 1,n), output composite;
6.	Output prime.

#### Miller Test:

### Sources
Weisstein, Eric W. "Pratt Certificate." From MathWorld--A Wolfram Web Resource. https://mathworld.wolfram.com/PrattCertificate.html
Weisstein, Eric W. "Atkin-Goldwasser-Kilian-Morain Certificate." From MathWorld--A Wolfram Web Resource. https://mathworld.wolfram.com/Atkin-Goldwasser-Kilian-MorainCertificate.html
"Pratt Certificates of Primality"
http://demonstrations.wolfram.com/PrattCertificatesOfPrimality/
Wolfram Demonstrations Project
Published: March 7 2011
Liskov M. (2005) Fermat Primality Test. In: van Tilborg H.C.A. (eds) Encyclopedia of Cryptography and Security. Springer, Boston, MA . https://doi.org/10.1007/0-387-23483-7_160
V. R. Pratt, “Every prime has a succinct certificate”, SIAM J. Computing 4 (1975), 214–220.
https://programmingpraxis.com/2012/11/13/frobenius-primality-test/




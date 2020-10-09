## A04 - ADFGX Implementation
### Mae-Jeanne Preville 
### Description:

Ultimately write a program (in language of choice) that implements the steps described in this document to implement the ADFGX cipher.
Your program should include functions that implement various components of the cipher to encrypt and decrypt. Basically, organize your code into functions and / or classes.
Any characters that are not A-Z can be ignored and filtered out. But they need to be handled and should not break your program.
Use of external libraries is OK as long as you document thier use and as long as you still implement the actual algorithm. (e.g. a library to clean text is ok).

Key components are:
1) ENCRYPTION (all done for you in pieces):
Reading parameters from command line to set up your program.
Building the polybius square using keyword1 (really the dictionary lookup is what it is).
Building the columnar transposition matrix and fractionating the message using keyword2.
Pulling the message out of this second matrix and writing it to a file.
2) DECRYPTION
All on you! All the programming tools you need are in this repo.

### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [cipher1frequency.txt](./cipher1frequency.txt)   | Number of times letters occur in cipher 1    |
|   2   | [cipher2frequency.txt](./cipher2frequency.txt)   | Number of times letters occur in cipher 2    |
|   3   | [frequency.py](./frequency.py)           | Letter frequency code.                       |
|   4   | [decrypted_1.txt](./decrypted_1.txt)     | Decrypted 1 text.                            |
|   5   | [decrypted_2.txt](./decrypted_2.txt)     | Decrypted 2 text.                            |


### Instructions

- Python was used for this project.

### Sources

- Counton.org
  - http://www.counton.org/explorer/codebreaking/frequency-analysis.php
- Practicalcryptography.com: 
  - http://practicalcryptography.com/ciphers/simple-substitution-cipher/

I used these sources to give me a better understanding of substitution ciphers.


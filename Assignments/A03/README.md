## A03 - Frequency Analysis
### Mae-Jeanne Preville 
### Description:

Two files were encrypted using a "substitution" cipher, and a list of letters were randomly shuffled multiple times. However, the key was never given therefore the process cannot be reversed. Help is needed to decipher these messages. It is not a shift cipher, so you cant brute force the shift value! So the only way to get these two messages vital to the safety of earth is to run a frequency analysis on them. 

First: Run a frequency analysis on the file ciphertext_1.txt and substitute each letter based on the calculated frequency using the table below. Punctuation is left for readability. All words are english words and the frequency distribution is a perfect match for the graph at the top. The text is common enough for you to deduce what it is, and google the answer.

Second: Do the same for ciphertext_2.txt and substitute again based on frequency. This one doesn't line up perfectly, but close enough to not make it too hard. This one is not as common as the first. But it is part of an extremely famous book. And part of a famous movie rant. So, good luck.

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

### Working

#### Cipher 1

<img src="https://user-images.githubusercontent.com/54781760/93484219-42232000-f8c7-11ea-92d2-0adb1ee579e2.jpg"  width=387 height=387/>


#### Cipher 2

<img src="https://user-images.githubusercontent.com/54781760/93485756-08531900-f8c9-11ea-9c51-99e7be0d9012.jpg"  width=387 height=387/>

### Sources

- Counton.org
  - http://www.counton.org/explorer/codebreaking/frequency-analysis.php
- Practicalcryptography.com: 
  - http://practicalcryptography.com/ciphers/simple-substitution-cipher/

I used these sources to give me a better understanding of substitution ciphers.

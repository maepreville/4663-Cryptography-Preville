import sys
import os

alphabet = [chr(x+97) for x in range(26)]


class Vigenere:
    def __init__(self,key=None,text=None):
        self.ciphertext = ''
        self.deciphertext = ''
        self.plaintext = ''
        self.key = ''

        if text:
            self.plaintext = text
        
        if key:
            self.key = key

    def setKey(self,key):
        self.key = key

    def encrypt(self,text=None):
        if not text == None:
            self.plaintext = text
        
        i = 0
        for letter in self.plaintext:
            if letter in alphabet:
                #print(f"{letter} {self.key[i]}")
                a = ord(letter) - 97
                b = ord(self.key[i]) - 97

                self.ciphertext += chr(((a + b) % 26) + 97)

                i = (i + 1) % len(self.key)
            else:
                self.ciphertext += letter
        

    def decrypt(self,text=None):
        if not text == None:
            self.plaintext = text
        
        i = 0
        for letter in self.plaintext:
            if letter in alphabet:
                #print(f"{letter} {self.key[i]}")
                a = ord(letter) - 97
                b = ord(self.key[i]) - 97

                self.deciphertext += chr(((a - b) % 26) + 97)

                i = (i + 1) % len(self.key)
            else:
                self.deciphertext += letter
    
    #def decrypt(self):
     #   pass


if __name__=='__main__':
    V = Vigenere('rhythm')

    #Encrypted message
    V.encrypt("the sky is green")
    print("Encrypted text: ")
    print(V.ciphertext)
    #print(V.ciphertext[2:])

    #Decrypted message
    print('') #Blank line
    V.decrypt(V.ciphertext)
    print("Decrypted text: ")
    print(V.deciphertext)
    

import sys
import os
import requests

alphabet = [chr(x+97) for x in range(26)]

class Frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.sort_freq = None
        self.total = 0

        for l in alphabet:
            self.freq[l] = 0
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1
                self.total += 1

        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def print(self):
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]}:{f[1]}")
        else:
            print(self.freq)

    def print_table(self):
        for i in range(5):
            for j in range(5):
                if j > 0:
                    print(" , ",end="")
                pct = (int(self.sort_freq[i*5+j][1])/self.total)*100
                pct = "{:5.2f}".format(pct)
                print(f"{self.sort_freq[i*5+j][0]}:{pct}%",end=" ")
            print("")


    def getNth(self,n):
        if self.sort_freq:
            return self.sort_freq[n][0]

        return None


if __name__=='__main__':
  
  f = open("ciphertext1.txt","r")
 
  text = f.read()
  
  print(" ")  
  print("Calculating frequency...")

  F = Frequency()

  F.count(text)

  F.print_table()

  print(F.getNth(2))

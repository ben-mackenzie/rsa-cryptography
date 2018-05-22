'''
1) Ben Mackenzie
2) Date: Created on Apr 12, 2018
3) Program specifications
I. Purpose of the program and any information pertaining to its description
This program explores RSA encryption and its underlying principles, 
including primality, managing large numbers, and file reading.

II. Input
This program takes as inputs several numbers used for encryption and decryption,
and also encrypted messages.

III. Output
The output of this program is a decoded and translated message.

IV. Bugs or Implemented Test Cases; and, any theoretical follow-up including assignment questions to be turned in for grading
A preliminary test message of 10 characters was used to build and test this program initially,
while a longer message with blank spaces and multiple cases was tested after.
'''

from scanner import Scanner
import helpers
import sys

def driver():
    #definitions of e, p, q
    inFile = Scanner("in.txt")
    ggg = inFile._next_str()  #e-
    e = inFile._next_int()
    ggg = inFile._next_str()  #p=
    p = inFile._next_int()
    ggg = inFile._next_str()  #q=
    q = inFile._next_int()
    #test for valid e
    if (p-1)%e==0 or (q-1)%e==0: 
        print("I must choose another e from teacher's website")
    else: 
        print("gcd(e,(p-1)(q-1))=1")
    #n calculation
    n = p*q 
    print("p="+str(p)+" q="+str(q))
    #d calculation
    d = helpers.BobCalculateD((p-1)*(q-1), e)
    print("d="+str(d))
    #message to encrypt
    message = 'The camera is hidden in the bushes'
    
    #encryption
    mStrList = helpers.getCode(message)
    cList = []
    for string in mStrList:    
        mInt = int(string)  #work only for 9-10 letters long    
        cList.append(mInt**e % n)             
    #c is encrypted message to post   nBI n-to post
    mStr = ('').join(mStrList)
    m = int(mStr)
    c = (' ').join([str(e) for e in cList])
    print("e= " + str(e))
    print("n= " + str(n))
    print("m= " + str(m))
    print("c= " + str(c))
    
    #writing encrypted message to file
    sys.stdout = open("encrypt.rsa", "w")
    print(c)
    sys.stdout.close()
    
    #reading encrypted file
    cypherFile = open("encrypt.rsa", "r")
    cypherBlocks = cypherFile.read().strip().split(' ')
    cypherFile.close()
    
    #decrypting text and writing to file
    sys.stdout = open("decrypt.rsa", "w")
    decryptedList = []
    for block in cypherBlocks:
        decryptedBlock = pow(int(block), d, n) 
        if len(str(decryptedBlock)) < 20:
            decryptedBlock = '0' + str(decryptedBlock)
        else:
            decryptedBlock = str(decryptedBlock)
        decryptedList.append(decryptedBlock)
    decryptedText = ('').join(decryptedList)
    helpers.PrintLetters(decryptedText)
    sys.stdout.close()


if __name__ == '__main__':
    driver()

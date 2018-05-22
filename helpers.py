'''
Created on Apr 12, 2018

@author: benjaminmackenzie
with help from https://brilliant.org/wiki/extended-euclidean-algorithm/
'''

import random

def gcd(e, m):
    """verifies that e is relatively prime to (p-1)(q-1) = m"""
    x = e
    y = m
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

def BobCalculateD(a, b):
    """returns d = y using exponent b and a = (p-1)(q-1)"""
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return y

def modular_pow(base, exponent, modulus):
    """takes an encoded group of 10 letters as the 'base' input,
    along with exponent 'e' and modulus 'n' and returns the 
    encrypted group of 10 letters"""
    if modulus == 1: 
        return 0
    #Assert :: (modulus - 1) * (modulus - 1) does not overflow base
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        #exponent = exponent >> 1
        base = (base * base) % modulus
    return result
     
def PrintLetters(string):
    '''Takes in a decrypted message as one long number,
    considers the numbers two at a time from back to front, 
    converting them to letters and adding the letters to output string.'''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    iters = len(string) // 2
    reversed = ''
    #start splitting from the back in case the original encryption had leading zero
    end = len(string) - 1
    start = end - 1
    while iters > 0:
        second = string[end]
        if end == 0:
            index = int(second) - 1
        else:
            first = string[start]
            index = int(first + second) - 1
        codedLetter = alph[index]
        reversed += codedLetter
        start -= 2
        end -= 2
        iters -= 1
    while reversed[0] == 'x':
        reversed = reversed[1::]
    print(reversed[::-1])
       
def getCode(string):
    '''converts English message to unencrypted blocks of 10 numbers
    with x's filling empty spaces in blocks of letters shorter than 10.
    Returns a list of converted blocks of 20 digits'''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    bet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    parsedString = ('').join(string.split(' ')).strip()
    subStrings = []
    coded = []
    iters = len(string) // 10
    start = 0
    end = 10
    #splits the parsed string into blocks of ten letters and stores them
    while iters > 0:
        subString = parsedString[start:end]
        subStrings.append(subString)
        start += 10
        end += 10
        iters -= 1
    #converts every substring of 10 letters into a 20 digit number
    for block in subStrings:
        #pads short strings with x's at end
        while len(block) < 10:
            block += 'x'
        convertedBlock = ''    
        for c in block:
            if c in alpha:
                c = alpha.index(c) + 1
                if c < 10:
                    c = '0' + str(c)
                else:
                    c = str(c)
            elif c in bet:
                c = bet.index(c) + 1
                if c < 10:
                    c = '0' + str(c)
                else:
                    c = str(c)
            convertedBlock += c
        coded.append(convertedBlock)
    return coded
    
def findPrime():    
    '''Returns a random prime number of length 19,
    used in conjunction with rabinMiller'''
    while True:
        num = random.randrange(2**(18), 2**(19))
        if rabinMiller(num):
            return num
    
def rabinMiller(num):
    '''Returns True if num is a prime number.
    from https://inventwithpython.com/rabinMiller.py'''
    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1
    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
                    

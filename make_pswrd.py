#!/bin/python3
from random import *
import re

def r():
    return randrange(1,7,1)

def raw_pwrd():
    return [[r() for x in range(5)] for y in range(6)]

def scrub(data):
    ls = []
    for lst in data:
        scrubbed = ""
        for elem in lst:
            scrubbed += str(elem)
        ls.append(scrubbed +"\t(.*)")
    return ls

def get_pwrd(ps, dware):
    word = ""
    for pat in ps:
        m = re.search(pat, dware)
        if m:
            word = word + m.group(1)
    return word

def upper_case( pwrd ):
    a = randrange(0, len(pwrd)-1)
    b = randrange(a, len(pwrd))
    newpwrd = pwrd[0:a]+(pwrd[a:b].upper())+pwrd[b:]
    return newpwrd


if __name__ == "__main__":
    ps = scrub( raw_pwrd() )
    dware = "/Path/to/your/copy/of/diceware.txt"
    f = open(dware, "r")
    words = f.read()
    password = upper_case(get_pwrd( ps, words ))
    print( password )    

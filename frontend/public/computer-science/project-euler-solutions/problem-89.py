import os
import sys
import numpy as np
from collections import Counter



scriptdir = os.path.abspath(os.path.dirname(sys.argv[0]))

src_filename = os.path.join(scriptdir, "data/p089_roman.txt")

file = open(src_filename, "r")

src = file.read()



all_numerals = [k for k in  src.split("\n")]

numeralValue = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

def romanNumeralToInt(rs):
    num = 0
    for i in range(len(rs)):
        if i == len(rs) - 1:
            num += numeralValue[rs[i]]
        else:
            if numeralValue[rs[i]] < numeralValue[rs[i+1]]:
                num -= numeralValue[rs[i]]
            else:
                num += numeralValue[rs[i]]
    return num

print(romanNumeralToInt("MMDCCCLXXVIII"))


minimalWay = {1 : "I", 4: "IV", 5: "V", 9: "IX", 18: "XVIII",
              10: "X", 40 : "XL", 50 : "L", 90 : "XC", 180: "CLXXX",
              100 : "C", 400 : "CD", 500 : "D", 900: "CM", 1800: "MDCCC", 1000 : "M"}

def validRomanNumeral(numeral):
    preceedingNumerals = {"C" : 0, "X" : 0, "I" : 0, "V" : 0, "L" : 0, "D" : 0}
    for i in range(len(numeral)):
        if numeral[i] in "V L D":
            preceedingNumerals[numeral[i]] += 1
            if preceedingNumerals[numeral[i]] > 1:
                return False
        if i!=len(numeral)-1:
            if numeralValue[numeral[i]] < max([numeralValue[n] for n in numeral[i+1:]]):
                if numeral[i] not in "C X I":
                    return False
                preceedingNumerals[numeral[i]] += 1
    if  max(preceedingNumerals.values()) > 1:
        return False
    return True

def findMinimalWay(k):
    if k in minimalWay:
        minimalWay[k]
    for n in range(1, k+1):
        if n not in minimalWay:
            possibleSums = [(i, n-i) for i in range(1, n//2 + 1)]
            minimalWay[n] = min(filter(validRomanNumeral, [minimalWay[t[1]]+minimalWay[t[0]] for t in possibleSums]), key=len)
    return minimalWay[k]

print(findMinimalWay(969))

difL = []

for numeral in all_numerals:
    difL.append(len(numeral) - len(findMinimalWay(romanNumeralToInt(numeral))))

print sum(difL)


# -*- coding: utf-8 -*-

"""Counvert to and from Roman numerals"""

#Defind Exceptions
import re
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass


MAX_ROMAN_NUMERAL = 4999

romanNumeralMap = (('M', 1000),
                   ('CM', 900),
                   ('D', 500),
                   ('CD', 400),
                   ('C', 100),
                   ('XC', 90),
                   ('L', 50),
                   ('XL', 40),.
                   ('X', 10),
                   ('IX', 9),
                   ('V', 5),
                   ('IV', 4),
                   ('I', 1))

toRomanTable = [ None ]
fromRomanTable = {}

def toRoman(n):
    """数字转换罗马字符"""
    if not (0 < n <= MAX_ROMAN_NUMERAL):
        raise OutOfRangeError, 'number out of range (must be 1..%s)' % MAX_ROMAN_NUMERAL
    if int(n) <> n:
        raise NotIntegerError, 'non-integers can not be converted'
    return toRomanTable[n]


def fromRoman(s):
    """罗马字符转换数字"""
    if not s:
        raise InvalidRomanNumeralError, 'Input can not blank'
    if not fromRomanTable.has_key(s):
        raise InvalidRomanNumeralError, 'Invalid Roman Numeral: %s' % s
    return fromRomanTable[s]

def toRomanDynamic(n):
    result = ''
    for numeral, integer in romanNumeralMap:
        if n >= integer:
            result = numeral
            n -= integer
            break
    if n > 0:
        result += toRomanTable[n]
    return result

def fillLookupTables():
    for integer in range(1,MAX_ROMAN_NUMERAL + 1):
        romanNumber = toRomanDynamic(integer)
        toRomanTable.append(romanNumber)
        fromRomanTable[romanNumber] = integer

fillLookupTables()





# if __name__ == '__main__':
#      input = raw_input('Enter your convert numeral:\n')
#     if type(input) == type('a'):
#         print fromRoman(str(input))
#     if type(input) == type(2):
#         print toRoman(int(input))
#     n_input = raw_input('Enter your number:\n')
#     s_input = raw_input('Enter your Roman numeral:\n')
#     print toRoman(int(n_input))
#     print fromRoman(s_input)
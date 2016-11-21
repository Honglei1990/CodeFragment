#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Counvert to and from Roman numerals"""

#Defind Exceptions
import re
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass



romanNumeralMap = (('M', 1000),
                   ('CM', 900),
                   ('D', 500),
                   ('CD', 400),
                   ('C', 100),
                   ('XC', 90),
                   ('L', 50),
                   ('XL', 40),
                   ('X', 10),
                   ('IX', 9),
                   ('V', 5),
                   ('IV', 4),
                   ('I', 1))

def toRoman(n):
    """数字转换罗马字符"""
    if not (0 < n < 4000):
        raise OutOfRangeError, 'number out of range (must be 1..3999)'
    if int(n) <> n:
        raise NotIntegerError, 'non-integers can not be converted'

    result = ''
    for numeral, integer in romanNumeralMap:
        while n >=  integer:
            result += numeral
            n -= integer
    return result


romanNumeralPatten = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'

def fromRoman(s):
    """罗马字符转换数字"""
    if not s:
        raise InvalidRomanNumeralError, 'Input can not blank'
    if not re.search(romanNumeralPatten, s):
        raise InvalidRomanNumeralError, 'Invalid Roman Numeral: %s' % s

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result




if __name__ == '__main__':
#      input = raw_input('Enter your convert numeral:\n')
#     if type(input) == type('a'):
#         print fromRoman(str(input))
#     if type(input) == type(2):
#         print toRoman(int(input))
    n_input = raw_input('Enter your number:\n')
    s_input = raw_input('Enter your Roman numeral:\n')
    print toRoman(int(n_input))
    print fromRoman(s_input)
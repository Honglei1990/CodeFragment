#!/usr/bin/python
# -*- coding:utf-8 -*-

import roman1
import unittest



class KnownValues(unittest.TestCase):
    knownValues = ((1, 'I'),
                   (2, 'II'),
                   (3, 'III'),
                   (4, 'IV'),
                   (5, 'V'),
                   (6, 'VI'),
                   (7, 'VII'),
                   (8, 'VIII'),
                   (9, 'IX'),
                   (10, 'X'),
                   (50, 'L'),
                   (100, 'C'),
                   (500, 'D'),
                   (1000, 'M'),
                   (31, 'XXXI'),
                   (148, 'CXLVIII'),
                   (294, 'CCXCIV'),
                   (312, 'CCCXII'),
                   (421, 'CDXXI'),
                   (528, 'DXXVIII'),
                   (621, 'DCXXI'),
                   (782, 'DCCLXXXII'),
                   (870, 'DCCCLXX'),
                   (941, 'CMXLI'),
                   (1043, 'MXLIII'),
                   (1110, 'MCX'),
                   (1226, 'MCCXXVI'),
                   (1301, 'MCCCI'),
                   (1485, 'MCDLXXXV'),
                   (1509, 'MDIX'),
                   (1607, 'MDCVII'),
                   (1754, 'MDCCLIV'),
                   (1832, 'MDCCCXXXII'),
                   (1993, 'MCMXCIII'),
                   (2074, 'MMLXXIV'),
                   (2152, 'MMCLII'),
                   (2212, 'MMCCXII'),
                   (2343, 'MMCCCXLIII'),
                   (2499, 'MMCDXCIX'),
                   (2574, 'MMDLXXIV'),
                   (2646, 'MMDCXLVI'),
                   (2723, 'MMDCCXXIII'),
                   (2892, 'MMDCCCXCII'),
                   (2975, 'MMCMLXXV'),
                   (3051, 'MMMLI'),
                   (3185, 'MMMCLXXXV'),
                   (3250, 'MMMCCL'),
                   (3313, 'MMMCCCXIII'),
                   (3408, 'MMMCDVIII'),
                   (3501, 'MMMDI'),
                   (3185, 'MMMCLXXXV'),
                   (3250, 'MMMCCL'),
                   (3313, 'MMMCCCXIII'),
                   (3408, 'MMMCDVIII'),
                   (3501, 'MMMDI'),
                   (3610, 'MMMDCX'),
                   (3743, 'MMMDCCXLIII'),
                   (3844, 'MMMDCCCXLIV'),
                   (3888, 'MMMDCCCLXXXVIII'),
                   (3940, 'MMMCMXL'),
                   (3999, 'MMMCMXCIX'),
                   (4000, 'MMMM'),
                   (4500, 'MMMMD'),
                   (4888, 'MMMMDCCCLXXXVIII'),
                   (4999, 'MMMMCMXCIX')
                   )
    def testToRomanKnownValues(self):
        for integer, numeral in self.knownValues:
            result = roman1.toRoman(integer)
            self.assertEqual(numeral, result)


class ToRomanBadInput(unittest.TestCase):
    def testTooLarge(self):
        """转换超出范围"""
        self.assertRaises(roman1.OutOfRangeError, roman1.toRoman, 5000)

    def testZero(self):
        """输入为0的"""
        self.assertRaises(roman1.OutOfRangeError, roman1.toRoman, 0)

    def testNegative(self):
        """输入为负数的"""
        self.assertRaises(roman1.OutOfRangeError, roman1.toRoman, -1)

    def testNonInteger(self):
        """输入为小数的"""
        self.assertRaises(roman1.NotIntegerError, roman1.toRoman, 0.5)

class FromToRomanBadInput(unittest.TestCase):
    def testTooManyRepeatedNumerals(self):
        """不能出现太多重复的数字"""
        for s in ('MMMMM', 'DD', 'LL', 'VV', 'CCCC', 'XXXX', 'IIII'):
            self.assertRaises(roman1.InvalidRomanNumeralError, roman1.fromRoman, s)

    def testRepeatedPairs(self):
        """不能出现重复的数字"""
        for s in ('CMCM', 'CDCD', 'XLXL', 'XCXC', 'IVIV', 'IXIX'):
            self.assertRaises(roman1.InvalidRomanNumeralError, roman1.fromRoman, s)

    def testMalformedAntecedent(self):
        """畸形的测试"""
        for s in ('IIMXCC', 'VX', 'DCM' ,'CMM', 'IXIV', 'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman1.InvalidRomanNumeralError, roman1.fromRoman, s)

    def testBlank(self):
        """previous test cases omitted for clarity (they haven't changed)"""
        self.assertRaises(roman1.InvalidRomanNumeralError, roman1.fromRoman, '')

class SanityCheck(unittest.TestCase):
    def testSanity(self):
        """fromRoman(toRoman(n)) == n  for all n"""
        for integer in range(1,5000):
            numeral = roman1.toRoman(integer)
            result = roman1.fromRoman(numeral)
            self.assertEqual(integer, result)

class CaseCheck(unittest.TestCase):
    def testToRomanCase(self):
        """toRoman should always return uppercase"""
        for i in range(1,5000):
            numeral = roman1.toRoman(i)
            self.assertEqual(numeral, numeral.upper())

    def testFromRomanCase(self):
        """fromRoman should only accept uppercase input"""
        for integer in range(1,5000):
            numeral = roman1.toRoman(integer)
            roman1.fromRoman(numeral.upper())
            self.assertRaises(roman1.InvalidRomanNumeralError, roman1.fromRoman, numeral.lower())


if __name__ == "__main__":
    unittest.main()
























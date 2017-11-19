class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tens = ['I', 'X', 'C', 'M', '']
        fives = ['V', 'L', 'D', '']
        roman = ''
        i = 0
        while True:
            num, digit = num // 10, num % 10
            one = tens[i]
            digit, left, right = [digit, '', fives[i]] if digit < 5 else [digit-5, fives[i], tens[i+1]]
            digit = digit % 5
            if digit == 4:
                s = one + right
            else:
                s = left + one * digit
            roman = s + roman
            if num == 0:
                break
            i += 1
        return roman

class Solution2(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ref = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
               ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
               ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
               ['', 'M', 'MM', 'MMM']]
        n = num
        i, s = 0, ''
        while n > 0:
            s = ref[i][n%10] + s
            n /= 10
            i += 1
        return s

class Solution3(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        n, i, res = num, 0, ''
        while n > 0:
            n, digit = n/10, n%10
            if digit < 4:
                s = ones[i]*digit
            elif digit == 4:
                s = ones[i]+fives[i]
            elif digit < 9:
                s = fives[i]+ones[i]*(digit-5)
            else:
                s = ones[i]+ones[i+1]
            res = s + res
            i += 1
        return res
                
                 
        
        
if __name__ == "__main__":
    from leetcodelib import test
    arguments = [1, 3, 5, 10, 23, 47, 94, 3297]
    answers = ['I', 'III', 'V', 'X', 'XXIII', 'XLVII', 'XCIV', 'MMMCCXCVII']
    test(Solution3().intToRoman, arguments, answers)
    
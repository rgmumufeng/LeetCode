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

if __name__ == "__main__":
    from leetcodelib import test
    arguments = [1, 3, 5, 10, 23, 47, 94, 3297]
    answers = ['I', 'III', 'V', 'X', 'XXIII', 'XLVII', 'XCIV', 'MMMCCXCVII']
    test(Solution().intToRoman, arguments, answers)
    
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
            
        slist = [""] * numRows
        i, direction = 0, 1
        for c in s:
            slist[i] += c
            if i == 0 and direction == -1:
                direction = 1
            elif i == numRows-1 and direction == 1:
                direction = -1
            i += direction
        
        return "".join(slist)
    
    
class Solution2(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        strlist = ["" for _ in xrange(numRows)]
        i, direction = 0, 1
        for c in s:
            strlist[i] += c
            i += direction
            if i == 0 or i == numRows-1:
                direction = -direction
        return "".join(strlist)

if __name__ == "__main__":
    arguments = [("PAYPALISHIRING", 3)]
    answers = ["PAHNAPLSIIGYIR"]
    from leetcodelib import test
    test(Solution().convert, arguments, answers)

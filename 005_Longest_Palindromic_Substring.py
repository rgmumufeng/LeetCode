class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def findpalin(center, odd=True):
            i = center-1 if odd else center
            j = center+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                    i, j = i-1, j+1
            return i+1, j
        
        h0, t0 = 0, 0
        for center in xrange(len(s)):
            h1, t1 = findpalin(center, True)
            h2, t2 = findpalin(center, False)
            h, t = (h1, t1) if t1-h1 > t2-h2 else (h2, t2)
            h0, t0 = (h, t) if t-h > t0-h0 else (h0, t0)
        return s[h0:t0]


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1: return s
            
        def is_palin(i, j):
            if i < 0: return False
            while i <= j:
                if s[i] != s[j]: return False
                i, j = i+1, j-1
            return True
        
        i0, j0 = 0, 0
        for j in xrange(1, len(s)):
            if j-j0 == 1 and i0 > 0 and s[j] == s[i0-1]:
                i0, j0 = i0-1, j
                #print "continue palin", s[i0:j0+1]
            else:
                for k in xrange(j-j0+i0-2, j-j0+i0+1):
                    if is_palin(k, j):
                        i0, j0 = k, j
                        break
                #print "current palin", s[i0:j0+1]
        return s[i0:j0+1]


if __name__ == "__main__":
    from leetcodelib import run_testfile
    testfile = __file__.replace('.py', '.yaml')
    run_testfile(testfile, Solution1().longestPalindrome)
    run_testfile(testfile, Solution2().longestPalindrome)
    

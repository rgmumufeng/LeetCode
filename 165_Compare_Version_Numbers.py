class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(x) if x else 0 for x in version1.split(".")]
        v2 = [int(x) if x else 0 for x in version2.split(".")]
        for i in xrange(max(len(v1), len(v2))):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            if a > b :
                return 1
            elif a < b:
                return -1
        return 0
    
class Solution2(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            a, i = self.readone(version1, i)
            b, j = self.readone(version2, j)
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
        
    def readone(self, version, i):
        n = 0
        while i < len(version) and version[i] != ".":
            n = n*10+int(version[i])
            i += 1
        if i >= len(version):
            return (n, i)
        else:
            return (n, i+1)

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    return

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buf4 = ["" for _ in xrange(4)]
        i = 0
        while i < n:
            shift = min(read4(buf4), n-i, 4)
            if not shift:
                break
            buf[i:i+shift] = buf4[:shift]
            i += shift
        return i

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution().read, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
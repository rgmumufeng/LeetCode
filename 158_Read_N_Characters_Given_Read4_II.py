def read4(buf):
    return

class Solution(object):
    def __init__(self):
        self.buf = ["" for _ in xrange(4)]
        self.h = self.t = 4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.h < self.t:
                buf[i] = self.buf[self.h]
                i += 1
                self.h += 1
            elif self.t == 4:
                self.h = 0
                self.t = read4(self.buf)
            else:
                break
        return i
            
                
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.mins = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.values.append(x)
        if not self.mins or self.mins[-1] > x:
            self.mins.append(x)
        else:
            self.mins.append(self.mins[-1])

    def pop(self):
        """
        :rtype: void
        """
        if self.values:
            self.values.pop()
            self.mins.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return None if not self.values else self.values[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return None if not self.mins else self.mins[-1]

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
from Queue import Queue
class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Queue()
        self._top = None
        
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """ 
        if self._top != None:
            self.q.put(self._top)
        self._top = x
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        res, self._top = self._top, None
        if not self.q.empty():
            q, self.q = self.q, Queue()
            for _ in xrange(q.qsize()-1):
                self.q.put(q.get())
            self._top = q.get()
        return res
        
        
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._top
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self._top == None

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print obj.pop()
    print obj.pop()
    print obj.pop()
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
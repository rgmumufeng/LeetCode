class TwoSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.nums[number] = self.nums.get(number, 0)+1
                
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.nums:
            target = value - i
            count = self.nums.get(target)
            if count == 2 or (count == 1 and target != i):
                return True
        return False
                


if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    #arguments = []
    #answers = []
    #test(Solution()., arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
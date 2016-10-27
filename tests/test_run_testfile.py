class Solution(object):
    def testfunction(self, a, b):
        return [a+b[0], a*b[1]]

if __name__ == "__main__":
    from solutions.leetcodelib import run_testfile
    testfile = "testfile2.yaml"
    arg_names = "a, b"
    run_testfile(testfile, Solution().testfunction)
    run_testfile(testfile, Solution().testfunction, 10)
    run_testfile(testfile, Solution().testfunction, [2, 3])
    run_testfile(testfile, Solution().testfunction, 's')
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = [x for x in path.split('/') if x]
        newpath = []
        for x in l:
            if x == '..' and newpath:
                newpath.pop()
            elif x != '.' and x != '..':
                newpath.append(x)
        return "/" + "/".join(newpath)
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = ["/home/", "/a/./b/../../c/", '/a//b/']
    answers = ["/home", "/c", '/a/b']
    test(Solution().simplifyPath, arguments, answers, [2])
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def rec(ss, n, paths):
            #print "processing", ss, n, paths
            if not ss and n == 4:
                ans = paths
            
            elif 0 <= n <= 4 and paths:
                ans1, ans2, ans3 = [], [], []
                if len(ss) > 0:
                    #print 'ans1', ss[1:], n+1, [p+[ss[0]] for p in paths]
                    ans1 = rec(ss[1:], n+1, [p+[ss[0]] for p in paths])
                if (len(ss) > 1 and ss[0] != '0'):
                    #print 'ans2', ss[2:], n+1, [p+[ss[0:2]] for p in paths]
                    ans2 = rec(ss[2:], n+1, [p+[ss[0:2]] for p in paths]) 
                if (len(ss) > 2 and 100 <= int(ss[0:3]) <= 255):
                    #print 'ans3', ss[3:], n+1, [p+[ss[0:3]] for p in paths]
                    ans3 = rec(ss[3:], n+1, [p+[ss[0:3]] for p in paths]) 
                ans = ans1+ans2+ans3
            
            else:
                ans = []
            #print "ans is", ans
            #print "finished processing", ss, n, paths
            #print 
            return ans
            
        ans = rec(s, 0, [[]])
        return [".".join(p) for p in ans]
    
    
class Solution2(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.rec(ans, s, 4, [])
        return [".".join(p) for p in ans]
        
    
    def rec(self, ans, s, k, tmp):
        if len(s) > k*3:
            return
        
        if k == 0:
            ans.append(tmp[:])
        else:
            for i in xrange(min(3, len(s)-k+1)):
                if (i==2 and int(s[:3]) > 255) or (i > 0 and s[0] == '0'):
                    continue
                self.rec(ans, s[i+1:], k-1, tmp+[s[:i+1]])
    
            

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    s1 = "25525511135"
    ans1 = ["255.255.11.135", "255.255.111.35"]
    
    s2 = "0000"
    ans2 = ["0.0.0.0"]
    
    s3 = "1111"
    ans3 = ["1.1.1.1"]
    
    arguments = [s1, s2, s3]
    answers = [ans1, ans2, ans3]
    test(Solution2().restoreIpAddresses, arguments, answers, mode='1D', inds=None)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
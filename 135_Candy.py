class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) <= 1:
            return len(ratings)
        
        tot = peak = curr = 1
        for i in xrange(1, len(ratings)):   
            follower = ratings[i+1] if i < len(ratings)-1 else ratings[i]
            if ratings[i] == ratings[i-1]:
                tot += 1
                peak = curr = 1
            else:
                curr += 1
                tot += curr
                if ratings[i] >= max(ratings[i-1], follower):
                    peak, curr = curr, 1
                elif ratings[i] <= min(ratings[i-1], follower):
                    tot = tot - min(curr, peak) + 1
                    peak = curr = 1
        return tot
    
class Solution2(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rty
        """
        if len(ratings) <= 1:
            return len(ratings)
        
        counts = [1]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                counts.append(counts[-1]+1)
            else:
                counts.append(1)
        for i in xrange(1, len(ratings)):
            if ratings[~i] > ratings[~i+1] and counts[~i] <= counts[~i+1]:
                counts[~i] = counts[~i+1] + 1
        return sum(counts)
                

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = [[1, 4, 3, 2, 1, 2, 4, 3, 2, 1], [4,2,3,4,1]]
    answers = [23, 9]
    test(Solution2().candy, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
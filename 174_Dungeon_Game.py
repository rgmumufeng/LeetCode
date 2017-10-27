class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 1
        m, n = len(dungeon), len(dungeon[0])
        d = [[None for j in xrange(n)] for i in xrange(m)]
        d[m-1][n-1] = self.fill(dungeon[m-1][n-1], 1)
        
        i = i0 = m-1
        j = j0 = n-1
        VMAX = float('inf')
        while i or j:
            #print i, j,
            if i == m-1 or j == 0:
                if i0 > 0:
                    i0 -= 1
                else:
                    j0 -= 1
                i, j = i0, j0
            else:
                i, j = i+1, j-1
            
            #print i, j
            godown = self.fill(dungeon[i][j], d[i+1][j]) if i+1 < m else VMAX
            goright = self.fill(dungeon[i][j], d[i][j+1]) if j+1 < n else VMAX
            d[i][j] = min(godown, goright)
            #print d
        return d[0][0]
          
    def fill(self, supplement, target):
        return target - supplement if supplement < target-1 else 1

class Solution2(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 1
        m, n = len(dungeon), len(dungeon[0])
        d = [[None for j in xrange(n)] for i in xrange(m)]
        
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                self.fill(dungeon, d, i, j)
        return d[0][0]
        
    def fill(self, dungeon, d, i, j):
        right = d[i][j+1] if j+1 < len(d[0]) else float('inf')
        down = d[i+1][j] if i+1 < len(d) else float('inf')
        target = 1 if right == down == float('inf') else min(right, down)
        d[i][j] = target - dungeon[i][j] if dungeon[i][j] < target else 1


if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    dungeon1 = [[3],[49],[38],[30],[-93],[-99],[13],[10],[6],[-77],[-83],[-76],[24],[-40],[-73]]
    arguments = [dungeon1]
    answers = [369]
    test(Solution2().calculateMinimumHP, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
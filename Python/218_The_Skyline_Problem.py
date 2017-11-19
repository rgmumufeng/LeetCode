# Solution adopted from https://discuss.leetcode.com/topic/34119/10-line-python-solution-104-ms
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # Scan the edge of the buildings from left to right. 
        # Use a heap (hp) to keep track of the "active" buildings. Since it is not trivial to remove
        # random element from heap, the old buildings will not be removed as long as there're higher
        # active buildings.
        # Whenever meet an edge, check the heap first. If there's any "expired" building whose right
        # edge is smaller/equal to current edge, remove it from the heap. Then check if the current
        # edge begins a new building. If it is, add it to the heap. Finally, find the highest building
        # in all active buildings (hp[0]). If it's height is different from previous skyline height
        # ([res[-1][1]), either higher or lower, add it to the result.
        # Note that, at the begining, (0, float("inf")) is put inside the heap to present the baseline
        # y=0, and [0, 0] is put inside res to avoid compare first building height with empty heap.
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        import heapq
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]
        
        
    
class Solution2(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings or not buildings[0]:
            return []
        left, right, height = zip(*buildings)
        ptx = sorted(list(set(left+right)))
        pty = [0 for _ in ptx]
        for bd in buildings:
            for i in xrange(len(ptx)):
                if ptx[i] < bd[0]:
                    continue
                elif ptx[i] >= bd[1]:
                    break
                else:
                    pty[i] = max(bd[2], pty[i])
        res = [[ptx[0], pty[0]]]
        for i in xrange(1, len(ptx)):
            if pty[i] != res[-1][1]:
                res.append([ptx[i], pty[i]])
        return res
                    
                
        
        
        
if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    area1 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    points1 = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    
    area2 = [[0, 2, 3], [2, 5, 3]]
    points2 = [[0, 3], [5, 0]]
    
    arguments = [area1, area2]
    answers = [points1, points2]
    test(Solution().getSkyline, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
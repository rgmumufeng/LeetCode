class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        for i in xrange(len(height)-1):
            for j in xrange(i+1, len(height)):
                area = min(height[i], height[j]) * (j-i)
                if area > maxarea:
                    maxarea = area
        return maxarea


class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ih, it = 0, len(height)-1
        sorted_height = sorted(list(enumerate(height)), key=lambda x: x[1])
        maxarea = 0
        for i, ai in sorted_height:
            while height[ih] < ai:
                ih += 1
            while height[it] < ai:
                it -= 1
            area = ai * max(abs(i-ih), abs(it-i))
            if area > maxarea:
                maxarea = area
        return maxarea


class Solution3(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        for i in xrange(len(height)):
            ih = 0
            while height[ih] < height[i]:
                ih += 1
            it = len(height)-1
            while height[it] < height[i]:
                it -= 1
            area = height[i] * max(abs(i-ih), abs(it-i))
            if area > maxarea:
                maxarea = area
        return maxarea


class Solution4(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        ih, it = 0, len(height)-1
        while ih < it:
            w = it - ih
            if height[ih] < height[it]:
                h = height[ih]
                ih += 1
            else:
                h = height[it]
                it -= 1
            area = w * h
            if area > maxarea:
                maxarea = area
        return maxarea

if __name__ == "__main__":
    from leetcodelib import test
    import json
    with open("011_COntainer_With_Most_Water.dat", "r") as f:
        arguments, answers = json.load(f)

    test(Solution1().maxArea, arguments, answers)
    test(Solution2().maxArea, arguments, answers)
    test(Solution3().maxArea, arguments, answers)
    test(Solution4().maxArea, arguments, answers)

        


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        label = node.label
        ref = {label: (node, UndirectedGraphNode(label))}
        stack = [label]
        while stack:
            node, center = ref[stack.pop()]
            for x in node.neighbors:
                if x.label not in ref:
                    ref[x.label] = (x, UndirectedGraphNode(x.label))
                    stack.append(x.label)
                center.neighbors.append(ref[x.label][1])
        return ref[label][1]
    
    
class Solution2:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        return self.copy(node, {})
    
    def copy(self, node, ref):
        label = node.label
        if label not in ref:
            ref[label] = UndirectedGraphNode(node.label)
            ref[label].neighbors = [self.copy(x, ref) for x in node.neighbors]
        return ref[label]
        

if __name__ == "__main__":
    from leetcodelib import test, update_testfile, run_testfile
    arguments = []
    answers = []
    test(Solution().cloneGraph, arguments, answers)
    
    #testfile = __file__.replace('.py', '.yaml')
    #arg_names = ""
    #update_testfile(testfile, arg_names, arguments, answers)
    #run_testfile(testfile, Solution().)
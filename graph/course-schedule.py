class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dependencyGraph = {}

        for clss, prereq in prerequisites:
            if prereq not in dependencyGraph:
                dependencyGraph[prereq] = []
            dependencyGraph[prereq].append(clss)
        
        whiteSet = set([x for x in range(numCourses)])
        greySet = set()
        blackSet = set()

        def checkCycle(node):
            if node in greySet:
                return True
            if node in blackSet:
                return False
            
            whiteSet.remove(node)
            greySet.add(node)
            if node in dependencyGraph:
                for n in dependencyGraph[node]:
                    if checkCycle(n):
                        return True
            
            greySet.remove(node)
            blackSet.add(node)
            return False

        while len(whiteSet) > 0:
            node = whiteSet.pop()
            whiteSet.add(node)
            if checkCycle(node):
                return False
        return True

            

        
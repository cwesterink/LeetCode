class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencyGraph = {}

        for clss, prereq in prerequisites:
            if prereq not in dependencyGraph:
                dependencyGraph[prereq] = []
            dependencyGraph[prereq].append(clss)
        
        whiteSet = set([x for x in range(numCourses)])
        greySet = set()
        blackSet = set()
        courses = []
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
            courses.append(node)
            return False

        for node in range(numCourses):
            if checkCycle(node):
                return []
        courses.reverse()
        return courses
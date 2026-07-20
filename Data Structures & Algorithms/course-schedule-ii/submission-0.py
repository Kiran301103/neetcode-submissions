class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prevMap={i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            prevMap[c].append(p)
        visit,cycle=set(),set()
        output=[]
        
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)
            for p in prevMap[c]:
                if dfs(p)==False:
                    return False
            cycle.remove(c)
            visit.add(c)
            output.append(c)
        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return output

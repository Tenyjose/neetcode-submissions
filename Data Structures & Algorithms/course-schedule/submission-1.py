class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create adjacency list:
        # prerequisiteMap[course] = list of prerequisites needed for this course
        prerequisiteMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prerequisiteMap[course].append(prereq)

        # state values:
        # 0 = unvisited
        # 1 = currently visiting / in current DFS path
        # 2 = fully visited / safe
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True
            
            state[course] = 1

            for preq in prerequisiteMap[course]:
                if not dfs(preq):
                    return False

            state[course] = 2

            return True


        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

            

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses
        result = []
        # first we have to create an adjacency list
        graph = {i : [] for i in range(numCourses)}
        for c,p in prerequisites:
            graph[p].append(c)  # notice we are geeting for each prerequisite.
            indegree[c] += 1

        queue = deque()
        for num in range (numCourses):
            if indegree[num] == 0:
                queue.append(num)

        while queue:
            course = queue.popleft()
            result.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if  indegree[next_course] == 0:
                    queue.append(next_course)


        if len(result) == numCourses:
            return result
        else:
            return []